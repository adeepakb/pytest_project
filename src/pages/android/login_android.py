import json
import os
import re
from appium.webdriver.common.touch_action import TouchAction
from cryptography.fernet import Fernet
from pytest_check import check
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from constants.constants import Login_Credentials
from pages.android.application_login import Login
from pages.android.homepage import HomePage
from pages.android.know_more import KnowMoreTest
from pages.base.login_base import LoginBase
from utilities.return_type import ReturnType
from utilities.tutor_common_methods import TutorCommonMethods
from pages.android.scroll_cards import ScrollCards
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from subprocess import Popen
from json import load
from utilities.staging_tlms import Stagingtlms
import logging
from constants.load_json import get_data
from utilities.common_methods import CommonMethods
from selenium.webdriver.support import expected_conditions as EC

CommonMethods = CommonMethods()


class LoginAndroid(Login):
    def __init__(self, driver):
        self.obj = TutorCommonMethods(driver)
        self.action = TouchAction(driver)
        self._scroll = ScrollCards(driver)
        self.driver = driver
        self.know_more = KnowMoreTest(self.driver)
        self.package_name = driver.desired_capabilities['appPackage']
        self.phone_number = "com.byjus.thelearningapp.premium:id/etPhoneNumber"
        self.password = "//*[contains(@resource-id, 'etPassword')]"
        self.next_btn = "//*[contains(@resource-id, 'btnNext')]"
        self.login_btn = "//*[contains(@resource-id, 'btnLogin')]"
        self.btn_session_board = '//*[contains(@resource-id,"ScheduleCard")]'
        self.cards = 'com.byjus.thelearningapp.premium:id/card_root'
        self.app_icon = '//*[contains(@content-desc,"Tutor+")]'
        self.app_list = '//*[@content-desc="Apps list"]'
        self.permission_alert = '//*[contains(@resource-id,"alert")]'
        self.alert_message = '//*[contains(@resource-id,"message")]'
        self.button_cls = 'android.widget.Button'
        self.offline_validation_layout = '//*[contains(@resource-id,"dialog_layout")]'
        self.country_dropdown_cls = 'android.widget.Spinner'
        self.text_view_cls = 'android.widget.TextView'
        self.otp_id = 'com.byjus.tutorplus:id/etOTP'
        self.snackbar = '//*[contains(@resource-id, "bar_text")]'
        self.dash_board_many = '//*[contains(@resource-id, "llScheduleList")]'
        self.btn_classroom = '//*[contains(@resource-id, "btnEnterClassroom")]'
        self.btn_personal = '//*[contains(@resource-id,"btnEnterPersonalise")]'
        self.profile_back_button = '//*[contains(@resource-id, "roundedNavButton")]'
        self.permission_container = '//*[@resource-id = "com.android.packageinstaller:id/desc_container"]'
        self.permission_container_tab = '//*[@resource-id = "com.android.permissioncontroller:id/content_container"]'
        self.premium_school_card = 'com.byjus.thelearningapp.premium:id/premiumSchoolCardView'
        self.OtpTxtBx_id = "com.byjus.thelearningapp.premium:id/etOTP"
        self.multiple_accounts_dialog = "com.byjus.thelearningapp.premium:id/dialog_linearlayout"
        self.user_profile_name = "com.byjus.thelearningapp.premium:id/tv_profile_name"
        self.profile_select_radio_button = "com.byjus.thelearningapp.premium:id/profile_select_radio_button"
        self.allow_btn_id = '//*[contains(@resource-id, "permission_allow_button")]'
        self.none_of_the_above_id = "com.google.android.gms:id/cancel"
        self.loginPageVerify_id = "//android.widget.Button[@text='Login']"
        self.welcome_button = "com.byjus.thelearningapp.premium:id/welcomeButton"
        self.loginBtn_id = "com.byjus.thelearningapp.premium:id/btnLogin"
        self.continue_button = "com.byjus.thelearningapp.premium:id/tv_submit"
        self.premium_login_text = 'id', '%s:id/img_premium_login' % self.package_name
        self.selected_text_view = 'id', '%s:id/selected_text_view' % self.package_name
        self.we_will_sendotp = 'id', '%s:id/tvWeWillSendOtp' % self.package_name
        self.register_text_on_login = 'id', '%s:id/tvRegister' % self.package_name
        self.byju_icon = 'id', '%s:id/iv_google_play_navigation_image' % self.package_name
        self.next_button = 'id', '%s:id/btnLogin' % self.package_name
        self.phone_number_text_field = 'id', '%s:id/etPhoneNumber' % self.package_name
        self.signout_button = 'id', '%s:id/signout' % self.package_name
        self.signout_confirm_button = 'id', '%s:id/primaryAction' % self.package_name
        self.dialog_message = 'id', '%s:id/dialog_message' % self.package_name
        self.dialog_try = 'id', '%s:id/primaryAction' % self.package_name
        self.dialog_contact = 'id', '%s:id/secondaryAction' % self.package_name
        self.dialog_description = 'id', '%s:id/dialog_description' % self.package_name
        self.sibling_profile_names = 'id', '%s:id/tv_profile_name' % self.package_name
        self.sibling_radio = 'id', '%s:id/profile_select_radio_button' % self.package_name
        self.sibling_continue = 'id', '%s:id/tv_submit' % self.package_name
        self.dialer = "id", "com.android.dialer:id/digits"
        self.welcome_text = 'id', '%s:id/welcomeTitle' % self.package_name
        super().__init__(driver)
        self.byjus_class_card = '//*[@resource-id = "com.byjus.thelearningapp.premium:id/home_card_title_text" and @text="Byju\'s Classes"]'
        self.home_card_layout = "com.byjus.thelearningapp.premium:id/home_card_layout"
        self.marketing_classes_image = 'com.byjus.thelearningapp.premium:id/marketing_classes_dynamic_image'
        self.subject_names = 'com.byjus.thelearningapp.premium:id/subject_name'

    def implicit_wait_for(self, pool):
        self.driver.implicitly_wait(pool)

    def click_on_premium_school(self, relaunch=False):
        if relaunch:
            detail = self.know_more.relaunch_app()
        self.obj.wait_for_locator('id', self.home_card_layout)
        element = self.obj.get_element('android_uiautomator','new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(resourceId("' + self.marketing_classes_image + '"))')
        width = element.size['width']
        height = element.size['height']
        self.action.press(None, element.location['x'] + (width / 2), height).wait(3000).move_to(
            x=element.location['x'] + (width / 2), y=2 * height).release().perform()
        element.click()
        try:
            self.obj.is_element_present('xpath', self.permission_container) or self.obj.is_element_present('xpath',self.permission_container_tab)
            self.allow_deny_permission(["Allow", "Allow", "Allow"])
        except:
            pass # skip

    # This step is only applicable in web. Hence skipping this for android
    def click_on_hamburger(self):
        pass

    def launch_and_navigate_to_login_page(self):
        self.obj.execute_command('adb shell pm clear com.byjus.thelearningapp.premium')
        self.obj.execute_command(
            'adb shell am start -n com.byjus.thelearningapp.premium/com.byjus.app.onboarding.activity.SplashActivity')
        self.allow_deny_permission(["Allow"])
        self.obj.wait_for_locator('xpath', self.loginPageVerify_id)
        self.obj.get_element('xpath', self.loginPageVerify_id).click()
        self.obj.wait_for_locator('id', self.none_of_the_above_id)
        self.obj.get_element('id', self.none_of_the_above_id).click()

    def enter_phone(self, phone_num=None):
        if phone_num is None:
            phone_num = get_data(Login_Credentials, 'login_detail3', 'mobile_no')
        self.wait_for_locator('xpath', self.phone_number)
        self.get_element('xpath', self.phone_number).clear()
        self.get_element('xpath', self.phone_number).send_keys(phone_num)

    def enter_otp(self, otp=None, sub_profile_type='primary') -> None:
        if otp is not None:
            self.get_element('id', self.otp_id).send_keys(otp)
        else:
            self.get_otp()

    # def enter_otp(self):
    #     self.obj.wait_for_locator('id', self.OtpTxtBx_id)
    #     self.obj.get_element('id', self.OtpTxtBx_id).send_keys(get_data(Login_Credentials, 'login_detail3', 'OTP'))
    #     self.select_profile()
    #     self.obj.element_click('id', self.continue_button)
    #     self.obj.wait_for_locator('id', self.welcome_button, 15)
    #     self.obj.element_click('id', self.welcome_button)

    def select_premium_school(self):
        device = CommonMethods.get_device_type(self.driver)
        if device == 'tab':
            self.obj.element_click('id', 'com.byjus.thelearningapp.premium:id/btnPremiumSchool')
            assert self.text_match('BYJU’S Premium School'), "text is not displayed "
        elif device == 'mobile':
            self.click_on_link("Byju's classes")
            assert self.text_match("Classes"), "text is not displayed"

    def click_on_next(self):
        self.obj.wait_for_locator('id', self.loginBtn_id)
        self.driver.find_element_by_id(self.loginBtn_id).click()

    def enter_password(self, psswd=None):
        self.obj.wait_for_locator('xpath', self.password)
        self.driver.find_element_by_xpath(self.password).send_keys(psswd)

    def select_profile(self):
        data = get_data(Login_Credentials, 'login_detail3', 'profile_one_to_many_and_mega')
        self.obj.wait_for_locator('id', self.multiple_accounts_dialog)
        if self.obj.is_element_present('id', self.multiple_accounts_dialog):
            # CommonMethods.scrollToElement(driver, data)
            profiles = self.obj.get_elements('id', self.user_profile_name)
            radio_buttons = self.obj.get_elements('id', self.profile_select_radio_button)
            for i in range(len(profiles)):
                if profiles[i].text == data:
                    radio_buttons[i].click()
                    break

    @staticmethod
    def switch_back_to_app():
        Popen('adb shell monkey -p com.byjus.tutorplus -c android.intent.category.LAUNCHER 1').wait()

    def is_app_icon_displayed(self) -> bool:
        """press home button"""
        self.driver.press_keycode(3)
        self.driver.press_keycode(3)
        screen_rect = self.driver.get_window_rect()
        x1 = x2 = screen_rect['width'] // 2
        y1 = screen_rect['height'] - (0.10 * screen_rect['height'])
        y2 = screen_rect['height'] - (0.75 * screen_rect['height'])
        self.driver.swipe(x1, y1, x2, y2, 500)
        self.obj.get_element('class_name', 'android.widget.EditText').send_keys("Tutor")
        icon_displayed = self.obj.get_element('xpath', self.app_icon).is_displayed()
        self.driver.press_keycode(3)
        if icon_displayed is True:
            return True
        return False

    def is_alert_displayed(self) -> bool:
        alert_obj = self.obj.get_element('xpath', self.permission_alert).is_displayed()
        alert_msg = self.obj.get_element('xpath', self.alert_message).text
        if alert_obj is True and "permissions are mandatory" in alert_msg:
            return True
        return False

    def allow_deny_permission(self, permissions: list):
        for permission in permissions:
            permission = permission.lower()
            if permission == 'allow':
                btn_action = self.obj.get_element(
                    'xpath', '//*[contains(@resource-id, "' + permission + '")]'
                )
                logging.info("Permission Allowed")
            elif permission == 'deny':
                btn_action = self.obj.get_element(
                    'xpath', '//*[contains(@resource-id, "' + permission + '")]'
                )
                logging.info("Permission Denied")
            else:
                logging.info("Not a valid permission")
                return 1
            btn_action.click()

    def is_login_form_displayed(self):
        login_form = self.obj.get_element('xpath', '//*[contains(@resource-id, "LoginContentForm")]').is_displayed()
        if login_form is True:
            return True
        return False

    def text_match(self, expected_text=None):
        text_matches = self.obj.is_text_match(expected_text)
        if text_matches is True:
            return ReturnType(True, '%s text is displayed' % expected_text)
        return ReturnType(False, '%s text is not displayed' % expected_text)

    def dropdown_select(self):
        self.obj.get_element('class_name', "android.widget.Spinner").click()
        drop_down = self.obj.get_element('class_name', 'android.widget.ListView')
        return drop_down

    def is_dropdown_displayed(self):
        drop_down = self.dropdown_select()
        drop_down_visible = drop_down.is_displayed()
        self.action.tap(x=10, y=100).perform()
        if drop_down_visible is True:
            return True
        return False

    def mobile_number_input(self):
        input_box = self.obj.get_element('xpath', self.phone_number).is_displayed()
        if input_box is True:
            return True
        return False

    def find_buttons(self):
        buttons = self.obj.get_elements('class_name', self.button_cls)
        return buttons

    def find_input_boxes(self):
        input_boxes = self.obj.get_elements('class_name', 'android.widget.EditText')
        return input_boxes

    def is_button_displayed(self, text):
        for button in self.find_buttons():
            if button.text == text:
                return ReturnType(True, '%s button is displayed' % text)
        return ReturnType(False, '%s button is not displayed' % text)

    def button_click(self, text):
        for button in self.find_buttons():
            if button.text == text:
                button.click()
                return ReturnType(True, text + " button is clicked")
        return ReturnType(False, text + " button is not clicked")

    def is_toast_message_displayed(self, message=None):
        toast_msg = self.obj.get_element('xpath', '//android.widget.Toast').text
        list_of_toast_msg = toast_msg.split('\n')
        condition = list()
        for msg in list_of_toast_msg:
            if msg in message:
                condition.append(True)
            else:
                condition.append(False)
        if all(condition):
            return True
        return False

    def clear_input_field(self):
        self.obj.get_element('xpath', self.phone_number).clear()

    def validate_error_msg(self, expected_text=None):
        actual_text = self.obj.get_element('xpath', '//*[contains(@resource-id, "PhoneError")]').text
        if expected_text.capitalize() == actual_text:
            return True
        return False

    def is_app_minimized(self):
        _status = self.obj.query_app_state('com.byjus.tutorplus')
        state = (_status // 3) == 1
        return state

    def is_all_permission_visible(self):
        dialog_box, page_num = None, None
        try:
            self.driver.implicitly_wait(0)
            page_num = self.obj.get_element(
                'xpath', '//*[contains(@resource-id, "current_page_text")]').text
        except NoSuchElementException:
            dialog_box = self.obj.get_element(
                'xpath', '//*[contains(@resource-id, "dialog_container")]').is_displayed()
        if dialog_box is not None:
            return dialog_box
        return page_num

    def is_password_field_visible(self):
        try:
            field_displayed = self.obj.get_element('xpath',
                                                   '//*[contains(@resource-id, "LayoutPassword")]').is_displayed()
            return field_displayed
        except NoSuchElementException:
            return False

    def field_visibility_text(self, parameter=None):
        try:
            actual_text = self.obj.get_element('xpath', '//*[contains(@text, "' + parameter + '")]').text
            return actual_text
        except NoSuchElementException:
            return str()

    def is_homescreen_displayed(self):
        try:
            home_screen = self.obj.get_element('xpath', '//*[contains(@resource-id, "TutorHomeLyt")]').is_displayed()
            return home_screen
        except NoSuchElementException:
            return False

    def click_on_session_card(self, index=None):
        session_cards_list = self.obj.get_elements('xpath', self.btn_session_board)
        session_cards_list[index].click()

    def toggle_wifi_connection(self, text):
        self.obj.toggle_wifi_connection(text)

    def is_offline_validation_layout_displayed(self):
        self.obj.wait_for_locator('xpath', self.offline_validation_layout)
        layout = self.obj.get_element('xpath', self.offline_validation_layout).is_displayed()
        if layout is True:
            return ReturnType(True, "Offline related bottom sheet dialog is displayed")
        return ReturnType(False, "Offline related bottom sheet dialog is not displayed")

    def verify_offline_validation_layout(self, text1=None, text2=None):
        self.obj.is_button_enabled(text1)
        self.obj.is_button_enabled(text2)

    def click_on_link(self, parameter=None):
        link = self.obj.get_element('xpath', '//android.widget.TextView[@text="' + parameter + '"]')
        link.click()

    def wait_for_dialog_to_be_invisible(self):
        self.obj.wait_for_invisibility_of_element('xpath', self.offline_validation_layout)

    def click_on_country_code_dropdown(self):
        self.obj.get_element('class_name', self.country_dropdown_cls).click()

    def enter_reg_mobile_number(self):
        self.enter_cc_and_phone_number()

    def enter_cc_and_phone_number(self, account_type='many'):
        self.click_on_country_code_dropdown()
        data = self.user_mobile
        # if account_type == 'many':
        #     data = Stagingtlms(self.driver).get_mobile_and_ccode()
        # elif account_type == 'personal':
        #
        #     data = str(get_data('../../config/config.json', 'account_with_password', 'mobile'))
        mobile_and_code = data.split('-')
        self.select_country_code(mobile_and_code[0])
        self.enter_phone(mobile_and_code[1])
        return mobile_and_code[1]

    def select_country_code(self, expected_text=None):
        self.obj.wait_for_locator('class_name', 'android.widget.ListView')
        country_codes = self.obj.get_elements('class_name', self.text_view_cls)
        drop_down = self.obj.get_element('class_name', 'android.widget.ListView')
        while True:
            for country_code in country_codes:
                actual = re.findall(r"[\\+0-9]+", country_code.text)[0]
                if expected_text == actual:
                    country_code.click()
                    return 0
            self._scroll.scroll_by_card(country_codes[-1], drop_down)
            drop_down = self.obj.get_element('class_name', 'android.widget.ListView')
            country_codes = self.obj.get_elements('class_name', self.text_view_cls)

    def wait_for_element_not_to_be_present(self, element=None, timeout=10):
        self.driver.implicitly_wait(1.5)
        while True:
            try:
                element_displayed = self.obj.get_element('xpath', element).is_displayed()
            except (NoSuchElementException, StaleElementReferenceException):
                break
            if element_displayed:
                loc = self.obj.get_element('xpath', element).location
                loc_x, loc_y = loc['x'], loc['y']
                self.action.press(x=loc_x, y=loc_y - 100).release().perform()
            elif timeout == 0:
                raise Exception("Element is always present within given time")
        self.driver.implicitly_wait(10)

    def is_otp_screen_displayed(self):
        self.wait_for_element_not_to_be_present('//*[contains(@resource-id, "dialog_layout")]')
        otp_page_displayed = self.obj.get_element('xpath',
                                                  '//*[contains(@resource-id, "otpVerificationForm")]').is_displayed()
        if otp_page_displayed is True:
            return True
        return False

    def verify_snack_bar_message(self, expected_text=None):
        try:
            snack_bar_text = self.obj.get_element('xpath', self.snackbar).text
            if snack_bar_text == expected_text:
                return True
            return False
        except (NoSuchElementException, StaleElementReferenceException):
            return None

    def is_auto_otp_dialog_box_displayed(self):
        try:
            bottom_sheet_dialog = self.obj.get_element('xpath',
                                                       '//*[contains(@resource-id, "dialog_layout")]').is_displayed()
            if bottom_sheet_dialog:
                return bottom_sheet_dialog
            return False
        except (NoSuchElementException, StaleElementReferenceException):
            return None

    def get_otp(self) -> None:
        OTP = Stagingtlms(self.driver).get_otp()
        self.wait_for_element_not_to_be_present('//*[contains(@resource-id, "dialog_layout")]')
        self.obj.get_element('id', self.otp_id).send_keys(OTP)

    def is_timer_displayed(self):
        try:
            timer = self.obj.get_element('xpath',
                                         '//*[contains(@resource-id, "Countdown")]').is_displayed()
            if timer:
                return timer
            return False
        except (NoSuchElementException, StaleElementReferenceException):
            return None

    def is_text_box_editable(self, previous_text=None):
        try:
            self.clear_input_field()
            self.enter_phone(previous_text)
            return True
        except NoSuchElementException:
            return False

    def click_on_edit_icon(self):
        self.obj.get_element('xpath', '//*[contains(@resource-id,"tvPhoneNo")]').click()

    def is_one_to_many_dashboard_displayed(self):
        self.implicit_wait_for(10)
        try:
            screen_displayed = self.obj.get_element(
                'xpath', self.dash_board_many).is_displayed()
        except NoSuchElementException:
            try:
                self.driver.find_element_by_xpath(
                    '//*[contains(@resource-id, "tvCancel")]').click()
            except (NoSuchElementException, StaleElementReferenceException):
                logging.log(10, "UP NEXT session pop up is not displayed")
            screen_displayed = self.obj.get_element(
                'xpath', self.dash_board_many).is_displayed()
        self.implicit_wait_for(0)
        if screen_displayed:
            return True
        return False

    def tap_bck_btn(self):
        self.obj.click_back()

    @staticmethod
    def __get_from_config(key):
        with open(r'../../config/config.json', 'r') as fp:
            raw_data = load(fp)
        return raw_data[key]

    def click_on_one_to_many(self):
        try:
            self.obj.get_element('xpath', self.btn_classroom).click()
        except NoSuchElementException:
            pass

    def select_country_code_other(self, expected_text=None):
        country_codes = self.obj.get_elements('class_name', self.text_view_cls)
        for country_code in country_codes:
            if expected_text not in country_code.text:
                country_code.click()
                break

    def enter_passwd(self):
        fp = '../../config/config.json'
        key = os.getenv('SECRET')
        f = Fernet(key)
        encrypted_data = get_data(fp, 'encrypted_data', 'token')
        decrypted_data = json.loads(f.decrypt(encrypted_data.encode('ascii')))
        psswd = decrypted_data['account_with_password']['password']
        self.enter_password(psswd)

    def reset_and_login_with_otp(self):
        self.execute_command('adb shell pm clear %s' % self.package_name)
        self.execute_command('adb shell monkey -p %s -c android.intent.category.LAUNCHER 1' % self.package_name)
        self.login_with_otp()
        self.implicit_wait_for(3)
        try:
            self.subscription_expired()
        except NoSuchElementException:
            pass
        try:
            self.get_element(*self.action_layout_dismiss, wait=False).click()
        except NoSuchElementException:
            pass
        try:
            self.get_element(*self.action_layout_ignore, wait=False).click()
        except NoSuchElementException:
            pass

    # this is an old method
    # def reset_and_login_with_otp(self):
    #     self.obj.execute_command('adb shell pm clear com.byjus.tutorplus')
    #     self.obj.execute_command('adb shell monkey -p com.byjus.tutorplus -c android.intent.category.LAUNCHER 1')
    #     self.allow_deny_permission(["Allow", "Allow", "Allow"])
    #     self.enter_reg_mobile_number()
    #     self.button_click("Next")
    #     try:
    #         self.click_on_link('Login with OTP')
    #     except NoSuchElementException:
    #         self.wait_for_element_not_to_be_present('//*[contains(@resource-id, "dialog_layout")]')
    #         self.enter_otp()
    #     else:
    #         self.wait_for_element_not_to_be_present('//*[contains(@resource-id, "dialog_layout")]')
    #         self.enter_otp()

    def cancel_session_join(self):
        try:
            self.driver.find_element_by_xpath(
                '//*[contains(@resource-id, "tvCancel")]').click()
        except (NoSuchElementException, StaleElementReferenceException):
            logging.log(10, "UP NEXT session pop up is not displayed")

    def verify_student_profile(self):
        try:
            if self.obj.is_element_present('xpath', '//*[contains(@resource-id, "ClassroomAvatarImg")]'):
                self.obj.get_element('xpath', '//*[contains(@resource-id, "ClassroomAvatarImg")]').click()
                expected_mobile_number = self.obj.get_element('xpath',
                                                              '//*[contains(@resource-id, "mobile_number")]').text

                account_details = '../../config/config.json'
                actual_mobile_number = str(get_data(account_details, 'account_details', 'mobile'))
                if expected_mobile_number == actual_mobile_number:
                    logging.info('classroom page verified')
                    self.obj.get_element('xpath', self.profile_back_button).click()
                else:
                    logging.info('Not expected user')
                    self.reset_and_login_with_otp()
            else:
                self.reset_and_login_with_otp()
        except:
            logging.info('Error in verifying classroom page')
        finally:
            try:
                self.cancel_session_join()
            except NoSuchElementException:
                pass

    def is_up_next_and_unattended_cards_displayed(self):
        list_of_cards = self.obj.get_elements('xpath', '//*[contains(@resource-id, "ScheduleCard")]')
        flag, card = None, None
        for card in list_of_cards:
            try:
                card.find_element_by_xpath('//*[contains(@resource-id, "up_next_label")]')
                flag = True
                break
            except NoSuchElementException:
                pass
        un_attended_cards = list_of_cards[list_of_cards.index(card)::]
        while flag:
            last_card = un_attended_cards[-1]
            if len(un_attended_cards) == 1:
                box = self.obj.get_element('xpath',
                                           '//*[contains(@resource-id, "rvScheduleList")]')
                self._scroll.scroll_by_card(last_card, box)
                un_attended_cards = self.obj.get_elements('xpath', '//*[contains(@resource-id, "ScheduleCard")]')
            else:
                try:
                    last_card.find_element_by_xpath('//*[contains(@resource-id, "SessionTakenDone")]')
                    return False
                except NoSuchElementException:
                    return True

    def navigate_to_login_screen(self):
        if "HomeActivity" in self.driver.current_activity or "ProfileActivity" in self.driver.current_activity:
            self.log_out_from_home_page_or_login_page()

        grant_permissions_activity = "GrantPermissionsActivity"
        login_activity = "LoginActivity"
        home_activity = "HomeActivity"
        profile_activity = "ProfileActivity"
        credential_picker = 'CredentialPickerActivity'
        self.wait_activity(grant_permissions_activity, timeout=5)
        if grant_permissions_activity in self.driver.current_activity:
            self.on_boarding_activity()
        if home_activity in self.driver.current_activity or profile_activity in self.driver.current_activity:
            self.log_out_from_home_page_or_login_page()
        if credential_picker in self.driver.current_activity:
            try:
                self.driver.tap([(128.90625, 335.90625)])
            except:
                logging.info("Credentials action dissmissed")
        if login_activity in self.driver.current_activity:

            return ReturnType(True, "Navigated to Login Screen")
        else:
            return ReturnType(False, "Couldn't navigate to Login Screen")

    def verify_login_screen_elements(self, text='', type=''):
        login_activity = "LoginActivity"
        # self.wait_activity(login_activity, timeout=5)
        otp_activity = 'VerifyActivity'
        if login_activity not in self.driver.current_activity and otp_activity not in self.driver.current_activity:
            return ReturnType(False, "User not in Login Screen")

        if type.lower() == 'all':
            self.verify_login_screen_elements(text="Premium Login")
            self.verify_login_screen_elements(text="autofill")
            self.verify_login_screen_elements(text="otp message")
            self.verify_login_screen_elements(text="next")
            self.verify_login_screen_elements(text="not a premium user?")
            self.verify_login_screen_elements(text="mobile number")
            self.verify_login_screen_elements(text="mobile number text field")
            raise NotImplementedError
        else:
            try:
                if text == 'Premium Login':
                    self.driver.implicitly_wait(4)
                    required_text = self.get_element(*self.premium_login_text).is_displayed()
                    return ReturnType(True, "{} text correct".format(text)) if required_text else ReturnType(
                        False, "{} text not correct".format(text))
                elif text.lower() == 'autofill':
                    required_text = self.get_element(*self.selected_text_view).text
                    return ReturnType(True, "{} text correct".format(text)) if required_text == "+91" else ReturnType(
                        False,
                        "{} text is not correct".format(
                            text))
                elif text.lower() == 'otp message' or text.lower() == 'we will send a 4 digit otp to verify':
                    required_text = self.get_element(*self.we_will_sendotp).text
                    return ReturnType(True, "{} text is correct".format(
                        text)) if required_text.lower() == "we will send a 4 digit otp to verify" else ReturnType(False,
                                                                                                                  "{} text is not correct".format(
                                                                                                                      text))
                elif text.lower() == 'next':
                    required_text = self.get_element(*self.next_button).text
                    return ReturnType(True, "{} text is correct".format(
                        text)) if required_text.lower() == text.lower() else ReturnType(False,
                                                                                        "{} text is not correct".format(
                                                                                            text))
                elif text.lower() == "not a premium user?".lower() or text.lower() == 'start free trial of'.lower() or text.lower() == 'Not a premium user?\nStart Free Trial of':
                    required_text = self.get_element(*self.register_text_on_login).text
                    return ReturnType(True, "{} text is correct".format(
                        text)) if text.lower() in required_text.lower() else ReturnType(False,
                                                                                        "{} text is not correct".format(
                                                                                            text))
                elif text.lower() == 'icon':
                    flag = self.get_element(*self.byju_icon).is_displayed()
                    return ReturnType(True, "{} text is correct".format(
                        text)) if flag else ReturnType(False,
                                                       "Byjus icon on login page not displayed")
                elif text.lower() == 'mobile number':

                    return ReturnType(True, "{} text is correct".format(
                        text)) if self.is_text_match(expected_text=text) else ReturnType(False,
                                                                                         "Byjus icon opn login page not displayed")
                elif text.lower() == 'mobile number text field':
                    check = self.get_element(*self.phone_number_text_field).is_displayed()
                    return ReturnType(True, "{} text is correct".format(
                        text)) if check else ReturnType(False,
                                                        "Byjus icon opn login page not displayed")
                elif text.lower() == 'this phone number is not registered with a premium account.':
                    self.driver.implicitly_wait(3)
                    if otp_activity in self.driver.current_activity or login_activity in self.driver.current_activity:
                        message = self.get_element(*self.dialog_message).text
                        return ReturnType(True, "{} message is correct and displayed".format(
                            text)) if text.lower() == message.lower() else ReturnType(
                            False, "{} message is incorrect or not displayed".format(text))
                    else:
                        ReturnType(
                            False, "{} message is incorrect or not displayed".format(text))
                elif text.lower() == 'try again':
                    flag = self.get_element(*self.dialog_try).is_displayed()
                    return ReturnType(True, "{} is displayed".format(text)) if flag else ReturnType(False,
                                                                                                    "{} is not being displayed".format(
                                                                                                        text))
                elif text.lower() == 'contact us':
                    flag = self.get_element(*self.dialog_contact).is_displayed()
                    return ReturnType(True, "{} is displayed".format(text)) if flag else ReturnType(False,
                                                                                                    "{} is not being displayed".format(
                                                                                                        text))


                else:
                    return ReturnType(False, "{} elemant not found".format(text))

            except:
                if text == '':
                    text = "Login screen"
                return ReturnType(False, "{} element is not found".format(text))

    def is_default_country_in_dropdown(self):
        if self.is_dropdown_displayed_without_clicking().result:
            self.close_dropdown()
        return self.verify_login_screen_elements(text='autofill')

    def verify_country_codes_in_dropdown(self,
                                         text='India(+91),UAE(+971),Bahrain(+973),Kuwait(+965),Oman(+968),'
                                              'Qatar(+974),Saudi Arabia(+966),United Arab Emirates (+971)',
                                         ordered=False):
        country_code_list = self.get_country_codes_from_dropdown()
        country_code_list_text = text.replace("(", " (").replace("  (", " (").split(",")
        if ordered is True:
            for i in range(len(country_code_list_text)):
                if not country_code_list[i] == country_code_list_text[i]:
                    return ReturnType(False,
                                      "{} country  code not found or not in order".format(country_code_list_text[i]))
        else:
            for country_codes_name in country_code_list_text:
                if country_codes_name not in country_code_list:
                    return ReturnType(False,
                                      "{} country  code not found or not in order".format(country_codes_name))
        return ReturnType(True, "Given elements in country drop down are correct")

    def verify_country_codes_in_dropdown_in_alphabetical_manner(self):
        country_code_list = self.get_country_codes_from_dropdown()
        country_code_list = country_code_list[8:]
        i = 1
        while i < len(country_code_list):
            if not (country_code_list[i] > country_code_list[i - 1]):
                return ReturnType(False, "Country code dropdown is not alphabetically sorted")
            i += 1
        return ReturnType(True, "Country code dropdown is  alphabetically sorted")

    def is_numeric_pad_displayed(self):
        return ReturnType(True, "keyboard is being shown") if self.driver.is_keyboard_shown() else ReturnType(False,
                                                                                                              "Keyboard is not shown ")

    def check_numeric_input_in_phone(self):
        self.wait_for_locator('xpath', self.phone_number)
        self.get_element('xpath', self.phone_number).clear()

        for let in "982@1sd;":
            self.get_element('xpath', self.phone_number).send_keys(let)

        input = self.get_text_in_mobile_number_input()
        return ReturnType(True, "User can input Numeric input only ") if input == "9821" else ReturnType(True,
                                                                                                         "User is able to input alphanumeric in the text field")

    def phone_number_field_is_empty(self):
        try:
            text = self.get_text_in_mobile_number_input()
            if not text:
                return ReturnType(True, "Phone number field is Empty")
            else:
                return ReturnType(False, "Phone number field is not  Empty")
        except:
            return ReturnType(False, "Phone number field is not  Empty")

    def login_for_new_user(self):
        try:
            self.reset_and_login_with_otp()
            self.wait_activity("HomeActivity")
            if "HomeActivity" in self.driver.current_activity:
                return ReturnType(True, "Successfully logged in for new user")
            else:
                return ReturnType(False, "Could not log in for new user")
        except:
            return ReturnType(False, "Could not log in for new user")

    def log_out_from_home_page_or_login_page(self):
        try:
            if "HomeActivity" in self.driver.current_activity:
                self.wait_for_locator(*self.hamburger_icon)
                self.get_element(*self.hamburger_icon).click()
                self.get_element(*self.home_drawer).click()
                self.scroll_to_element("Sign out")
                self.get_element(*self.signout_button).click()
                self.get_element(*self.signout_confirm_button).click()
                self.wait_activity("LoginActivity")
                if "LoginActivity" in self.driver.current_activity:
                    return ReturnType(True, "Successfully logged out")
                else:
                    return ReturnType(False, "user not successfully logged out")
            elif "ProfileActivity" in self.driver.current_activity:
                self.get_element(*self.signout_button).click()
                self.get_element(*self.signout_confirm_button).click()
                self.wait_activity("LoginActivity")
                if "LoginActivity" in self.driver.current_activity:
                    return ReturnType(True, "Successfully logged out")
                else:
                    return ReturnType(False, "user not successfully logged out")
            else:
                return ReturnType(False, "user not successfully logged out as not in home activity or profile activity")

        except:
            return ReturnType(False, "user not successfully logged out")

    def check_mobile_number_field_is_prefilled_with_previous_logged_in_account(self):
        set_mobile_number = self.get_text_in_mobile_number_input()
        mobile_number = self.user_mobile

        return ReturnType(True, "Mobile number is prefilled with previous mobile number {}".format(
            set_mobile_number)) if set_mobile_number in mobile_number else ReturnType(False,
                                                                                      "Mobile number is not prefilled with previous mobile number {}".format(
                                                                                          set_mobile_number))

    def is_otp_screen_shown(self):
        self.wait_activity("VerifyActivity")
        if "VerifyActivity" in self.driver.current_activity:
            return ReturnType(True, "user is in otp page")
        else:
            return ReturnType(True, "user is in otp page")

    def is_app_on_screen(self):
        return ReturnType(True, "App is on screen") if self.package_name in self.driver.page_source else ReturnType(
            False, "App is not on screen")

    def tap_on_byju_icon(self):
        try:
            self.get_element(*self.byju_icon).click()
            return ReturnType(True, "Clicked on byju's app icon on login")
        except:
            return ReturnType(False, "Couldnt click on byju's app icon on login")

    def user_navigates_to_play_store(self):

        unauthenticated_play_store = 'UnauthenticatedMainActivity'
        main_activity = 'MainActivity'
        self.wait_activity(main_activity)
        current_activity = self.driver.current_activity

        if unauthenticated_play_store in current_activity or main_activity in current_activity:
            return ReturnType(True, " User successfully navigated to playstore")
        else:
            return ReturnType(False, " User successfully navigated to playstore")

    def verify_login_screen(self):
        login_activity = "LoginActivity"
        self.wait_activity(login_activity)
        if login_activity in self.driver.current_activity:
            return ReturnType(True, "User in login screen")
        else:
            return ReturnType(False, "User is not in login screen")

    def tap_on_button(self, text):
        try:
            if text.lower() == "try again":
                self.get_element(*self.dialog_try).click()
            elif text.lower() == "contact us":
                self.get_element(*self.dialog_contact).click()

            elif text.lower() == 'get started':
                self.get_element(*self.welcome_btn).click()
            return ReturnType(True, "Successfully tapped on {}  button".format(text))
        except:
            return ReturnType(False, "Could not  tap on {}  button".format(text))

    def verify_dialer(self):
        self.wait_activity("MainActivity")
        current_activity = self.driver.current_activity
        if "MainActivity" in current_activity:
            return ReturnType(True, "User is on dialer screen")
        else:
            return ReturnType(False, "User is not on dialer screen")

    def verify_dialer_with_number(self, number="+91 9241333666"):
        dialed_number = self.get_element(*self.dialer).text.replace(" ", "")
        number = number.replace(" ", "")
        if dialed_number == number:
            return ReturnType(True, "Dialed number is correct")
        else:
            return ReturnType(True, "Dialed number is correct")

    def verify_sibling_screen(self):
        self.driver.implicitly_wait(2)
        try:
            if self.get_element(*self.dialog_description).is_displayed():
                return ReturnType(True, "Sibling prifile dialog displayed")
            else:
                return ReturnType(False, "Sibling prifile  dialog not displayed")
        except:
            return ReturnType(False, "Sibling prifile  dialog not displayed")

    def scroll_to_profile_and_click(self, select_profile_name="", click=False):
        select_profile_name = select_profile_name if select_profile_name else self.profile_name
        if not click:
            self.get_element(
                'android_uiautomator',
                'UiScrollable(UiSelector().resourceId("com.byjus.thelearningapp.premium:id/rv_user_profile")).'
                'setSwipeDeadZonePercentage(0.05).'
                f'scrollTextIntoView("{select_profile_name}")'
            ).is_displayed()
        else:
            self.get_element(
                'android_uiautomator',
                'UiScrollable(UiSelector().resourceId("com.byjus.thelearningapp.premium:id/rv_user_profile")).'
                'setSwipeDeadZonePercentage(0.05).'
                f'scrollTextIntoView("{select_profile_name}")'
            ).click()

    def verify_sibling_screen_profiles(self):
        login_data = self.login_data
        user_mobile = self.user_mobile
        selected_user = None

        for user in login_data:
            if login_data[user]['mobile_number'] == user_mobile:
                selected_user = user
                selected_user = login_data[selected_user]
                break

        profiles = {key: value for (key, value) in selected_user.items() if "profile" in key}
        elements_name_list = self.get_sibling_screen_elements_names()
        check.equal(len(profiles), len(elements_name_list),
                    "Elements might be missing in login file or all profiles are not displayed")
        sucsess = []
        for element in profiles:
            sucsess.append(profiles[element]["profile_name"] in elements_name_list)

        return ReturnType(True, "Elements in profile switch screen are correct") if all(sucsess) else ReturnType(False,
                                                                                                                 "Elements profile switch screen are not correct ")

    def get_sibling_screen_elements_names(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.presence_of_element_located(self.sibling_profile_names))
        elements_name_list = set()
        elements1 = self.get_elements(*self.sibling_profile_names)
        for element in elements1:
            elements_name_list.add(element.text)
        self.scroll_to_profile_and_click()
        wait.until(EC.presence_of_element_located(self.sibling_profile_names))
        elements2 = self.get_elements(*self.sibling_profile_names)
        for element in elements2:
            elements_name_list.add(element.text)
        return elements_name_list

    def verify_sibling_screen_radio_buttons(self):
        login_data = self.login_data
        user_mobile = self.user_mobile
        selected_user = None

        for user in login_data:
            if login_data[user]['mobile_number'] == user_mobile:
                selected_user = user
                selected_user = login_data[selected_user]
                break

        profiles = {key: value for (key, value) in selected_user.items() if "profile" in key}
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.presence_of_element_located(self.sibling_radio))
        elements_radio_list = []
        elements1 = self.get_elements(*self.sibling_radio)
        for element in elements1:
            elements_radio_list.append(element.is_displayed())
        self.scroll_to_profile_and_click()
        wait.until(EC.presence_of_element_located(self.sibling_radio))
        elements2 = self.get_elements(*self.sibling_radio)
        for element in elements2:
            elements_radio_list.append(element.is_displayed())
        return ReturnType(True, "no of radion buttons in sibling screen is correct") if len(profiles) <= len(
            elements_radio_list) and all(elements_radio_list) else ReturnType(False,
                                                                              "no of radion buttons in sibling screen are correct")

    def click_on_continue_button(self):
        try:
            self.get_element(*self.sibling_continue).click()
            return ReturnType(True, "Clicked on continue button on sibling screen")
        except:
            return ReturnType(True, "Clicked on continue button on sibling screen")

    def verify_welcome_screen_text(self):
        try:
            text = self.get_element(*self.welcome_text).text
            if "Hi" in text:
                return ReturnType(True, "Welcome screen text is correct")
            else:
                return ReturnType(False, "Welcome screen text is not correct")
        except:
            return ReturnType(False, "Welcome screen text is not correct")

    def verify_country_code(self, country_code="+91"):
        required_text = self.get_element(*self.selected_text_view).text
        return ReturnType(True,
                          "{} text correct".format(country_code)) if required_text == country_code else ReturnType(
            False,
            "{} text is not correct".format(
                country_code))

    def subscription_expired(self, action="dismiss"):
        try:
            self.get_element(*self.action_layout_dismiss).click()
        except NoSuchElementException:
            pass
        try:
            self.get_element(*self.action_layout_ignore).click()
        except NoSuchElementException:
            pass
        expired_msg_displayed = self.get_element(*self.expired_msg_title).is_displayed()
        if expired_msg_displayed and action.lower() == "dismiss":
            self.get_element(*self.expired_later_btn).click()
        elif expired_msg_displayed and action.lower() == "call us":
            self.get_element(*self.se_call_us).click()
        elif expired_msg_displayed:
            raise NotImplementedError(f"Action of type \"{action}\" is not yet implemented.")
        return ReturnType(True, "Expired message is being displayed ") if expired_msg_displayed else ReturnType(True,
                                                                                                                "Expired message is not being displayed ")

    def verify_bottom_sheet_details(self):
        dialog_lyt_displayed = self.get_element(*self.dialog_layout).is_displayed()
        if dialog_lyt_displayed:
            cls_started_title_displayed = self.get_element(*self.bs_class_started_title).is_displayed()
            subject_name_displayed = self.get_element(*self.bs_subject_name).is_displayed()
            topic_name_displayed = self.get_element(*self.bs_topic_name).is_displayed()
            join_btn_displayed = self.get_element(*self.bs_join_btn).is_displayed()
            cancel_btn_displayed = self.get_element(*self.bs_cancel_btn).is_displayed()
            return ReturnType(True, "items in bottom sheet are correctly displayed") if all(
                (cls_started_title_displayed, subject_name_displayed, topic_name_displayed, join_btn_displayed,
                 cancel_btn_displayed)) else ReturnType(False, "items in bottom sheet are correctly displayed")

        return ReturnType(False, "Bottoms sheet is not available")

    def join_the_class_bottom_sheet(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, self.bs_join_btn[-1]))).click()

    def clear_app_data_and_relaunch_the_app(self):
        try:
            self.execute_command('adb shell pm clear %s' % self.package_name)
            self.execute_command('adb shell monkey -p %s -c android.intent.category.LAUNCHER 1' % self.package_name)
            return ReturnType(True, "Cleared the app and relauncehd")
        except:
            return ReturnType(False, "Couldn't clear the app and relauncehd")

    def verify_home_page_loaded(self):
        return self.text_match("Byju's Classes")

    def navigate_to_home_screen(self):
        HomePage(self.driver).navigate_to_home_screen(self.driver)

    def navigate_to_one_to_many_and_mega_user(self):
        HomePage(self.driver).navigate_to_one_to_many_and_mega_user(self.driver)

    def login_as_free_user(self):
        HomePage(self.driver).reset_and_login_with_otp(self.driver, "free")

    def click_on_completed_card(self, index):
        cards_list = self.obj.get_elements('id', self.subject_names)
        cards_list[index].click()


class LoginException(Exception):
    pass
