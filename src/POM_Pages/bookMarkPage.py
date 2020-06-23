from appium import webdriver
import sys
import os
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import logging
import json
import logging
from Constants.constants import CONFIG_PATH
from Constants.load_json import *
from Constants.constants import Hamburger_Options

from Utilities.common_methods import CommonMethods
from Constants.constants import CONFIG_PATH, Login_Credentials, Hamburger_Options
import logging
import pytest
from conftest import browser
# from POM_Pages.ConceptSummaryScreen import CommonMethods
# from Utilities.interrupt import click_on_back_button


page_value = None
CommonMethods = CommonMethods()

data_file = CONFIG_PATH

featureFileName = "Bookmarks"


class BookMark():

    def __init__(self, browser):
        self.browser = browser

    phone_num = (By.ID, "com.byjus.thelearningapp.premium:id/etPhoneNumber")
    country_Code = "com.byjus.thelearningapp.premium:id/spnrCountry"
    video = "//android.widget.ImageView[@instance='2']"
    Btn_test = "com.byjus.thelearningapp.premium:id/chapter_list_item_test_txtvw"
    Btn_practice = "com.byjus.thelearningapp.premium:id/practice_mode_bottom_txtvw"
    Btn_play_pause = "//android.widget.ImageView[@instance='3']"
    loginBtn_id = "com.byjus.thelearningapp.premium:id/btnLogin"
    OtpTxtBx_id = "com.byjus.thelearningapp.premium:id/etOTP"
    librayBtn_id = (By.ID, "com.byjus.thelearningapp.premium:id/optionalNav")
    first_videoLnk_xpath = "//android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp.premium:id/chapter_view_group' and @index=1]/androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_videos_lstvw']/android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp.premium:id/chapter_video_list_cardview' and @index = 0]"
    videoFrame_id = "com.byjus.thelearningapp.premium:id/exo_subtitles"
    # videoPauseBtn_id = "com.byjus.thelearningapp.premium:id/exo_pause"
    # videoPlayBtn_id = "com.byjus.thelearningapp.premium:id/exo_play"
    analytics_icon = (By.ID, "com.byjus.thelearningapp.premium:id/iv_analysis")
    videoPlayingNow_xpath = "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/video_list_view']//android.widget.LinearLayout[@index=0]//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_video_subitem_name_txtv' and @selected = 'true']"
    google_termsBtn_id = "com.android.chrome:id/terms_accept"
    nextBtn_id = "com.android.chrome:id/next_button"
    negativeBtn_id = "com.android.chrome:id/negative_button"
    progressTime_id = "com.byjus.thelearningapp.premium:id/exo_position"
    remaingTime_id = "com.byjus.thelearningapp.premium:id/exo_duration"
    tenSecFwdBtn_id = "com.byjus.thelearningapp.premium:id/exo_ffwd"
    tenSecBkwdBtn_id = "com.byjus.thelearningapp.premium:id/exo_rew"
    byjusAppPackage = "com.byjus.thelearningapp"
    skipBtn_id = "com.byjus.thelearningapp.premium:id/buttonSkip"
    allow_btn_id = "com.android.packageinstaller:id/permission_allow_button"
    skipBtn_id = "com.byjus.thelearningapp.premium:id/buttonSkip"

    #     Login Locators
    # com.byjus.thelearningapp.premium:id/backNav
    back_button_id = (By.ID, "com.byjus.thelearningapp.premium:id/backNav")
    profile_name_hamburger = (By.ID, "com.byjus.thelearningapp.premium:id/home_drawer_txtvw_profile_name")
    account_details_title = (By.ID, "com.byjus.thelearningapp.premium:id/account_details_title")
    profile_mob_num = (By.ID, "com.byjus.thelearningapp.premium:id/mobile_number")
    country_Code = (By.ID, "com.byjus.thelearningapp.premium:id/spnrCountry")
    loginBtn_id = (By.ID, "com.byjus.thelearningapp.premium:id/btnLogin")
    OtpTxtBx_id = (By.ID, "com.byjus.thelearningapp.premium:id/etOTP")
    allow_btn_id = (By.ID, "com.android.packageinstaller:id/permission_allow_button")
    none_of_the_above_id = (By.ID, "com.google.android.gms:id/cancel")
    loginPageVerify_id = (By.XPATH, "//android.widget.TextView[@text='Login']")
    phone_num = (By.ID, "com.byjus.thelearningapp.premium:id/etPhoneNumber")
    user_name_profile_page = (By.ID, "com.byjus.thelearningapp.premium:id/tvUserName")
    ham_btn_id = (By.ID, "com.byjus.thelearningapp.premium:id/roundedNavButton")
    all_subjects = (By.XPATH,
                    "//android.widget.GridLayout//android.widget.FrameLayout[@resource-id='com.byjus.thelearningapp.premium:id/home_subject_cardview']")
    all_bookmark_sub = (
    By.XPATH, "//android.widget.HorizontalScrollView//android.widget.LinearLayout//android.widget.TextView")

    # subject  personalised  screen locators
    Library_btn = (By.XPATH, ("//android.widget.Button[@text='Library']"))
    personalised_btn = (By.XPATH, ("//android.widget.Button[@text='Personalised']"))
    first_video_mob=(By.XPATH,("//android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp.premium:id/chapter_view_group' and @index=1]/androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_videos_lstvw']/android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp.premium:id/chapter_video_list_cardview' and @index = 0]"))
    first_video_tab = (By.XPATH, (
        "//android.widget.FrameLayout[@resource-id='com.byjus.thelearningapp.premium:id/chapter_view_group' and @index = 1]"))
    video_tab_list_close = (By.ID, ("com.byjus.thelearningapp.premium:id/video_list_close"))
    video_initial_play = (By.ID, ("com.byjus.thelearningapp.premium:id/ivPlay"))
    video_tap_playicon = (By.ID, ("com.byjus.thelearningapp.premium:id/exo_play"))
    videoFrame_id = (By.ID, ("com.byjus.thelearningapp.premium:id/exo_subtitles"))
    video_tab_PauseBtn_id = (By.ID, ("com.byjus.thelearningapp.premium:id/exo_pause"))
    video_player_tab_bookmark = (By.ID, ("com.byjus.thelearningapp.premium:id/bookmark"))
    Video_player_tab_backbtn = (By.ID, ("com.byjus.thelearningapp.premium:id/back"))
    personalizeScreen_xpath = (By.XPATH, ("//android.widget.Button[@text='Personalised']"))

    # Bookmarks

    filter_txt = (By.XPATH, "//android.widget.Button[@text='Filter']")
    mathematics_txt = (By.XPATH, "//android.widget.TextView[@text='Mathematics']")
    physics_txt = (By.XPATH, "//android.widget.TextView[@text='Physics']")
    chemistry_txt = (By.XPATH, ("//android.widget.TextView[@text='Chemistry']"))
    all_txt = (By.XPATH, ("//android.widget.TextView[@text='All']"))
    biology_txt = (By.XPATH, ("//android.widget.TextView[@text='Biology']"))
    comp_exam_txt = (By.XPATH, ("//android.widget.TextView[@text='Competitive Exam - Mocks']"))
    previous_txt = (By.XPATH, ("//android.widget.TextView[@text='Previous Years Papers']"))
    all_sub = (By.ID, ("com.byjus.thelearningapp.premium:id/home_subject_name_txtvw"))
    ham_bookmark = (By.XPATH, ("//android.widget.TextView[@text='Bookmarks']"))
    # ham_page=(By.XPATH,("//android.widget.TextView[@text='Bookmarks']"))
    bookmark_icon = (By.XPATH, (
        "//androidx.recyclerview.widget.RecyclerView//android.widget.RelativeLayout[@index=0]//android.widget.ImageView[@resource-id='com.byjus.thelearningapp.premium:id/ivBookmarkTag']"))
    no_bookmark = (By.XPATH, ("//android.widget.TextView[@text='No Bookmarks']"))
    Bookmark_tab = (By.ID, ("com.byjus.thelearningapp.premium:id/bookmark"))

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
    loginPageVerify_id = (By.XPATH, "//android.widget.TextView[@text='Login']")
    phone_num = (By.ID, "com.byjus.thelearningapp.premium:id/etPhoneNumber")
    user_name_profile_page = (By.ID, "com.byjus.thelearningapp.premium:id/tvUserName")
    homescreen_corana_dialog_ok_btn = (By.XPATH, "//android.widget.TextView[@text = 'OK']")
    homescreen_corana_dialog = (By.ID, "com.byjus.thelearningapp.premium:id/dialog_layout")

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
                actual_mob_num = getdata(data_file, 'profile_credentials3', 'mobileNum')
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

    def verify_badge(self, browser):
        if CommonMethods.wait_for_element_visible(browser, self.video_badge_close_btn, 2):
            CommonMethods.elementClick(browser, self.video_badge_close_btn)

    def verify_corana_dialog(self, browser):
        if CommonMethods.wait_for_element_visible(browser, self.homescreen_corana_dialog, 10):
            CommonMethods.elementClick(browser, self.homescreen_corana_dialog_ok_btn)

    def tap_on_device_back_btn(self, browser):
        sleep(3)
        CommonMethods.click_on_device_back_btn(browser)

    def tap_on_back_arrow_btn(self, browser):
        sleep(3)
        back_arrow = CommonMethods.getElement(browser, self.practice_back_arrow_btn)
        back_arrow.click()

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
                CommonMethods.click_on_device_back_btn(browser)
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
        try:
            if CommonMethods.wait_for_element_visible(browser, self.ham_btn_id, 5):
                CommonMethods.elementClick(browser, self.ham_btn_id)

            else:
                logging.info('Hamburger menu Not Found')
                pytest.fail("Failed due to Hamburger Menu")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'hamburger_verify')

        except:
            CommonMethods.exception(browser, featureFileName, 'hamburger_verify')

    def bookmark_verify(self, browser):
        try:
            if CommonMethods.wait_for_element_visible(browser, self.ham_bookmark, 3):
                CommonMethods.elementClick(browser, self.ham_bookmark)
            else:
                logging.info('Hamburger menu Not Found')
                pytest.fail("Failed due to Hamburger Menu")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'bookmark_verify')

        except:
            CommonMethods.exception(browser, featureFileName, 'bookmark_verify')

    ''' bookmark_screen  verifies  bookmark screen text     '''

    def bookmark_screen(self, browser):
        try:
            check = CommonMethods.wait_for_element_visible(browser, self.ham_bookmark, 3)

            if check == True:
                logging.info("Bookmark present ")

            else:
                logging.info('page Not Found')
                pytest.fail("Failed due to Hamburger Menu")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'bookmark_screen')

        except:
            CommonMethods.exception(browser, featureFileName, 'bookmark_screen')

    ''' filter_option  verifies filter option  is present in bookmark screen     '''

    def filter_option(self, browser):
        try:
            check = CommonMethods.wait_for_element_visible(browser, self.filter_txt, 3)

            if check == True:
                logging.info("Element is visible ")

            else:
                logging.info('Filter text   Not Found')
                pytest.fail("Failed due to Bookmark elements")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'filter_option')

        except:
            CommonMethods.exception(browser, featureFileName, 'filter_option')

    def nobookmark_txt(self, browser):
        try:
            check = CommonMethods.wait_for_element_visible(browser, self.no_bookmark, 3)

            if check == True:
                logging.info("Element is visible ")

            else:
                logging.info('No Bookmarks text   Not Found')
                pytest.fail("Failed due to Bookmark elements")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'nobookmark_txt')

        except:
            CommonMethods.exception(browser, featureFileName, 'nobookmark_txt')

    ''' bmark_back  verifies backbutton is present or not    '''

    def bmark_back(self, browser):
        try:
            check = CommonMethods.wait_for_element_visible(browser, self.back_button_id, 3)

            if check == True:
                logging.info("Element is visible ")

            else:
                logging.info('back button    Not Found')
                pytest.fail("Failed due to Bookmark elements")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'bmark_back')

        except:
            CommonMethods.exception(browser, featureFileName, 'bmark_back')

    ''' bmark_back_btn_click  clicks on bookmark screen  app backbutton    '''

    def bmark_back_btn_click(self, browser):
        try:
            check = CommonMethods.wait_for_element_visible(browser, self.back_button_id, 3)

            if check == True:
                CommonMethods.elementClick(browser, self.back_button_id)
                logging.info("Element is visible  and clicked ")

            else:
                logging.info('No Bookmarks text   Not Found')
                pytest.fail("Failed due to Bookmark elements")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'bmark_back_btn_click')

        except:
            CommonMethods.exception(browser, featureFileName, 'bmark_back_btn_click')

    ''' subject_txt  verifies subjects from home screen and bookmark screen   '''

    def subject_txt(self, browser):
        try:

            check = CommonMethods.wait_for_element_visible(browser, self.all_txt, 5)

            if check == True:
                logging.info("Element is visible and present  ")

            else:
                logging.info('All option is    Not Found')
                pytest.fail("Failed due to Bookmark elements")
            sub = CommonMethods.getElements(browser, self.all_bookmark_sub)

            ''' Bookmark list is taken from below code'''
            Blist = []
            for ele in sub:
                sub_txt = ele.text
                print("#########################" + sub_txt)
                Blist.append(sub_txt)
            print(Blist)
            Blist.pop(0)
            print(Blist)
            CommonMethods.elementClick(browser, self.back_button_id)
            sublist = CommonMethods.getElements(browser, self.all_sub)

            '''subject list is taken from home screen '''
            slist = []
            for ele in sublist:
                sub_txt = ele.text
                print("#########################" + sub_txt)
                slist.append(sub_txt)
            print(slist)
            print(slist)
            if Blist == slist:
                print("List are identical")
            else:
                print("list elements are not identical")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'subject_txt')

        except:
            CommonMethods.exception(browser, featureFileName, 'subject_txt')

    def homescreen_verify(self, browser):

        try:
            check = CommonMethods.wait_for_element_visible(browser, self.ham_btn_id, 5)
            if check == True:
                logging.info("Home screen verified ")

            else:
                logging.info('Hamburger menu Not Found')
                pytest.fail("Failed due to Hamburger Menu")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'homescreen_verify')

        except:
            CommonMethods.exception(browser, featureFileName, 'homescreen_verify')

    def device_back(self, browser):
        try:
            CommonMethods.click_on_device_back_btn(browser)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'device_back')

        except:
            CommonMethods.exception(browser, featureFileName, 'device_back')

    ''' subject_tap  taps on the respective subject  '''

    def subject_tap(self, browser, text):

        try:
            sub_opt = (By.XPATH, "//android.widget.TextView[@text=\'" + text + "\']")
            check = CommonMethods.wait_for_element_visible(browser, sub_opt, 5)
            if check == True:
                logging.info("Element is visible ")
                CommonMethods.elementClick(browser, sub_opt)
            else:
                browser.find_element_by_android_uiautomator(
                    'new UiScrollable(new UiSelector().scrollable(true)).setAsHorizontalList().scrollIntoView(new UiSelector().textContains("' + text + '"))')
                CommonMethods.elementClick(browser, sub_opt)

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'math_tap')

        except:
            CommonMethods.exception(browser, featureFileName, 'math_tap')

    ''' sub_highlight_Verify  verifies highlight bar is present  '''

    def sub_highlight_Verify(self, browser, text):

        try:
            sub_opt = (By.XPATH, "//android.widget.TextView[@text=\'" + text + "\']")
            high = CommonMethods.getAttributeOfElement(browser, 'selected', sub_opt)
            print("########################" + high)
            if (high == "true"):
                logging.info("subject is highlighted ")
            else:
                logging.info('subject failed to highlight')
                pytest.fail("Failed due to Bookmark subject highlight")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'sub_highlight_Verify')

        except:
            CommonMethods.exception(browser, featureFileName, 'sub_highlight_Verify')

    ''' remove_bookmark  removes bookmark item '''

    def remove_bookmark(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.bookmark_icon)
            if check == False:
                logging.info("No Bookmarks items are present ")
            else:
                while check == True:
                    CommonMethods.elementClick(browser, self.bookmark_icon)
                    check = CommonMethods.isElementPresent(browser, self.bookmark_icon)

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'remove_bookmark')
        except:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'remove_bookmark')

    ''' bookmark_present   bookmark  item is present or not '''

    def bookmark_present(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.bookmark_icon)
            if check == True:
                logging.info(" Bookmarks items are present ")
            else:
                logging.info("bookmark items are not present")
                pytest.fail("Bookmark is not present ")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'bookmark_present')
        except:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'bookmark_present')

    def pause_video(self, browser):
        check = True
        wait_count = 0
        try:
            while check and wait_count < 15:
                wait_count += 1
                CommonMethods.elementClick(browser, self.videoFrame_id)
                CommonMethods.elementClick(browser, self.video_tab_PauseBtn_id)
                flag = CommonMethods.wait_for_element_visible(browser, self.video_tap_playicon, 2)
                check = not flag
        except:
            logging.info('Error in pausing the video')

    ''' check_bookmark   bookmark  is present or not '''

    def check_bookmark(self, browser):
        try:

            check = CommonMethods.isElementPresent(browser, self.bookmark_icon)
            if check == False:
                logging.info("No Bookmarks items are present ")
            else:
                logging.info("Bookmark content is present ")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'check_bookmark')
        except:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'check_bookmark')

    def check_nobookmark(self, browser, text):
        try:
            sub_opt = (By.XPATH, "//android.widget.TextView[@text=\'" + text + "\']")
            check = CommonMethods.isElementPresent(browser, sub_opt)
            if check == True:
                logging.info("No Bookmarks text is  present ")
            else:
                logging.info("Bookmark content is present ")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'check_nobookmark')
        except:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'check_nobookmark')

    ''' check_nobookmark_text  check nobookmark text is present or not '''

    def check_nobookmark_text(self, browser, text):
        try:
            sub_opt = (By.XPATH, ("//android.widget.TextView[@text=\'" + text + "\']"))
            # sub_opt = (By.XPATH,"//android.widget.TextView[@text=\'"+text+"\']")

            check = CommonMethods.isElementPresent(browser, sub_opt)
            if check == True:
                logging.info("No Bookmarks text is  present ")
                pytest.fail("Text no Bookmark is present")
            else:
                logging.info("Bookmark content is present ")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'check_nobookmark_text')
        except:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'check_nobookmark_text')

    ''' navigate_to_library  navigates to library screen from home screen '''

    def navigate_to_library(self, browser, sub):
        try:
            pythonSub_xpath = (By.XPATH, "//android.widget.TextView[@text=\'" + sub + "\']")
            CommonMethods.wait_for_locator(browser, pythonSub_xpath, 15)
            CommonMethods.elementClick(browser, pythonSub_xpath)
            if CommonMethods.isElementPresent(browser, self.personalizeScreen_xpath):
                pass
            else:
                CommonMethods.wait_for_locator(browser, self.librayBtn_id, 15)
                CommonMethods.elementClick(browser, self.librayBtn_id)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'navigate_to_library')

        except:
            CommonMethods.exception(browser, featureFileName, 'navigate_to_library')

    ''' initial_remove_bookmark  removes existing bookmark from bookmark screen   '''

    def initial_remove_bookmark(self, browser):
        try:
            CommonMethods.wait_for_element_visible(browser, self.ham_btn_id, 5)
            CommonMethods.elementClick(browser, self.ham_btn_id)
            CommonMethods.wait_for_element_visible(browser, self.ham_bookmark, 3)
            CommonMethods.elementClick(browser, self.ham_bookmark)
            CommonMethods.wait_for_element_visible(browser, self.ham_bookmark, 3)
            check = CommonMethods.isElementPresent(browser, self.bookmark_icon)
            if check == False:
                logging.info("No Bookmarks items are present ")
                CommonMethods.click_on_device_back_btn(browser)
            else:
                while check == True:
                    CommonMethods.elementClick(browser, self.bookmark_icon)

                    check = CommonMethods.isElementPresent(browser, self.bookmark_icon)

                CommonMethods.click_on_device_back_btn(browser)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'initial_remove_bookmark')
        except:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'initial_remove_bookmark')

    ''' Bookmark_video  methods bookmarks video from library  '''

    def Bookmark_video(self, browser):
        try:
            self.navigate_to_library(browser, 'Mathematics')
            check = CommonMethods.isElementPresent(browser, self.first_video_mob)
            if check == True:
                CommonMethods.elementClick(browser, self.first_video_mob)
                #CommonMethods.wait_for_element_visible(browser, self.video_tab_list_close, 3)
                #CommonMethods.elementClick(browser, self.video_tab_list_close)
                check_initial = CommonMethods.isElementPresent(browser, self.video_initial_play)
                if check_initial == True:
                    CommonMethods.elementClick(browser, self.video_initial_play)
                    sleep(5)
                    # self.pause_video(browser)
                    CommonMethods.elementClick(browser, self.videoFrame_id)
                    CommonMethods.elementClick(browser, self.video_tab_PauseBtn_id)
                    CommonMethods.wait_for_element_visible(browser, self.Bookmark_tab, 5)
                    CommonMethods.elementClick(browser, self.Bookmark_tab)
                    while True:
                        if CommonMethods.isElementPresent(browser, self.analytics_icon):
                            logging.info('User is in Home screen')
                            break
                        else:
                            CommonMethods.click_on_device_back_btn(browser)
                            sleep(2)
                    # # CommonMethods.elementClick(browser,self.Bookmark_tab)
                    # CommonMethods.click_on_device_back_btn(browser)
                    # sleep(2)
                    # CommonMethods.click_on_device_back_btn(browser)

                else:

                    logging.info("video is playing ")
                    sleep(5)
                    # self.pause_video(browser)
                    CommonMethods.elementClick(browser, self.videoFrame_id)
                    CommonMethods.elementClick(browser, self.video_tab_PauseBtn_id)
                    CommonMethods.wait_for_element_visible(browser, self.Bookmark_tab, 5)
                    CommonMethods.elementClick(browser, self.Bookmark_tab)
                    while True:
                        if CommonMethods.isElementPresent(browser, self.analytics_icon):
                            logging.info('User is in Home screen')
                            break
                        else:
                            CommonMethods.click_on_device_back_btn(browser)
                            sleep(2)
                    # CommonMethods.click_on_device_back_btn(browser)
                    # sleep(2)
                    # CommonMethods.click_on_device_back_btn(browser)


            else:
                logging.info("failed to navigate to videolist screen ")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'Bookmark_video')

        except:
            CommonMethods.exception(browser, featureFileName, 'Bookmark_video')


























