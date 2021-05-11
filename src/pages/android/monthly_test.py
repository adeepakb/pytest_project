import json
import pickle
import random
import re
import time
from datetime import datetime, timedelta
from datetime import datetime
from time import sleep

from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from constants.constants import Login_Credentials
from constants.load_json import get_data
from pages.android.application_login import Login
from pages.android.scroll_cards import ScrollCards
from pages.android.session_requisite import SessionRequisite
from utilities.staging_tllms import Stagingtllms
from pages.android.student_dashboard_otm import StudentDashboardOneToMega
from pages.android.masterclass import MasterClass
from pages.base.monthly_test import MonthlyTestBase
from utilities.tutor_common_methods import TutorCommonMethods
from utilities.exceptions import *


class MonthlyTest(MonthlyTestBase, TutorCommonMethods):

    def __init__(self, driver):
        self.driver = driver
        self.login = Login(driver)
        self.action = TouchAction(driver)
        self.scroll_cards = ScrollCards(driver)
        self.session_requisite = SessionRequisite(self.driver)
        self.master_class = MasterClass(self.driver)
        super().__init__(driver)
        self.device_type = self.get_device_type()
        self.staging = Stagingtllms(self.driver)
        self.dashboard = StudentDashboardOneToMega(self.driver)
        self.__init_locators(self.device_type)
        self.count=0

    def __init_locators(self, device_type):
        package_name = self.driver.capabilities['appPackage'] + ':id'
        self.card_root = "id", "%s/card" % package_name
        self.subject_name = "id", "%s/subject_name" % package_name
        self.topic_name = "id", "%s/session_title" % package_name
        self.topic_name_for_pre_post ="id", "%s/topic_name" % package_name
        self.status ="id", "%s/post_requisite_status" % package_name
        self.heading = "id", "%s/requisite_item_heading" % package_name
        self.session_time = "id", "%s/session_time" % package_name
        self.wish_text = "id", "%s/strip_title" % package_name
        self.start_test_btn = "id", "%s/card_strip_btn" % package_name
        self.assessment_bg = "id", "%s/iv_assessment_bg" % package_name
        self.for_you = '//android.widget.LinearLayout[@content-desc="For you"]/android.widget.TextView'
        self.completed = '//android.widget.LinearLayout[@content-desc="Completed"]/android.widget.TextView'
        self.timer_content_message =  "id", "%s/timer_content_message" % package_name
        self.begin_assignment ='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[3]/android.view.View/android.widget.Button'
        self.no_of_questions= '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[3]/android.view.View/android.view.View[1]'
        self.next_button = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[4]/android.view.View[2]/android.widget.Button'
        self.finish_button ='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[4]/android.view.View[2]/android.widget.Button[2]'
        self.exit_assignment = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[3]/android.view.View[2]/android.view.View[1]'


        self.instruction_close_iv = "id", "%s/ivCloseInstruction" % package_name
        self.instruction_title = "id", "%s/tvInstructionTitle" % package_name
        self.instruction_time_details = "id", "%s/tvInstructionSubTitle" % package_name
        self.instruction_start_btn_W = "id", "%s/btStartButton" % package_name
        self.sd_toolbar_title = "id", "%s/toolbar_title" % package_name
        self.sd_action_bar_message = "id", "%s/tvActionTitle" % package_name
        self.sd_start_btn = "id", "%s/btnAction" % package_name
        self.sd_pre_req_header = 'id', '%s/prepareSessionTitleTextView' % package_name
        self.sd_post_req_header = 'id', '%s/reviseTitleTextView' % package_name
        self.sd_requisite_title = 'id', '%s/tvTitle' % package_name
        self.assessment_start_btn = "id", "%s/tvWorksheetActionText" % package_name
        self.next_question = "css_selector", "button#next-question"
        self.instruction_start_btn_N = "id", "%s/test_start_button" % package_name
        self.side_bar_nav = "css_selector", "#showRight"
        self.question_list = "css_selector", ".nav-group > li"
        self.previous_question = "css_selector", "#previous-question"
        self.feed_back_btn = "css_selector", "#give-feedback"
        self.flag_btn = "css_selector", "#review-later"
        self.reg_pre_date = "id", "%s/pre_requisite_time" % package_name
        self.reg_pr_date = "id", "%s/post_requisite_date" % package_name
        self.reg_pr_topic_name = "id", "%s/topic_name" % package_name
        self.reg_topic_name = "id", "%s/session_title" % package_name
        self.reg_session_time = "id", "%s/session_time" % package_name
        self.reg_subject_name = "id", "%s/subject_name" % package_name
        self.pop_up_msg = "id", "android:id/message"
        self.pop_up_ok = "id", "android:id/button1"
        self.retry = "id", "%s/btnRetry" % package_name
        self.completed_msg = "id", "%s/post_requisite_status" % package_name
        self.completed_icon = "id", "%s/post_requisite_status_icon" % package_name

    def verify_session_details(self, detail=None, screen="dashboard"):
        detail = detail.lower()
        if detail is None:
            raise TypeError('"detail" argument cannot be "NoneType"')
        elif detail == "subject title":
            title_text = self.get_element(*self.subject_name).text.lower()
            if title_text == "unit test" or title_text == "monthly test" or title_text == "half yearly test":
                return True
        elif detail == "topic name":
            return self.get_element(*self.topic_name).is_displayed()
        elif detail == "session time":
            schedule_details = self.get_element(*self.session_time).text
            schedule_match = re.findall(r'(?:\d{2}\D{0,3}\s\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec),\s'
                                        r'(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday))|Tomorrow'
                                        r'|Today, \d{1,2}:\d{2}\s(?i:AM|PM)',
                                        schedule_details)
            return bool(schedule_match)
        elif detail == "wish text":
            if screen == "dashboard":
                w_t = self.get_element(*self.wish_text).text
            elif screen == "details screen":
                w_t = self.get_element(*self.sd_action_bar_message).text
            else:
                raise Exception("not a valid screen")
            if w_t == "Good luck for the test":
                return True
            return False
        elif detail == "start test button":
            if screen == "dashboard":
                btn_text = self.get_element(*self.start_test_btn).text
            elif screen == "details screen":
                btn_text = self.get_element(*self.sd_action_bar_message).text
            else:
                raise Exception("not a valid screen")
            if btn_text == "Start Test":
                return True
            return False
        elif detail == "test icon":
            return self.get_element(*self.assessment_bg).is_displayed()
        elif detail == "completed status":
            completed_text = self.get_element(*self.completed_msg).text.lower()
            completed_icon = self.get_element(*self.completed_icon).is_displayed()
            return completed_text == "completed" and completed_icon

    def is_test_card_displayed(self):
        cards = self.get_elements(*self.card_root)
        for card in cards:
            try:
                title = card.find_element(*self.subject_name).text.lower()
            except NoSuchElementException:
                title = card.find_element(*self.master_class.card_label_tv).text.lower()
            if "test" in title:
                return True
        cards = self.get_elements(*self.card_root)
        for card in cards:
            try:
                title = card.find_element(*self.subject_name).text.lower()
            except NoSuchElementException:
                title = card.find_element(*self.master_class.card_label_tv).text.lower()
            if "test" in title:
                return True
        return False

    def click_on_for_you_tab(self):
        self.get_element('xpath',
                             self.for_you).click()

    def click_on_completed_tab(self):
        self.get_element('xpath',
                             self. completed).click()

    def get_card_detail(self):
        card = self.get_element(*self.card_root)
        title = card.find_element(*self.subject_name).text.lower()
        session_time= card.find_element(*self.session_time).text
        session_title = card.find_element(*self.topic_name).text
        return title,session_time,session_title

    def click_on_button(self ,button_name):
        btn_text = self.get_element(*self.start_test_btn).text
        if btn_text.lower() == button_name.lower():
            self.get_element(*self.start_test_btn).click()
        else:
            raise ElementNotFoundError(button_name+ 'not found')


    def is_status_displayed(self, status):
        if status.lower() == 'completed':
            try:
                return self.get_element('xpath',
                                        self.completed).isDisplayed()
            except:
                return False

    def is_button_displayed(self, button_name):
        if button_name.lower() == 'resume':
            return self.get_element(*self.start_test_btn).is_displayed()

        return False

    def do_assignment(self, finish =True):
        start_button = self.get_element('xpath',self.begin_assignment)
        start_button_text =start_button.text
        number = int(self.get_element('xpath', self.no_of_questions).text.split(':')[1])
        if start_button_text.lower() == 'continue assessment' or start_button_text.lower() == 'start assessment':
            start_button.click()
        else:
            raise ElementNotFoundError(start_button + 'is being displayed, required continue assignment or start assignment')

        for qn in range(1, number):
            self.get_element('xpath', self.next_button).click()

        if finish:
            self.get_element('xpath', self.finish_button).click()



    def check_no_interruption_in_assignment(self):
        try:
            time.sleep(3000)
            if self.get_element('xpath',self.exit_assignment).is_displayed():
                self.count+=1
                if self.count > 20:
                    return True
                self.check_no_interruption_in_assignment()
            else:
                self.count=0
                return False
        except:
            self.count=0
            return False

















    def start_test(self):
        self.get_element(*self.start_test_btn).click()

    def take_test(self):
        if self.wait_activity("TestStartActivity"):
            self.get_element(*self.instruction_start_btn_N).click()

    def verify_test_instruction_screen(self, detail=None):
        ins_title = self.get_element(*self.instruction_title).text.lower()
        assert ins_title == "test instructions"
        assert self.get_element(*self.instruction_close_iv).is_displayed()
        assert self.get_element(*self.instruction_time_details).is_displayed()
        if detail == "start button":
            assert self.get_element(*self.instruction_start_btn_W).is_displayed()

    def click_on_test_card(self):
        cards = self.get_elements(*self.card_root)
        for card in cards:
            card_title = card.find_element(*self.subject_name)
            if "TEST" in card_title.text:
                card_title.click()
                return True
        return False

    def is_session_details_page_displayed(self):
        self.driver.implicitly_wait(10)
        retry = 2
        try:
            while retry:
                if self.get_element(*self.sd_toolbar_title).text == "Test Details":
                    return True
                else:
                    retry -= 1
                    sleep(1)
        except NoSuchElementException:
            return False
        finally:
            self.driver.implicitly_wait(5)

    def verify_last_question(self, **kwargs):
        number_of_questions = kwargs["db"].number_of_questions
        q_no = int(self.get_element("css_selector", '.question_num > span').text)
        print("1. total: %s, last question: %s." % (number_of_questions, q_no))
        for _ in range((number_of_questions - q_no)):
            self.webdriver_wait(15).until(ec.element_to_be_clickable((
                By.CSS_SELECTOR, self.next_question[-1]
            ))).click()
            if q_no == int(self.get_element("css_selector", '.question_num > span').text):
                self.driver.execute_script('document.querySelector("button#next-question").click()')
            q_no = int(self.get_element("css_selector", '.question_num > span').text)
        q_no = int(self.get_element("css_selector", '.question_num > span').text)
        print("2. total: %s, last question: %s." % (number_of_questions, q_no))
        self.driver.switch_to.context(self.driver.contexts[0])
        return number_of_questions == q_no

    def start_assessment_web(self, **kwargs):
        try:
            self.get_element(*self.instruction_start_btn_W).click()
        except NoSuchElementException:
            pass
        self.driver.switch_to.context(self.driver.contexts[-1])
        number_of_questions = int(self.get_element("css_selector", ".assignment_instructions > h4 .primary").text)
        kwargs["db"].number_of_questions = number_of_questions
        self.webdriver_wait(15).until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#begin-assessment'))).click()
        try:
            self.webdriver_wait(15).until(ec.invisibility_of_element((By.CSS_SELECTOR, '#begin-assessment')))
        except TimeoutException:
            element_force_click = """document.getElementById("begin-assessment").click()"""
            self.driver.execute_script(element_force_click)

    def is_end_finish_button_displayed(self):
        self.driver.switch_to.context(self.driver.contexts[-1])
        exit_assessment_text = self.get_element("css_selector", '#exit-assessment').text.lower()
        finish_submit = self.get_element("css_selector", "#end-assessment").text.lower()
        self.driver.switch_to.context(self.driver.contexts[0])
        if exit_assessment_text == "exit assessment" and finish_submit == "finish":
            return True
        return False

    def is_resume_button_displayed(self):
        btn_name = self.get_element(*self.start_test_btn).text
        if btn_name.lower() == "resume":
            return True
        return False

    def select_random_question(self, view="web"):
        if view.lower() == "web":
            self.get_element(*self.side_bar_nav).click()
            question_list = self.get_elements(*self.question_list)
            question_list = question_list[1:] if len(question_list) > 1 else None
            if question_list is not None:
                try:
                    self.webdriver_wait(10).until(ec.visibility_of_element_located(
                        (By.CSS_SELECTOR, self.question_list[-1])))
                except TimeoutException:
                    self.driver.execute_script("document.querySelector('%s').click()" % self.side_bar_nav[-1])
                self.webdriver_wait(10).until(ec.visibility_of_element_located(
                    (By.CSS_SELECTOR, self.question_list[-1])))
                random.choice(question_list).click()
            else:
                raise RequisiteError("'Test Requisite' assessment should have at least 2 questions")
            self.driver.execute_script("document.querySelector('%s').click()" % self.side_bar_nav[-1])
        else:
            raise NotImplementedError()

    def verify_web_assessment_screen(self, **kwargs):
        self.start_assessment_web(db=kwargs["db"])
        self.select_random_question(view="web")
        next_btn_displayed = self.get_element(*self.next_question).is_displayed()
        previous_btn_displayed = self.get_element(*self.previous_question).is_displayed()
        feedback_btn_displayed = self.get_element(*self.feed_back_btn).is_displayed()
        flag_btn_displayed = self.get_element(*self.flag_btn).is_displayed()
        displayed = [next_btn_displayed, previous_btn_displayed,
                     feedback_btn_displayed, flag_btn_displayed]
        return all(displayed)

    def saved_session(self, db):
        try:
            with open('../../config/login_web_temp.pkl', 'rb') as io_read:
                c = pickle.load(io_read)
                if not bool(c):
                    raise EOFError from None
                else:
                    return c
        except (EOFError, FileNotFoundError):
            self.login_learn_staging(db)
            return list()

    def login_learn_staging(self, context):
        user = get_data(Login_Credentials, context.login_profile, context.user_profile)
        otp, sibling_name = user["OTP"], user[context.sub_profile]["profile_name"]
        names = sibling_name.split()
        hash_sibling_name = str()
        for name in names:
            part = name.replace(name[1:], "x"*len(name[1:])).strip()
            format_part = part if names.index(name) == len(names) - 1 else part + " "
            hash_sibling_name += format_part
        chrome_driver = self.staging.chrome_driver
        wait = WebDriverWait(chrome_driver, 20)
        chrome_driver.get("https://learn-staging.byjus.com/")
        chrome_driver.find_element_by_xpath("//span[text() = 'LOGIN']").click()
        chrome_driver.find_element("id", "enterNumber").send_keys(user["mobile_number"].split("+91-")[-1])
        chrome_driver.find_element('css selector', ".enterMobileContinueButton").click()
        profiles = chrome_driver.find_elements("css selector", ".inputEleBox > div")
        retry = 3
        while not profiles or retry:
            profiles = chrome_driver.find_elements("css selector", ".inputEleBox > div")
            if profiles:
                retry = 0
            else:
                retry -= 1
            sleep(1)
        for profile in profiles:
            name = profile.find_element("css selector", ".profile-name").text
            if name == hash_sibling_name:
                profile.find_element("css selector", ".profile-radio-container > .checkmark").click()
                profiles.clear()
        wait.until(ec.element_to_be_clickable(("css selector", "button[type=submit]"))).click()
        wait.until(ec.visibility_of_element_located(("css selector", "#enterPassNumber"))).send_keys(otp)
        wait.until(ec.element_to_be_clickable(("css selector", "button[type=submit]"))).click()
        with open("../../config/login_web_temp.pkl", "wb") as fd:
            pickle.dump(chrome_driver.get_cookies(), fd)

    def resume_assessment_on_web(self, **kwargs):
        self.staging.session_relaunch()
        chrome_driver = self.staging.chrome_driver
        cookies = self.saved_session(kwargs["db"])
        wait = WebDriverWait(chrome_driver, 20)
        if cookies:
            chrome_driver.get("https://learn-staging.byjus.com/premium-school/dashboard")
            for cookie in cookies:
                chrome_driver.add_cookie(cookie)
            chrome_driver.find_element_by_xpath("//span[text() = 'LOGIN']").click()
        wait.until(ec.element_to_be_clickable(("xpath", "//*[text()=\"Byju’s Classes\"]"))).click()
        wait.until(
            ec.visibility_of_element_located(("xpath", "//*[text()=\"UPNEXT\"]")))
        up_next_header = chrome_driver.find_element("xpath", "//*[text()=\"UPNEXT\"]")
        chrome_driver.execute_script("arguments[0].scrollIntoView(true);", up_next_header)
        session_card = chrome_driver.find_element("xpath",
                                                  "//*[contains(text(), \"Unit Test\") or "
                                                  "contains(text(), \"Montly Test\") or "
                                                  "contains(text(), \"Yearly Test\")]/../../..")
        kwargs["db"].resume_btn_displayed = session_card.find_element(
            "xpath", ".//*[text()=\"RESUME\"]"
        ).is_displayed()

    def get_up_test_topic_name(self, session_type="regular"):
        sessions = self.get_elements(*self.card_root)
        for session in sessions:
            try:
                time_details = session.find_element(*self.reg_session_time).text
                topic_name = session.find_element(*self.reg_topic_name).text
            except NoSuchElementException:
                try:
                    time_details = session.find_element(*self.reg_pr_date).text
                except NoSuchElementException:
                    time_details = session.find_element(*self.reg_pre_date).text
                try:
                    topic_name = session.find_element(*self.reg_pr_topic_name).text
                except NoSuchElementException:
                    topic_name = session.find_element(*self.reg_topic_name).text
            today = datetime.now().strftime("%d")
            if today in time_details.lower() or "today" in time_details.lower():
                if session_type == "regular":
                    try:
                        subject_name = session.find_element(*self.reg_subject_name).text
                    except NoSuchElementException:
                        continue
                elif session_type == "masterclass":
                    try:
                        subject_name = session.find_element(*self.master_class.card_label_tv).text
                    except NoSuchElementException:
                        continue
                else:
                    raise NotImplementedError("subject other than 'regular' and 'masterclass' is not yet implemented.")
                return subject_name, topic_name
            else:
                return None, None
        else:
            raise Exception("No test session are scheduled today.")

    def assessment_confirmation_pop_up(self):
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.get_element("css_selector", '#exit-assessment').click()
        self.driver.switch_to.context(self.driver.contexts[0])
        try:
            msg = self.get_element(*self.pop_up_msg).text
            self.click_back()
            return "finish this assessment" in msg.lower()
        except NoSuchElementException:
            return False

    def offline_assessment(self, **kwargs):
        self.start_assessment_web(**kwargs)
        self.driver.switch_to.context(self.driver.contexts[0])
        self.toggle_wifi_connection("off")
        self.click_back()
        retry = 3
        while retry:
            try:
                self.toggle_wifi_connection("on")
                self.get_element(*self.retry).click()
                return True
            except NoSuchElementException:
                retry -= 1
                sleep(1)
        return False

    def submit_assessment_offline(self, **kwargs):
        self.start_assessment_web(**kwargs)
        self.driver.switch_to.context(self.driver.contexts[0])
        self.toggle_wifi_connection("off")
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.verify_last_question(**kwargs)
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.get_element("css_selector", "#end-assessment").click()

    def is_error_msg_displayed(self):
        self.driver.switch_to.context(self.driver.contexts[0])
        self.get_element(*self.pop_up_ok).click()
        self.driver.switch_to.context(self.driver.contexts[-1])
        message = "Unable to submit the test. Please make sure that you are connected to the internet."
        messages_inner = self.get_elements("css_selector", ".messenger-message-inner")
        for message_inner in messages_inner:
            if message_inner.is_displayed():
                return message_inner.text == message
        return False

    def book_master_class(self, **kwargs):
        self.staging.verify_and_add_slot(cohort="14", course_tag="masterclass", end_hour=0, end_minutes=3)
        self.dashboard.refresh()
        self.master_class.book_master_class(new_session=True, **kwargs)

    def complete_assessment_session(self, **kwargs):
        self.start_test()
        self.start_assessment_web(**kwargs)
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.verify_last_question(**kwargs)
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.get_element("css_selector", "#end-assessment").click()
        self.driver.switch_to.context(self.driver.contexts[0])
        self.get_element(*self.pop_up_ok).click()
        return True

    @staticmethod
    def is_session_end_time_reached():
        with open("../../test_data/classroom_details.json") as fd:
            time_details = json.load(fd)["time"]
        end_time = time_details.split("\n")[-1].split()[-1]
        current_time = datetime.now().strftime("%H %M")
        eh, em = list(map(int, end_time.split(":")))
        ch, cm = list(map(int, current_time.split()))
        if ch > eh or (ch == eh and cm > em):
            return True
        else:
            return False

    def is_assessment_displayed_in_completed_tab(self):
        self.dashboard.ps_home_page_tab(tab_name="completed")
        card = self.get_element(*self.card_root)
        try:
            subj_name = card.find_element(*self.reg_subject_name).text
        except NoSuchElementException:
            subj_name = card.find_element(*self.master_class.card_label_tv).text
        date_month = card.find_element(*self.reg_pr_date).text
        cd_cm = datetime.now().strftime("%d %b")
        return "test" in subj_name.lower() and date_month == cd_cm

    def is_start_test_btn_displayed_at_start_time(self):
        with open("../../test_data/classroom_details.json") as fd:
            details = json.load(fd)
        session_time_dt = details["time"].split("\n")
        start_time = session_time_dt[-1].split()[0]
        time_now = datetime.now().strftime("%H %M")
        sh, sm = list(map(int, start_time.split(":")))
        ch, cm = list(map(int, time_now.split()))
        if sh == ch:
            if sm > cm:
                diff = sm - cm
            else:
                diff = 0
        elif sh > ch:
            if sm < cm:
                diff = 60 - cm
            else:
                diff = sm - cm
        else:
            diff = 0
        diff *= 60
        print(f"waiting for up to {diff} minutes.")
        while diff:
            try:
                return self.get_element(*self.start_test_btn).is_displayed()
            except NoSuchElementException:
                if diff % 20 == 0:
                    print("waiting for start button to be displayed...")
                sleep(1)
                diff -= 1
        else:
            return self.get_element(*self.start_test_btn).is_displayed()
