from time import sleep
from selenium.webdriver.common.by import By
import json

import logging
from Constants.constants import CONFIG_PATH
from Constants.load_json import *
from Constants.constants import Hamburger_Options
from selenium.common.exceptions import NoSuchElementException
from Utilities.common_methods import CommonMethods
from Constants.constants import CONFIG_PATH, Login_Credentials, Hamburger_Options
import logging
import pytest

# from POM_Pages.videopage import data_file
# fp = open(r'C:\Users\Mural\OneDrive\Desktop\application_data.json','r')
# fp=  open(r'C:\EclipseWorkspaces\csse120\Pytest_BDD\src/test_data/application_data.json','r')
# my_dict = json.loads(fp.read())
# fp.close()

# PATH = lambda p: os.path.abspath(
#    os.path.join(os.path.dirname(__file__), p)
# )
# 
# sys.path.append(PATH('./loginpage/'))
# from login import BaseSetup

# sys.path.append(PATH('../../../Utilities/'))
# from POM_Pages.Hamburgermenu import Hamburger


page_value = None
CommonMethods = CommonMethods()

data_file = CONFIG_PATH

featureFileName = "Hamburger Menu"


class Hamburger:
    def __init__(self, driver):
        self.driver = driver

    loc_allow_btn_id = "com.android.packageinstaller:id/permission_allow_button"
    cont_allow_btn_id = "com.android.packageinstaller:id/permission_allow_button"
    mob_Field_id = "com.byjus.thelearningapp:id/etPhoneNumber"
    #drp_den_id="com.byjus.thelearningapp:id/spnrCountry"
    nxt_btn_id = "com.byjus.thelearningapp:id/btnLogin"
    otp_msg_id = "com.byjus.thelearningapp:id/etOTP"
    ham_btn_id = (By.ID, "com.byjus.thelearningapp.premium:id/roundedNavButton")
    optins_list_id = (By.ID, "com.byjus.thelearningapp:id/home_drawer_lstvw_options")
    prof_btn_id = (By.ID, "com.byjus.thelearningapp.premium:id/home_drawer_imgvw_arrow_right")
    prof_acc_det_id = (By.ID, "com.byjus.thelearningapp.premium:id/account_details_title")
    prof_details_id = (By.ID, "com.byjus.thelearningapp.premium:id/profile_details")
    bmark_xpath = (By.XPATH, "//android.widget.TextView[@text='Bookmarks']")
    Bookmark_page_id = (By.ID, "com.byjus.thelearningapp.premium:id/header_title_text")
    Enqiure_now = (By.XPATH, "//android.widget.Button[@text='Enquire Now']")
    Enquire_page_xpath = (By.XPATH, "//android.view.View[@text='Enquire Now']")
    School_league_xpath = (By.XPATH, "//android.widget.TextView[@text='School Super League']")
    School_league_page_xpath = (By.XPATH, "//android.view.View[@text='Discovery']")
    #     Login Locators
    back_button_id = (By.ID, "com.byjus.thelearningapp.premium:id/backNav")
    profile_name_hamburger = (By.ID, "com.byjus.thelearningapp.premium:id/home_drawer_txtvw_profile_name")
    account_details_title = (By.ID, "com.byjus.thelearningapp.premium:id/account_details_title")
    profile_mob_num = (By.ID, "com.byjus.thelearningapp.premium:id/mobile_number")
    country_Code = (By.ID, "com.byjus.thelearningapp.premium:id/spnrCountry")
    loginBtn_id = (By.ID, "com.byjus.thelearningapp.premium:id/btnLogin")
    OtpTxtBx_id = (By.ID, "com.byjus.thelearningapp.premium:id/etOTP")
    allow_btn_id = (By.ID, "com.android.packageinstaller:id/permission_allow_button")
    none_of_the_above_id = (By.ID, "com.google.android.gms:id/cancel")
    loginPageVerify_id = (By.XPATH, "//android.widget.Button[@text='Login']")
    multiple_accounts_dialog = (By.ID, "com.byjus.thelearningapp.premium:id/dialog_linearlayout")
    user_profile_name = (By.ID, "com.byjus.thelearningapp.premium:id/tv_profile_name")
    profile_select_radio_button = (By.ID, "com.byjus.thelearningapp.premium:id/profile_select_radio_button")
    continue_button = (By.ID, "com.byjus.thelearningapp.premium:id/tv_submit")
    welcome_button = (By.ID, "com.byjus.thelearningapp.premium:id/welcomeButton")
    phone_num = (By.ID, "com.byjus.thelearningapp.premium:id/etPhoneNumber")
    user_name_profile_page = (By.ID, "com.byjus.thelearningapp.premium:id/name")
    homescreen_corana_dialog_ok_btn = (By.XPATH, "//android.widget.TextView[@text = 'OK']")
    homescreen_corana_dialog = (By.ID, "com.byjus.thelearningapp:id/dialog_layout")

    def reset_and_login_with_otp(self, driver):
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
        CommonMethods.scrollToElementAndClick(driver, getdata(Login_Credentials, 'login_detail3'
                                                               , 'country_code'))
        CommonMethods.enterText(driver, getdata(Login_Credentials, 'login_detail3', 'mobile_no'),
                                self.phone_num)
        CommonMethods.wait_for_locator(driver, self.loginBtn_id, 15)
        CommonMethods.elementClick(driver, self.loginBtn_id)

        CommonMethods.wait_for_locator(driver, self.OtpTxtBx_id, 15)
        CommonMethods.enterText(driver, getdata(Login_Credentials, 'login_detail3', 'OTP'),
                                self.OtpTxtBx_id)
        if CommonMethods.wait_for_element_visible(driver, self.multiple_accounts_dialog, 5):
            profiles = CommonMethods.getElements(driver, self.user_profile_name)
            radio_buttons = CommonMethods.getElements(driver, self.profile_select_radio_button)
            for profile in profiles:
                for button in radio_buttons:
                    if profile.text == getdata(Login_Credentials, 'login_detail3', 'profile_name'):
                        button.click()
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
                actual_mob_num = getdata(data_file, 'profile_credentials', 'mobileNum')
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

    #
    # def verify_badge(self, driver):
    #     if CommonMethods.wait_for_element_visible(driver, self.video_badge_close_btn, 2):
    #         CommonMethods.elementClick(driver, self.video_badge_close_btn)

    def verify_corana_dialog(self, driver):
        if CommonMethods.wait_for_element_visible(driver, self.homescreen_corana_dialog, 10):
            CommonMethods.elementClick(driver, self.homescreen_corana_dialog_ok_btn)

    def tap_on_device_back_btn(self, driver):
        sleep(3)
        CommonMethods.click_on_device_back_btn(driver)

    # def tap_on_back_arrow_btn(self, driver):
    #     sleep(3)
    #     back_arrow = CommonMethods.getElement(driver, self.practice_back_arrow_btn)
    #     back_arrow.click()

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
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'navigateToHomeScreen')

        except:
            CommonMethods.exception(driver, featureFileName, 'navigateToHomeScreen')

    def hamburger_verify(self, driver):
        # sleep(5)
        try:
            if CommonMethods.wait_for_element_visible(driver, self.ham_btn_id, 15):
                CommonMethods.elementClick(driver, self.ham_btn_id)
            else:
                logging.info('Hamburger menu Not Found')
                pytest.fail("Failed due to Hamburger Menu")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'hamburger_verify')
        except:
            CommonMethods.exception(driver, featureFileName, 'hamburger_verify')

    def Profilescreen_tap(self, driver):
        try:
            if CommonMethods.wait_for_element_visible(driver, self.prof_btn_id, 5):
                CommonMethods.elementClick(driver, self.prof_btn_id)

            else:
                logging.info("Profile button not found")
                pytest.fail("failed due to profile button")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'Profilescreen_tap')
        except:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'Profilescreen_tap')

    '''Profile screen method will verify the text in the profile screen'''

    def profilescreen_verify(self, driver):
        try:
            CommonMethods.scrollToElement(driver, "Account Details")
            if CommonMethods.wait_for_element_visible(driver, self.prof_acc_det_id, 10):
                act_txt = CommonMethods.getAttributeOfElement(driver, 'text', self.prof_acc_det_id)

                print("Actual Text--------------", act_txt)
                exp_txt = "Account Details"
                assert act_txt == exp_txt, "Account details text  failed "
                # CommonMethods.is_element_visible( driver,self.prof_details_id)
                CommonMethods.click_on_device_back_btn(driver)

            else:
                logging.info("Request home page text not found")
                pytest.fail(" Text Request home demo page not found ")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'profilescreen_verify')
        except:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'profilescreen_verify')

    '''hamburger Enquire now  will click on Enquire now option'''

    def hamburger_enquire_now(self, driver):
        try:
            if CommonMethods.wait_for_element_visible(driver, self.Enqiure_now, 10):
                CommonMethods.elementClick(driver, self.Enqiure_now)

            else:
                logging.info("Enquire now  button  not found")
                pytest.fail("Enquire now button not visible in the screen ")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'hamburger_enquire_now')
        except:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'hamburger_enquire_now')

    '''request homedemo page will verify the request home demo page screen '''

    def enquire_now_page(self, driver):

        try:
            sleep(10)
            if CommonMethods.wait_for_element_visible(driver, self.Enquire_page_xpath, 10):
                act_txt = CommonMethods.getAttributeOfElement(driver, 'text', self.Enquire_page_xpath)

                print("Actual text===================", act_txt)
                exp_txt = "Enquire Now"
                assert act_txt == exp_txt, "Enquire Now assert failed"
                CommonMethods.click_on_device_back_btn(driver)
            #
            else:
                logging.info("Enquire Now page text not found")
                pytest.fail(" Text Enquire Now page not found ")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'enquire_now_page')
        except:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'enquire_now_page')

    '''hamburger spl method will search for spl option on hamburger '''

    def hamburger_spl(self, driver):

        try:
            check = CommonMethods.isElementPresent(driver, self.School_league_xpath)
            if check == True:
                logging.info("Element is visiable without scroll")
            else:
                while check == False:
                    size = driver.get_window_size()
                    starty = int(size["height"] * 0.80)
                    endy = int(size["height"] * 0.30)
                    startx = int(size["width"] * 0.20)
                    sleep(2)
                    driver.swipe(startx, starty, startx, endy, 1000)
                    check = CommonMethods.isElementPresent(driver, self.School_league_xpath)
                    break
            CommonMethods.elementClick(driver, self.School_league_xpath)
            logging.info("school super league is clicked")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'hamburger_spl')
        except:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'hamburger_spl')

    ''' ssl verify method will verify the text present in DSSL page'''

    def ssl_verify(self, driver):
        try:
            sleep(10)
            if CommonMethods.wait_for_element_visible(driver, self.School_league_page_xpath, 5):
                act_txt = CommonMethods.getAttributeOfElement(driver, 'text', self.School_league_page_xpath)

                print("Actual text============================", act_txt)
                exp_txt = "Discovery"
                assert act_txt == exp_txt, "Discovery super League text failed "
                CommonMethods.click_on_device_back_btn(driver)
            else:
                logging.info("Discovery super League text failed")
                pytest.fail(" Text Discovery super League text failed ")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'ssl_verify')
        except:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'ssl_verify')

    def Hamburger_page(self, driver, text):

        try:

            key = text
            exp_txt = getdata(Hamburger_Options, 'hamburger_options', key)
            print(exp_txt)
            ham_page = (By.XPATH, "//android.widget.TextView[@text=\'" + exp_txt + "\']")
            if CommonMethods.wait_for_element_visible(driver, ham_page, 10):
                act_txt = CommonMethods.getAttributeOfElement(driver, 'text', ham_page)
                print("=================================================")
                print(act_txt)
                print(exp_txt)
                print("==============================================================")
                assert act_txt == exp_txt, " Page text failed to match"
                CommonMethods.click_on_device_back_btn(driver)
            else:
                logging.info("Discovery super League text failed")
                pytest.fail(" Text Discovery super League text failed ")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'Hamburger_page')
        except:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'Hamburger_page')

    ''' tap hamburger option will tap on the options which are present on Hamburger '''

    def tap_hamburger_option(self, driver, text):

        ham_opt = (By.XPATH, "//android.widget.TextView[@text=\'" + text + "\']")

        check = CommonMethods.isElementPresent(driver, ham_opt)
        if check == True:
            CommonMethods.elementClick(driver, ham_opt)

        else:
            print(" Element not found ")
            logging.info("Locator not found")

    def scroll_hamburg_verify(self, driver, text):
        try:
            ham_opt = (By.XPATH, "//android.widget.TextView[@text=\'" + text + "\']")

            check = CommonMethods.isElementPresent(driver, ham_opt)
            if check == True:
                logging.info("Element is visiable without scroll")
            else:
                while check == False:
                    size = driver.get_window_size()
                    starty = int(size["height"] * 0.80)
                    endy = int(size["height"] * 0.30)
                    startx = int(size["width"] * 0.20)
                    sleep(2)
                    driver.swipe(startx, starty, startx, endy, 1000)
                    check = CommonMethods.isElementPresent(driver, ham_opt)
                    break
            CommonMethods.elementClick(driver, ham_opt)
            logging.info("Element found and  clicked")
            key = text
            exp_txt = getdata(Hamburger_Options, 'hamburger_options', key)
            print(exp_txt)
            ham_page = (By.XPATH, "//android.widget.TextView[@text=\'" + exp_txt + "\']")
            if CommonMethods.wait_for_element_visible(driver, ham_page, 3):
                act_txt = CommonMethods.getAttributeOfElement(driver, 'text', ham_page)
                print("=================================================")
                print(act_txt)
                print(exp_txt)
                print("==============================================================")
                assert act_txt == exp_txt, " Page text failed to match"
                CommonMethods.click_on_device_back_btn(driver)
            else:
                logging.info("Required text failed")
                pytest.fail(" text failed ")


        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'scroll_hamburg_verify')
        except:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'scroll_hamburg_verify')

    def profile_button(self, driver):
        try:
            if CommonMethods.wait_for_element_visible(driver, self.prof_btn_id, 10):
                CommonMethods.elementClick(driver, self.prof_btn_id)
            else:
                logging.info("Profile button not found")
                pytest.fail("failed in absence of profile button ")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'profile_button')

    def scroll(self, driver, start_y, end_y, start_x, end_x):

        size = driver.get_window_size()
        starty = int(size["height"] * start_y)
        endy = int(size["height"] * end_y)
        startx = int(size["width"] * start_x)
        endx = int(size["height"] * end_x)

        driver.swipe(startx, starty, endx, endy, 1000)
