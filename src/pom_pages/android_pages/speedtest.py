import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import InvalidElementStateException, StaleElementReferenceException
import requests
from utilities.common_methods import CommonMethods
from pom_pages.android_pages.login_android import Login
import xml.etree.ElementTree as ET
from utilities.tutor_common_methods import TutorCommonMethods

CommonMethods = CommonMethods()


class SpeedTest:
    def __init__(self, driver):
        self.obj = TutorCommonMethods(driver)
        self.action = TouchAction(driver)
        self.login = Login(driver)
        self.driver = driver
        self.action = TouchAction(driver)
        self.root = None
        self.back_navigation = '//*[@resource-id = "com.byjus.thelearningapp.premium:id/roundedNavButton"]'

    def capture_speedtest_screen(self):
        time.sleep(4)
        print(self.driver.page_source)
        self.root = ET.fromstring(self.driver.page_source)

    def is_view_text_match_element_tree(self, expected_text):
        flag = False
        view_elements = self.root.findall(".//android.view.View")
        for ele in view_elements:
            print(ele.attrib["text"])
            actual_text = ele.attrib["text"]
            if (expected_text == actual_text) or (expected_text in actual_text):
                flag = True
        return flag

    def verify_view_text_present(self, text):
        assert self.is_view_text_match_element_tree(text), text + " text is not present"

    def is_text_match_element_tree(self, expected_text):
        flag = False
        text_elements = self.root.findall(".//android.widget.TextView")
        for ele in text_elements:
            print(ele.attrib["text"])
            actual_text = ele.attrib["text"]
            if expected_text == actual_text:
                flag = True
        return flag

    def verify_text_present(self, text):
        assert self.is_text_match_element_tree(text), text + " text is not present"

    def verify_appback_button(self):
        assert self.root.findall('.//*[@resource-id = "com.byjus.thelearningapp.premium:id/roundedNavButton"]')[
                   0] is not None, 'Back navigation is not present'

    def tap_on_appback_button(self):
        self.obj.element_click('xpath', self.back_navigation)

    def verify_button(self, text):
        try:
            self.obj.is_button_displayed(text)
        except StaleElementReferenceException:
            pass

    def text_match_after_speedtest_success(self, text):
        self.obj.wait_for_locator('xpath', '//*[contains(@resource-id, "btButton")]', 15)
        if self.obj.is_element_present('xpath', '//*[contains(@resource-id, "btButton")]'):
            self.obj.is_text_match(text)

    def verify_offline_dialog_disappeared(self):
        self.obj.wait_for_invisibility_of_element('xpath', '//*[contains(@resource-id, "dialog_layout")]')

    def tap_outside_dialog_layout(self):
        try:
            self.action.tap(None, x=100, y=100).release().perform()
        except InvalidElementStateException:
            pass

    @staticmethod
    def send_put_request(speed_test_value, speed_test_result_value):
        url = "https://api.tllms.com/internal/staging/tutor_plus/internal_api/v1/settings/"
        headers = {'Content-Type': 'application/json',
                   'Accept': 'application/json'}

        payload = {"one_to_many_skip_speed_test": speed_test_value,
                   "one_to_many_skip_speed_test_result": speed_test_result_value}
        r = requests.put(url, json=payload, headers=headers)
        print(r.status_code)

    def is_speed_test_screen_present(self):
        time.sleep(2)
        if self.obj.is_text_match("Speedtest"):
            return True
        else:
            return False

    def clear_app_from_recents_and_relaunch(self):
        self.obj.clear_app_from_recents()
        self.obj.execute_command(
            'adb shell monkey -p com.byjus.thelearningapp.premium -c android.intent.category.LAUNCHER 1')

    def verify_portrait_mode(self):
        orientation = self.driver.orientation
        assert orientation == 'PORTRAIT', " speed test screen does not support portrait mode for mobile devices"
