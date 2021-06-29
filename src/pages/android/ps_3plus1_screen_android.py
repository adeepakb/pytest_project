import re
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from pages.base.ps3_plus1_screen_base import PS_3Plus1ScreenBase
from utilities.tutor_common_methods import TutorCommonMethods
from pages.android.login_android import LoginAndroid
from utilities.common_methods import CommonMethods

CommonMethods = CommonMethods()


class ReturnType():
    def __init__(self, result, reason):
        self.result = result
        self.reason = reason


class PS_3Plus1ScreenAndroid(PS_3Plus1ScreenBase):
    def __init__(self, driver):
        self.obj = TutorCommonMethods(driver)
        self.login = LoginAndroid(driver)
        self.driver = driver
        self.action = TouchAction(driver)
        self.calender_icon = 'com.byjus.thelearningapp.premium:id/ivSessionCalendar'
        self.time_icon = 'com.byjus.thelearningapp.premium:id/ivTime'
        self.date = 'com.byjus.thelearningapp.premium:id/sessionDatetv'
        self.time = 'com.byjus.thelearningapp.premium:id/timeTv'
        self.roundedNavButton = 'com.byjus.thelearningapp.premium:id/roundedNavButton'
        self.cardArrowButton = 'com.byjus.thelearningapp.premium:id/cardArrowButton'
        self.subject_names = 'com.byjus.thelearningapp.premium:id/subject_name'
        self.date_time = 'com.byjus.thelearningapp.premium:id/session_time'
        self.choose_topic_title = 'com.byjus.thelearningapp.premium:id/tvChooseTopicTitle'
        self.choose_topic_select = 'com.byjus.thelearningapp.premium:id/ivChooseTopicSelectButton'
        self.topic_list = 'com.byjus.thelearningapp.premium:id/rv_topics'
        self.content_cards = 'com.byjus.thelearningapp.premium:id/content_card'
        self.extra_session_tag = 'com.byjus.thelearningapp.premium:id/extra_session_tag'
        self.session_desc = 'com.byjus.thelearningapp.premium:id/sessionDescriptionTv'
        self.ps_tabs = 'androidx.appcompat.app.ActionBar$Tab'

    def is_calendar_with_date_present(self):
        if self.obj.is_element_present('id', self.calender_icon) and self.obj.is_element_present('id', self.date):
            return ReturnType(True, 'Date is displayed with the calendar icon')
        else:
            return ReturnType(False, 'Date is not displayed with the calendar icon')

    def is_timestamp_with_time_present(self):
        if self.obj.is_element_present('id', self.time_icon) and self.obj.is_element_present('id', self.time):
            return ReturnType(True, 'Time is displayed with the timestamp icon')
        else:
            return ReturnType(False, 'Time is not displayed with the timestamp icon')

    def is_back_button_present(self):
        if self.obj.is_element_present('id', self.roundedNavButton):
            return ReturnType(True, 'back icon is present')
        else:
            return ReturnType(False, 'back icon is not present')

    def is_forward_button_present(self):
        if self.obj.is_element_present('id', self.cardArrowButton):
            return ReturnType(True, 'forward icon is present')
        else:
            return ReturnType(False, 'forward icon is not present')

    def verify_optional_mandatory_class_present(self):
        mandatory_subjects = ['BIOLOGY', 'CHEMISTRY', 'PHYSICS', 'MATHEMATICS']
        optional_subject = 'SELECT A TOPIC'
        mandatory_subject_found = False
        optional_subject_found = False
        self.obj.scroll_to_element('SELECT A TOPIC')
        subject_names_element = self.obj.get_elements('id', self.subject_names)
        for element in subject_names_element:
            subject = element.text
            if subject in mandatory_subjects:
                mandatory_subject_found = True
            if subject == optional_subject:
                optional_subject_found = True
        if mandatory_subject_found and optional_subject_found:
            return ReturnType(True, "Both mandatory and optional sessions are displayed")
        else:
            return ReturnType(True, "Both mandatory and optional sessions are not displayed")

    def is_date_time_present(self):
        if self.obj.is_element_present('id', self.date_time):
            return ReturnType(True,"Date and time are displayed")
        else:
            return ReturnType(True, "Date and time are not displayed")

    def verify_change_topic_not_present_mandatory_session(self):
        mandatory_subjects = ['BIOLOGY', 'CHEMISTRY', 'PHYSICS', 'MATHEMATICS']
        subject_names_element = self.obj.get_elements('id', self.subject_names)
        for element in subject_names_element:
            subject = element.text
            if subject in mandatory_subjects:
                element.click()
                assert not self.obj.is_text_match(
                    "Choose your topic"), "Choose topic option is present for mandatory session "
                self.obj.get_element('id', self.roundedNavButton).click()

    def find_latest_mandatory_topic(self):
        mandatory_subjects = ['BIOLOGY', 'CHEMISTRY', 'PHYSICS', 'MATHEMATICS']
        content_cards = self.obj.get_elements('id', self.content_cards)
        title = None
        for card in content_cards:
            subject = card.find_element_by_xpath('//*[contains(@resource-id, "subject_name")]').text
            if subject in mandatory_subjects:
                title = card.find_element_by_xpath('//*[contains(@resource-id, "session_title")]').text
        return title

    def verify_date_time_format(self):
        session_date = self.obj.get_element('id', self.date_time).text
        m = re.match(
            "(([0-3][0-9] (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec), (Sunday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday))|(Today)), ((([1-9])|(1[0-2])):([0-5])(0|5)\s(A|P)M)",
            session_date)
        assert m is not None, "Session date is not in DD MMM,DAY format " \
                              "and time is not in H:MM AM/PM format"

    def card_arrow_button_click(self):
        self.obj.get_element('id', self.cardArrowButton).click()

    # def verify_choose_topic_screen(self):
    #     self.obj.get_element('id', self.cardArrowButton).click()
    #     return self.obj.is_element_present('id', self.choose_topic_title) and \
    #            self.obj.is_element_present('id', self.choose_topic_select) and self.obj.is_text_match(
    #         "Choose your topic")

    def verify_topic_select_button(self):
        topic_list = self.obj.get_elements('id', self.topic_list)
        for topic in topic_list:
            try:
                choose_topic_title = topic.find_element_by_xpath(
                    '//*[contains(@resource-id, "tvChooseTopicTitle")]').is_displayed()
                choose_topic_select = topic.find_element_by_xpath(
                    '//*[contains(@resource-id, "ivChooseTopicSelectButton")]').is_displayed()
                return ReturnType(choose_topic_title and choose_topic_select,"choose topic screen consists of the topic list with radio button")
            except NoSuchElementException:
                return ReturnType(False,"choose topic screen does not consist of the topic list with radio button")


    def tap_back_icon(self):
        self.obj.get_element('id', self.roundedNavButton).click()

    def verify_choose_topic_title(self, latest_topic_title):
        topic_title_list = self.obj.get_elements('id', self.choose_topic_title)
        flag = False
        for choose_topic in topic_title_list:
            choose_topic_title = choose_topic.text
            if int(choose_topic_title.split()[1]) <= int(latest_topic_title.split()[1]):
                flag = True
        if flag:
            return ReturnType(flag, "choose topic list consist of topics which are mandatory && occurred in past")
        else:
            return ReturnType(flag, "choose topic list doesn't consist of topics which are mandatory && occurred in past")

    def select_first_topic(self):
        topic_select_list = self.obj.get_elements('id', self.choose_topic_select)
        topic_select_list[0].click()

    def verify_extra_session_booked(self):
        try:
            self.obj.get_element('id', self.extra_session_tag).is_displayed()
            flag = True
        except NoSuchElementException:
            flag = False
        if flag:
            return ReturnType(flag, "User has booked revision class")
        else:
            return ReturnType(flag, "User doesn't have any booked revision class")

    def tap_on_booked_extra_session(self):
        self.obj.get_element('id', self.extra_session_tag).click()

    def is_session_desc_present(self):
        if self.obj.is_element_present('id', self.session_desc):
            return ReturnType(True, "Selected topic summary is displayed")
        else:
            return ReturnType(False, "Selected topic summary is not displayed")

    def change_topic_and_verify(self):
        self.obj.click_link("Change Your Topic")
        topic_title_list = self.obj.get_elements('id', self.choose_topic_title)
        updated_topic_title = topic_title_list[1].text
        topic_select_list = self.obj.get_elements('id', self.choose_topic_select)
        topic_select_list[1].click()
        self.obj.button_click("Done")
        assert self.obj.is_text_match(updated_topic_title), "Topic not changed"

    def verify_ps_tabs(self, expected_text):
        text_elements = self.obj.get_elements('class_name', 'android.widget.LinearLayout')
        for element in text_elements:
            if expected_text == element.get_attribute('content-desc'):
                return ReturnType(True, '%s Tab is present' % expected_text)
        return ReturnType(False, '%s Tab is not present' % expected_text)

    def tap_on_tab(self, text):
        self.obj.get_element('xpath',
                             '//android.widget.LinearLayout[@content-desc="' + text + '"]/android.widget.TextView').click()
