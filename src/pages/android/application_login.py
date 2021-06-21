import re
import subprocess
from time import sleep
from appium.webdriver.common.touch_action import TouchAction

from pages.base.application_login import LoginBase
from utilities.return_type import ReturnType
from utilities.tutor_common_methods import TutorCommonMethods
from pages.android.scroll_cards import ScrollCards
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from subprocess import Popen
from json import load
from utilities.staging_tllms import Stagingtllms
import logging
from constants.load_json import get_data
from constants.constants import *
import pytest_check as check


class Login(LoginBase, TutorCommonMethods):
    def __init__(self, driver=None):
        self.action = TouchAction(driver)
        self._scroll = ScrollCards(driver)
        self.package_name = driver.desired_capabilities['appPackage']
        self.driver = driver
        self.phone_number = "//*[contains(@resource-id, 'etPhoneNumber')]"
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
        self.otp_id = '%s:id/etOTP' % self.package_name
        self.snack_bar = '//*[contains(@resource-id, "bar_text")]'
        self.dash_board_many = '//*[contains(@resource-id, "llScheduleList")]'
        self.btn_classroom = '//*[contains(@resource-id, "btnClassroom")]'
        self.btn_personal = '//*[contains(@resource-id,"btnPersonalise")]'
        self.btn_premium = '//*[contains(@resource-id,"btnPremiumSchool")]'
        self.profile_back_button = '//*[contains(@resource-id, "roundedNavButton")]'
        self.on_boarding_login_btn = "id", "%s:id/buttonLogin" % self.package_name
        self.multi_account_list = 'id', '%s:id/rv_user_profile' % self.package_name
        self.multi_account_radio_btn = 'id', '%s:id/profile_select_radio_button' % self.package_name
        self.submit_account = 'id', '%s:id/tv_submit' % self.package_name
        self.welcome_btn = 'id', '%s:id/welcomeButton' % self.package_name
        self.close_badge_reward = 'id', '%s:id/ivCloseBtn' % self.package_name
        self.hamburger_icon = 'id', '%s:id/roundedNavButton' % self.package_name
        self.switch_profile_btn = 'id', '%s:id/home_drawer_btn_switch_profile' % self.package_name
        self.home_drawer = 'id', '%s:id/home_drawer_imgvw_arrow_right' % self.package_name
        self.garde_rv_tv = 'id', '%s:id/tvGrade' % self.package_name
        self.grade_rv = 'id', '%s:id/course_view_group' % self.package_name
        self.grade_name_view = 'id', '%s:id/course_name_view' % self.package_name
        self.grade_radio_btn_view = 'id', '%s:id/course_radio_button_view' % self.package_name
        self.user_profile_name = 'id', '%s:id/tvUserName' % self.package_name
        self.user_profile_phone = 'id', '%s:id/mobile_number' % self.package_name
        self.none_number_select = 'id', 'com.google.android.gms:id/cancel'
        self.bottom_sheet_layout = 'id', '%s:id/design_bottom_sheet' % self.package_name
        self.action_layout_ignore = 'id', '%s:id/tvCancel' % self.package_name
        self.action_layout_dismiss = 'id', '%s:id/tv_secondaryAction' % self.package_name
        self.permission_deny_btn = 'xpath', '//*[contains(@resource-id, "permission_deny_button")]'
        self.permission_allow_btn = 'xpath', '//*[contains(@resource-id, "permission_allow_button")]'
        self.login_data, self.user_mobile, self.profile_name, self.otp, self.premium_id = None, None, None, None, None
        self.os_version_major = int(subprocess.getoutput("adb shell getprop ro.build.version.release").split(".")[0])
        self.premium_login_text = 'id', '%s:id/img_premium_login' % self.package_name
        self.selected_text_view = 'id', '%s:id/drop_down_text_view' % self.package_name
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

        self.set_user_profile()
        super().__init__(driver)

    def implicit_wait_for(self, pool=15):
        self.driver.implicitly_wait(pool)

    def set_user_profile(self, login_profile='login_details_3', user_profile='user_1', sub_profile='profile_1'):
        self.login_data = get_data(Login_Credentials, login_profile)
        self.user_mobile = self.login_data[user_profile]["mobile_number"]
        self.profile_name = self.login_data[user_profile][sub_profile]["profile_name"]
        self.otp = self.login_data[user_profile]["OTP"]
        self.premium_id = self.login_data[user_profile][sub_profile]["premium_id"]
        return self

    def grant_permissions(self, p_type='allow'):
        grant_permissions_activity = "GrantPermissionsActivity"
        count = 5
        current_activity = self.driver.current_activity
        permission_deny_btn = 'xpath', '//*[contains(@resource-id, "permission_deny_button")]'
        permission_allow_btn = 'xpath', '//*[contains(@resource-id, "permission_allow_button")]'
        while grant_permissions_activity in current_activity and count:
            if p_type == 'allow':
                self.get_element(*permission_allow_btn).click()
            else:
                self.get_element(*permission_deny_btn).click()
            current_activity = self.driver.current_activity
            count -= 1

    def switch_profile(self):
        if "HomeActivity" in self.driver.current_activity:
            self.get_element(*self.hamburger_icon).click()
            self.get_element(*self.switch_profile_btn).click()
        self.get_element(
            'android_uiautomator',
            'UiScrollable(UiSelector().resourceId("com.byjus.thelearningapp.premium:id/rv_user_profile")).'
            'setSwipeDeadZonePercentage(0.25).'
            f'scrollTextIntoView("{self.profile_name}")'
        ).click()
        self.get_element(*self.submit_account).click()

    def switch_grade(self, grade=None):
        self.get_element(*self.hamburger_icon).click()
        self.get_element(*self.home_drawer).click()
        for grade_view in self.get_elements(*self.grade_rv):
            if grade in grade_view.find_element_by_id(self.grade_name_view[-1]).text:
                grade_view.find_element_by_id(self.grade_radio_btn_view[-1]).click()
                self.click_back()
                self.clear_app_from_recents()
                return True
        return False

    def verify_user_profile(self):
        badge_activity = "EarnedBadgeActivity"
        badge_screen_active = self.wait_activity(badge_activity, 5)
        if badge_screen_active:
            self.get_element(*self.close_badge_reward).click()
        self.implicit_wait_for(3)
        try:
            self.get_element(*self.action_layout_dismiss, wait=False).click()
        except NoSuchElementException:
            pass
        try:
            self.get_element(*self.action_layout_ignore, wait=False).click()
        except NoSuchElementException:
            pass
        self.implicit_wait_for(5)
        self.get_element(*self.hamburger_icon).click()
        self.get_element(*self.home_drawer).click()
        profile_activity = self.wait_activity("ProfileActivity", 20)
        grade = self.get_element(*self.garde_rv_tv).text
        if int(grade.strip(grade[grade.index("th"):])) < 6:
            self.user_profile_name = 'id', '%s:id/tvName' % self.package_name
        if profile_activity:
            if self.get_device_type() == 'tab':
                profile_phn_number = self.get_element(
                    'android_uiautomator',
                    'UiScrollable(new UiSelector()).setSwipeDeadZonePercentage(0.15).scrollIntoView(resourceId('
                    '"' + self.user_profile_phone[-1] + '"))'
                ).text
                profile_name = self.get_element(
                    'android_uiautomator',
                    'UiScrollable(new UiSelector()).setSwipeDeadZonePercentage(0.15).scrollIntoView(resourceId('
                    '"' + self.user_profile_name[-1] + '"))'
                ).text
            else:
                profile_phn_number = self.get_element(*self.user_profile_phone).text
                profile_name = self.get_element(*self.user_profile_name).text
            if profile_phn_number != self.user_mobile:
                self.reset_and_login_with_otp()
            elif profile_name != self.profile_name:
                self.click_back()
                self.switch_profile()
                try:
                    self.implicit_wait_for(3)
                    self.get_element(*self.action_layout_ignore, wait=False).click()
                except NoSuchElementException:
                    pass
            else:
                self.click_back()

    def verify_home_screen(self):
        home_activity = "HomeActivity"
        badge_activity = "EarnedBadgeActivity"
        user_home_activity = "UserHomeActivity"
        otm_home_activity = "OneToMegaHomeActivity"
        badge_screen_active = self.wait_activity(badge_activity, 5)
        if badge_screen_active:
            self.get_element(*self.close_badge_reward)
        self.wait_activity(home_activity)
        current_activity = self.driver.current_activity.split(".")[-1]
        if user_home_activity == current_activity or otm_home_activity == current_activity:
            retry = 2
            while not self.wait_activity(home_activity, 5) and retry:
                self.click_back()
                retry -= 1
            self.verify_user_profile()
        elif home_activity != current_activity:
            self.reset_and_login_with_otp()
        elif home_activity == current_activity:
            self.verify_user_profile()
        badge_screen_active = self.wait_activity(badge_activity, 10)
        if badge_screen_active:
            self.get_element(*self.close_badge_reward)

    def on_boarding_activity(self):
        grant_permissions_activity = "GrantPermissionsActivity"
        premium_on_boarding_activity = "PremiumOnBoardingActivity"
        gsm_activity = "CredentialPickerActivity"
        badge_activity = "EarnedBadgeActivity"
        self.wait_activity(grant_permissions_activity, 5)
        current_activity = self.driver.current_activity
        if grant_permissions_activity in current_activity:
            self.grant_permissions()
            self.get_element(*self.on_boarding_login_btn).click()
            if self.wait_activity(gsm_activity, 5):
                self.implicit_wait_for(0)
                try:
                    self.get_element(*self.none_number_select).click()
                except NoSuchElementException:
                    pass
        elif gsm_activity in current_activity:
            self.get_element(*self.none_number_select).click()
        elif premium_on_boarding_activity in current_activity:
            self.get_element(*self.on_boarding_login_btn).click()
        badge_screen_active = self.wait_activity(badge_activity, 10)
        if badge_screen_active:
            self.get_element(*self.close_badge_reward).click()
        self.implicit_wait_for(15)

    def click_on_premium_school(self):
        timeout = 3
        element = None
        while timeout:
            try:
                element = self.get_element(
                    'android_uiautomator',
                    'UiScrollable(UiSelector()).setSwipeDeadZonePercentage(0.25).'
                    'scrollIntoView(resourceId("com.byjus.thelearningapp.premium:id/marketing_classes_dynamic_image"))')
                break
            except NoSuchElementException:
                timeout -= 1
                if timeout == 1:
                    self.driver.launch_app()
                sleep(1)
        if not timeout:
            raise LoginException("Premium School card might not be displayed!")
        try:
            element.click()
            if not self.wait_activity('OneToMegaHomeActivity', 5):
                self.grant_permissions()
                try:
                    self.get_element('xpath', self.btn_premium).click()
                except NoSuchElementException:
                    pass
        except NoSuchElementException:
            raise LoginException("Premium School card might not be displayed!")

    def enter_phone(self, phone_num=None):
        self.wait_for_locator('xpath', self.phone_number)
        self.get_element('xpath', self.phone_number).clear()
        self.get_element('xpath', self.phone_number).send_keys(phone_num)

    def get_text_in_mobile_number_input(self):
        self.wait_for_locator('xpath', self.phone_number)
        return self.get_element('xpath', self.phone_number).text

    def click_on_next(self):
        self.wait_for_locator('xpath', self.next_btn)
        self.driver.find_element_by_xpath(self.next_btn).click()

    def enter_password(self, psswd=None):
        self.wait_for_locator('xpath', self.password)
        self.driver.find_element_by_xpath(self.password).send_keys(psswd)

    def switch_back_to_app(self):
        Popen('adb shell monkey -p %s -c android.intent.category.LAUNCHER 1' % self.package_name).wait()

    def is_app_icon_displayed(self) -> bool:
        """press home button"""
        self.driver.press_keycode(3)
        self.driver.press_keycode(3)
        screen_rect = self.driver.get_window_rect()
        x1 = x2 = screen_rect['width'] // 2
        y1 = screen_rect['height'] - (0.10 * screen_rect['height'])
        y2 = screen_rect['height'] - (0.75 * screen_rect['height'])
        self.driver.swipe(x1, y1, x2, y2, 500)
        self.get_element('class_name', 'android.widget.EditText').send_keys("Tutor")
        icon_displayed = self.get_element('xpath', self.app_icon).is_displayed()
        self.driver.press_keycode(3)
        if icon_displayed:
            return True
        return False

    def is_alert_displayed(self) -> bool:
        alert_obj = self.get_element('xpath', self.permission_alert).is_displayed()
        alert_msg = self.get_element('xpath', self.alert_message).text
        if alert_obj is True and "permissions are mandatory" in alert_msg:
            return True
        return False

    def allow_deny_permission(self, permissions=None):
        for permission in permissions:
            permission = permission.lower()
            if permission == 'allow':
                btn_action = self.get_element(
                    'xpath', '//*[contains(@resource-id, "' + permission + '")]'
                )
                logging.info("Permission Allowed")
            elif permission == 'deny':
                btn_action = self.get_element(
                    'xpath', '//*[contains(@resource-id, "' + permission + '")]'
                )
                logging.info("Permission Denied")
            else:
                logging.info("Not a valid permission")
                return 1
            btn_action.click()

    def is_login_form_displayed(self):
        login_form = self.get_element('xpath', '//*[contains(@resource-id, "LoginContentForm")]').is_displayed()
        if login_form is True:
            return True
        return False

    def text_match(self, expected_text=None):
        text_matches = self.is_text_match(expected_text)
        if text_matches is True:
            return True
        return False

    def dropdown_select(self):
        self.get_element('class_name', "android.widget.Spinner").click()
        drop_down = self.get_element('class_name', 'android.widget.ListView')
        return drop_down

    def is_dropdown_displayed(self):
        drop_down = self.dropdown_select()
        drop_down_visible = drop_down.is_displayed()
        self.action.tap(x=10, y=100).perform()
        if drop_down_visible is True:
            return ReturnType(True, "Dropdown is being displayed")
        return ReturnType(False, "Dropdown is not being displayed")

    def close_dropdown(self):
        self.action.tap(x=10, y=100).perform()

    def is_dropdown_displayed_without_clicking(self):
        drop_down = self.get_element('class_name', 'android.widget.ListView')
        drop_down_visible = drop_down.is_displayed()
        if drop_down_visible is True:
            return ReturnType(True, "Dropdown is being displayed")
        return ReturnType(False, "Dropdown is not being displayed")

    def mobile_number_input(self):
        input_box = self.get_element('xpath', self.phone_number).is_displayed()
        if input_box is True:
            return True
        return False

    def find_buttons(self):
        buttons = self.get_elements('class_name', self.button_cls)
        return buttons

    def find_input_boxes(self):
        input_boxes = self.get_elements('class_name', 'android.widget.EditText')
        return input_boxes

    def is_toast_message_displayed(self, message=None):
        toast_msg = self.get_element('xpath', '//android.widget.Toast').text
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
        self.get_element('xpath', self.phone_number).clear()

    def validate_error_msg(self, expected_text=None):
        try:
            actual_text = self.get_element('xpath', '//*[contains(@resource-id, "PhoneError")]').text
            if expected_text.capitalize() == actual_text:
                return True
            return False
        except:
            return False

    def is_app_minimized(self):
        _status = self.query_app_state('com.byjus.tutorplus')
        state = (_status // 3) == 1
        return state

    def is_all_permission_visible(self):
        dialog_box, page_num = None, None
        try:
            self.driver.implicitly_wait(0)
            page_num = self.get_element(
                'xpath', '//*[contains(@resource-id, "current_page_text")]').text
        except NoSuchElementException:
            dialog_box = self.get_element(
                'xpath', '//*[contains(@resource-id, "dialog_container")]').is_displayed()
        if dialog_box is not None:
            return dialog_box
        return page_num

    def is_password_field_visible(self):
        try:
            field_displayed = self.get_element('xpath', '//*[contains(@resource-id, "LayoutPassword")]').is_displayed()
            return field_displayed
        except NoSuchElementException:
            return False

    def field_visibility_text(self, parameter=None):
        try:
            actual_text = self.get_element('xpath', '//*[contains(@text, "' + parameter + '")]').text
            return actual_text
        except NoSuchElementException:
            return str()

    def is_homescreen_displayed(self):
        try:
            home_screen = self.get_element('xpath', '//*[contains(@resource-id, "TutorHomeLyt")]').is_displayed()
            return home_screen
        except NoSuchElementException:
            return False

    def click_on_session_card(self, index=None):
        session_cards_list = self.get_elements('xpath', self.btn_session_board)
        session_cards_list[index].click()

    def is_offline_validation_layout_displayed(self):
        layout = self.get_element('xpath', self.offline_validation_layout).is_displayed()
        if layout is True:
            return True
        return False

    def verify_offline_validation_layout(self, text1=None, text2=None):
        self.is_button_enabled(text1)
        self.is_button_enabled(text2)

    def click_on_link(self, parameter=None):
        link = self.get_element('xpath', '//android.widget.TextView[@text="' + parameter + '"]')
        link.click()

    def wait_for_dialog_to_be_invisible(self):
        self.wait_for_invisibility_of_element('xpath', self.offline_validation_layout)

    def click_on_country_code_dropdown(self):
        self.get_element('class_name', self.country_dropdown_cls).click()

    def enter_reg_mobile_number(self):
        self.enter_cc_and_phone_number()

    def enter_cc_and_phone_number(self, account_type='many'):
        self.click_on_country_code_dropdown()
        data = self.user_mobile
        # if account_type == 'many':
        #     # data = Stagingtllms(self.driver, staging_login=False).get_mobile_and_ccode()
        # elif account_type == 'personal':
        #     data = str(get_data('../../config/config.json', 'account_with_password', 'mobile'))
        mobile_and_code = data.split('-')
        self.select_country_code(mobile_and_code[0])
        self.enter_phone(mobile_and_code[1])
        return mobile_and_code[1]

    def click_on_mobile_number_field(self):
        self.wait_for_locator('xpath', self.phone_number)
        self.get_element('xpath', self.phone_number).click()

    def select_country_code(self, expected_text=None):
        self.wait_for_locator('class_name', 'android.widget.ListView')
        country_codes = self.get_elements('class_name', self.text_view_cls)
        drop_down = self.get_element('class_name', 'android.widget.ListView')
        while True:
            for country_code in country_codes:
                actual = re.findall(r"[\\+0-9]+", country_code.text)[0]
                if expected_text == actual:
                    country_code.click()
                    return 0
            self._scroll.scroll_by_card(country_codes[-1], drop_down)
            drop_down = self.get_element('class_name', 'android.widget.ListView')
            country_codes = self.get_elements('class_name', self.text_view_cls)

    def get_country_codes_from_dropdown(self, expected_text=None):
        if not self.is_dropdown_displayed_without_clicking().result:
            self.click_on_country_code_dropdown()
        self.wait_for_locator('class_name', 'android.widget.ListView')
        country_codes = self.get_elements('class_name', self.text_view_cls)
        drop_down = self.get_element('class_name', 'android.widget.ListView')
        country_codes_list = []
        for country_code in country_codes:
            country_codes_list.append(country_code.text.replace("(", " (").replace("  (", " ("))
        return country_codes_list

    def wait_for_element_not_to_be_present(self, element=None, timeout=30):
        self.driver.implicitly_wait(0)
        while timeout:
            try:
                e = self.get_element('xpath', element, wait=False)
                if e.is_displayed():
                    ele_loc = e.location
                    x = ele_loc['x']
                    y = ele_loc['y'] - 20
                    self.action.tap(x=x, y=y).perform()
            except (NoSuchElementException, StaleElementReferenceException):
                break
            timeout -= 1
        if not timeout:
            raise Exception("Element is always present within given time")
        self.driver.implicitly_wait(10)

    def is_otp_screen_displayed(self):
        self.wait_for_element_not_to_be_present('//*[contains(@resource-id, "dialog_layout")]')
        otp_page_displayed = self.get_element('xpath',
                                              '//*[contains(@resource-id, "otpVerificationForm")]').is_displayed()
        if otp_page_displayed is True:
            return True
        return False

    def verify_snack_bar_message(self, expected_text=None):
        try:
            snack_bar_text = self.get_element('xpath', self.snack_bar).text
            if snack_bar_text == expected_text:
                return True
            return False
        except (NoSuchElementException, StaleElementReferenceException):
            return None

    def is_auto_otp_dialog_box_displayed(self):
        try:
            bottom_sheet_dialog = self.get_element('xpath',
                                                   '//*[contains(@resource-id, "dialog_layout")]').is_displayed()
            if bottom_sheet_dialog:
                return bottom_sheet_dialog
            return False
        except (NoSuchElementException, StaleElementReferenceException):
            return None

    def enter_otp(self, otp=None, sub_profile_type='primary') -> None:
        if otp is not None:
            self.get_element('id', self.otp_id).send_keys(otp)
        else:
            self.get_otp()

    def get_otp(self) -> None:
        otp = Stagingtllms(self.driver).get_otp(self.user_mobile)
        self.wait_for_element_not_to_be_present('//*[contains(@resource-id, "dialog_layout")]')
        self.get_element('id', self.otp_id).send_keys(otp)

    def is_timer_displayed(self):
        try:
            timer = self.get_element('xpath', '//*[contains(@resource-id, "Countdown")]').is_displayed()
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
        self.get_element('xpath', '//*[contains(@resource-id,"tvPhoneNo")]').click()

    def is_one_to_many_dashboard_displayed(self):
        self.implicit_wait_for(10)
        try:
            screen_displayed = self.get_element(
                'xpath', self.dash_board_many).is_displayed()
        except NoSuchElementException:
            try:
                self.driver.find_element_by_xpath(
                    '//*[contains(@resource-id, "tvCancel")]').click()
            except (NoSuchElementException, StaleElementReferenceException):
                logging.log(10, "UP NEXT session pop up is not displayed")
            screen_displayed = self.get_element(
                'xpath', self.dash_board_many).is_displayed()
        self.implicit_wait_for(0)
        if screen_displayed:
            return True
        return False

    def tap_bck_btn(self):
        self.click_back()

    @staticmethod
    def get_from_config(key):
        with open(r'../../config/config.json', 'r') as fp:
            raw_data = load(fp)
        return raw_data[key]

    def click_on_one_to_many(self):
        try:
            self.get_element('xpath', self.btn_classroom).click()
        except NoSuchElementException:
            pass

    def select_country_code_other(self, expected_text=None):
        country_codes = self.get_elements('class_name', self.text_view_cls)
        for country_code in country_codes:
            if expected_text not in country_code.text:
                country_code.click()
                break

    def enter_passwd(self):
        psswd = str(get_data('../../config/config.json', 'account_with_password', 'password'))
        self.enter_password(psswd)

    def login_with_otp(self):
        retry = 5
        timeout = 20
        self.on_boarding_activity()
        verify_activity = "VerifyActivity"
        self.enter_reg_mobile_number()
        self.button_click("Next")
        self.wait_for_element_not_to_be_present('//*[contains(@resource-id, "dialog_layout")]')
        try:
            if self.otp is None:
                raise ValueError("OTP")
            while retry:
                self.implicit_wait_for(0)
                try:
                    self.enter_otp(self.otp)
                    self.implicit_wait_for(15)
                    retry = 0
                except NoSuchElementException:
                    self.wait_for_element_not_to_be_present('//*[contains(@resource-id, "dialog_layout")]')
        except ValueError as error:
            if error.args[0] == 'OTP':
                self.enter_otp()
            else:
                raise
        current_activity = self.driver.current_activity
        if verify_activity in current_activity:
            self.implicit_wait_for(0)
            try:
                self.get_element(
                    'android_uiautomator',
                    'UiScrollable(UiSelector()).setSwipeDeadZonePercentage(0.25).'
                    f'scrollTextIntoView("{self.profile_name}")'
                ).click()
                self.get_element(*self.submit_account).click()
            except NoSuchElementException:
                pass
        dialog_visible = True
        self.implicit_wait_for(0)
        while timeout:
            try:
                if dialog_visible:
                    dialog_layout = self.get_element(*self.bottom_sheet_layout, wait=False)
                    if dialog_layout.is_displayed():
                        dialog_layout.find_element_by_id(self.action_layout_ignore[-1]).click()
                        dialog_visible = False
                self.get_element(*self.welcome_btn).click()
                timeout = 0
            except (NoSuchElementException, StaleElementReferenceException):
                timeout -= 1
                if timeout == 5:
                    dialog_visible = False
                sleep(1)
        self.implicit_wait_for(15)

    def reset_and_login_with_otp(self):
        self.execute_command('adb shell pm clear %s' % self.package_name)
        self.execute_command('adb shell monkey -p %s -c android.intent.category.LAUNCHER 1' % self.package_name)
        self.login_with_otp()

    def cancel_session_join(self):
        try:
            self.driver.find_element_by_xpath(
                '//*[contains(@resource-id, "tvCancel")]').click()
        except (NoSuchElementException, StaleElementReferenceException):
            logging.log(10, "UP NEXT session pop up is not displayed")

    def verify_student_profile(self):
        try:
            if self.is_element_present('xpath', '//*[contains(@resource-id, "ClassroomAvatarImg")]'):
                self.get_element('xpath', '//*[contains(@resource-id, "ClassroomAvatarImg")]').click()
                expected_mobile_number = self.get_element('xpath', '//*[contains(@resource-id, "mobile_number")]').text
                account_details = '../../config/config.json'
                actual_mobile_number = str(get_data(account_details, 'account_details', 'mobile'))
                if expected_mobile_number == actual_mobile_number:
                    logging.info('classroom page verified')
                    self.get_element('xpath', self.profile_back_button).click()
                else:
                    self.reset_and_login_with_otp()
            else:
                self.reset_and_login_with_otp()
        except NoSuchElementException:
            logging.info('Error in verifying classroom page')
        finally:
            try:
                self.cancel_session_join()
            except NoSuchElementException:
                pass

    def is_up_next_and_unattended_cards_displayed(self):
        list_of_cards = self.get_elements('xpath', '//*[contains(@resource-id, "ScheduleCard")]')
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
                box = self.get_element('xpath', '//*[contains(@resource-id, "rvScheduleList")]')
                self._scroll.scroll_by_card(last_card, box)
                un_attended_cards = self.get_elements('xpath', '//*[contains(@resource-id, "ScheduleCard")]')
            else:
                try:
                    last_card.find_element_by_xpath('//*[contains(@resource-id, "SessionTakenDone")]')
                    return False
                except NoSuchElementException:
                    return True

    def tap_on(self, text=None):
        element = self.get_element(
            'android_uiautomator',
            'UiScrollable(UiSelector()).setSwipeDeadZonePercentage(0.25).'
            'scrollIntoView(textMatches("%s"))' % text)
        element.click()
        re.findall(r'(?i)premium school', element.text)

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
            raise NotImplementedError
        else:
            try:
                if text == 'Premium Login':
                    sleep(2)

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
                elif text.lower() == 'this phone number is not registered with a premium account':
                    sleep(3)
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
                                         text='India(+91+),UAE(+971),Bahrain(+973),Kuwait(+965),Oman(+968),'
                                              'Qatar(+974),Saudi Arabia(+966),United Arab Emirates (+971)',
                                         ordered=True):
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
        sleep(2)

        unauthenticated_play_store = 'UnauthenticatedMainActivity'
        main_activity = 'MainActivity'
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
        sleep(1)
        try:
            if self.get_element(*self.dialog_description).is_displayed():
                return ReturnType(True, "Sibling prifile dialog displayed")
            else:
                return ReturnType(False, "Sibling prifile  dialog not displayed")
        except:
            return ReturnType(False, "Sibling prifile  dialog not displayed")

    def verify_sibling_screen_profiles(self):
        elements = self.get_elements(*self.sibling_profile_names)
        if len(elements) > 1:
            return ReturnType(True, "Sibling profiles are shown")
        else:
            return ReturnType(False, "Sibling profiles are not shown")

    def verify_sibling_screen_radio_buttons(self):
        elements = self.get_elements(*self.sibling_radio)
        if len(elements) > 1:
            return ReturnType(True, "Sibling radio buttons  are shown")
        else:
            return ReturnType(False, "Sibling radio buttons are not shown")

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

    def verify_country_code(self,country_code="+91"):
        required_text = self.get_element(*self.selected_text_view).text
        return ReturnType(True, "{} text correct".format(country_code)) if required_text == country_code else ReturnType(
            False,
            "{} text is not correct".format(
                country_code))


class LoginException(Exception):
    pass
