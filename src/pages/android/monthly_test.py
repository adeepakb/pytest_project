import re
import time
from datetime import datetime, timedelta
from time import sleep

from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException

from pages.android.application_login import Login
from pages.android.scroll_cards import ScrollCards
from pages.android.session_requisite import SessionRequisite
from utilities.staging_tllms import Stagingtllms
from pages.android.student_dashboard_otm import StudentDashboardOneToMega
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



    def verify_session_card_details(self, detail=None):
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
            w_t = self.get_element(*self.wish_text).text
            if w_t == "Good luck for the test":
                return True
            return False
        elif detail == "start test button":
            btn_text = self.get_element(*self.start_test_btn).text
            if btn_text == "Start Test":
                return True
            return False
        elif detail == "test icon":
            return self.get_element(*self.assessment_bg).is_displayed()
        elif detail=='topic_name_for_pre_post':
            return self.get_element(*self.topic_name_for_pre_post).is_displayed()
        elif detail == 'status':
            return self.get_element(*self.status).is_displayed()
        elif detail == 'heading':
            return self.get_element(*self.heading).is_displayed()



    def is_test_card_displayed(self):
        card = self.get_element(*self.card_root)
        title = card.find_element(*self.subject_name).text.lower()
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
















