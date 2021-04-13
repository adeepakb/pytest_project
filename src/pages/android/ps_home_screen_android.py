import re
import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from utilities.staging_tlms import Stagingtlms
from utilities.tutor_common_methods import TutorCommonMethods
from pages.android.login_android import LoginAndroid
from utilities.common_methods import CommonMethods
from pages.base.ps_home_screen_base import PSHomeScreenBase
CommonMethods = CommonMethods()


class PS_Homescreen_Android(PSHomeScreenBase):
    def __init__(self, driver):
        self.obj = TutorCommonMethods(driver)
        self.login = LoginAndroid(driver)
        self.driver = driver
        self.action = TouchAction(driver)
        self.ps_tabs = 'androidx.appcompat.app.ActionBar$Tab'
        self.for_you_tab = '//androidx.appcompat.app.ActionBar.Tab[@content-desc="For you"]/android.widget.TextView'
        self.get_help = 'com.byjus.thelearningapp.premium:id/optionalNav'
        self.back_navigation = 'com.byjus.thelearningapp.premium:id/backNav'
        self.bottom_sheet = 'com.byjus.thelearningapp.premium:id/bottomSheet'
        self.close_chat = 'com.byjus.thelearningapp.premium:id/closeChatBtn'
        self.arrow_button = 'com.byjus.thelearningapp.premium:id/arrow_btn'
        self.requisite_items = 'com.byjus.thelearningapp.premium:id/llRequisiteContentLyt'
        self.home_tabs = 'com.byjus.thelearningapp.premium:id/premium_school_home_tabs'
        self.home_page_title = 'com.byjus.thelearningapp.premium:id/toolbar_title'
        self.design_bottom_sheet = 'com.byjus.thelearningapp.premium:id/design_bottom_sheet'
        self.bottom_sheet_book = 'com.byjus.thelearningapp.premium:id/bt_primaryAction'
        self.bottom_sheet_dismiss ='com.byjus.thelearningapp.premium:id/tv_secondaryAction'
        self.byjus_classes_banner= 'com.byjus.thelearningapp.premium:id/ivMarketingBannerTop'

    def verify_ps_tabs(self, expected_text):
        text_elements = self.obj.get_elements('class_name', self.ps_tabs)
        for element in text_elements:
            if expected_text == element.get_attribute('content-desc'):
                return True
        return False

    def tap_on_tab(self, text):
        self.obj.get_element('xpath',
                             '//android.widget.LinearLayout[@content-desc="' + text + '"]/android.widget.TextView').click()

    def verify_arrow_present_for_each_requisite(self):
        if len(self.obj.get_elements('id', self.requisite_items)) == len(self.obj.get_elements('id', self.arrow_button)):
            return True
        else:
            return False

    def is_tab_selected(self, text):
        try:
            displayed = self.obj.get_element('xpath',
                                             '//android.widget.LinearLayout[@content-desc="' + text + '"]/android.widget.TextView').is_selected()
            if displayed:
                return True
            return False
        except NoSuchElementException:
            return None

    def click_back(self):
        self.obj.click_back()

    def tap_on_get_help(self):
        self.obj.get_element('id', self.get_help).click()
        time.sleep(8)
        self.obj.click_back()

    def is_get_help_present(self):
        return self.obj.is_element_present('id', self.get_help)

    def is_back_nav_present(self):
        return self.obj.is_element_present('id', self.back_navigation)

    def is_bottom_sheet_present(self):
        return self.obj.is_element_present('id', self.bottom_sheet)

    def close_get_help(self):
        self.obj.get_element('id', self.close_chat).click()

    def verify_get_help_close(self):
        return self.obj.is_element_present('id', self.close_chat)

    def verify_card_details(self):
        subject_name = self.driver.find_element_by_xpath(
            '//*[contains(@resource-id, "subject_name")]').text
        topic_name = self.driver.find_element_by_xpath(
            '//*[contains(@resource-id, "session_title")]').text
        session_time = self.driver.find_element_by_xpath(
            '//*[contains(@resource-id, "session_time")]').text

        assert all(v is not None for v in [subject_name, topic_name]), "Session card details not loaded"
        m = re.match(
            "[0-3][0-9] (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec), (Sunday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday)|(Today), [01]?[0-9]:[0-5][0-9] (AM|PM)",
            session_time)
        assert m is not None, "Session time is in DD MMM,DAY, HH:MM am/pm format"

    def verify_session_details_card_loaded(self):
        subject_name = self.obj.get_element('xpath', '//*[contains(@resource-id, "subjectNametv")]').text
        topic_name = self.obj.get_element('xpath', '//*[contains(@resource-id, "chapterNametv")]').text
        session_date = self.obj.get_element('xpath', '//*[contains(@resource-id, "sessionDatetv")]').text
        session_time = self.obj.get_element('xpath', '//*[contains(@resource-id, "timeTv")]').text
        session_desc = self.obj.get_element('xpath', '//*[contains(@resource-id, "sessionDescriptionTv")]').text
        details_dict = {
            "Subject": subject_name,
            "Topic": topic_name,
            "Schedule Date": session_date,
            "Schedule Time": session_time,
            "Session Desc": session_desc
        }
        assert all(v is not None for v in [subject_name, topic_name, session_time, session_date,
                                           session_desc]), "Session card details not loaded"
        return details_dict

    def verify_button(self, text):
        self.obj.is_button_displayed(text)
        return self.obj.is_button_enabled(text)

    def attach_post_requisite_with_assessement(self, driver,assessment_name):
        Stagingtlms(driver).attach_requisite(assessment_name)

    def detach_post_requisite(self,driver):
        Stagingtlms(driver).detach_requisite()

    def verify_completed_card_details(self):
        subject_name = self.obj.get_element('id', 'com.byjus.thelearningapp.premium:id/subject_name').text
        if self.obj.is_element_present('id', 'com.byjus.thelearningapp.premium:id/session_title'):
            topic_name = self.obj.get_element('id', 'com.byjus.thelearningapp.premium:id/session_title').text
        else:
            topic_name = self.obj.get_element('id', 'com.byjus.thelearningapp.premium:id/topic_name').text
        session_status = self.obj.get_element('id', 'com.byjus.thelearningapp.premium:id/post_requisite_status').text
        session_date = self.obj.get_element('id', 'com.byjus.thelearningapp.premium:id/post_requisite_date').text
        details_dict = {
            "Subject": subject_name,
            "Topic": topic_name,
            "Schedule Date": session_date,
            "Session status": session_status
        }
        assert (all(v is not None for v in [subject_name,topic_name, session_date,session_status]) and session_status == "Completed"), "Completed Session card details not loaded"
        return details_dict

    def tap_outside_dialog_layout(self):
        self.action.tap(None, x=100, y=100).release().perform()

    def is_user_in_ps_page(self):
        return (self.obj.get_element('id', self.home_page_title).text == 'Classes' and
                self.obj.get_element('id', self.home_tabs).is_displayed())

    def verify_bottom_sheet(self):
        return (self.obj.get_element('id','com.byjus.thelearningapp.premium:id/tv_title').text == "BYJU's Classes" and
                self.obj.get_element('id', self.bottom_sheet_book).text == 'Book a Free Trial' and
                self.obj.get_element('id', self.bottom_sheet_dismiss).text == 'Dismiss' and
                self.obj.get_element('id', self.design_bottom_sheet).is_displayed())

    def verify_banner(self):
        return self.obj.get_element('id',self.byjus_classes_banner)
