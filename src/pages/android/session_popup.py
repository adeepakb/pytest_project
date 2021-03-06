import logging
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from utilities.tutor_common_methods import TutorCommonMethods
from pages.android.student_session import StudentSessionAndroid


class SessionAlert(TutorCommonMethods):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.studentsession = StudentSessionAndroid(driver)
        self.title_download_popup = '//*[contains(@resource-id, "txt_title_popup")]'
        self.download_btn = '//*[contains(@resource-id, "download_button")]'
        self.cancel_download_btn = '//*[contains(@resource-id, "CancelDownload")]'

    def verify_popup_present(self):
        timeout = 15
        while timeout:
            try:
                element = self.driver.find_element_by_xpath(
                    '//*[contains(@resource-id, "dialog_layout")]').is_displayed()
                logging.debug('session popup is displayed')
                break
            except (NoSuchElementException,StaleElementReferenceException):
                timeout -= 5
        logging.debug('session popup is not displayed')

    def join_session_btn(self):
        self.driver.find_element_by_xpath(
            '//*[contains(@resource-id, "btnJoinSession")]').click()

    def get_session_details(self):
        subject_name = self.driver.find_element_by_xpath(
            '//*[contains(@resource-id, "SubjectName")]').text
        topic_name = self.driver.find_element_by_xpath(
            '//*[contains(@resource-id, "TopicName")]').text
        session_started_time = self.driver.find_element_by_xpath(
            '//*[contains(@resource-id, "TimeStamp")]').text

    def cancel_join_session(self):
        try:
            self.driver.find_element_by_xpath(
                '//*[contains(@resource-id, "tvCancel")]').click()
        except (NoSuchElementException, StaleElementReferenceException):
            logging.log(10, "UP NEXT session pop up is not displayed")

    def get_session_card_details(self):
        subject_name = self.driver.find_element_by_xpath(
            '//*[contains(@resource-id, "subjectName")]').text
        topic_name = self.driver.find_element_by_xpath(
            '//*[contains(@resource-id, "chapterName")]').text
        session_time = self.driver.find_element_by_xpath(
            '//*[contains(@resource-id, "sessionTime")]').text
        details = [subject_name, topic_name, session_time]
        return details

    def content_card_loaded(self):
        subject_name = self.get_element('xpath', '//*[contains(@resource-id, "subject_name")]').text
        try:
            topic_name = self.get_element('xpath', '//*[contains(@resource-id, "session_title")]').text
        except NoSuchElementException:
            topic_name = self.get_element('xpath', '//*[contains(@resource-id, "topic_name")]').text
        try:
            session_time = self.get_element('xpath', '//*[contains(@resource-id, "session_time")]').text
        except NoSuchElementException:
            try:
                session_time = self.get_element('xpath', '//*[contains(@resource-id, "pre_requisite_time")]').text
            except NoSuchElementException:
                session_time = self.get_element('xpath', '//*[contains(@resource-id, "post_requisite_date")]').text
        content_dict = {
            "Subject": subject_name,
            "Topic": topic_name,
            "Schedule Time": session_time,
        }
        assert all(v is not None for v in [subject_name, topic_name, session_time]), "content card not loaded"
        return content_dict


    def verify_session_card_details_loaded(self):
        subject_name = self.get_element('xpath', '//*[contains(@resource-id, "subjectNametv")]').text
        topic_name = self.get_element('xpath', '//*[contains(@resource-id, "chapterNametv")]').text
        session_date = self.get_element('xpath', '//*[contains(@resource-id, "sessionDatetv")]').text
        session_time = self.get_element('xpath', '//*[contains(@resource-id, "timeTv")]').text
        details_dict = {
            "Subject": subject_name,
            "Topic": topic_name,
            "Schedule Date": session_date,
            "Schedule Time": session_time,
        }
        assert all(v is not None for v in [subject_name, topic_name, session_time, session_date]), "Session card details not loaded"
        return details_dict


    def is_asset_download_present(self):
        self.driver.implicitly_wait(5)
        try:
            self.get_element('xpath', self.title_download_popup)
            return True
        except NoSuchElementException:
            return False


    def download_asset(self):
        if self.is_asset_download_present():
            try:
                self.get_element('xpath', self.download_btn).click()
            except NoSuchElementException:
                pass


    def cancel_download_asset(self):
        if self.is_asset_download_present():
            try:
                self.get_element('xpath', self.cancel_download_btn).click()
            except NoSuchElementException:
                pass