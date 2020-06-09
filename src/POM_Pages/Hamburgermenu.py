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
    def __init__(self, browser):
        self.browser = browser

    loc_allow_btn_id = "com.android.packageinstaller:id/permission_allow_button"
    cont_allow_btn_id = "com.android.packageinstaller:id/permission_allow_button"
    mob_Field_id = "com.byjus.thelearningapp:id/etPhoneNumber"
    #drp_den_id="com.byjus.thelearningapp:id/spnrCountry"
    nxt_btn_id = "com.byjus.thelearningapp:id/btnLogin"
    otp_msg_id = "com.byjus.thelearningapp:id/etOTP"
    ham_btn_id = (By.ID, "com.byjus.thelearningapp.premium:id/roundedNavButton")
    #ham_btn_id = (By.ID, "com.byjus.thelearningapp.premium:id/backNav")
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
    OtpTxtBx_id = (By.ID, "com.byjus.thelearningapp:id/etOTP")
    allow_btn_id = (By.ID, "com.android.packageinstaller:id/permission_allow_button")
    none_of_the_above_id = (By.ID, "com.google.android.gms:id/cancel")
    loginPageVerify_id = (By.XPATH, "//android.widget.TextView[@text='Login']")
    phone_num = (By.ID, "com.byjus.thelearningapp.premium:id/etPhoneNumber")
    user_name_profile_page = (By.ID, "com.byjus.thelearningapp.premium:id/tvUserName")
    homescreen_corana_dialog_ok_btn = (By.XPATH, "//android.widget.TextView[@text = 'OK']")
    homescreen_corana_dialog = (By.ID, "com.byjus.thelearningapp:id/dialog_layout")

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
                    CommonMethods.run('adb shell pm clear com.byjus.thelearningapp')
                    CommonMethods.run(
                        'adb shell am start -n com.byjus.thelearningapp/com.byjus.app.onboarding.activity.SplashActivity')
                    CommonMethods.accept_notification(browser, self.allow_btn_id)
                    CommonMethods.accept_notification(browser, self.allow_btn_id)
                    CommonMethods.click_none_of_the_above(browser, self.none_of_the_above_id)
                    CommonMethods.wait_for_locator(browser, self.country_Code, 15)
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
                    return True
            else:
                logging.info('user is not in Home page')
                return False
        except:
            logging.info('Error in Verifing Home Page')

    def verify_to_login_page(self, browser):
        if CommonMethods.wait_for_element_visible(browser, self.allow_btn_id, 3):
            CommonMethods.accept_notification(browser, self.allow_btn_id)
            CommonMethods.accept_notification(browser, self.allow_btn_id)
            CommonMethods.click_none_of_the_above(browser, self.none_of_the_above_id)
            CommonMethods.wait_for_locator(browser, self.country_Code, 15)
            CommonMethods.elementClick(browser, self.country_Code)
            sleep(1)
            CommonMethods.scrollToElementAndClick(browser, getdata(Login_Credentials, 'login_detail3', 'country_code'))
            CommonMethods.enterText(browser, getdata(Login_Credentials, 'login_detail3', 'mobile_no'), self.phone_num)
            CommonMethods.wait_for_locator(browser, self.loginBtn_id, 15)
            CommonMethods.elementClick(browser, self.loginBtn_id)
            CommonMethods.wait_for_locator(browser, self.OtpTxtBx_id, 15)
            CommonMethods.enterText(browser, getdata(Login_Credentials, 'login_detail3', 'OTP'), self.OtpTxtBx_id)
        elif CommonMethods.wait_for_element_visible(browser, self.loginBtn_id, 3):
            CommonMethods.wait_for_locator(browser, self.country_Code, 15)
            CommonMethods.elementClick(browser, self.country_Code)
            sleep(2)
            CommonMethods.scrollToElementAndClick(browser, getdata(Login_Credentials, 'login_detail3'
                                                                   , 'country_code'))
            CommonMethods.enterText(browser, getdata(Login_Credentials, 'login_detail3', 'mobile_no'), self.phone_num)
            CommonMethods.wait_for_locator(browser, self.loginBtn_id, 15)
            CommonMethods.elementClick(browser, self.loginBtn_id)
            CommonMethods.wait_for_locator(browser, self.OtpTxtBx_id, 15)
            CommonMethods.enterText(browser, getdata(Login_Credentials, 'login_detail3', 'OTP'), self.OtpTxtBx_id)
            return True
        else:
            logging.info('User verified Login page')
    #
    # def verify_badge(self, browser):
    #     if CommonMethods.wait_for_element_visible(browser, self.video_badge_close_btn, 2):
    #         CommonMethods.elementClick(browser, self.video_badge_close_btn)

    def verify_corana_dialog(self, browser):
        if CommonMethods.wait_for_element_visible(browser, self.homescreen_corana_dialog, 10):
            CommonMethods.elementClick(browser, self.homescreen_corana_dialog_ok_btn)

    def tap_on_device_back_btn(self, browser):
        sleep(3)
        CommonMethods.click_on_device_back_btn(browser)

    # def tap_on_back_arrow_btn(self, browser):
    #     sleep(3)
    #     back_arrow = CommonMethods.getElement(browser, self.practice_back_arrow_btn)
    #     back_arrow.click()

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
            elif CommonMethods.wait_for_element_visible(browser, self.allow_btn_id,
                                                        3) or CommonMethods.wait_for_element_visible(browser,
                                                                                                     self.loginBtn_id,
                                                                                                     3):
                self.verify_to_login_page(browser)
                self.verify_corana_dialog(browser)
                self.verify_home_page(browser)
            # VideoPage.subject_rgb_lst = self.get_the_rgb_lst(browser, subject_rgb)
            else:
                logging.info('Error in navigating to home page')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'navigateToHomeScreen')

        except:
            CommonMethods.exception(browser, featureFileName, 'navigateToHomeScreen')

    def hamburger_verify(self, browser):
        # sleep(5)
        try:
            if CommonMethods.wait_for_element_visible(browser, self.ham_btn_id, 15):
                CommonMethods.elementClick(browser, self.ham_btn_id)
            else:
                logging.info('Hamburger menu Not Found')
                pytest.fail("Failed due to Hamburger Menu")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'hamburger_verify')
        except:
            CommonMethods.exception(browser, featureFileName, 'hamburger_verify')

    def Profilescreen_tap(self, browser):
        try:
            if CommonMethods.wait_for_element_visible(browser, self.prof_btn_id, 5):
                CommonMethods.elementClick(browser, self.prof_btn_id)

            else:
                logging.info("Profile button not found")
                pytest.fail("failed due to profile button")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'Profilescreen_tap')
        except:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'Profilescreen_tap')

    '''Profile screen method will verify the text in the profile screen'''

    def profilescreen_verify(self, browser):
        try:
            if CommonMethods.wait_for_element_visible(browser, self.prof_acc_det_id, 10):
                act_txt = CommonMethods.getAttributeOfElement(browser, 'text', self.prof_acc_det_id)

                print("Actual Text--------------", act_txt)
                exp_txt = "Account Details"
                assert act_txt == exp_txt, "Account details text  failed "
                # CommonMethods.is_element_visible( browser,self.prof_details_id)
                CommonMethods.click_on_device_back_btn(browser)

            else:
                logging.info("Request home page text not found")
                pytest.fail(" Text Request home demo page not found ")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'profilescreen_verify')
        except:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'profilescreen_verify')

    '''hamburger Enquire now  will click on Enquire now option'''

    def hamburger_enquire_now(self, browser):
        try:
            if CommonMethods.wait_for_element_visible(browser, self.Enqiure_now, 10):
                CommonMethods.elementClick(browser, self.Enqiure_now)

            else:
                logging.info("Enquire now  button  not found")
                pytest.fail("Enquire now button not visible in the screen ")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'hamburger_enquire_now')
        except:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'hamburger_enquire_now')

    '''request homedemo page will verify the request home demo page screen '''

    def enquire_now_page(self, browser):

        try:
            sleep(10)
            if CommonMethods.wait_for_element_visible(browser, self.Enquire_page_xpath, 10):
                act_txt = CommonMethods.getAttributeOfElement(browser, 'text', self.Enquire_page_xpath)

                print("Actual text===================", act_txt)
                exp_txt = "Enquire Now"
                assert act_txt == exp_txt, "Enquire Now assert failed"
                CommonMethods.click_on_device_back_btn(browser)
            #
            else:
                logging.info("Enquire Now page text not found")
                pytest.fail(" Text Enquire Now page not found ")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'enquire_now_page')
        except:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'enquire_now_page')

    '''hamburger spl method will search for spl option on hamburger '''

    def hamburger_spl(self, browser):

        try:
            check = CommonMethods.isElementPresent(browser, self.School_league_xpath)
            if check == True:
                logging.info("Element is visiable without scroll")
            else:
                while check == False:
                    size = browser.get_window_size()
                    starty = int(size["height"] * 0.80)
                    endy = int(size["height"] * 0.30)
                    startx = int(size["width"] * 0.20)
                    sleep(2)
                    browser.swipe(startx, starty, startx, endy, 1000)
                    check = CommonMethods.isElementPresent(browser, self.School_league_xpath)
                    break
            CommonMethods.elementClick(browser, self.School_league_xpath)
            logging.info("school super league is clicked")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'hamburger_spl')
        except:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'hamburger_spl')

    ''' ssl verify method will verify the text present in DSSL page'''

    def ssl_verify(self, browser):
        try:
            sleep(10)
            if CommonMethods.wait_for_element_visible(browser, self.School_league_page_xpath, 5):
                act_txt = CommonMethods.getAttributeOfElement(browser, 'text', self.School_league_page_xpath)

                print("Actual text============================", act_txt)
                exp_txt = "Discovery"
                assert act_txt == exp_txt, "Discovery super League text failed "
                CommonMethods.click_on_device_back_btn(browser)
            else:
                logging.info("Discovery super League text failed")
                pytest.fail(" Text Discovery super League text failed ")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'ssl_verify')
        except:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'ssl_verify')

    def Hamburger_page(self, browser, text):

        try:

            key = text
            exp_txt = getdata(Hamburger_Options, 'hamburger_options', key)
            print(exp_txt)
            ham_page = (By.XPATH, "//android.widget.TextView[@text=\'" + exp_txt + "\']")
            if CommonMethods.wait_for_element_visible(browser, ham_page, 10):
                act_txt = CommonMethods.getAttributeOfElement(browser, 'text', ham_page)
                print("=================================================")
                print(act_txt)
                print(exp_txt)
                print("==============================================================")
                assert act_txt == exp_txt, " Page text failed to match"
                CommonMethods.click_on_device_back_btn(browser)
            else:
                logging.info("Discovery super League text failed")
                pytest.fail(" Text Discovery super League text failed ")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'Hamburger_page')
        except:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'Hamburger_page')

    ''' tap hamburger option will tap on the options which are present on Hamburger '''

    def tap_hamburger_option(self, browser, text):

        ham_opt = (By.XPATH, "//android.widget.TextView[@text=\'" + text + "\']")

        check = CommonMethods.isElementPresent(browser, ham_opt)
        if check == True:
            CommonMethods.elementClick(browser, ham_opt)

        else:
            print(" Element not found ")
            logging.info("Locator not found")

    def scroll_hamburg_verify(self, browser, text):
        try:
            ham_opt = (By.XPATH, "//android.widget.TextView[@text=\'" + text + "\']")

            check = CommonMethods.isElementPresent(browser, ham_opt)
            if check == True:
                logging.info("Element is visiable without scroll")
            else:
                while check == False:
                    size = browser.get_window_size()
                    starty = int(size["height"] * 0.80)
                    endy = int(size["height"] * 0.30)
                    startx = int(size["width"] * 0.20)
                    sleep(2)
                    browser.swipe(startx, starty, startx, endy, 1000)
                    check = CommonMethods.isElementPresent(browser, ham_opt)
                    break
            CommonMethods.elementClick(browser, ham_opt)
            logging.info("Element found and  clicked")
            key = text
            exp_txt = getdata(Hamburger_Options, 'hamburger_options', key)
            print(exp_txt)
            ham_page = (By.XPATH, "//android.widget.TextView[@text=\'" + exp_txt + "\']")
            if CommonMethods.wait_for_element_visible(browser, ham_page, 3):
                act_txt = CommonMethods.getAttributeOfElement(browser, 'text', ham_page)
                print("=================================================")
                print(act_txt)
                print(exp_txt)
                print("==============================================================")
                assert act_txt == exp_txt, " Page text failed to match"
                CommonMethods.click_on_device_back_btn(browser)
            else:
                logging.info("Required text failed")
                pytest.fail(" text failed ")


        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'scroll_hamburg_verify')
        except:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'scroll_hamburg_verify')

    def profile_button(self, browser):
        try:
            if CommonMethods.wait_for_element_visible(browser, self.prof_btn_id, 10):
                CommonMethods.elementClick(browser, self.prof_btn_id)
            else:
                logging.info("Profile button not found")
                pytest.fail("failed in absence of profile button ")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'profile_button')

    def scroll(self, browser, start_y, end_y, start_x, end_x):

        size = browser.get_window_size()
        starty = int(size["height"] * start_y)
        endy = int(size["height"] * end_y)
        startx = int(size["width"] * start_x)
        endx = int(size["height"] * end_x)

        browser.swipe(startx, starty, endx, endy, 1000)
