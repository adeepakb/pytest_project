import time
import logging
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException, \
    StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from constants.constants import Login_Credentials
from utilities.staging_tlms import Stagingtlms
from constants.load_json import getdata
from utilities.tutor_common_methods import TutorCommonMethods


class MentorSession:
    def __init__(self, driver):
        self.driver = driver
        self.obj = TutorCommonMethods(driver)
        self.chrome_options = Options()
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--headless')
        self.chrome_driver = webdriver.Chrome(options=self.chrome_options)
        self.tlms = Stagingtlms(driver)
        self.byjus_icon = "//img[contains(@src,'data:image/png')]"
        self.subject = '//*[@class = "subjectText"]'
        self.topic = '//*[@class = "topicText"]'
        self.chat_container = '//div[@class= "chatContainer"]'
        self.chat_toggle = '//span[@class= "MuiSwitch-root"]'
        self.live_chat_close = "//img[@class='chatCloseIcon']"
        self.end_button_timer = '//*[@class= "session-button timer"]'
        self.end_button = '//*[text() = "End Session Now"]'
        self.live_chat_header = "//*[text()='Live Chat']"
        self.up_arrow_button = '//*[@class= "fa fa-angle-up"]'
        self.type_something_inputcard = '//input[@placeholder="Type something"]'
        self.relaunch_error = "//*[contains(@class ,'Mui-error')]"
        self.chat_icon = "//img[@src='/static/media/chatPopup.3398527e.svg']"
        self.ban = "//*[@class='action']"
        self.ban_student_cancel = "//div[@class='popupActionButton' and text()='Cancel']"
        self.ban_student_ban = "//div[@class='popupActionButton' and text()='Ban']"
        self.ban_student_popup = "//div[@class ='popupWrapper']"
        self.reply_button = "//*[@class='replyBtn']"
        self.approve_message = "//*[@id='approve_svg__b']"
        self.reject_message = "//*[@id='reject_svg__b']"
        self.exo_overlay = '//*[@resource-id = "com.byjus.thelearningapp.premium:id/exo_overlay"]'

    def is_byjus_icon_present(self):
        self.wait_for_locator_webdriver(self.byjus_icon)
        return self.chrome_driver.find_element_by_xpath(self.byjus_icon).is_displayed()

    def get_subject_name(self):
        self.wait_for_locator_webdriver(self.subject)
        return self.chrome_driver.find_element_by_xpath(self.subject).text

    def get_topic_name(self):
        self.wait_for_locator_webdriver(self.topic)
        return self.chrome_driver.find_element_by_xpath(self.topic).text

    def is_chat_box_present(self):
        self.wait_for_locator_webdriver(self.chat_container)
        return self.chrome_driver.find_element_by_xpath(self.chat_container).is_displayed()

    def is_toggle_present(self):
        self.wait_for_locator_webdriver(self.chat_toggle)
        return self.chrome_driver.find_element_by_xpath(self.chat_toggle).is_displayed()

    def is_end_button_present(self):
        self.wait_for_locator_webdriver(self.end_button)
        return self.chrome_driver.find_element_by_xpath(self.end_button).is_displayed()

    def tutor_end_session(self):
        self.wait_for_clickable_element_webdriver(self.end_button_timer)
        self.chrome_driver.find_element_by_xpath(self.end_button_timer).click()
        self.wait_for_clickable_element_webdriver(self.end_button)
        self.chrome_driver.find_element_by_xpath(self.end_button).click()
        self.wait_for_locator_webdriver("//button[@class = 'endBtn']")
        self.chrome_driver.find_element_by_xpath("//button[@class = 'endBtn']").click()

    def close_mentor_session_tab(self):
        self.chrome_driver.close()

    def wait_for_locator_webdriver(self, locator_value):
        try:
            WebDriverWait(self.chrome_driver, 15).until(EC.presence_of_element_located((By.XPATH, locator_value)))
        except TimeoutException:
            print("Timed out while waiting for page to load")

    def wait_for_clickable_element_webdriver(self, locator_value):
        try:
            WebDriverWait(self.chrome_driver, 15).until(EC.element_to_be_clickable((By.XPATH, locator_value)))
        except TimeoutException:
            print("Timed out while waiting for page to load")

    def toggle_chat(self, text):
        current_toggle_status = self.check_toggle_state()
        if text == "off" and current_toggle_status:
            self.wait_for_locator_webdriver(self.chat_toggle)
            self.chrome_driver.find_element_by_xpath(self.chat_toggle).click()
        elif text == "on" and (not current_toggle_status):
            self.wait_for_locator_webdriver(self.chat_toggle)
            self.chrome_driver.find_element_by_xpath(self.chat_toggle).click()
        else:
            pass

    def check_toggle_state(self):
        try:
            checked_flag = self.chrome_driver.find_element_by_xpath(
                "//*[contains(@class,'Mui-checked')]").is_displayed()
        except NoSuchElementException:
            checked_flag = False
        return checked_flag

    def page_refresh(self):
        self.chrome_driver.refresh()

    def verify_type_something_text(self):
        self.wait_for_locator_webdriver(self.type_something_inputcard)
        assert self.chrome_driver.find_element_by_xpath(
            self.type_something_inputcard).is_displayed(), "Type something text is not present"

    def verify_zero_online_text(self):
        self.wait_for_locator_webdriver("//*[@class='online']")
        assert self.chrome_driver.find_element_by_xpath(
            "//*[@class='online']").text == 'Online', "Online text is not present"

    def is_icon_selected(self, icon):
        xpath = getattr(self, "%s_icon" % icon, None)
        if xpath is None:
            raise
        self.wait_for_locator_webdriver(xpath)
        element = self.chrome_driver.find_element_by_xpath(xpath)
        parent_classname = self.chrome_driver.execute_script('return arguments[0].parentNode.className', element)
        assert 'toolActiveBtn' in parent_classname, "Icon is not selected"

    def send_message_in_chat(self, text):
        timeout = 15
        while timeout:
            try:
                self.chrome_driver.find_element_by_xpath(self.type_something_inputcard).send_keys(text)
                self.chrome_driver.find_element_by_xpath(self.type_something_inputcard).send_keys(Keys.RETURN)
                break
            except (NoSuchElementException, ElementNotInteractableException):
                timeout -= 5
                logging.debug('chat is not displayed')

    def login_as_tutor(self):
        path = '../config/config.json'
        email = str(getdata(path, 'staging_access', 'email'))
        password = str(getdata(path, 'staging_access', 'password'))
        self.chrome_driver.get('https://staging.tllms.com/admin')
        self.chrome_driver.maximize_window()
        self.wait_for_locator_webdriver("//input[@id='email']")
        self.chrome_driver.find_element_by_xpath("//input[@id='email']").send_keys(email)
        self.wait_for_locator_webdriver("//button[@type='submit']")
        self.chrome_driver.find_element_by_xpath("//button[@type='submit']").click()
        self.wait_for_locator_webdriver("//input[@type='email']")
        self.chrome_driver.find_element_by_xpath("//input[@type='email']").send_keys(email)
        self.chrome_driver.find_element_by_xpath("//input[@type='email']").send_keys(Keys.ENTER)
        self.wait_for_clickable_element_webdriver("//input[@type='password']")
        self.chrome_driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
        self.chrome_driver.find_element_by_xpath("//input[@type='password']").send_keys(Keys.ENTER)

    def start_tutor_session(self, course='primary'):
        url = self.tlms.get_tutor_url(course)
        self.login_as_tutor()
        self.wait_for_locator_webdriver("//li[@id='mentoring']")
        self.chrome_driver.get(url)
        self.wait_for_locator_webdriver("//span[contains(text(),'LOGIN')]")
        self.chrome_driver.save_screenshot("image2.png")
        self.chrome_driver.find_element_by_xpath("//span[contains(text(),'LOGIN')]").click()
        return url

    # def wait_for_reset_buffer_time_to_complete(self):
    #     WebDriverWait(self.chrome_driver, 120).until(EC.invisibility_of_element_located((By.XPATH, )))

    def wait_for_reset_buffer_time_to_complete(self):
        # keeping appium driver alive while waiting for session to start during buffer time
        for i in range(10):
            try:
                video_present =self.driver.find_element_by_xpath(self.exo_overlay).is_displayed()
                endpopup_present =self.chrome_driver.find_element_by_xpath("//div[@class='endPopupContainer']").is_displayed()
                if endpopup_present and (not video_present) :
                    time.sleep(10)
            except (NoSuchElementException,TimeoutException):
                break


    def verify_tutor_unable_to_join_session_again(self):
        self.wait_for_locator_webdriver("//span[contains(text(),'LOGIN')]")
        self.chrome_driver.find_element_by_xpath("//span[contains(text(),'LOGIN')]").click()
        self.wait_for_locator_webdriver(self.relaunch_error)
        error_message = self.chrome_driver.find_element_by_xpath(self.relaunch_error).text
        assert ('Your session is ended' in error_message), "Tutor is able to join session again even after ending " \
                                                           "session "
        self.chrome_driver.close()

    def reopen_chrome_browser(self, tutor_url):
        self.chrome_driver = webdriver.Chrome()
        self.login_as_tutor()
        self.wait_for_locator_webdriver("//li[@id='mentoring']")
        self.chrome_driver.get(tutor_url)
        self.wait_for_locator_webdriver("//span[contains(text(),'LOGIN')]")
        self.chrome_driver.find_element_by_xpath("//span[contains(text(),'LOGIN')]").click()

    def verify_ban_approve_reject_present(self):
        is_ban_present = self.chrome_driver.find_element_by_xpath(self.ban).is_displayed()
        is_approve_present = self.chrome_driver.find_element_by_css_selector('#approve_svg__b').is_displayed()
        is_reject_present = self.chrome_driver.find_element_by_css_selector('#reject_svg__b').is_displayed()
        return is_ban_present and is_approve_present and is_reject_present

    def verify_tutor_chat_window(self):
        self.wait_for_clickable_element_webdriver(self.chat_icon)
        self.chrome_driver.find_element_by_xpath(self.chat_icon).click()
        self.wait_for_locator_webdriver(self.live_chat_header)
        time.sleep(3)
        assert self.chrome_driver.find_element_by_xpath(
            self.live_chat_header).is_displayed(), "Live chat header is not present"
        self.wait_for_locator_webdriver(self.live_chat_close)
        assert self.chrome_driver.find_element_by_xpath(
            self.live_chat_close).is_displayed(), "chat close icon is not present"
        self.verify_type_something_text()
        assert self.chrome_driver.find_element_by_xpath(self.type_something_inputcard).is_enabled(), \
            "text field is not enabled.No cursor in the text field"

    def verify_student_name_present(self):
        user_name = getdata(Login_Credentials, 'login_detail3', 'profile_one_to_many_and_mega')
        assert self.chrome_driver.find_element_by_xpath(
            "//*[text()='" + user_name + "']").is_displayed(), "student name is not present"

    def tap_chat_icon(self):
        self.wait_for_clickable_element_webdriver(self.chat_icon)
        self.chrome_driver.find_element_by_xpath(self.chat_icon).click()

    def tap_ban_icon(self):
        self.wait_for_clickable_element_webdriver(self.ban)
        self.chrome_driver.find_element_by_xpath(self.ban).click()

    def verify_ban_options_and_buttons(self):
        self.wait_for_locator_webdriver(self.ban_student_popup)
        expected_option_list = ['Inappropriate Content', 'Abusive Language', 'Content Sharing', 'Others']
        actual_option_list = []
        options = self.chrome_driver.find_elements_by_xpath("//div[@class='popupOption']")
        for option in options:
            value = option.text
            actual_option_list.append(value)
        assert expected_option_list == actual_option_list, \
            "Ban options - Inappropriate Content, Abusive Language, Content Sharing, Others are not preseent"
        assert self.chrome_driver.find_element_by_xpath(self.ban_student_cancel).is_displayed() and \
               self.chrome_driver.find_element_by_xpath(
                   self.ban_student_ban).is_displayed(), "Cancel and Ban buttons are not present"

    def verify_default_ban_option(self):
        is_checked = self.chrome_driver.find_element_by_xpath(
            '//input[@value = "inappropriate_content"]').get_attribute('checked')
        assert is_checked, "Inappropriate Content option is not selected by default"

    def verify_ban_cancel(self):
        self.chrome_driver.find_element_by_xpath(self.ban_student_cancel).click()
        try:
            self.chrome_driver.find_element_by_xpath(self.ban_student_popup).is_displayed()
        except NoSuchElementException:
            print("clicked on Cancel button and pop-up did go off")

    def verify_click_outside_ban_popup(self):
        self.wait_for_clickable_element_webdriver(self.ban)
        self.chrome_driver.find_element_by_xpath(self.ban).click()
        ActionChains(self.chrome_driver).move_by_offset(100, 100).click().perform()
        try:
            self.chrome_driver.find_element_by_xpath(self.ban_student_popup).is_displayed()
        except NoSuchElementException:
            print("clicked on outside popup and pop-up did go off")

    def verify_ban_student(self):
        # ban student and verify Banned student messages are not be shown
        self.tap_chat_icon()
        self.wait_for_locator_webdriver(self.ban_student_popup)
        self.wait_for_clickable_element_webdriver(self.ban)
        self.chrome_driver.find_element_by_xpath(self.ban).click()
        self.chrome_driver.find_element_by_xpath(self.ban_student_ban).click()
        try:
            user_name = getdata(Login_Credentials, 'login_detail3', 'profile_one_to_many_and_mega')
            self.chrome_driver.find_element_by_xpath("//*[text()='" + user_name + "']").is_displayed()
        except NoSuchElementException:
            print("banned student messages are not present")

    def tap_on_approve_message(self):
        time.sleep(5)
        self.wait_for_clickable_element_webdriver(self.approve_message)
        elements = self.chrome_driver.find_elements_by_xpath("//*[@class='action']")
        elements[2].click()

    def tap_on_reject_message(self):
        time.sleep(5)
        self.wait_for_clickable_element_webdriver(self.reject_message)
        elements = self.chrome_driver.find_elements_by_xpath("//*[@class='action']")
        elements[1].click()

    def is_message_present_for_tutor(self, text):
        try:
            self.wait_for_locator_webdriver("//*[@class='text' and text()='" + text + "']")
            self.chrome_driver.find_element_by_xpath("//*[@class='text' and text()='" + text + "']").is_displayed()
            return True
        except (NoSuchElementException, StaleElementReferenceException):
            return False
