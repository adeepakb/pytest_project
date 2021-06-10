import re
from appium.webdriver.common.touch_action import TouchAction
from constants.constants import Login_Credentials
from pages.android.homepage import HomePage
from pages.base.login_base import LoginBase
from utilities.tutor_common_methods import TutorCommonMethods
from pages.android.scroll_cards import ScrollCards
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from subprocess import Popen
from json import load
from utilities.staging_tlms import Stagingtlms
import logging
from constants.load_json import getdata
from utilities.common_methods import CommonMethods

CommonMethods = CommonMethods()


class ReturnType():
    def __init__(self, result, reason):
        self.result = result
        self.reason = reason


class LoginAndroid(LoginBase):
    def __init__(self, driver):
        self.obj = TutorCommonMethods(driver)
        self.action = TouchAction(driver)
        self._scroll = ScrollCards(driver)
        self.driver = driver
        self.phone_number = "com.byjus.thelearningapp.premium:id/etPhoneNumber"
        self.password = "//*[contains(@resource-id, 'etPassword')]"
        self.next_btn = "//*[contains(@resource-id, 'btnNext')]"
        self.login_btn = "//*[contains(@resource-id, 'btnLogin')]"
        self.btn_session_board = '//*[contains(@resource-id,"ScheduleCard")]'
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
        self.byjus_class_card = '//*[@resource-id = "com.byjus.thelearningapp.premium:id/home_card_title_text" and @text="Byju\'s Classes"]'
        self.home_card_layout = "com.byjus.thelearningapp.premium:id/home_card_layout"
        self.marketing_classes_image = 'com.byjus.thelearningapp.premium:id/marketing_classes_dynamic_image'

    def implicit_wait_for(self, pool):
        self.driver.implicitly_wait(pool)

    def click_on_premium_school(self):
        try:
            self.obj.wait_for_locator('id', self.home_card_layout)
            self.obj.get_element('android_uiautomator', 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(text("Byju\'s Classes"))')
            self.obj.element_click('xpath',self.byjus_class_card)
            if self.obj.is_element_present('xpath', self.permission_container) or self.obj.is_element_present('xpath',self.permission_container_tab):
                self.allow_deny_permission(["Allow", "Allow", "Allow"])
        except NoSuchElementException:
            self.obj.element_click('id', 'com.byjus.thelearningapp.premium:id/backToTopClick')
            element = self.obj.get_element('android_uiautomator', 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(resourceId("'+self.marketing_classes_image+'"))')
            width = element.size['width']
            height = element.size['height']
            self.action.press(None,element.location['x']+(width/2),height).wait(3000).move_to(x=element.location['x']+(width/2), y=2*height).release().perform()
            element.click()

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

    def enter_phone(self):
        self.obj.wait_for_locator('id', self.phone_number)
        self.obj.get_element('id', self.phone_number).send_keys(
            getdata(Login_Credentials, 'login_detail3', 'mobile_no'))

    def enter_otp(self):
        self.obj.wait_for_locator('id', self.OtpTxtBx_id)
        self.obj.get_element('id', self.OtpTxtBx_id).send_keys(getdata(Login_Credentials, 'login_detail3', 'OTP'))
        self.select_profile()
        self.obj.element_click('id', self.continue_button)
        self.obj.wait_for_locator('id', self.welcome_button, 15)
        self.obj.element_click('id', self.welcome_button)

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

    def enter_password(self, psswd):
        self.obj.wait_for_locator('xpath', self.password)
        self.driver.find_element_by_xpath(self.password).send_keys(psswd)

    def select_profile(self):
        data = getdata(Login_Credentials, 'login_detail3', 'profile_one_to_many_and_mega')
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

    def text_match(self, expected_text):
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
                return True
        return False

    def is_toast_message_displayed(self, message):
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

    def validate_error_msg(self, expected_text):
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

    def field_visibility_text(self, parameter):
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

    def click_on_session_card(self, index):
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

    def verify_offline_validation_layout(self, text1, text2):
        self.obj.is_button_enabled(text1)
        self.obj.is_button_enabled(text2)

    def click_on_link(self, parameter):
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
        data = None
        if account_type == 'many':
            data = Stagingtlms(self.driver).get_mobile_and_ccode()
        elif account_type == 'personal':
            data = str(getdata('../../config/config.json', 'account_with_password', 'mobile'))
        mobile_and_code = data.split('-')
        self.select_country_code(mobile_and_code[0])
        self.enter_phone(mobile_and_code[1])
        return mobile_and_code[1]

    def select_country_code(self, expected_text):
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

    def wait_for_element_not_to_be_present(self, element, timeout=10):
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

    def verify_snack_bar_message(self, expected_text):
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

    def get_otp(self, driver) -> None:
        OTP = Stagingtlms(driver).get_otp()
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

    def is_text_box_editable(self, previous_text):
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

    def select_country_code_other(self, expected_text):
        country_codes = self.obj.get_elements('class_name', self.text_view_cls)
        for country_code in country_codes:
            if expected_text not in country_code.text:
                country_code.click()
                break

    def enter_passwd(self):
        psswd = str(getdata('../../config/config.json', 'account_with_password', 'password'))
        self.enter_password(psswd)

    def reset_and_login_with_otp(self):
        self.obj.execute_command('adb shell pm clear com.byjus.tutorplus')
        self.obj.execute_command('adb shell monkey -p com.byjus.tutorplus -c android.intent.category.LAUNCHER 1')
        self.allow_deny_permission(["Allow", "Allow", "Allow"])
        self.enter_reg_mobile_number()
        self.button_click("Next")
        try:
            self.click_on_link('Login with OTP')
        except NoSuchElementException:
            self.wait_for_element_not_to_be_present('//*[contains(@resource-id, "dialog_layout")]')
            self.enter_otp()
        else:
            self.wait_for_element_not_to_be_present('//*[contains(@resource-id, "dialog_layout")]')
            self.enter_otp()

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
                actual_mobile_number = str(getdata(account_details, 'account_details', 'mobile'))
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

    def verify_home_page_loaded(self):
        return self.text_match("Byju's Classes")

    def navigate_to_home_screen(self):
        HomePage(self.driver).navigate_to_home_screen(self.driver)

    def navigate_to_one_to_many_and_mega_user(self):
        HomePage(self.driver).navigate_to_one_to_many_and_mega_user(self.driver)

    def login_as_free_user(self):
        HomePage(self.driver).reset_and_login_with_otp(self.driver, "free")