import os
import string
import sys
from random import randint

from cryptography.fernet import Fernet
from selenium.webdriver import ActionChains
import json
import pickle
import random
import re
import time
import warnings
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException, InvalidSessionIdException, \
    StaleElementReferenceException, ElementNotInteractableException, SessionNotCreatedException, \
    NoAlertPresentException, UnableToSetCookieException, InvalidElementStateException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from utilities.tutor_common_methods import TutorCommonMethods
from constants.load_json import get_data
from selenium.webdriver.chrome.options import Options
from datetime import datetime, timedelta
from utilities.exceptions import *
from datetime import datetime , timedelta



class Stagingtllms(TutorCommonMethods):

    def __init__(self, driver):
        self.driver = driver
        self.chrome_options = Options()
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument("--window-size=1600,900")
        try:
            with open("../../config/chrome_session.json", "r") as fp:
                chrome_session = json.load(fp)
        except FileNotFoundError:
            chrome_session = None
        if not chrome_session:
            self.chrome_driver = webdriver.Chrome(options=self.chrome_options)
            _d = {'session_url': self.chrome_driver.service.service_url, 'session_id': self.chrome_driver.session_id}
            with open("../../config/chrome_session.json", "w") as fp:
                json.dump(_d, fp)
        else:
            self.chrome_driver = webdriver.Chrome(options=self.chrome_options)
            self.chrome_driver.quit()
            self.chrome_driver.command_executor._url = chrome_session["session_url"]
            self.chrome_driver.session_id = chrome_session["session_id"]
        super().__init__(driver)
        self.__init()
        self.cohort_grade, self.syllabus_grade = None, None

    def __const(self, sub_profile_type='primary'):
        self.TUTOR_PLUS_CMS_URL = 'https://tutor-plus-cms-staging.tllms.com/'
        self.STAGING_TLLMS_URL = 'https://staging.tllms.com/admin/'
        self.ATTACHMENT_DETAILS = '../../config/attachments.json'
        self.LOGIN_DETAILS = '../../config/login_data.json'
        self.REQUISITE_DETAILS = '../../config/ps_requisite.json'
        fp = '../config/config.json'
        key = os.getenv('SECRET')
        f = Fernet(key)
        encrypted_data = get_data(fp, 'encrypted_data', 'token')
        decrypted_data = json.loads(f.decrypt(encrypted_data.encode('ascii')))
        self.EMAIL = decrypted_data['staging_access']['email']
        self.PASSWORD = decrypted_data['staging_access']['password']
        self.IN_REQ = 'in_req'
        self.POST_REQ = 'post_req'
        self.PRE_REQ = 'pre_req'
        self.ALL_PRE_POST_REQ = 'all_pre_post'
        self.PROFILE = 'login_details_3'
        self.MOBILE = 'mobile_number'
        self.USER = 'profile_name'
        self.PREMIUM_ID = 'premium_id'
        self.OTP = 'OTP'

    def __init(self):
        self.__const()
        self.wait = WebDriverWait(self.chrome_driver, timeout=30)
        self.url_session_user_wise = self.STAGING_TLLMS_URL + 'student_sessions/#scheduling-sessions-user-wise'
        try:
            self.premium_id = str(get_data('../config/config.json', 'profile_credentials', 'premium_id'))
        except KeyError:
            pass
        self.today = datetime.today().strftime('%Y-%m-%d')

    def save_session(self):
        self.chrome_driver.implicitly_wait(5)
        self.chrome_driver.find_element(By.CSS_SELECTOR, 'img[src]')
        self.chrome_driver.get_screenshot_as_file("view.png")
        with open('../../config/login.pkl', 'wb') as io_write:
            pickle.dump(self.chrome_driver.get_cookies(), io_write)

    def login_to_staging(self, cms_login=None):
        email = self.EMAIL
        password = self.PASSWORD
        try:
            if cms_login:
                self.chrome_driver.get(self.TUTOR_PLUS_CMS_URL)
                self.wait_for_locator_webdriver("//span[contains(text(),'LOGIN')]")
                self.chrome_driver.find_element_by_xpath("//span[contains(text(),'LOGIN')]").click()
            else:
                self.chrome_driver.get(self.STAGING_TLLMS_URL)
            self.chrome_driver.maximize_window()
            self.wait_for_locator_webdriver("//input[@id='email']")
            self.chrome_driver.find_element_by_xpath("//input[@id='email']").send_keys(email)
            self.wait_for_locator_webdriver("//button[@type='submit']")
            self.chrome_driver.find_element_by_xpath("//button[@type='submit']").click()
            self.wait_for_locator_webdriver("//input[@type='email']")
            self.wait_for_clickable_element_webdriver("//input[@type='email']")
            self.chrome_driver.find_element_by_xpath("//input[@type='email']").send_keys(email)
            self.chrome_driver.find_element_by_xpath("//input[@type='email']").send_keys(Keys.ENTER)
            self.wait_for_clickable_element_webdriver("//input[@type='password']")
            self.chrome_driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
            self.chrome_driver.find_element_by_xpath("//input[@type='password']").send_keys(Keys.ENTER)
        except NoSuchElementException:
            self.chrome_driver.get_screenshot_as_file("failed.png")
            raise Exception("Unable to login to staging")

    def get_tutor_url(self, course='primary', premium_id='primary'):
        email = str(get_data('../config/config.json', 'staging_access', 'email'))
        today = datetime.today().strftime('%Y-%m-%d')
        if course == 'primary':
            session_course_id = str(get_data('../config/login_data.json', 'login_detail3', 'course_id_primary'))
            premium_id = str(get_data('../config/config.json', 'account_details', 'premium_id'))
        elif course == 'secondary':
            session_course_id = str(get_data('../config/login_data.json', 'login_detail3', 'course_id_secondary'))
            premium_id = str(get_data('../config/config.json', 'account_details', 'premium_id'))
        elif course == 'ternary':
            session_course_id = str(get_data('../config/login_data.json', 'login_detail1', 'course_id'))
            premium_id = str(get_data('../config/login_data.json', 'login_detail1', 'premium_id'))

        self.login_to_staging()
        self.wait_for_clickable_element_webdriver("//*[text()='Mentoring']")
        self.chrome_driver.find_element_by_xpath("//*[text()='Mentoring']").click()
        self.wait_for_clickable_element_webdriver("//*[text()='1:M - Schedule Student Sessions']")
        self.chrome_driver.find_element_by_xpath("//*[text()='1:M - Schedule Student Sessions']").click()

        self.wait_for_locator_webdriver("//a[text()='Scheduling Sessions(User Wise)']")
        self.chrome_driver.find_element_by_xpath("//a[text()='Scheduling Sessions(User Wise)']").click()
        self.chrome_driver.implicitly_wait(5)
        self.wait_for_locator_webdriver("//input[@id ='target_date']")
        self.chrome_driver.find_element_by_xpath("//input[@id ='target_date']").send_keys(today)
        self.wait_for_locator_webdriver("//input[@id ='premium_account_id']")
        self.chrome_driver.find_element_by_xpath("//input[@id ='premium_account_id']").send_keys(premium_id)
        self.wait_for_locator_webdriver("//input[@value ='Start Scheduling']")
        self.chrome_driver.find_elements_by_xpath("//input[@value ='Start Scheduling']")[1].click()

        tutor_url = None
        rows = len(self.chrome_driver.find_elements_by_xpath("//table[contains(@class,'index_table')]/tbody/tr"))
        cols = len(self.chrome_driver.find_elements_by_xpath("//table[contains(@class,'index_table')]/thead/tr/th"))

        email_col = meeting_col = 8
        tagged_col = status_col = None
        for i in range(1, cols):
            header = self.chrome_driver.find_elements_by_xpath(
                "//table[contains(@class,'index_table')]/thead/tr/th[" + str(i) + "]")[0].text
            if header == 'Teaching Material/Video Tagged':
                tagged_col = i
            elif header == 'Status':
                status_col = i

        for r in range(1, rows + 1):
            try:
                status = self.chrome_driver.find_element_by_xpath(
                    "//tr[" + str(r) + "]/td[" + str(status_col) + "]").text
                # incase of multiple sessions in same day
                course_details = self.chrome_driver.find_element_by_xpath(
                    "//tr[" + str(r) + "]/td[" + str(tagged_col) + "]/div[@class='course_details']").text
                course_id = re.search(r'^.*?\bCourse id : (\d+)', course_details).group(1)
                if 'one_to_mega' in status and course_id == session_course_id:
                    self.chrome_driver.find_element_by_xpath("//tr[" + str(r) + "]/td[" + str(
                        email_col) + "]/li[@id='teacher_email_input']/input[@id='teacher_email']").clear()
                    self.chrome_driver.find_element_by_xpath("//tr[" + str(r) + "]/td[" + str(
                        email_col) + "]/li[@id='teacher_email_input']/input[@id='teacher_email']").send_keys(email)
                    tutor_url = self.chrome_driver.find_element_by_xpath("//tr[" + str(r) + "]/td[" + str(
                        meeting_col) + "]/li[@id='meeting_url_input']/input[@id='meeting_url']").get_attribute('value')
                    break

            except NoSuchElementException:
                continue

        self.chrome_driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
        self.chrome_driver.save_screenshot("image1.png")
        self.chrome_driver.close()
        return tutor_url

    def get_mobile_and_ccode(self, profile='login_details_3', user_profile='user_1', sub_profile='profile_1'):
        from pages.android.application_login import Login
        login = Login(self.driver)
        mobile = login.set_user_profile(profile, user_profile, sub_profile).user_mobile
        return mobile

    def get_otp(self, cc_mobile=None, account_type=None):
        # complete_mobile = self.get_mobile_and_ccode()
        if account_type == 'asset_not_tagged_account_details':
            cc_mobile = str(get_data('../config/config.json', 'asset_not_tagged_account_details', 'mobile'))
        self.session_relaunch()
        self.wait_for_locator_webdriver("//li[@id='otp']")
        self.chrome_driver.find_element_by_xpath("//li[@id='otp']").click()
        self.wait_for_locator_webdriver("//li[@id='mobile_otps']")
        self.chrome_driver.find_element_by_xpath("//li[@id='mobile_otps']").click()
        self.chrome_driver.find_element_by_css_selector("#q_mobile_no").send_keys(cc_mobile)
        self.wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='commit']"))).click()
        otp = self.chrome_driver.find_element_by_css_selector("td.col-otp").text
        self.chrome_driver.close()
        return otp

    def wait_for_locator_webdriver(self, locator_value=None):
        try:
            WebDriverWait(self.chrome_driver, 15, ignored_exceptions=[StaleElementReferenceException]).until(
                ec.presence_of_element_located((By.XPATH, locator_value)))
        except TimeoutException:
            print("Timed out while waiting for page to load")

    def wait_for_clickable_element_webdriver(self, locator_value=None):
        try:
            WebDriverWait(self.chrome_driver, 15).until(ec.element_to_be_clickable((By.XPATH, locator_value)))
        except TimeoutException:
            print("Timed out while waiting for page to load")

    def wait_for_element_not_present_webdriver(self, locator_value=None):
        try:
            WebDriverWait(self.chrome_driver, 15).until(ec.invisibility_of_element_located((By.XPATH, locator_value)))
        except TimeoutException:
            print("Timed out while waiting for page to load")

    def login_to_cms_staging(self):
        email = str(get_data('../config/config.json', 'staging_access', 'email'))
        password = str(get_data('../config/config.json', 'staging_access', 'password'))
        # Login to CMS
        self.chrome_driver.get('https://tutor-plus-cms-staging.tllms.com/?page=1')
        self.chrome_driver.maximize_window()
        self.wait_for_locator_webdriver("//span[contains(text(),'LOGIN')]")
        self.chrome_driver.find_element_by_xpath("//span[contains(text(),'LOGIN')]").click()
        self.wait_for_locator_webdriver("//input[@id='email']")
        self.chrome_driver.implicitly_wait(2)
        self.wait_for_clickable_element_webdriver("//input[@id='email']")
        self.chrome_driver.find_element_by_xpath("//input[@id='email']").send_keys(email)
        self.wait_for_locator_webdriver("//button[@type='submit']")
        self.chrome_driver.find_element_by_xpath("//button[@type='submit']").click()
        self.wait_for_locator_webdriver("//input[@type='email']")
        self.chrome_driver.find_element_by_xpath("//input[@type='email']").send_keys(email)
        self.wait_for_locator_webdriver("//span[contains(text(),'Next')]")
        self.chrome_driver.find_element_by_xpath("//span[contains(text(),'Next')]").click()
        self.wait_for_clickable_element_webdriver("//input[@type='password']")
        self.chrome_driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
        self.wait_for_locator_webdriver("//span[contains(text(),'Next')]")
        self.chrome_driver.find_element_by_xpath("//span[contains(text(),'Next')]").click()

    def close_driver(self):
        self.chrome_driver.close()

    def saved_session(self):
        try:
            with open('../../config/login.pkl', 'rb') as io_read:
                c = pickle.load(io_read)
                if not bool(c):
                    raise EOFError from None
                else:
                    return c
        except (EOFError, FileNotFoundError):
            self.login_to_staging()
            self.save_session()
            return list()

    def session_relaunch(self, cms=False):
        retry = 1
        url = self.STAGING_TLLMS_URL if cms is False else self.TUTOR_PLUS_CMS_URL
        while retry:
            session = self.saved_session()
            self.chrome_driver.quit()
            self.chrome_driver = webdriver.Chrome(options=self.chrome_options)
            self.__init()
            if bool(session):
                self.chrome_driver.get(url)
                try:
                    [self.chrome_driver.add_cookie(s) for s in session]
                except UnableToSetCookieException:
                    self.chrome_driver.get_screenshot_as_file("../../test_data/view.png")
                    raise
                self.chrome_driver.get(url)
                if '/users/sign_in' in self.chrome_driver.current_url:
                    self.login_to_staging().save_session()
                    break
                elif cms:
                    self.chrome_driver.find_element("xpath", "//span[text()='LOGIN']").click()
                    self.wait_for_element_not_present_webdriver("//span[text()='LOGIN']")
                    try:
                        self.chrome_driver.implicitly_wait(5)
                        self.chrome_driver.find_element("css selector", "img[src]")
                    except NoSuchElementException:
                        pass
                    if self.TUTOR_PLUS_CMS_URL in self.chrome_driver.current_url:
                        self.save_session()
                        break
                    else:
                        retry -= 1
                elif url in self.chrome_driver.current_url:
                    break
                else:
                    retry -= 1
        else:
            raise SessionNotCreatedException("New session could not be created") from None

    def get_premium_id(self, profile='login_details_3', user_profile=None, sub_profile=None):
        from pages.android.application_login import Login
        login = Login(self.driver)
        login.set_user_profile(profile, user_profile, sub_profile)
        login_data = self.LOGIN_DETAILS
        m, i, u = login.user_mobile, login.premium_id, login.profile_name
        if i is None:
            with open(login_data, "r+") as io_write:
                data = json.load(io_write)
                io_write.seek(0)
                user = data[profile][user_profile][sub_profile]
                user.update({self.PREMIUM_ID: self._pid(u, m)})
                json.dump(data, io_write, indent=4)
            return user[self.PREMIUM_ID], True
        return i, False

    def _pid(self, user_profile=None, mobile=None):
        self.session_relaunch()
        self.chrome_driver.implicitly_wait(3)
        self.chrome_driver.find_element(By.ID, 'users').click()
        self.chrome_driver.find_element(By.ID, 'q_mobile').send_keys(mobile)
        self.chrome_driver.find_element(By.CSS_SELECTOR, '.buttons > input').click()

        users_col = self.chrome_driver.find_elements(By.CSS_SELECTOR, "tbody > tr")
        try:
            f_name, l_name = user_profile.split(maxsplit=1)
        except ValueError:
            f_name, l_name = user_profile, ""
        for user in users_col:
            first_name = user.find_element(By.CSS_SELECTOR, ".col.col-first_name").text
            last_name = user.find_element(By.CSS_SELECTOR, ".col.col-last_name").text
            if first_name == user_profile:
                user.find_element(By.CSS_SELECTOR, ".col.col-id>a").click()
                break
            elif first_name == f_name and last_name == l_name:
                user.find_element(By.CSS_SELECTOR, ".col.col-id>a").click()
                break
        else:
            raise UnknownUserProfile("none matched against given user")
        _id = self.chrome_driver.find_element(By.CSS_SELECTOR, ".row.row-premium_account > td > a").text
        return _id

    def working_day(self, days=None):
        for d in range(1, 6):
            if not self.is_holiday(datetime.now() + timedelta(days)):
                date = datetime.now() + timedelta(days)
                break
            days += d
        else:
            raise DateError("no working day available")
        return date

    def otm_home_screen(self):
        from pages.android.student_dashboard_otm import StudentDashboardOneToMega
        __o = StudentDashboardOneToMega(self.driver)
        otm_home_activity = 'OneToMegaHomeActivity'
        user_home_activity = 'UserHomeActivity'
        home_activity = 'HomeActivity'
        if otm_home_activity in self.driver.current_activity:
            pass
        elif user_home_activity in self.driver.current_activity:
            self.get_element('xpath', __o.login.btn_premium).click()
        elif home_activity in self.driver.current_activity:
            __o.login.click_on_premium_school()
        else:
            self.driver.close_app()
            self.driver.launch_app()
            __o.login.click_on_premium_school()
        return __o

    def get_session_completed_up_next_date(self, completed=None):
        __o = self.otm_home_screen()
        last_date, up_nxt_date = __o.last_completed_session_up_next(completed)
        __o.click_app_back_btn()
        if __o.login.wait_activity("UserHomeActivity", 3):
            __o.click_app_back_btn()
        return last_date, up_nxt_date.split(',')[0]

    def date_check(self, session=None, completed=None):
        name = type(session).__name__
        if isinstance(session, str):
            if session == 'yesterday':
                days = -1
            elif session == 'today':
                days = 0
            elif session == 'tomorrow':
                days = 1
            elif session == 'completed' or session == 'up next':
                session_desc = self.get_session_completed_up_next_date(completed=completed)
                if session == 'completed':
                    ssn = session_desc[0]
                else:
                    ssn = session_desc[-1]
                details = ssn.split()
                if details[0].lower() != 'today':
                    date, month = details
                    current_month = time.strftime('%b')
                    if month == current_month:
                        days = int(date) - int(time.strftime('%d'))
                        working_day = datetime.now() + timedelta(days)
                        return working_day
                    else:
                        raise DateError(
                            "session completed month ('%s') is not in the current month ('%s')" % (month, current_month)
                        )
                elif details[0].lower() == 'today':
                    days = 0
                else:
                    raise NotImplementedError(f"'{ssn}' session is not yet implemented.")
            else:
                raise DateError("not implemented, provide day in ('int' or 'float') instead")
        elif isinstance(session, int):
            days = session
        else:
            raise TypeError(f"expected 'str' or 'int', got '{name}' type instead")
        return self.working_day(days)

    def _req_grp_name(self, r=None, a=None):
        t = r.lower()
        c = a.lower()
        r_d = self.REQUISITE_DETAILS
        if t == 'in':
            o = get_data(r_d, self.IN_REQ)
            if c == 'assessment':
                n = o[c]
                return n
            else:
                raise AssetTypeError(r, a)
        elif t == 'pre':
            o = get_data(r_d, self.PRE_REQ)
            if c == 'all' or c == 'assessment' or c == 'journey' or c == 'k12 video' or c == 'practice' or c == 'video':
                if c == 'video':
                    c = 'k12 video'
                c = "_".join(c.split())
                n = o[c]
            else:
                raise AssetTypeError(r, a)
        elif t == 'post':
            o = get_data(r_d, self.POST_REQ)
            if c == 'all' or c == 'assessment' or c == 'journey' or c == 'k3 video' or c == 'k12 video' or c == 'video':
                if c == 'video':
                    c = random.choice(('k3 video', 'k12 video'))
                c = "_".join(c.split())
                n = o[c]
            elif c == 'assessment_k12' or c == "two":
                n = o["assessment_k12"]
            else:
                raise AssetTypeError(r, a)
        elif t == 'all_pre_post':
            o = get_data(r_d, self.ALL_PRE_POST_REQ)
            n = o
        elif t == 'pre_post_ak3_29':
            o = get_data(r_d, "pre_post_ak3_29")
            n = o
        elif t == "unit test":
            o = get_data(r_d, "unit_test_all")
            n = o
        elif t == "monthly test":
            o = get_data(r_d, "monthly_test_all")
            n = o
        elif t == "monthly test pre":
            o = get_data(r_d, "monthly_test_pre")
            n = o
        else:
            raise RequisiteTypeError(r)
        return n

    def _requisite_group(self, rt=None, at=None, mode='attach'):
        self.chrome_driver.switch_to.window(self.chrome_driver.window_handles[-1])
        if mode.lower() == 'attach':
            grp_id = self._req_grp_name(rt, at)
            input_box = self.chrome_driver.find_element(By.CSS_SELECTOR, ".input-box")
            input_box.clear()
            input_box.send_keys(grp_id)
            self.chrome_driver.find_element(By.CSS_SELECTOR, "button[label=Save]").click()
            attached_id = self.chrome_driver.find_element(
                "xpath",
                f"//div[contains(text(), \"{self.cohort_grade}\") and contains(text(), \"{self.syllabus_grade}\")]"
                f"/../..//span[@class=\"requisite_group_id\"]"
            ).text
            if grp_id != attached_id:
                raise AttachmentError("'Requisite Group' attachment might not be successful.")
        # elif mode.lower() == 'detach':
        #     self.chrome_driver.find_element(By.XPATH, '//a[text()="Detach Requisite Group"]').click()
        #     self.chrome_driver.switch_to.alert.accept()
        #     notice = self.chrome_driver.find_element(By.CSS_SELECTOR, ".flashes .flash").text
        #     if "detached" not in notice.lower():
        #         raise AttachmentError("'Requisite Group' detachment might not be successful.")
        else:
            raise InvalidModeSelection(f"'{mode}' is not a valid mode.")
        return self

    def _session_user_wise(self, session=None, user_profile=None,
                           sub_profile=None, profile='login_details_3', completed=None):
        time_details = self.date_check(session, completed=completed)
        p_id, status = self.get_premium_id(profile=profile, user_profile=user_profile, sub_profile=sub_profile)
        date = str(time_details).split(maxsplit=1)[0]
        student_session_url = 'https://staging.tllms.com/admin/student_sessions'
        try:
            if not status:
                self.session_relaunch()
            self.chrome_driver.execute_script(f"window.open('{student_session_url}');")
        except InvalidSessionIdException:
            self.session_relaunch()
            self.chrome_driver.execute_script(f"window.open('{student_session_url}');")
        self.chrome_driver.switch_to.window(self.chrome_driver.window_handles[-1])
        self.chrome_driver.find_element(By.ID, 'ui-id-2').click()
        self.chrome_driver.find_element(By.ID, "premium_account_id").send_keys(p_id)
        self.chrome_driver.execute_script('document.getElementById("target_date").removeAttribute("readonly")')
        self.chrome_driver.find_element(By.ID, 'target_date').clear()
        self.chrome_driver.find_element(By.ID, 'target_date').send_keys(date + '\n')
        self.chrome_driver.find_element(
            By.XPATH, '//div[@id="scheduling-sessions-user-wise"]//li[@id="_submit_action"]/input').click()
        if self.chrome_driver.current_url == student_session_url:
            raise ClassRoomNotFoundError(f"no classrooms found for the specified user on {date}.")

    def attach_requisite_group(self, grade, req_type=None, asset_type=None, days=None, **kwargs):
        profile, user_profile, sub_profile = kwargs["profile"], kwargs["user_profile"], kwargs["sub_profile"]
        if grade == "8":
            self.cohort_grade = "14-8th"
            self.syllabus_grade = "VIII-CBSE"
        elif grade == "4":
            self.cohort_grade = "29-4th"
            self.syllabus_grade = "IV-CBSE"
        else:
            raise NotImplementedError("Requisite attachment for grades other than '8' and '4' and syllabus 'CBSE' is "
                                      "not yet implemented")
        self._session_user_wise(session=days, profile=profile, user_profile=user_profile, sub_profile=sub_profile)
        tmb_id = get_data("../config/attachments.json", "one_to_mega", grade)["tmb_id"]
        uri = "tmbs/%s" % tmb_id
        self.chrome_driver.implicitly_wait(5)
        self.chrome_driver.get(self.TUTOR_PLUS_CMS_URL + uri)
        self.chrome_driver.find_element_by_xpath('//span[text()="LOGIN"]').click()
        self.chrome_driver.find_element("css selector", "button[label=Requisites]").click()
        self.chrome_driver.find_element(
            "xpath",
            f"//div[contains(text(), \"{self.cohort_grade}\") and contains(text(), \"{self.syllabus_grade}\")]"
            f"/../..//a[contains(text(), \"RG\")]"
        ).click()
        self._requisite_group(req_type, asset_type)
        self.attach_session_video(grade=grade, session=days, override=True, **kwargs)

    def close_tabs(self):
        windows = self.chrome_driver.window_handles
        for window in windows:
            self.chrome_driver.switch_to.window(window)
            self.chrome_driver.close()

    def _session_url(self, topic_name=None):
        if topic_name is None:
            url = self.chrome_driver.find_element(
                By.XPATH,
                "(//tr/td[contains(text(),'one_to_mega')])[1]/following-sibling::td/li[@id='meeting_url_input']/input"
            ).get_attribute('value')
            email = self.chrome_driver.find_element(
                By.XPATH,
                "//tr/td[contains(text(),'one_to_mega')]/following-sibling::td/li[@id='teacher_email_input']/input"
            )
            return url, email
        else:
            sessions = self.chrome_driver.find_elements(
                By.XPATH, "(//tr/td[contains(text(),'one_to_mega')])")
            for session in sessions:
                raw_topic_name = session.find_element_by_xpath('./preceding-sibling::td[4]').text
                if topic_name in raw_topic_name:
                    m_url = session.find_element_by_xpath(
                        "./following-sibling::td/li[@id='meeting_url_input']/input").get_attribute('value')

                    e_mail = session.find_element_by_xpath(
                        "./following-sibling::td/li[@id='teacher_email_input']/input")
                    return m_url, e_mail
            else:
                raise SessionNotFoundError(f"the session with the topic name '{topic_name}' is not found on the page.")

    def end_ongoing_session(self, rate_action='skip', topic_name=None, user_profile=None, sub_profile=None):
        timeout = 240
        # todo: log: get sub_profile_type
        if rate_action == 'skip':
            if user_profile is None and sub_profile is None:
                self._session_user_wise(session='today', user_profile='user_1', sub_profile='profile_1')  # TODO
            else:
                self._session_user_wise(session='today', user_profile=user_profile, sub_profile=sub_profile)
        elif rate_action == 'rate':
            if user_profile is None and sub_profile is None:
                self._session_user_wise(session='today', user_profile='user_2', sub_profile='profile_1')
            else:
                self._session_user_wise(session='today', user_profile=user_profile, sub_profile=sub_profile)
        m_url, email_input = self._session_url(topic_name)
        self.chrome_driver.execute_script(f"arguments[0].setAttribute('value', '{self.EMAIL}')", email_input)
        self.chrome_driver.find_element(By.CSS_SELECTOR, '#_submit_action').click()
        self.chrome_driver.get(m_url)
        self.wait_for_clickable_element_webdriver('//span[text()="LOGIN"]')
        self.chrome_driver.find_element(By.XPATH, '//span[text()="LOGIN"]').click()
        try:
            count = 20
            while timeout:
                try:
                    self.chrome_driver.find_element(By.CSS_SELECTOR, '.endPopupContainer .subText')
                    timeout -= 1
                    sleep(1)
                    count = 0
                except NoSuchElementException:
                    if not count:
                        timeout -= timeout
                    else:
                        count -= 1
                        sleep(0.5)
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

    def detach_requisite_attachment(self, profile='login_details_3', user_profile='user_1', sub_profile='profile_1'):
        self.session_relaunch()
        self._session_user_wise(
            session='completed', profile=profile, user_profile=user_profile, sub_profile=sub_profile)
        self.chrome_driver.find_element(
            By.XPATH, "//tr/td[contains(text(),'one_to_mega')]/preceding-sibling::td/a").click()
        self._requisite_group(None, None, mode='detach').close_tabs()

    def is_otm_session_activity(self):
        __o = self.otm_home_screen()
        return __o.is_join_now_btn_displayed().result

    def get_otm_first_session_detail(
            self, profile='login_details_3', user_profile='user_1', sub_profile='profile_1', completed=None):
        self.session_relaunch()
        self._session_user_wise(
            session='completed', profile=profile, user_profile=user_profile, sub_profile=sub_profile,
            completed=completed)
        session_detail = self.chrome_driver.find_element(
            By.XPATH,
            "(//tr/td[contains(text(),'one_to_mega')])[1]/preceding-sibling::td[4]").text.lower()
        return session_detail

    def reset_session_one_to_mega(
            self, profile='login_details_3', user_profile='user_1',
            sub_profile='profile_1', completed=None, topic_name=None):
        self.session_relaunch()
        self._session_user_wise(
            session='completed', profile=profile, user_profile=user_profile, sub_profile=sub_profile,
            completed=completed)
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
                        self.chrome_driver.implicitly_wait(3)
                        mega_session.find_element(By.XPATH, "./following-sibling::td/a[text()='Reset']").click()
                        self.otm_home_screen()
                elif sd > cd:
                    self.otm_home_screen()
                    # SessionResetException("Reset-Error: 'session yet to be started.'")
                else:
                    SessionResetException("Reset-Error: 'session reached the end time.'")
            else:
                SessionResetException("Reset-Error: 'session is not in the current month.'")
        else:
            raise SessionResetException("Reset-Error: 'session is not in the current year.'")

    def topic_id_row(self, tid=None):
        for cl in range(1, 11):
            col = self.chrome_driver.find_element(By.XPATH, "((//tbody/tr)[%s]/td/div)[1]" % cl)
            if int(col.text) == tid:
                return self.chrome_driver.find_elements(By.XPATH, "((//tbody/tr)[%s]/td)" % cl)

    def _license_key(self, this=None, label=None, attachment=None, tag=None):
        try:
            if "hls" in label:
                video_hls = attachment['hls']
                input_box = this.find_element(By.XPATH, tag)
                if input_box.get_attribute('value') == "":
                    input_box.clear()
                    input_box.send_keys(video_hls['license_key'])
                else:
                    input_box.clear()
                    input_box.send_keys(video_hls['license_key'])
            elif "dash" in label:
                video_hls = attachment['dash']
                input_box = this.find_element(By.XPATH, tag)
                if input_box.get_attribute('value') == "":
                    input_box.clear()
                    input_box.send_keys(video_hls['license_key'])
                else:
                    input_box.clear()
                    input_box.send_keys(video_hls['license_key'])
            else:
                raise NotImplementedError(f"'{label}' is not yet implemented")
        except (ElementNotInteractableException, InvalidElementStateException):
            """input fields are disabled"""
            pass

    def _video_url(self, this=None, label=None, attachment=None, tag=None):
        try:
            if "hls" in label:
                video_hls = attachment['hls']
                input_box = this.find_element(By.XPATH, tag)
                if input_box.get_attribute('value') == "":
                    input_box.clear()
                    input_box.send_keys(video_hls['video_url'])
                else:
                    input_box.clear()
                    input_box.send_keys(video_hls['video_url'])
            elif "dash" in label:
                video_dash = attachment['dash']
                input_box = this.find_element(By.XPATH, tag)
                if input_box.get_attribute('value') == "":
                    input_box.clear()
                    input_box.send_keys(video_dash['video_url'])
                else:
                    input_box.clear()
                    input_box.send_keys(video_dash['video_url'])
            else:
                raise NotImplementedError(f"'{label}' is not yet implemented")
        except (ElementNotInteractableException, InvalidElementStateException):
            """input fields are disabled"""
            pass

    def _write_key_license(self, topic_id_col_elements=None, tag_label=None, tag_input=None, video_n='video_0'):
        video_attachment = get_data(self.ATTACHMENT_DETAILS, 'one_to_mega', video_n)
        for col in topic_id_col_elements:
            self.chrome_driver.implicitly_wait(0)
            try:
                element_label = col.find_element(By.XPATH, tag_label).text.lower()
            except NoSuchElementException:
                continue
            if "key" in element_label:
                self._license_key(this=col, label=element_label, attachment=video_attachment, tag=tag_input)
            elif "url" in element_label:
                self._video_url(this=col, label=element_label, attachment=video_attachment, tag=tag_input)

    def _attachment_write(self, tmb_id, tmb_name=None, topic_id=None):
        if tmb_id is None:
            raise TypeError("'tmb_id' must be str, not None")
        topics_uri = 'raw_topics/%s'
        topic_id = int(topic_id)
        self.chrome_driver.get('https://tutor-plus-cms-staging.tllms.com/' + (topics_uri % topic_id))
        try:
            self.chrome_driver.find_element_by_xpath('//span[text()="LOGIN"]').click()
        except NoSuchElementException:
            pass
        self.wait_for_locator_webdriver("//div[text()='Edit']")
        self.chrome_driver.find_element("css selector", "button[label=Edit]").click()
        self.wait_for_locator_webdriver("//div[contains(text(), \"TMB\")]/following-sibling::div//input")
        drp_box_input = self.chrome_driver.find_element(
            "xpath", "//div[contains(text(), \"TMB\")]/following-sibling::div//input")
        drp_box_input.clear()
        drp_box_input.click()
        drp_box_input.send_keys(Keys.CONTROL + "a" + Keys.BACKSPACE)
        drp_box_input.send_keys(tmb_name)
        self.wait_for_locator_webdriver(".tmbTagOption .tagOptionIdText")
        list_options = self.chrome_driver.find_elements("css selector", ".tmbTagOption .tagOptionIdText")
        if len(list_options) != 0:
            try:
                for option in list_options:
                    if option.text == tmb_id:
                        option.click()
                        break
                    else:
                        raise Exception(f"ID Error: \"{tmb_id}\" is not displayed in the list")
            except StaleElementReferenceException:
                pass
        chapter_input = self.chrome_driver.find_element("css selector", "input[placeholder=\"Enter Chapter\"]")
        chapter_input.clear()
        chapter_input.send_keys("null")
        self.chrome_driver.find_element("css selector", "button[label=Save]").click()
        try:
            missing_param = self.chrome_driver.find_element("id", "message-id").text
            print("missing param........................", missing_param)
            raise AttachmentError(missing_param)
        except NoSuchElementException:
            pass

    def attach_session_video(self, grade, session='today', override=False, **kwargs):
        profile, user_profile, sub_profile = kwargs["profile"], kwargs["user_profile"], kwargs["sub_profile"]
        tmb_id = get_data("../config/attachments.json", "one_to_mega", grade)["tmb_id"]
        tmb_name = get_data("../config/attachments.json", "one_to_mega", grade)["tmb_name"]
        self.get_premium_id(profile=profile, user_profile=user_profile, sub_profile=sub_profile)
        self.chrome_driver.implicitly_wait(10)
        cr_details = self.student_session_details(session, profile, user_profile, sub_profile)
        try:
            channel_id = kwargs["channel_id"]
        except KeyError:
            channel_id = None
        for cr_detail in cr_details:
            video_details = cr_detail["teaching material/video tagged"]
            if channel_id == cr_detail["channel"]:
                details = list(re.findall(r"(?i:(course\sid.*:\s\d*)(?:[^\b]*)(topic\sid\s:\s\d*))", video_details)[-1])
                course_id, topic_id = details[0].split(':')[-1].strip(), details[-1].split(':')[-1].strip()
                self._attachment_write(tmb_id, topic_id=topic_id, tmb_name=tmb_name)
            elif "no" in video_details.lower() or override:
                details = list(re.findall(r"(?i:(course\sid.*:\s\d*)(?:[^\b]*)(topic\sid\s:\s\d*))", video_details)[-1])
                course_id, topic_id = details[0].split(':')[-1].strip(), details[-1].split(':')[-1].strip()
                self._attachment_write(tmb_id, topic_id=topic_id, tmb_name=tmb_name)

    @staticmethod
    def booking_time(hours, minutes, end_hour=None, end_minutes=0, day=None):
        time_now = datetime.now()
        if day is not None and day.lower() == 'tomorrow':
            n_day = (time_now + timedelta(days=1)).strftime("%A")
            return n_day, "8:00", "23:00"
        if minutes is None:
            mins = 32
        else:
            mins = 30 + int(minutes)
        if int(time_now.strftime("%S")) >= 45:
            time_now = datetime.now()
            mins = 33 if minutes is None else 30 + int(minutes) + 3
        start_time = (time_now + timedelta(hours=0, minutes=mins))
        if end_hour is None:
            if hours is not None:
                end_hour = int(hours) if int(hours) > 0 else 1
            else:
                end_hour = 23 - int(start_time.strftime("%H"))
        end_time = (start_time + timedelta(hours=end_hour, minutes=end_minutes)).strftime("%H:%M")
        c_day, ac_time = start_time.strftime('%A %H:%M').split()
        return c_day, ac_time, end_time

    @staticmethod
    def get_available_slots(b_day: str, b_time: str):
        with open('../../config/course.json') as io_read:
            course = json.load(io_read)['cbse_4']
        main_slots = course['slots']
        i = 0
        for main_slot in main_slots:
            if len(main_slots[main_slot]) == 3:
                slots = ['slot_0', 'slot_1', 'slot_2']
            elif len(main_slots[main_slot]) == 2:
                slots = ['slot_0', 'slot_1']
            elif len(main_slots[main_slot]) == 1:
                slots = ['slot_0']
            elif len(main_slots[main_slot]) == 0:
                slots = list()
            else:
                raise NotImplementedError('slot booking more than three is not yet implemented.')
            for s in slots:
                slot = main_slots[main_slot][s]
                ah, am = tuple(map(int, slot['start_time'].split(":")))
                ch, cm = tuple(map(int, b_time.split(":")))
                if b_day == slot['day']:
                    if ch == ah:
                        if am == cm:
                            return main_slot, slots[i]
                        elif abs((am - cm)) < 2:
                            return main_slot, slots[i]
                i += 1
            i = 0
        return None, None

    def _add_slot(self, booking_time=None, new_course_id=None):
        def group_name(d, t):
            return "auto_" + str(time.strptime(d, "%A").tm_wday + 1) + ''.join(t.split(":"))

        self.session_relaunch(cms=True)
        self.chrome_driver.get(
            f"https://tutor-plus-cms-staging.tllms.com/neo_courses/%s/slot_groups/new" % new_course_id)
        ms_count = 1
        freq = int(self.chrome_driver.find_element("css selector", ".elipseMinus + input").get_attribute("value"))
        slot_count = abs(ms_count - freq)
        if ms_count < freq:
            for _ in range(slot_count):
                self.chrome_driver.find_element("xpath", "//div[@class=\"elipseMinus\"][text()=\"-\"]").click()
        elif ms_count > freq:
            for _ in range(slot_count):
                self.chrome_driver.find_element("xpath", "//div[@class=\"elipseMinus\"][text()=\"+\"]").click()
        number_of_slots = int(len(self.chrome_driver.find_elements('css selector', 'div.slotCardContainer')))
        if ms_count != number_of_slots:
            raise SlotUpdateError("'Mandatory Sessions Count' and 'Number Of Slots' should be same")
        b_day, start_time, end_time = booking_time
        weeks = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', "Saturday", "Sunday")
        for i, day in enumerate(weeks, 1):
            if day.lower() == b_day.lower():
                index = i
                break
        else:
            raise Exception("DayFormatException: bad day format '%s'" % b_day)
        grp_name = group_name(b_day, start_time)
        self.chrome_driver.find_element_by_css_selector("input.slotNameInput").send_keys(grp_name)
        dropdowns = self.chrome_driver.find_elements(
            By.XPATH, "(//label[text()=\"Day*\"]/../following-sibling::div)//div[text()=\"Select the day\"]")
        items = list(range(1, len(dropdowns) * 2, 2))
        for i, dropdown in enumerate(dropdowns):
            dropdown.click()
            index = index if index + i < 8 else 0
            self.chrome_driver.find_elements("css selector", "div#menu- .MuiListItem-button")[index + i].click()
            self.chrome_driver.find_element("xpath",
                                            "(//input[@class=\"slotInput\"])[%s]" % items[i]
                                            ).send_keys(start_time)
            self.chrome_driver.find_element("xpath",
                                            "(//input[@class=\"slotInput\"])[%s]" % (items[i] + 1)).send_keys(
                end_time)
            self.chrome_driver.find_element("xpath", "//div[text()=\"Select Session Type\"][1]").click()
            self.chrome_driver.find_element("xpath", "//li[text()=\"Mandatory\"]").click()
        self.chrome_driver.find_element("css selector", "button.submitButton[type=button]").click()
        new_slot_grp_url = self.chrome_driver.current_url
        try:
            self.chrome_driver.implicitly_wait(5)
            self.chrome_driver.find_element("xpath", "//*[text()=\"Create New Slot Group\"]")
        except NoSuchElementException:
            pass
        timeout = 2
        while timeout:
            if self.chrome_driver.current_url != new_slot_grp_url:
                ths = self.chrome_driver.find_elements("css selector", ".tableHeaderTextStyle")
                id_index = [ths.index(i) for i in ths if i.text.lower() == "id"][-1]
                tds = self.chrome_driver.find_elements("css selector", ".tableBodyTextStyle span")
                sl_id, sl_name = tds[id_index].text, tds[id_index + 1].text
                return sl_id, sl_name
            else:
                timeout -= 1
                sleep(1)
        else:
            self.chrome_driver.quit()
            raise SlotUpdateError(
                f"Cannot update slot in "
                f"'https://tutor-plus-cms-staging.tllms.com/neo_courses/{new_course_id}/slot_groups'")

    def _add_batch(self, new_course_id, *slot_details):
        uri = "neo_courses/%s" % new_course_id
        url = self.TUTOR_PLUS_CMS_URL + uri
        new_batch_url = url + "/batches/new"
        self.chrome_driver.get(url)
        self.chrome_driver.find_element("css selector", ".batches-container .btn").click()
        batch_input, slot_drp_dwn, topic_drp_dwn = self.chrome_driver.find_elements("css selector", "input[type=text]")
        date_fields = self.chrome_driver.find_elements("css selector", "input[type=date]")
        topic_count = self.chrome_driver.find_element("css selector", "input[type=number]")
        today, tomorrow = datetime.today().strftime('%m%d%Y'), (datetime.today() + timedelta(days=1)).strftime('%m%d%Y')
        batch_name = "test_batch_" + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(5))
        batch_input.send_keys(batch_name)
        slot_drp_dwn.click()
        slot_id, slot_grp_name = slot_details
        for char in slot_grp_name:
            slot_drp_dwn.send_keys(char)
            sleep(0.15)
        drp_dwn_ids = self.chrome_driver.find_elements("css selector", ".slotGroup-id")
        for drp_dwn_id in drp_dwn_ids:
            if drp_dwn_id.text.lower() == "id:"+slot_id:
                drp_dwn_id.click()
                break
        else:
            raise SlotNotFoundException(
                f"NAME: \"{slot_grp_name}\", ID: \"{slot_id}\" is not found in the \"Slot Group\" list")
        date_fields[0].send_keys(today)
        date_fields[1].send_keys(tomorrow)
        self.chrome_driver.find_element(
            "xpath", "//*[text()=\"Holiday Preference*\"]/following-sibling::div//input/..").click()
        self.chrome_driver.find_elements("css selector", "#menu- li")[1].click()
        topic_drp_dwn.click()
        self.chrome_driver.find_element("css selector", "ul[role=listbox] > li").click()
        topic_count.send_keys("5")
        self.chrome_driver.find_element("css selector", "button[type=button][label=Next]").click()
        timeout = 2
        while timeout:
            if self.chrome_driver.current_url != new_batch_url:
                break
            else:
                timeout -= 1
                sleep(1)
        else:
            raise BatchUpdateError("took too long to add new batch")
        self.chrome_driver.quit()

    def verify_and_add_slot(self, cohort, course_tag, hours=None, minutes=None, end_hour=None, end_minutes=0, day=None):
        """
        Example:
        cohort - 14 (for 8th CBSE)
        course_tag - free trial or masterclass
        """
        with open('../../config/course.json') as io_read:
            course = json.load(io_read)["cbse"][cohort][course_tag]
        new_course_id = course['id']
        b_day, start_time, *_ = b_time = self.booking_time(
            hours=hours, minutes=minutes, day=day, end_hour=end_hour, end_minutes=end_minutes)
        # available_slots = self.get_available_slots(b_day, start_time)
        # if all(available_slots) is False:
        slot_details = self._add_slot(b_time, new_course_id)
        self._add_batch(new_course_id, *slot_details)
        # with open('../../config/slots.json', 'r+') as io_write:
        #     course = json.load(io_write)
        #     io_write.seek(0)
        #     course['cbse_4']['slots'].update(slot)
        #     json.dump(course, io_write, indent=2)
        # else:
        #     return available_slots

    def student_session_details(self, days, profile, user_profile, sub_profile):
        # self.attach_session_video(profile, user_profile, sub_profile, session=days)
        self._session_user_wise(session=days, profile=profile, user_profile=user_profile, sub_profile=sub_profile)
        headers = self.chrome_driver.find_elements("css selector", "thead > tr > th")
        content_rows = self.chrome_driver.find_elements("css selector", "tbody > tr")
        session_details = dict()
        session_list = list()
        for j, row in enumerate(content_rows, 1):
            if j % 2 != 0:
                contents_row = row.find_elements("css selector", "td")
                for i, header in enumerate(headers):
                    if header.text.strip() != "":
                        session_details.update({header.text.strip().lower(): contents_row[i].text.strip()})
                session_list.append(session_details.copy())
        return session_list

