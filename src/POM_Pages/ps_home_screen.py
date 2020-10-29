import logging
import re
import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from Utilities.tutor_common_methods import TutorCommonMethods
from src.POM_Pages.application_login import Login
from Utilities.common_methods import CommonMethods

CommonMethods = CommonMethods()


class PS_Homescreen:
    def __init__(self, driver):
        self.obj = TutorCommonMethods(driver)
        self.login = Login(driver)
        self.driver = driver
        self.action = TouchAction(driver)
        self.ps_tabs = 'androidx.appcompat.app.ActionBar$Tab'
        self.for_you_tab = '//androidx.appcompat.app.ActionBar.Tab[@content-desc="For you"]/android.widget.TextView'
        self.get_help = 'com.byjus.thelearningapp.premium:id/optionalNav'
        self.back_navigation = 'com.byjus.thelearningapp.premium:id/backNav'
        self.bottom_sheet ='com.byjus.thelearningapp.premium:id/bottomSheet'
        self.close_chat ='com.byjus.thelearningapp.premium:id/closeChatBtn'

    def verify_ps_tabs(self, expected_text):
        text_elements = self.obj.get_elements('class_name', self.ps_tabs)
        for element in text_elements:
            if expected_text == element.get_attribute('content-desc'):
                return True
        return False

    def tap_on_tab(self,text):
        self.obj.get_element('xpath', '//androidx.appcompat.app.ActionBar.Tab[@content-desc="'+text+'"]/android.widget.TextView').click()

    def is_tab_selected(self,text):
        try:
            displayed = self.obj.get_element('xpath', '//androidx.appcompat.app.ActionBar.Tab[@content-desc="'+text+'"]/android.widget.TextView').is_selected()
            if displayed:
                return True
            return False
        except NoSuchElementException:
            return None

    def click_back(self):
        self.obj.click_back()

    def tap_on_get_help(self):
        self.obj.get_element('id',self.get_help).click()
        time.sleep(2)
        self.obj.click_back()

    def is_get_help_present(self):
        return self.obj.is_element_present('id', self.get_help)

    def is_back_nav_present(self):
        return self.obj.is_element_present('id', self.back_navigation)

    def is_bottom_sheet_present(self):
        return self.obj.is_element_present('id',self.bottom_sheet)

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
        self.obj.is_button_enabled(text)

    def verify_completed_card_details(self):
        subject_name = self.obj.get_element('xpath', '//*[contains(@resource-id, "subject_name")]').text
        if self.obj.is_element_present('xpath', '//*[contains(@resource-id, "session_title")]'):
            topic_name = self.obj.get_element('xpath', '//*[contains(@resource-id, "session_title")]').text
        else:
            topic_name = self.obj.get_element('xpath', '//*[contains(@resource-id, "topic_name")]').text
        session_date = self.obj.get_element('xpath', '//*[contains(@resource-id, "post_requisite_date")]').text
        session_status = self.obj.get_element('xpath', '//*[contains(@resource-id, "post_requisite_status")]').text
        details_dict = {
            "Subject": subject_name,
            "Topic": topic_name,
            "Schedule Date": session_date,
            "Session status": session_status
        }
        assert all(v is not None for v in [subject_name, topic_name, session_date,
                                           session_status]), "Completed Session card details not loaded"
        return details_dict

    def tap_outside_dialog_layout(self):
        self.action.tap(None, x=100, y=100).release().perform()