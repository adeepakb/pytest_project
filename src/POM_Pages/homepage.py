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
from Utilities.API_methods import *
from Utilities.common_methods import CommonMethods
from Constants.constants import CONFIG_PATH, Login_Credentials
from Constants.load_json import getdata

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
    allow_btn_id = (By.ID, "com.android.packageinstaller:id/permission_allow_button")
    none_of_the_above_id = (By.ID, "com.google.android.gms:id/cancel")
    loginPageVerify_id = (By.XPATH, "//android.widget.Button[@text='Login']")
    welcome_button = (By.ID, "com.byjus.thelearningapp.premium:id/welcomeButton")

    #    home Page Locators
    dialogBoxUnregisteredNo_id = (By.ID, "com.byjus.thelearningapp.premium:id/dialog_layout")
    registerBtnInDialog_id = (By.ID, "com.byjus.thelearningapp.premium:id/primaryAction")
    register_page_name_field = (By.ID, "com.byjus.thelearningapp.premium:id/etName")
    register_page_mobile_num_field = (By.ID, "com.byjus.thelearningapp.premium:id/etPhoneNumber")
    register_page_email_txt_bx = (By.ID, "com.byjus.thelearningapp.premium:id/etEmail")
    register_page_register_btn = (By.ID, "com.byjus.thelearningapp.premium:id/btnRegister")

    def __init__(self, browser):
        self.browser = browser

    def handle_covid19_popup_secondary_ok_opn(self, browser):
        try:
            CommonMethods.wait_for_element_visible(browser, self.covid19_pop_up, 5)
            check = CommonMethods.isElementPresent(browser, self.covid19_pop_up)
            if check == True:
                CommonMethods.elementClick(browser, self.covid19_secondary_ok_opt)
                logging.info("stay safe covid19 pop up is present")
        except:
            logging.info("stay safe covid19 pop up is not present")

    def click_on_subject(self, browser):
        #browser.find_element_by_xpath(self.btn_mathematics).click()
        CommonMethods.elementClick(browser, self.btn_mathematics)

    def cancle_for_google_auto_suggestion(self, browser):
        check = CommonMethods.isElementPresent(browser, self.mob_no_auto_sugestion)
        try:
            if check == True:
                CommonMethods.elementClick(browser, self.mob_no_auto_sugestion)
                logging.info("auto suggestion for mob no was displayed")
                logging.info("successfully clicked on cancel auto suggestion")
        except:
            logging.info("auto suggestion for mob no was not displayed")

    def select_subject_mathematics(self, browser):
        CommonMethods.wait_for_locator(browser, self.btn_mathematics_xpath, 15)
        CommonMethods.elementClick(browser, self.btn_mathematics_xpath)

    def verify_corana_dialog(self, browser):
        if CommonMethods.wait_for_element_visible(browser, self.homescreen_corana_dialog, 10):
            CommonMethods.elementClick(browser, self.homescreen_corana_dialog_ok_btn)

    def tap_on_device_back_btn(self, browser):
        CommonMethods.click_on_device_back_btn(browser)

    #     ----
    def verify_to_login_page(self, browser, code, countrycode, mobno, otp):
        try:
            if CommonMethods.wait_for_element_visible(browser, self.allow_btn_id, 3):
                CommonMethods.accept_notification(browser, self.allow_btn_id)
                CommonMethods.accept_notification(browser, self.allow_btn_id)
                CommonMethods.click_none_of_the_above(browser, self.none_of_the_above_id)
                CommonMethods.wait_for_locator(browser, self.country_Code, 15)
                CommonMethods.elementClick(browser, self.country_Code)
                sleep(1)
                CommonMethods.scrollToElementAndClick(browser, countrycode)
                CommonMethods.enterText(browser, mobno, self.phone_num)
                CommonMethods.wait_for_locator(browser, self.loginBtn_id, 15)
                CommonMethods.elementClick(browser, self.loginBtn_id)
                CommonMethods.wait_for_locator(browser, self.OtpTxtBx_id, 15)
                CommonMethods.enterText(browser, otp, self.OtpTxtBx_id)
            elif CommonMethods.isElementPresent(browser, self.loginBtn_id) == True:
                CommonMethods.wait_for_locator(browser, self.country_Code, 15)
                CommonMethods.elementClick(browser, self.country_Code)
                sleep(2)
                CommonMethods.scrollToElementAndClick(browser, countrycode)
                CommonMethods.enterText(browser, mobno, self.phone_num)
                CommonMethods.wait_for_locator(browser, self.loginBtn_id, 15)
                CommonMethods.elementClick(browser, self.loginBtn_id)
                CommonMethods.wait_for_locator(browser, self.OtpTxtBx_id, 15)
                CommonMethods.enterText(browser, otp, self.OtpTxtBx_id)
                return True
            else:
                logging.info('Error in verify_to_login_page in Homepage')
        except:
            logging.info('Error in verify_to_login_page method in Homepage')

    def reset_and_login_with_otp(self, browser):
        CommonMethods.run('adb shell pm clear com.byjus.thelearningapp.premium')
        CommonMethods.run(
            'adb shell am start -n com.byjus.thelearningapp.premium/com.byjus.app.onboarding.activity.SplashActivity')
        CommonMethods.accept_notification(browser, self.allow_btn_id)
        CommonMethods.wait_for_locator(browser, self.loginPageVerify_id, 5)
        CommonMethods.elementClick(browser, self.loginPageVerify_id)
        CommonMethods.click_none_of_the_above(browser, self.none_of_the_above_id)
        CommonMethods.wait_for_locator(browser, self.country_Code, 5)
        CommonMethods.elementClick(browser, self.country_Code)
        sleep(2)
        CommonMethods.scrollToElementAndClick(browser, getdata(Login_Credentials, 'login_detail3'
                                                               , 'country_code'))
        CommonMethods.enterText(browser, getdata(Login_Credentials, 'login_detail3', 'mobile_no'),
                                self.phone_num)
        CommonMethods.wait_for_locator(browser, self.loginBtn_id, 15)
        CommonMethods.elementClick(browser, self.loginBtn_id)
        CommonMethods.wait_for_locator(browser, self.OtpTxtBx_id, 15)
        CommonMethods.enterText(browser, getdata(Login_Credentials, 'login_detail3', 'OTP'),
                                self.OtpTxtBx_id)
        if CommonMethods.wait_for_element_visible(browser, self.multiple_accounts_dialog, 5):
            profiles = CommonMethods.getElements(browser, self.user_profile_name)
            radio_buttons = CommonMethods.getElements(browser, self.profile_select_radio_button)
            for profile in profiles:
                for button in radio_buttons:
                    if profile.text == getdata(Login_Credentials, 'login_detail3', 'profile_name'):
                        button.click()
                        break
        CommonMethods.elementClick(browser, self.continue_button)
        CommonMethods.wait_for_locator(browser, self.welcome_button, 15)
        CommonMethods.elementClick(browser, self.welcome_button)

    def verify_home_page(self, browser):
        print("------------------------method")
        try:
            if CommonMethods.wait_for_element_visible(browser, self.back_button_id, 3):
                CommonMethods.elementClick(browser, self.back_button_id)
                CommonMethods.wait_for_locator(browser, self.profile_name_hamburger, 5)
                CommonMethods.elementClick(browser, self.profile_name_hamburger)
                CommonMethods.wait_for_locator(browser, self.user_name_profile_page, 5)
                account_text = CommonMethods.getTextOfElement(browser, self.account_details_title)
                CommonMethods.scrollToElement(browser, account_text)
                expected_mob_num = CommonMethods.getTextOfElement(browser, self.profile_mob_num)
                actual_mob_num = getdata(data_file, 'profile_credentials', 'mobileNum')
                if CommonMethods.verifyTwoText(actual_mob_num, expected_mob_num):
                    print("---------------above")
                    CommonMethods.click_on_device_back_btn(browser)
                    print("----------------------below")
                    logging.info('home page verified')
                else:
                    self.reset_and_login_with_otp(browser)
                    return True
            else:
                logging.info('user is not in Home page')
                return False
        except:
            logging.info('Error in Verifing Home Page')

    def navigate_to_home_screen(self, browser):
        try:
            # subject_rgb = (By.XPATH,"//android.widget.TextView[@text=\'"+text+"\']")
            if CommonMethods.wait_for_element_visible(browser, self.homescreen_corana_dialog, 6):
                CommonMethods.elementClick(browser, self.homescreen_corana_dialog_ok_btn)
                self.verify_home_page(browser)
                # VideoPage.subject_rgb_lst = self.get_the_rgb_lst(browser, subject_rgb)
            elif CommonMethods.wait_for_element_visible(browser, self.back_button_id, 3):
                # self.verify_badge(browser)
                self.verify_home_page(browser)
                # VideoPage.subject_rgb_lst = self.get_the_rgb_lst(browser, subject_rgb)
            else:
                self.reset_and_login_with_otp(browser)
        except NoSuchElementException:
            logging.info('Error in navigating to home page')

        except:
            logging.info('Error in navigating to home page')

    def after_delete_the_user(self, browser, code, countrycode, mobno, otp):
        try:
            CommonMethods.wait_for_element_visible(browser, countrycode, 15)
            CommonMethods.scrollToElementAndClick(browser, countrycode)
            CommonMethods.enterText(browser, mobno, self.phone_num)
            CommonMethods.wait_for_locator(browser, self.loginBtn_id, 15)
            CommonMethods.elementClick(browser, self.loginBtn_id)
        except NoSuchElementException:
            logging.info("Failed Locator in Method after_delete_the_user")

    def check_dialog_box_display(self, browser, grade):
        try:
            CommonMethods.wait_for_element_visible(browser, self.dialogBoxUnregisteredNo_id, 20)
            check = CommonMethods.isElementPresent(browser, self.dialogBoxUnregisteredNo_id)
            if (check == True):
                logging.info('Dialog box for unregistered no is displayed')
                CommonMethods.elementClick(browser, self.registerBtnInDialog_id)
                CommonMethods.wait_for_element_visible(browser, self.chooseCourse_Title_xpath, 7)
                CommonMethods.scrollToElementAndClick(browser, grade)
            else:
                logging.info('Dialog box is not present')
                logging.info("Failed Locator in Method checkDialogBoxDisplay")
                pytest.fail("Failed Due to Locator in Login Page")
        except NoSuchElementException:
            logging.info("Failed Locator in Method checkDialogBoxDisplay")
            pytest.fail("Failed Due to Locator in Login Page")

    def register_mobile_num(self, browser, name, mobile_num, email, otp):
        try:
            if CommonMethods.wait_for_element_visible(browser, self.register_page_name_field, 10):
                CommonMethods.enterText(browser, name, self.register_page_name_field)
                CommonMethods.enterText(browser, mobile_num, self.register_page_mobile_num_field)
                CommonMethods.enterText(browser, email, self.register_page_email_txt_bx)
                CommonMethods.elementClick(browser, self.register_page_register_btn)
                CommonMethods.wait_for_element_visible(browser, self.OtpTxtBx_id, 15)
                CommonMethods.enterText(browser, otp, self.OtpTxtBx_id)
                if CommonMethods.wait_for_element_visible(browser, self.homescreen_corana_dialog, 20):
                    CommonMethods.elementClick(browser, self.covid19_secondary_ok_opt)

        except:
            logging.info('Error in register_mobile_num method in Homepage')

    #     ------------------
    def verify_to_login_page_for_new_user(self, browser, code, countrycode, mobno, otp, grade, name, mobile_num, email,
                                          mob_with_country_code):
        try:
            if CommonMethods.wait_for_element_visible(browser, self.allow_btn_id, 3) == True:
                CommonMethods.accept_notification(browser, self.allow_btn_id)
                CommonMethods.accept_notification(browser, self.allow_btn_id)
                CommonMethods.click_none_of_the_above(browser, self.none_of_the_above_id)
                CommonMethods.wait_for_locator(browser, self.country_Code, 15)
                CommonMethods.elementClick(browser, self.country_Code)
                sleep(1)
                CommonMethods.scrollToElementAndClick(browser, countrycode)
                CommonMethods.enterText(browser, mobno, self.phone_num)
                CommonMethods.wait_for_locator(browser, self.loginBtn_id, 15)
                CommonMethods.elementClick(browser, self.loginBtn_id)
                if CommonMethods.isElementPresent(browser, self.registerBtnInDialog_id) == True:
                    self.check_dialog_box_display(browser, grade)
                    self.register_mobile_num(browser, name, mobile_num, email, otp)
                else:
                    delete_single_registered_mobile_num(browser, mob_with_country_code)
                    self.after_delete_the_user(browser, code, countrycode, mobno, otp)
                    self.check_dialog_box_display(browser, grade)
                    self.register_mobile_num(browser, name, mobno, email, otp)
            elif CommonMethods.isElementPresent(browser, self.loginBtn_id) == True:
                CommonMethods.wait_for_locator(browser, self.country_Code, 15)
                CommonMethods.elementClick(browser, self.country_Code)
                sleep(2)
                CommonMethods.scrollToElementAndClick(browser, countrycode)
                CommonMethods.enterText(browser, mobno, self.phone_num)
                CommonMethods.wait_for_locator(browser, self.loginBtn_id, 15)
                CommonMethods.elementClick(browser, self.loginBtn_id)
                if CommonMethods.isElementPresent(browser, self.registerBtnInDialog_id) == True:
                    self.check_dialog_box_display(browser, grade)
                    self.register_mobile_num(browser, name, mobile_num, email, otp)
                else:
                    delete_single_registered_mobile_num(browser, mob_with_country_code)
                    self.after_delete_the_user(browser, code, countrycode, mobno, otp)
                    self.check_dialog_box_display(browser, grade)
                    self.register_mobile_num(browser, name, mobno, email, otp)

            else:
                logging.info('Error in verify_to_login_page_for_new_user in Homepage')
        except:
            logging.info('Error in verify_to_login_page_for_new_user method in Homepage')

    def navigate_to_home_screen_for_new_user(self, browser, code, countrycode, mobno, otp, grade, name, mobile_num,
                                             email, mob_with_country_code):
        try:
            if CommonMethods.isElementPresent(browser, self.homescreen_corana_dialog) == True:
                CommonMethods.elementClick(browser, self.covid19_secondary_ok_opt)
                delete_single_registered_mobile_num(browser, mob_with_country_code)
                self.verify_to_login_page_for_new_user(browser, code, countrycode, mobno, otp, grade, name, mobile_num,
                                                       email, mob_with_country_code)
            elif CommonMethods.isElementPresent(browser, self.back_button_id) == True:
                delete_single_registered_mobile_num(browser, mob_with_country_code)
                self.verify_to_login_page_for_new_user(browser, code, countrycode, mobno, otp, grade, name, mobile_num,
                                                       email, mob_with_country_code)
            elif CommonMethods.isElementPresent(browser, self.loginBtn_id) == True:
                self.verify_to_login_page_for_new_user(browser, code, countrycode, mobno, otp, grade, name, mobile_num,
                                                       email, mob_with_country_code)

            elif CommonMethods.isElementPresent(browser, self.allow_btn_id) == True:
                self.verify_to_login_page_for_new_user(browser, code, countrycode, mobno, otp, grade, name, mobile_num,
                                                       email, mob_with_country_code)
            else:
                pytest.fail("failed in navigate_to_home_screen_for_new_user")
                logging.info("failed in navigate_to_home_screen_for_new_user")
        except:
            logging.info('Error in navigate_to_home_screen_for_new_user method in Homepage')
