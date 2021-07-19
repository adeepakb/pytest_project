import json
import re
import subprocess
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from cryptography.fernet import Fernet
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

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

from selenium.webdriver.support import expected_conditions as EC


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
        self.dialog_layout = "id", "%s:id/dialog_layout" % self.package_name
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
        self.expired_later_btn = 'id', "%s:id/tvLater" % self.package_name
        self.se_call_us = 'id', "%s:id/btnCallUs" % self.package_name
        self.expired_msg_title = 'xpath', "//*[@text=\"Subscription Expired!\"]"
        self.bs_class_started_title = "id", "%s:id/tvClassStarted" % self.package_name
        self.bs_subject_name = "id", "%s:id/tvSubjectName" % self.package_name
        self.bs_topic_name = "id", "%s:id/tvSessionTitle" % self.package_name
        self.bs_join_btn = "id", "%s:id/btnJoinNow" % self.package_name
        self.bs_cancel_btn = "id", "%s:id/tvCancel" % self.package_name
        self.login_data, self.user_mobile, self.profile_name, self.otp, self.premium_id = None, None, None, None, None
        # self.os_version_major = int(subprocess.getoutput("adb shell getprop ro.build.version.release").split(".")[0])

        self.set_user_profile()
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 30)

    def implicit_wait_for(self, poll=15):
        self.driver.implicitly_wait(poll)

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
            'setSwipeDeadZonePercentage(0.1).'
            f'scrollTextIntoView("{self.profile_name}")'
        ).click()
        self.get_element(*self.submit_account).click()

    def switch_grade(self, grade=None):
        self.get_element(*self.hamburger_icon).click()
        self.get_element(*self.home_drawer).click()
        self.get_element(*self.garde_rv_tv).click()
        for grade_view in self.get_elements(*self.grade_rv):
            if str(grade) in grade_view.find_element_by_id(self.grade_name_view[-1]).text:
                grade_view.find_element_by_id(self.grade_radio_btn_view[-1]).click()
                self.click_back()
                self.clear_app_from_recents()
                self.driver.launch_app()
                return True
        return False

    @staticmethod
    def switch_back_to_app():
        Popen('adb shell monkey -p com.byjus.tutorplus -c android.intent.category.LAUNCHER 1').wait()

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

    def verify_user_profile(self):
        badge_activity = "EarnedBadgeActivity"
        badge_screen_active = self.wait_activity(badge_activity, 5)
        if badge_screen_active:
            self.get_element(*self.close_badge_reward).click()
        self.implicit_wait_for(5)
        try:
            self.get_element(*self.action_layout_dismiss, wait=False).click()
        except NoSuchElementException:
            pass
        try:
            self.get_element(*self.action_layout_ignore, wait=False).click()
        except NoSuchElementException:
            pass
        self.implicit_wait_for(3)
        # try:
        #     self.subscription_expired()
        #     self.get_element(*self.hamburger_icon).click()
        # except NoSuchElementException:
        try:
            self.get_element(*self.hamburger_icon).click()
            self.get_element(*self.home_drawer).click()
        except NoSuchElementException:
            self.reset_and_login_with_otp()
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
        badge_screen_active = self.wait_activity(badge_activity, 3)
        if badge_screen_active:
            self.get_element(*self.close_badge_reward)
        self.wait_activity(home_activity)
        current_activity = self.driver.current_activity.split(".")[-1]
        if user_home_activity == current_activity or otm_home_activity == current_activity:
            retry = 2
            while not self.wait_activity(home_activity, 3) and retry:
                self.click_back()
                retry -= 1
            self.verify_user_profile()
        elif home_activity != current_activity:
            self.reset_and_login_with_otp()
        elif home_activity == current_activity:
            self.verify_user_profile()
        badge_screen_active = self.wait_activity(badge_activity, 3)
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
        timeout = 1
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
                self.driver.implicitly_wait(2)
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

    def is_login_form_displayed(self):
        login_form = self.get_element('xpath', '//*[contains(@resource-id, "LoginContentForm")]').is_displayed()
        if login_form is True:
            return True
        return False

    def text_match(self, expected_text=None):
        text_matches = self.is_text_match(expected_text)
        if text_matches is True:
            return ReturnType(True, '%s text is displayed' % expected_text)
        return ReturnType(False, '%s text is not displayed' % expected_text)

    def dropdown_select(self):
        self.get_element('class_name', "android.widget.Spinner").click()
        drop_down = self.get_element('class_name', 'android.widget.ListView')
        return drop_down

    def is_dropdown_displayed(self):
        try:
            drop_down = self.dropdown_select()
            drop_down_visible = drop_down.is_displayed()
            self.action.tap(x=10, y=100).perform()
            if drop_down_visible is True:
                return ReturnType(True, "Dropdown is being displayed")
            return ReturnType(False, "Dropdown is not being displayed")
        except:
            return ReturnType(False, "Dropdown is not being displayed")

    def close_dropdown(self):
        self.action.tap(x=10, y=100).perform()

    def is_dropdown_displayed_without_clicking(self):
        try:
            drop_down = self.get_element('class_name', 'android.widget.ListView')
            drop_down_visible = drop_down.is_displayed()
            if drop_down_visible is True:
                return ReturnType(True, "Dropdown is being displayed")
            return ReturnType(False, "Dropdown is not being displayed")
        except:
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
        layout = self.get_element(*self.dialog_layout).is_displayed()
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
        self.wait_for_invisibility_of_element(*self.dialog_layout)

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
        fp = '../../config/config.json'
        key = os.getenv('SECRET')
        f = Fernet(key)
        encrypted_data = get_data(fp, 'encrypted_data', 'token')
        decrypted_data = json.loads(f.decrypt(encrypted_data.encode('ascii')))
        psswd = decrypted_data['account_with_password']['password']
        self.enter_password(psswd)

    def login_with_otp(self, bottom_sheet_dismiss=True):
        retry = 5
        if bottom_sheet_dismiss:
            timeout = 20
        else:
            timeout = 0
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
        if not timeout:
            try:
                self.get_element(*self.welcome_btn).click()
            except (NoSuchElementException, StaleElementReferenceException):
                pass
        while timeout:
            try:
                if dialog_visible:
                    dialog_layout = self.get_element(*self.bottom_sheet_layout, wait=False)
                    if dialog_layout.is_displayed():
                        if timeout % 2 == 0:
                            dialog_layout.find_element_by_id(self.action_layout_ignore[-1]).click()
                            dialog_visible = False
                        else:
                            dialog_layout.find_element_by_id(self.action_layout_dismiss[-1]).click()

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

    def subscription_expired(self, action="dismiss"):
        try:
            self.get_element(*self.action_layout_dismiss, wait=False).click()
        except NoSuchElementException:
            pass
        try:
            self.get_element(*self.action_layout_ignore, wait=False).click()
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
            return ReturnType(True, "items in bottom sheet are correctly dosplayed") if all(
                (cls_started_title_displayed, subject_name_displayed, topic_name_displayed, join_btn_displayed,
                 cancel_btn_displayed)) else ReturnType(False, "items in bottom sheet are correctly dosplayed")

        return ReturnType(False, "Bottoms sheet is not available")

    def join_the_class_bottom_sheet(self):
        self.wait.until(ec.element_to_be_clickable((By.ID, self.bs_join_btn[-1]))).click()


class LoginException(Exception):
    pass
