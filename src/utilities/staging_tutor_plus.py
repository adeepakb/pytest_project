import json
import re
import sys
import time
import warnings
from datetime import datetime, timedelta

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from constants.load_json import get_data
from utilities.staging_tllms import Stagingtllms
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException, TimeoutException, \
    StaleElementReferenceException
from utilities.exceptions import *


class StagingTutorPlus(Stagingtllms):

    def __init__(self, driver):
        super().__init__(driver)
        self.__init_locators()
        self.__const()
        self.login_profile, self.user_profile, self.sub_profile, self.day = None, None, None, None

    def __init_locators(self):
        self.channel_input_box = "css selector", "input.inputSearch"
        self.convert_session_btn = "xpath", "//span[text()=\"Convert to Assessment Session\"]"
        self.confirmation_dialog = "css selector", ".confirmation-wrapper"
        self.dialog_ok_btn = "xpath", "//button/span[text()=\"Yes\"]"
        self.dialog_cancel_btn = "xpath", "//button/span[text()=\"Cancel\"]"
        self.assessment_text = "xpath", "//*[text()=\"Assessment Session\"]"

    def __const(self, *args):
        self.TUTOR_PLUS_STAGING_URL = "https://tutor-plus-staging.tllms.com/"

    def set_user(self, login_profile='login_details_3', user_profile='user_1', sub_profile='profile_1', day="today"):
        self.login_profile, self.user_profile = login_profile, user_profile
        self.sub_profile, self.day = sub_profile, day
        return self

    def convert_video_session(self, subject_topic_name, day="today", assessment_type="unit test",**kwargs):
        db = kwargs['db']
        session_details = self.student_session_details(day, self.login_profile, self.user_profile, self.sub_profile)
        subject_name, topic_name = subject_topic_name
        db.sd = session_details
        self.chrome_driver.implicitly_wait(10)
        if subject_name is None and topic_name is None:
            with open("../../test_data/classroom_details.json") as fd:
                s_detail = json.load(fd)
            channel_id = s_detail["channel"]
        elif subject_name.lower() == "monthly test" or subject_name.lower() == "unit test" or \
                subject_name.lower() == "half yearly test":
            with open("../../test_data/classroom_details.json") as fd:
                s_detail = json.load(fd)
            channel_id = s_detail["channel"]
        else:
            session_details = session_details[::-1]
            for session_detail in session_details:
                session_detail_desc = session_detail["session detail"]
                if subject_name.lower() in session_detail_desc.lower() or topic_name.lower() in session_detail_desc.lower():
                    with open("../../test_data/classroom_details.json", "w") as fd:
                        json.dump(session_detail, fd)
                    channel_id = session_detail["channel"]
                    s_detail = session_detail
                    break
            else:
                raise Exception("Expected channel id not found.")
        uri = "studentSessions/%s" % channel_id
        self.chrome_driver.get(self.TUTOR_PLUS_STAGING_URL + uri)
        self.chrome_driver.find_element("xpath", "//span[text()=\"LOGIN\"]").click()
        try:
            assert self.chrome_driver.find_element(*self.assessment_text).text.lower() == "assessment session"
            return
        except NoSuchElementException:
            self._session_user_wise(session=self.day, user_profile=self.user_profile, sub_profile=self.sub_profile)
            self.__reset_session(s_detail)
        self.chrome_driver.implicitly_wait(10)
        self.chrome_driver.get(self.TUTOR_PLUS_STAGING_URL + uri)
        self.chrome_driver.find_element("xpath", "//span[text()=\"LOGIN\"]").click()
        self.chrome_driver.find_element("xpath", "//*[text()=\"Attach Requisite Group\"]").click()
        self.chrome_driver.find_element("css selector", "div.selectedValue").click()
        if assessment_type == 'unit test':
            req_grp = get_data("../../config/ps_requisite.json", "unit_test_all")
        elif assessment_type == 'monthly test':
            req_grp = get_data("../../config/ps_requisite.json", "monthly_test_all")
        elif assessment_type == "pre-post":
            req_grp = get_data("../../config/ps_requisite.json", "all_pre_post")
        else:
            raise NotImplementedError("assessment type other 'unit test' and 'monthly test' is not yet implemented.")
        for char in req_grp:
            self.chrome_driver.find_element("css selector", "input.dropdownSearch").send_keys(char)
            time.sleep(0.02)
        grp_names = self.chrome_driver.find_elements("css selector", ".dropdownListItem")
        retry = 4
        while retry:
            time.sleep(1)
            grp_names = self.chrome_driver.find_elements("css selector", ".dropdownListItem")
            if grp_names:
                retry = 0
            else:
                retry -= 1
        retry = 2
        while retry:
            try:
                for grp_name in grp_names:
                    if grp_name.text == req_grp:
                        grp_name.click()
                        retry = 0
                        break
                else:
                    raise RequisiteException("Test", f"\"{req_grp}\"")
            except StaleElementReferenceException:
                grp_names.clear()
                grp_names = self.chrome_driver.find_elements("css selector", ".dropdownListItem")
                retry -= 1
        self.chrome_driver.find_element("css selector", "button[type=button]").click()
        try:
            self.chrome_driver.switch_to.alert.accept()
        except NoAlertPresentException:
            pass
        try:
            success_msg = self.chrome_driver.find_element("css selector", "#message-id").text
            if not success_msg.lower() == "attached successfully":
                warnings.warn(
                    UserWarning("Requisite group attachment might not be successful or message might have been changed."
                                )
                )
        except NoSuchElementException:
            warnings.warn(UserWarning("Requisite group attachment might not be successful"))
        self.chrome_driver.find_element(*self.convert_session_btn).click()
        self.chrome_driver.find_element(*self.dialog_ok_btn).click()

    def reset_session_otm(self, topic_name):
        mega_sessions = self.chrome_driver.find_elements_by_xpath("//tr/td[contains(text(),'one_to_mega')]")
        mega_session = mega_sessions[0]
        for mega_session in mega_sessions:
            mega_topic_name = mega_session.find_element_by_xpath("./preceding-sibling::td[4]").text
            if topic_name.lower() in mega_topic_name.lower():
                break
        t = mega_session.find_element(By.XPATH, "./preceding-sibling::td/b/..").text
        date_time = t.split('\n')
        session_date, session_time = date_time[0], date_time[-1]
        struct_time = time.strptime(session_date, '%d-%b-%Y')
        cd, cm, cy = list(map(int, time.strftime("%d %m %Y").split()))
        sd, sm, sy = struct_time.tm_mday, struct_time.tm_mon, struct_time.tm_year
        ch = int(time.strftime("%H"))
        ah = int(session_time.split("-")[-1].strip().split(":")[0])
        if sy == cy:
            if sm == cm:
                if sd == cd:
                    if ah > ch:
                        mega_session.find_element(By.XPATH, "./following-sibling::td/a[text()='Reset']").click()
                elif sd > cd:
                    SessionResetException("Reset-Error: 'session yet to be started.'")
                else:
                    SessionResetException("Reset-Error: 'session reached the end time.'")
            else:
                SessionResetException("Reset-Error: 'session is not in the current month.'")
        else:
            raise SessionResetException("Reset-Error: 'session is not in the current year.'")

    def end_session_otm(self, topic_name):
        timeout = 240
        m_url, email_input = self._session_url(topic_name)
        self.chrome_driver.execute_script(f"arguments[0].setAttribute('value', '{self.EMAIL}')", email_input)
        self.chrome_driver.find_element(By.CSS_SELECTOR, '#_submit_action').click()
        self.chrome_driver.get(m_url)
        self.wait_for_clickable_element_webdriver('//span[text()="LOGIN"]')
        self.chrome_driver.find_element(By.XPATH, '//span[text()="LOGIN"]').click()
        self.chrome_driver.implicitly_wait(0)
        try:
            count = 20
            while timeout:
                try:
                    self.chrome_driver.find_element(By.CSS_SELECTOR, '.endPopupContainer .subText')
                    timeout -= 1
                    time.sleep(1)
                    count = 0
                except NoSuchElementException:
                    if not count:
                        timeout -= timeout
                    else:
                        count -= 1
                        time.sleep(0.5)
            self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '.session-button.timer'))).click()
            self.chrome_driver.find_element(By.XPATH, "//div[text()='End Session Now']").click()
            self.chrome_driver.find_element(By.CSS_SELECTOR, ".endBtn").click()
            info = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "label.Mui-error"))).text
            if 'ended now' in info.lower():
                return True
            else:
                warnings.warn("tutor session might not be ended properly")
        except TimeoutException:
            err_msg = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "label.Mui-error"))).text
            if 'session is ended' in err_msg.lower():
                return True
            elif 'not authorized' in err_msg.lower():
                raise UnknownUserProfile(
                    f"'{self.EMAIL}' is not a valid tutor email or not updated in 'Schedule Page'.") from None
            else:
                raise SessionNotEndedError('session might not be ended or could not validate the message') from None

    def __reset_session(self, session_details: dict):
        session_time = session_details["time"]
        session_topic = session_details["session detail"]
        s_time, e_time = re.findall(r"\d{2}:\d{2} - \d{2}:\d{2}", session_time)[-1].split(" - ")
        sh, sm = list(map(int, s_time.split(":")))
        eh, em = list(map(int, e_time.split(":")))
        ch = int(time.strftime("%H"))
        cm = int(time.strftime("%M"))
        if eh > ch:
            if ch >= (sh + 2):
                self.reset_session_otm(session_topic)
            elif sh > ch:
                return
            elif sh == ch and sm > cm:
                return
            else:
                self.end_session_otm(session_topic)
                self._session_user_wise(session=self.day, profile=self.login_profile, user_profile=self.user_profile,
                                        sub_profile=self.sub_profile)
                self.reset_session_otm(session_topic)
        elif eh == ch:
            if sm > cm:
                return
            elif sm <= cm < em:
                self.end_session_otm(session_topic)
                self._session_user_wise(session=self.day, profile=self.login_profile, user_profile=self.user_profile,
                                        sub_profile=self.sub_profile)
                self.reset_session_otm(session_topic)
        else:
            raise SessionEndedError("cannot reset the already ended session.")


    def modify_test_requisite_assessment(self, channel_id, field, day, status,time=None):
        """
        """
        if channel_id is None:
            self.session_relaunch()
            with open("../../test_data/classroom_details.json") as fd:
                channel_id = json.load(fd)["channel"]
        try:
            assert self.chrome_driver.find_element(*self.assessment_text).text.lower() == "assessment session"
        except:
            self.chrome_driver.get("https://tutor-plus-staging.tllms.com/studentSessions/%s" % channel_id)
            self.chrome_driver.find_element(By.XPATH, '//span[text()="LOGIN"]').click()

        self.chrome_driver.implicitly_wait(15)
        asset_id = self.chrome_driver.find_element("xpath",
                                                   "//*[text()=\"OneToMany::TestRequisite\"]/../..//*[text("
                                                   ")=\"ASSESSMENT_ID\"]/following-sibling::td").text
        self.chrome_driver.get("https://staging.tllms.com/admin/assessments/%s/edit" % asset_id)
        if status == "expire":
            if day == "yesterday":
                date_time = (datetime.now() + timedelta(days=-1)).strftime("%d-%m-%Y %H:%M")
            elif day == "today":
                date_time = (datetime.now() + timedelta(minutes=-2)).strftime("%d-%m-%Y %H:%M")
            else:
                raise NotImplementedError()
            date_time_list = date_time.split(":")
            minutes = date_time_list.pop()
            date_time = ":".join(date_time_list)
            if time is not None:
                date_time = time.strftime("%d-%m-%Y %H:%M")
            if field.lower() == "start_time":
                self.chrome_driver.find_element(
                    "css selector", "#assessment_available_starting").click()
                self.chrome_driver.find_element(
                    "css selector", "#assessment_available_starting").send_keys(date_time)
            elif field.lower() == "end_time":
                self.chrome_driver.find_element(
                    "css selector", "#assessment_available_until").click()
                self.chrome_driver.find_element(
                    "css selector", "#assessment_available_until").clear()
                self.chrome_driver.find_element(
                    "css selector", "#assessment_available_until").send_keys(date_time)
            elif field.lower() == "result_time":
                self.chrome_driver.find_element(
                    "css selector", "#assessment_send_results_at").clear()
                self.chrome_driver.find_element(
                    "css selector", "#assessment_send_results_at").send_keys(date_time)
            else:
                raise NotImplementedError()
            self.chrome_driver.find_element("css selector", "input[name=commit]").click()
        else:
            raise NotImplementedError()

    def change_assessment_time(self,db,minutes_to_add=0,current=True):
        sd = db.sd
        if current:
            time_required = datetime.strptime(datetime.now().strftime('%d-%b-%Y %H:%M'), '%d-%b-%Y %H:%M')
            two_minute = timedelta(minutes_to_add=2)
            time_required_new = time_required + two_minute
        else:
            time_list = sd[0]['time'].replace("\n", " ").split(" - ")
            date = time_list[0].split(" ")[0]
            new_timelist = []
            new_timelist.append(date)
            new_timelist.append(" " + time_list[1])
            new_time = "".join(new_timelist)
            time_required = datetime.strptime(new_time, '%d-%b-%Y %H:%M')
            two_minute = timedelta(minutes=2)
            time_required_new = time_required + two_minute

        self.modify_test_requisite_assessment(sd[0]['channel'], field="end_time", day='today', status='expire',
                                          time=time_required_new)