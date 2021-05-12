import re
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

    def __init_locators(self, device_type):
        package_name = self.driver.capabilities['appPackage'] + ':id'
        self.card_root = "id", "%s/card" % package_name
        self.subject_name = "id", "%s/subject_name" % package_name
        self.topic_name = "id", "%s/session_title" % package_name
        self.session_time = "id", "%s/session_time" % package_name
        self.wish_text = "id", "%s/strip_title" % package_name
        self.start_test_btn = "id", "%s/card_strip_btn" % package_name
        self.assessment_bg = "id", "%s/iv_assessment_bg" % package_name

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

    def is_test_card_displayed(self):
        card = self.get_element(*self.card_root)
        title = card.find_element(*self.subject_name).text.lower()
        if "test" in title:
            return True
        return False
