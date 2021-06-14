'''it will show the home page options like subjects'''

from appium import webdriver
from time import sleep
import time
import sys
import os
from appium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import inspect
from selenium.webdriver.common.by import By
import logging
import pytest
from utilities.API_methods import *
from utilities.common_methods import CommonMethods
from constants.constants import CONFIG_PATH, Login_Credentials
from constants.load_json import get_data

CommonMethods = CommonMethods()


class HomePage():
    country_Code_id = (By.ID, "com.byjus.thelearningapp.premium:id/spnrCountry")
    phone_num_id = (By.ID, "com.byjus.thelearningapp.premium:id/etPhoneNumber")
    login_header_id = (By.ID, "com.byjus.thelearningapp.premium:id/header_title_text")
    OtpTxtBx_id = (By.ID, "com.byjus.thelearningapp.premium:id/etOTP")
    btn_mathematics_xpath = (By.XPATH, "//android.widget.TextView[@text='Mathematics']")
    txt_greetingText_id = (By.ID, "com.byjus.thelearningapp.premium:id/header_greeting_text")
    multiple_accounts_dialog = (By.ID, "com.byjus.thelearningapp.premium:id/dialog_linearlayout")
    user_profile_name = (By.ID, "com.byjus.thelearningapp.premium:id/tv_profile_name")
    profile_select_radio_button = (By.ID, "com.byjus.thelearningapp.premium:id/profile_select_radio_button")
    continue_button = (By.ID, "com.byjus.thelearningapp.premium:id/tv_submit")
    mob_no_auto_sugestion = (By.ID, "com.google.android.gms:id/cancel")
    user_name_profile_page = (By.ID, "com.byjus.thelearningapp.premium:id/tvUserName")
    country_Code = (By.ID, "com.byjus.thelearningapp.premium:id/spnrCountry")
    phone_num = (By.ID, "com.byjus.thelearningapp.premium:id/etPhoneNumber")
    loginBtn_id = (By.ID, "com.byjus.thelearningapp.premium:id/btnLogin")
    covid19_pop_up = (By.ID, "com.byjus.thelearningapp.premium:id/dialog_layout")
    homescreen_corana_dialog_ok_btn = (By.ID, "com.byjus.thelearningapp.premium:id/bt_primaryAction")
    homescreen_corana_dialog = (By.ID, "com.byjus.thelearningapp.premium:id/dialog_layout")
    profile_name = (By.ID, "com.byjus.thelearningapp.premium:id/header_title_text")
    covid19_secondary_ok_opt = (By.ID, "com.byjus.thelearningapp.premium:id/tv_secondaryAction")
    covid19_primary_reserve_noe_opn = (By.ID, "com.byjus.thelearningapp.premium:id/bt_primaryAction")
    free_live_classes_screen = (By.XPATH, "//android.view.View[@text='Free Live Classes']")

    #     ----------------
    #     On boarding screen locators
    skipBtn_id = (By.ID, "com.byjus.thelearningapp.premium:id/buttonSkip")

    #    Choose you course locators
    chooseCourse_Title_xpath = (By.XPATH, "//android.widget.TextView[@text='your course']")

    #    Register Page locators
    noneOftheAbove_xpath = (By.XPATH, "//android.widget.Button[@text='None of the above']")
    login_link_id = (By.ID, "com.byjus.thelearningapp.premium:id/tvLoginBl")

    #     Login Screen Locators
    back_button_id = (By.ID, "com.byjus.thelearningapp.premium:id/backNav")
    profile_name_hamburger = (By.ID, "com.byjus.thelearningapp.premium:id/home_drawer_txtvw_profile_name")
    account_details_title = (By.ID, "com.byjus.thelearningapp.premium:id/account_details_title")
    profile_mob_num = (By.ID, "com.byjus.thelearningapp.premium:id/mobile_number")
    # allow_btn_id = (By.ID, "com.android.packageinstaller:id/permission_allow_button")
    # allow_btn_id = (By.ID, "com.android.permissioncontroller:id/permission_allow_button")
    allow_btn_id = (By.XPATH, '//*[contains(@resource-id, "permission_allow_button")]')
    none_of_the_above_id = (By.ID, "com.google.android.gms:id/cancel")
    loginPageVerify_id = (By.XPATH, "//android.widget.Button[@text='Login']")
    cancel_join_now = (By.ID, "com.byjus.thelearningapp.premium:id/tvCancel")
    welcome_button = (By.ID, "com.byjus.thelearningapp.premium:id/welcomeButton")

    #    home Page Locators
    dialogBoxUnregisteredNo_id = (By.ID, "com.byjus.thelearningapp.premium:id/dialog_layout")
    registerBtnInDialog_id = (By.ID, "com.byjus.thelearningapp.premium:id/primaryAction")
    register_page_name_field = (By.ID, "com.byjus.thelearningapp.premium:id/etName")
    register_page_mobile_num_field = (By.ID, "com.byjus.thelearningapp.premium:id/etPhoneNumber")
    register_page_email_txt_bx = (By.ID, "com.byjus.thelearningapp.premium:id/etEmail")
    register_page_register_btn = (By.ID, "com.byjus.thelearningapp.premium:id/btnRegister")

    def __init__(self, driver):
        self.driver = driver

    def handle_covid19_popup_secondary_ok_opn(self, driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.covid19_pop_up, 5)
            check = CommonMethods.isElementPresent(driver, self.covid19_pop_up)
            if check == True:
                CommonMethods.elementClick(driver, self.covid19_secondary_ok_opt)
                logging.info("stay safe covid19 pop up is present")
        except:
            logging.info("stay safe covid19 pop up is not present")

    def click_on_subject(self, driver):
        # driver.find_element_by_xpath(self.btn_mathematics).click()
        CommonMethods.elementClick(driver, self.btn_mathematics)

    def cancle_for_google_auto_suggestion(self, driver):
        check = CommonMethods.isElementPresent(driver, self.mob_no_auto_sugestion)
        try:
            if check == True:
                CommonMethods.elementClick(driver, self.mob_no_auto_sugestion)
                logging.info("auto suggestion for mob no was displayed")
                logging.info("successfully clicked on cancel auto suggestion")
        except:
            logging.info("auto suggestion for mob no was not displayed")

    def select_subject_mathematics(self, driver):
        CommonMethods.wait_for_locator(driver, self.btn_mathematics_xpath, 15)
        CommonMethods.elementClick(driver, self.btn_mathematics_xpath)

    def verify_corana_dialog(self, driver):
        if CommonMethods.wait_for_element_visible(driver, self.homescreen_corana_dialog, 10):
            CommonMethods.elementClick(driver, self.homescreen_corana_dialog_ok_btn)

    def tap_on_device_back_btn(self, driver):
        CommonMethods.click_on_device_back_btn(driver)

    #     ----
    def verify_to_login_page(self, driver, code, countrycode, mobno, otp):
        try:
            if CommonMethods.wait_for_element_visible(driver, self.allow_btn_id, 3):
                CommonMethods.accept_notification(driver, self.allow_btn_id)
                CommonMethods.accept_notification(driver, self.allow_btn_id)
                CommonMethods.click_none_of_the_above(driver, self.none_of_the_above_id)
                CommonMethods.wait_for_locator(driver, self.country_Code, 15)
                CommonMethods.elementClick(driver, self.country_Code)
                sleep(1)
                CommonMethods.scrollToElementAndClick(driver, countrycode)
                CommonMethods.enterText(driver, mobno, self.phone_num)
                CommonMethods.wait_for_locator(driver, self.loginBtn_id, 15)
                CommonMethods.elementClick(driver, self.loginBtn_id)
                CommonMethods.wait_for_locator(driver, self.OtpTxtBx_id, 15)
                CommonMethods.enterText(driver, otp, self.OtpTxtBx_id)
            elif CommonMethods.isElementPresent(driver, self.loginBtn_id) == True:
                CommonMethods.wait_for_locator(driver, self.country_Code, 15)
                CommonMethods.elementClick(driver, self.country_Code)
                sleep(2)
                CommonMethods.scrollToElementAndClick(driver, countrycode)
                CommonMethods.enterText(driver, mobno, self.phone_num)
                CommonMethods.wait_for_locator(driver, self.loginBtn_id, 15)
                CommonMethods.elementClick(driver, self.loginBtn_id)
                CommonMethods.wait_for_locator(driver, self.OtpTxtBx_id, 15)
                CommonMethods.enterText(driver, otp, self.OtpTxtBx_id)
                return True
            else:
                logging.info('Error in verify_to_login_page in Homepage')
        except:
            logging.info('Error in verify_to_login_page method in Homepage')

    def login_as_three_plus_one_user(self, driver):
        CommonMethods.run('adb shell pm clear com.byjus.thelearningapp.premium')
        CommonMethods.run(
            'adb shell am start -n com.byjus.thelearningapp.premium/com.byjus.app.onboarding.activity.SplashActivity')
        CommonMethods.accept_notification(driver, self.allow_btn_id)
        CommonMethods.wait_for_locator(driver, self.loginPageVerify_id, 5)
        CommonMethods.elementClick(driver, self.loginPageVerify_id)
        CommonMethods.click_none_of_the_above(driver, self.none_of_the_above_id)
        CommonMethods.wait_for_locator(driver, self.country_Code, 5)
        CommonMethods.elementClick(driver, self.country_Code)
        sleep(2)
        CommonMethods.scrollToElementAndClick(driver, get_data(Login_Credentials, 'login_detail4', 'country_code'))
        CommonMethods.enterText(driver, get_data(Login_Credentials, 'login_detail4', 'mobile_no'), self.phone_num)
        CommonMethods.wait_for_locator(driver, self.loginBtn_id, 15)
        CommonMethods.elementClick(driver, self.loginBtn_id)
        CommonMethods.wait_for_locator(driver, self.OtpTxtBx_id, 15)
        CommonMethods.enterText(driver, get_data(Login_Credentials, 'login_detail4', 'OTP'), self.OtpTxtBx_id)

        data = get_data(Login_Credentials, 'login_detail4', 'profile_one_to_many_and_mega')
        if CommonMethods.wait_for_element_visible(driver, self.multiple_accounts_dialog, 5):
            CommonMethods.scrollToElement(driver, data)
            profiles = CommonMethods.getElements(driver, self.user_profile_name)
            radio_buttons = CommonMethods.getElements(driver, self.profile_select_radio_button)
            for i in range(len(profiles)):
                if profiles[i].text == data:
                    radio_buttons[i].click()
                    break
        CommonMethods.elementClick(driver, self.continue_button)
        CommonMethods.wait_for_locator(driver, self.welcome_button, 15)
        CommonMethods.elementClick(driver, self.welcome_button)

    def login_as_another_one_mega_user(self, driver,login_detail):
        CommonMethods.run('adb shell pm clear com.byjus.thelearningapp.premium')
        CommonMethods.run(
            'adb shell am start -n com.byjus.thelearningapp.premium/com.byjus.app.onboarding.activity.SplashActivity')
        CommonMethods.accept_notification(driver, self.allow_btn_id)
        CommonMethods.wait_for_locator(driver, self.loginPageVerify_id, 5)
        CommonMethods.elementClick(driver, self.loginPageVerify_id)
        CommonMethods.click_none_of_the_above(driver, self.none_of_the_above_id)
        CommonMethods.wait_for_locator(driver, self.country_Code, 5)
        CommonMethods.elementClick(driver, self.country_Code)
        sleep(2)
        CommonMethods.scrollToElementAndClick(driver, get_data(Login_Credentials, login_detail, 'country_code'))
        CommonMethods.enterText(driver, get_data(Login_Credentials, login_detail, 'mobile_no'), self.phone_num)
        CommonMethods.wait_for_locator(driver, self.loginBtn_id, 15)
        CommonMethods.elementClick(driver, self.loginBtn_id)
        CommonMethods.wait_for_locator(driver, self.OtpTxtBx_id, 15)
        CommonMethods.enterText(driver, get_data(Login_Credentials, login_detail, 'OTP'), self.OtpTxtBx_id)

        data = get_data(Login_Credentials, login_detail, 'profile_one_to_many_and_mega')
        if CommonMethods.wait_for_element_visible(driver, self.multiple_accounts_dialog, 5):
            CommonMethods.scrollToElement(driver, data)
            profiles = CommonMethods.getElements(driver, self.user_profile_name)
            radio_buttons = CommonMethods.getElements(driver, self.profile_select_radio_button)
            for i in range(len(profiles)):
                if profiles[i].text == data:
                    radio_buttons[i].click()
                    break
        CommonMethods.elementClick(driver, self.continue_button)
        # CommonMethods.wait_for_locator(driver, self.cancel_join_now, 15)
        # CommonMethods.elementClick(driver, self.cancel_join_now)
        CommonMethods.wait_for_locator(driver, self.welcome_button, 15)
        CommonMethods.elementClick(driver, self.welcome_button)

    def reset_and_login_with_otp(self, driver, account_type='personal'):
        CommonMethods.run('adb shell pm clear com.byjus.thelearningapp.premium')
        CommonMethods.run(
            'adb shell am start -n com.byjus.thelearningapp.premium/com.byjus.app.onboarding.activity.SplashActivity')
        CommonMethods.accept_notification(driver, self.allow_btn_id)
        CommonMethods.wait_for_locator(driver, self.loginPageVerify_id, 5)
        CommonMethods.elementClick(driver, self.loginPageVerify_id)
        CommonMethods.click_none_of_the_above(driver, self.none_of_the_above_id)
        CommonMethods.wait_for_locator(driver, self.country_Code, 5)
        CommonMethods.elementClick(driver, self.country_Code)
        sleep(2)
        CommonMethods.scrollToElementAndClick(driver, get_data(Login_Credentials, 'login_detail3'
                                                               , 'country_code'))
        CommonMethods.enterText(driver, get_data(Login_Credentials, 'login_detail3', 'mobile_no'),
                                self.phone_num)
        CommonMethods.wait_for_locator(driver, self.loginBtn_id, 15)
        CommonMethods.elementClick(driver, self.loginBtn_id)
        CommonMethods.wait_for_locator(driver, self.OtpTxtBx_id, 15)
        CommonMethods.enterText(driver, get_data(Login_Credentials, 'login_detail3', 'OTP'),
                                self.OtpTxtBx_id)
        data = None
        if account_type == 'personal':
            data = get_data(Login_Credentials, 'login_detail3', 'profile_name')
        elif account_type == 'one_to_many':
            data = get_data(Login_Credentials, 'login_detail3', 'profile_name_one_to_many')
        elif account_type == 'one_to_many_and_mega':
            data = get_data(Login_Credentials, 'login_detail3', 'profile_one_to_many_and_mega')

        if CommonMethods.wait_for_element_visible(driver, self.multiple_accounts_dialog, 5):
            CommonMethods.scrollToElement(driver, data)
            profiles = CommonMethods.getElements(driver, self.user_profile_name)
            radio_buttons = CommonMethods.getElements(driver, self.profile_select_radio_button)
            for i in range(len(profiles)):
                if profiles[i].text == data:
                    radio_buttons[i].click()
                    break
        CommonMethods.elementClick(driver, self.continue_button)
        CommonMethods.wait_for_locator(driver, self.welcome_button, 15)
        CommonMethods.elementClick(driver, self.welcome_button)

    def verify_home_page(self, driver):
        print("------------------------method")
        try:
            if CommonMethods.wait_for_element_visible(driver, self.back_button_id, 3):
                CommonMethods.elementClick(driver, self.back_button_id)
                CommonMethods.wait_for_locator(driver, self.profile_name_hamburger, 5)
                CommonMethods.elementClick(driver, self.profile_name_hamburger)
                CommonMethods.wait_for_locator(driver, self.user_name_profile_page, 5)
                CommonMethods.scrollToElement(driver, 'Account Details')
                CommonMethods.wait_for_locator(driver, self.profile_mob_num, 5)
                expected_mob_num = CommonMethods.getTextOfElement(driver, self.profile_mob_num)
                actual_mob_num = get_data(data_file, 'profile_credentials', 'mobileNum')
                if CommonMethods.verifyTwoText(actual_mob_num, expected_mob_num):
                    print("---------------above")
                    CommonMethods.click_on_device_back_btn(driver)
                    print("----------------------below")
                    logging.info('home page verified')
                else:
                    self.reset_and_login_with_otp(driver)
                    return True
            else:
                logging.info('user is not in Home page')
                return False
        except:
            logging.info('Error in Verifing Home Page')

    def verify_user_name(self, driver, account_type):
        print("------------------------method")
        try:
            if CommonMethods.wait_for_element_visible(driver, self.back_button_id, 3):
                CommonMethods.elementClick(driver, self.back_button_id)
                CommonMethods.wait_for_locator(driver, self.profile_name_hamburger, 5)
                CommonMethods.elementClick(driver, self.profile_name_hamburger)
                CommonMethods.wait_for_locator(driver, self.user_name_profile_page, 5)
                actual_username = None
                if account_type == 'one_to_many_and_mega':
                    actual_username = get_data(Login_Credentials, 'login_detail3', 'profile_one_to_many_and_mega')
                elif account_type == 'one_to_many':
                    actual_username = get_data(Login_Credentials, 'login_detail3', 'profile_name_one_to_many')
                expected_username = CommonMethods.getTextOfElement(driver, self.user_name_profile_page)
                if CommonMethods.verifyTwoText(expected_username, actual_username):
                    print("---------------above")
                    CommonMethods.click_on_device_back_btn(driver)
                    print("----------------------below")
                    logging.info('user name verified')
                else:
                    self.reset_and_login_with_otp(driver,account_type)
                    return True
            else:
                logging.info('user is not in Home page')
                return False
        except:
            logging.info('Error in Verifing Home Page')

    def navigate_to_home_screen(self, driver):
        try:
            # subject_rgb = (By.XPATH,"//android.widget.TextView[@text=\'"+text+"\']")

            if CommonMethods.wait_for_element_visible(driver, self.homescreen_corana_dialog, 6):
                CommonMethods.elementClick(driver, self.homescreen_corana_dialog_ok_btn)
                self.verify_home_page(driver)
                # VideoPage.subject_rgb_lst = self.get_the_rgb_lst(driver, subject_rgb)
            elif CommonMethods.wait_for_element_visible(driver, self.back_button_id, 3):
                # self.verify_badge(driver)
                self.verify_home_page(driver)
                # VideoPage.subject_rgb_lst = self.get_the_rgb_lst(driver, subject_rgb)
            else:
                self.reset_and_login_with_otp(driver)
        except NoSuchElementException:
            logging.info('Error in navigating to home page')

        except:
            logging.info('Error in navigating to home page')

    def navigate_to_one_to_many_user(self, driver):
        if CommonMethods.wait_for_element_visible(driver, self.back_button_id, 3):
            self.verify_user_name(driver, 'one_to_many')
        else:
            self.reset_and_login_with_otp(driver, 'one_to_many')

    def navigate_to_one_to_many_and_mega_user(self, driver):
        if CommonMethods.wait_for_element_visible(driver, self.back_button_id, 3):
            self.verify_user_name(driver, 'one_to_many_and_mega')
        else:
            self.reset_and_login_with_otp(driver, 'one_to_many_and_mega')

    def navigate_to_three_plus_one_user(self, driver):
        try:
            if CommonMethods.wait_for_element_visible(driver, self.back_button_id, 3):
                CommonMethods.elementClick(driver, self.back_button_id)
                CommonMethods.wait_for_locator(driver, self.profile_name_hamburger, 5)
                CommonMethods.elementClick(driver, self.profile_name_hamburger)
                CommonMethods.wait_for_locator(driver, self.user_name_profile_page, 5)
                actual_username = get_data(Login_Credentials, 'login_detail4', 'profile_one_to_many_and_mega')
                expected_username = CommonMethods.getTextOfElement(driver, self.user_name_profile_page)
                if CommonMethods.verifyTwoText(expected_username, actual_username):
                    print("---------------above")
                    CommonMethods.click_on_device_back_btn(driver)
                    print("----------------------below")
                    logging.info('user name verified')
                else:
                    self.login_as_three_plus_one_user(driver)
            else:
                logging.info('user is not in Home page')
                self.login_as_three_plus_one_user(driver)
        except:
            logging.info('Error in Verifing Home Page')

    def after_delete_the_user(self, driver, code, countrycode, mobno, otp):
        try:
            CommonMethods.wait_for_element_visible(driver, countrycode, 15)
            CommonMethods.scrollToElementAndClick(driver, countrycode)
            CommonMethods.enterText(driver, mobno, self.phone_num)
            CommonMethods.wait_for_locator(driver, self.loginBtn_id, 15)
            CommonMethods.elementClick(driver, self.loginBtn_id)
        except NoSuchElementException:
            logging.info("Failed Locator in Method after_delete_the_user")

    def check_dialog_box_display(self, driver, grade):
        try:
            CommonMethods.wait_for_element_visible(driver, self.dialogBoxUnregisteredNo_id, 20)
            check = CommonMethods.isElementPresent(driver, self.dialogBoxUnregisteredNo_id)
            if (check == True):
                logging.info('Dialog box for unregistered no is displayed')
                CommonMethods.elementClick(driver, self.registerBtnInDialog_id)
                CommonMethods.wait_for_element_visible(driver, self.chooseCourse_Title_xpath, 7)
                CommonMethods.scrollToElementAndClick(driver, grade)
            else:
                logging.info('Dialog box is not present')
                logging.info("Failed Locator in Method checkDialogBoxDisplay")
                pytest.fail("Failed Due to Locator in Login Page")
        except NoSuchElementException:
            logging.info("Failed Locator in Method checkDialogBoxDisplay")
            pytest.fail("Failed Due to Locator in Login Page")

    def register_mobile_num(self, driver, name, mobile_num, email, otp):
        try:
            if CommonMethods.wait_for_element_visible(driver, self.register_page_name_field, 10):
                CommonMethods.enterText(driver, name, self.register_page_name_field)
                CommonMethods.enterText(driver, mobile_num, self.register_page_mobile_num_field)
                CommonMethods.enterText(driver, email, self.register_page_email_txt_bx)
                CommonMethods.elementClick(driver, self.register_page_register_btn)
                CommonMethods.wait_for_element_visible(driver, self.OtpTxtBx_id, 15)
                CommonMethods.enterText(driver, otp, self.OtpTxtBx_id)
                if CommonMethods.wait_for_element_visible(driver, self.homescreen_corana_dialog, 20):
                    CommonMethods.elementClick(driver, self.covid19_secondary_ok_opt)

        except:
            logging.info('Error in register_mobile_num method in Homepage')

    #     ------------------
    def verify_to_login_page_for_new_user(self, driver, code, countrycode, mobno, otp, grade, name, mobile_num, email,
                                          mob_with_country_code):
        try:
            if CommonMethods.wait_for_element_visible(driver, self.allow_btn_id, 3) == True:
                CommonMethods.accept_notification(driver, self.allow_btn_id)
                CommonMethods.accept_notification(driver, self.allow_btn_id)
                CommonMethods.click_none_of_the_above(driver, self.none_of_the_above_id)
                CommonMethods.wait_for_locator(driver, self.country_Code, 15)
                CommonMethods.elementClick(driver, self.country_Code)
                sleep(1)
                CommonMethods.scrollToElementAndClick(driver, countrycode)
                CommonMethods.enterText(driver, mobno, self.phone_num)
                CommonMethods.wait_for_locator(driver, self.loginBtn_id, 15)
                CommonMethods.elementClick(driver, self.loginBtn_id)
                if CommonMethods.isElementPresent(driver, self.registerBtnInDialog_id) == True:
                    self.check_dialog_box_display(driver, grade)
                    self.register_mobile_num(driver, name, mobile_num, email, otp)
                else:
                    delete_single_registered_mobile_num(driver, mob_with_country_code)
                    self.after_delete_the_user(driver, code, countrycode, mobno, otp)
                    self.check_dialog_box_display(driver, grade)
                    self.register_mobile_num(driver, name, mobno, email, otp)
            elif CommonMethods.isElementPresent(driver, self.loginBtn_id) == True:
                CommonMethods.wait_for_locator(driver, self.country_Code, 15)
                CommonMethods.elementClick(driver, self.country_Code)
                sleep(2)
                CommonMethods.scrollToElementAndClick(driver, countrycode)
                CommonMethods.enterText(driver, mobno, self.phone_num)
                CommonMethods.wait_for_locator(driver, self.loginBtn_id, 15)
                CommonMethods.elementClick(driver, self.loginBtn_id)
                if CommonMethods.isElementPresent(driver, self.registerBtnInDialog_id) == True:
                    self.check_dialog_box_display(driver, grade)
                    self.register_mobile_num(driver, name, mobile_num, email, otp)
                else:
                    delete_single_registered_mobile_num(driver, mob_with_country_code)
                    self.after_delete_the_user(driver, code, countrycode, mobno, otp)
                    self.check_dialog_box_display(driver, grade)
                    self.register_mobile_num(driver, name, mobno, email, otp)

            else:
                logging.info('Error in verify_to_login_page_for_new_user in Homepage')
        except:
            logging.info('Error in verify_to_login_page_for_new_user method in Homepage')

    def navigate_to_home_screen_for_new_user(self, driver, code, countrycode, mobno, otp, grade, name, mobile_num,
                                             email, mob_with_country_code):
        try:
            if CommonMethods.isElementPresent(driver, self.homescreen_corana_dialog) == True:
                CommonMethods.elementClick(driver, self.covid19_secondary_ok_opt)
                delete_single_registered_mobile_num(driver, mob_with_country_code)
                self.verify_to_login_page_for_new_user(driver, code, countrycode, mobno, otp, grade, name, mobile_num,
                                                       email, mob_with_country_code)
            elif CommonMethods.isElementPresent(driver, self.back_button_id) == True:
                delete_single_registered_mobile_num(driver, mob_with_country_code)
                self.verify_to_login_page_for_new_user(driver, code, countrycode, mobno, otp, grade, name, mobile_num,
                                                       email, mob_with_country_code)
            elif CommonMethods.isElementPresent(driver, self.loginBtn_id) == True:
                self.verify_to_login_page_for_new_user(driver, code, countrycode, mobno, otp, grade, name, mobile_num,
                                                       email, mob_with_country_code)

            elif CommonMethods.isElementPresent(driver, self.allow_btn_id) == True:
                self.verify_to_login_page_for_new_user(driver, code, countrycode, mobno, otp, grade, name, mobile_num,
                                                       email, mob_with_country_code)
            else:
                pytest.fail("failed in navigate_to_home_screen_for_new_user")
                logging.info("failed in navigate_to_home_screen_for_new_user")
        except:
            logging.info('Error in navigate_to_home_screen_for_new_user method in Homepage')
