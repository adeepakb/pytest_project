from appium import webdriver
import sys
import os
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import subprocess
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
# from POM_Pages.ConceptSummaryScreen import CommonMethods
# from Utilities.interrupt import click_on_back_button


page_value = None
CommonMethods = CommonMethods()

data_file = CONFIG_PATH

featureFileName = "Bookmarks"


class BookMark():

    def __init__(self, driver):
        self.driver = driver

    phone_num = (By.ID, "com.byjus.thelearningapp.premium:id/etPhoneNumber")
    country_Code = (By.ID, "com.byjus.thelearningapp.premium:id/spnrCountry")
    video = "//android.widget.ImageView[@instance='2']"
    Btn_test = "com.byjus.thelearningapp.premium:id/chapter_list_item_test_txtvw"
    Btn_practice = "com.byjus.thelearningapp.premium:id/practice_mode_bottom_txtvw"
    Btn_play_pause = "//android.widget.ImageView[@instance='3']"
    loginBtn_id = (By.ID, "com.byjus.thelearningapp.premium:id/btnLogin")
    OtpTxtBx_id = (By.ID, "com.byjus.thelearningapp.premium:id/etOTP")
    librayBtn_id = (By.XPATH,"//android.widget.Button[@text='Library']")
    first_videoLnk_xpath = "//android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp.premium:id/chapter_view_group' and @index=1]/androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_videos_lstvw']/android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp.premium:id/chapter_video_list_cardview' and @index = 0]"
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

    # Login Locators
    back_button_id = (By.ID, "com.byjus.thelearningapp.premium:id/backNav")
    profile_name_hamburger = (By.ID, "com.byjus.thelearningapp.premium:id/home_drawer_txtvw_profile_name")
    account_details_title = (By.ID, "com.byjus.thelearningapp.premium:id/account_details_title")
    profile_mob_num = (By.ID, "com.byjus.thelearningapp.premium:id/mobile_number")
    allow_btn_id = (By.XPATH, "//*[contains(@resource-id, 'permission_allow_button')]")
    none_of_the_above_id = (By.ID, "com.google.android.gms:id/cancel")
    loginPageVerify_id = (By.XPATH, "//android.widget.Button[@text='Login']")
    multiple_accounts_dialog = (By.ID,"com.byjus.thelearningapp.premium:id/dialog_linearlayout")
    user_profile_name = (By.ID,"com.byjus.thelearningapp.premium:id/tv_profile_name")
    profile_select_radio_button = (By.ID,"com.byjus.thelearningapp.premium:id/profile_select_radio_button")
    continue_button = (By.ID,"com.byjus.thelearningapp.premium:id/tv_submit")
    welcome_button = (By.ID, "com.byjus.thelearningapp.premium:id/welcomeButton")
    user_name_profile_page = (By.ID, "com.byjus.thelearningapp.premium:id/tvUserName")
    ham_btn_id = (By.ID, "com.byjus.thelearningapp.premium:id/roundedNavButton")
    all_subjects = (By.XPATH,
                    "//android.widget.GridLayout//android.widget.FrameLayout[@resource-id='com.byjus.thelearningapp.premium:id/home_subject_cardview']")
    all_bookmark_sub = (
        By.XPATH, "//android.widget.HorizontalScrollView//android.widget.LinearLayout//android.widget.TextView")

    homescreen_corana_dialog_ok_btn = (By.XPATH, "//android.widget.TextView[@text = 'OK']")
    homescreen_corana_dialog = (By.ID, "com.byjus.thelearningapp.premium:id/dialog_layout")
    # subject  personalised  screen locators
    Library_btn = (By.XPATH, ("//android.widget.Button[@text='Library']"))
    personalised_btn = (By.XPATH, ("//android.widget.Button[@text='Personalised']"))
    first_video_mob = (By.XPATH, (
        "//android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp.premium:id/chapter_view_group' and @index=1]/androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_videos_lstvw']/android.widget.FrameLayout[@resource-id='com.byjus.thelearningapp.premium:id/chapter_video_list_cardview' and @index = 0]"))
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

    def verify_badge(self, driver):
        if CommonMethods.wait_for_element_visible(driver, self.video_badge_close_btn, 2):
            CommonMethods.elementClick(driver, self.video_badge_close_btn)

    def verify_corana_dialog(self, driver):
        if CommonMethods.wait_for_element_visible(driver, self.homescreen_corana_dialog, 10):
            CommonMethods.elementClick(driver, self.homescreen_corana_dialog_ok_btn)

    def tap_on_device_back_btn(self, driver):
        sleep(3)
        CommonMethods.click_on_device_back_btn(driver)

    def tap_on_back_arrow_btn(self, driver):
        sleep(3)
        back_arrow = CommonMethods.getElement(driver, self.practice_back_arrow_btn)
        back_arrow.click()

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
        try:
            if CommonMethods.wait_for_element_visible(driver, self.ham_btn_id, 5):
                CommonMethods.elementClick(driver, self.ham_btn_id)

            else:
                logging.info('Hamburger menu Not Found')
                pytest.fail("Failed due to Hamburger Menu")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'hamburger_verify')

        except:
            CommonMethods.exception(driver, featureFileName, 'hamburger_verify')

    def bookmark_verify(self, driver):
        try:
            if CommonMethods.wait_for_element_visible(driver, self.ham_bookmark, 3):
                CommonMethods.elementClick(driver, self.ham_bookmark)
            else:
                logging.info('Hamburger menu Not Found')
                pytest.fail("Failed due to Hamburger Menu")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'bookmark_verify')

        except:
            CommonMethods.exception(driver, featureFileName, 'bookmark_verify')

    ''' bookmark_screen  verifies  bookmark screen text     '''

    def bookmark_screen(self, driver):
        try:
            check = CommonMethods.wait_for_element_visible(driver, self.ham_bookmark, 3)

            if check == True:
                logging.info("Bookmark present ")

            else:
                logging.info('page Not Found')
                pytest.fail("Failed due to Hamburger Menu")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'bookmark_screen')

        except:
            CommonMethods.exception(driver, featureFileName, 'bookmark_screen')

    ''' filter_option  verifies filter option  is present in bookmark screen     '''

    def filter_option(self, driver):
        try:
            check = CommonMethods.wait_for_element_visible(driver, self.filter_txt, 3)

            if check == True:
                logging.info("Element is visible ")

            else:
                logging.info('Filter text   Not Found')
                pytest.fail("Failed due to Bookmark elements")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'filter_option')

        except:
            CommonMethods.exception(driver, featureFileName, 'filter_option')

    def nobookmark_txt(self, driver):
        try:
            check = CommonMethods.wait_for_element_visible(driver, self.no_bookmark, 3)

            if check == True:
                logging.info("Element is visible ")

            else:
                logging.info('No Bookmarks text   Not Found')
                pytest.fail("Failed due to Bookmark elements")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'nobookmark_txt')

        except:
            CommonMethods.exception(driver, featureFileName, 'nobookmark_txt')

    ''' bmark_back  verifies backbutton is present or not    '''

    def bmark_back(self, driver):
        try:
            check = CommonMethods.wait_for_element_visible(driver, self.back_button_id, 3)

            if check == True:
                logging.info("Element is visible ")

            else:
                logging.info('back button    Not Found')
                pytest.fail("Failed due to Bookmark elements")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'bmark_back')

        except:
            CommonMethods.exception(driver, featureFileName, 'bmark_back')

    ''' bmark_back_btn_click  clicks on bookmark screen  app backbutton    '''

    def bmark_back_btn_click(self, driver):
        try:
            check = CommonMethods.wait_for_element_visible(driver, self.back_button_id, 3)

            if check == True:
                CommonMethods.elementClick(driver, self.back_button_id)
                logging.info("Element is visible  and clicked ")

            else:
                logging.info('No Bookmarks text   Not Found')
                pytest.fail("Failed due to Bookmark elements")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'bmark_back_btn_click')

        except:
            CommonMethods.exception(driver, featureFileName, 'bmark_back_btn_click')

    ''' subject_txt  verifies subjects from home screen and bookmark screen   '''

    def subject_txt(self, driver):
        try:

            check = CommonMethods.wait_for_element_visible(driver, self.all_txt, 5)

            if check == True:
                logging.info("Element is visible and present  ")

            else:
                logging.info('All option is    Not Found')
                pytest.fail("Failed due to Bookmark elements")
            sub = CommonMethods.getElements(driver, self.all_bookmark_sub)

            ''' Bookmark list is taken from below code'''
            Blist = []
            for ele in sub:
                sub_txt = ele.text
                print("#########################" + sub_txt)
                Blist.append(sub_txt)
            print(Blist)
            Blist.pop(0)
            print(Blist)
            CommonMethods.elementClick(driver, self.back_button_id)
            sublist = CommonMethods.getElements(driver, self.all_sub)

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
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'subject_txt')

        except:
            CommonMethods.exception(driver, featureFileName, 'subject_txt')

    def homescreen_verify(self, driver):

        try:
            check = CommonMethods.wait_for_element_visible(driver, self.ham_btn_id, 5)
            if check == True:
                logging.info("Home screen verified ")

            else:
                logging.info('Hamburger menu Not Found')
                pytest.fail("Failed due to Hamburger Menu")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'homescreen_verify')

        except:
            CommonMethods.exception(driver, featureFileName, 'homescreen_verify')

    def device_back(self, driver):
        try:
            CommonMethods.click_on_device_back_btn(driver)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'device_back')

        except:
            CommonMethods.exception(driver, featureFileName, 'device_back')

    ''' subject_tap  taps on the respective subject  '''

    def subject_tap(self, driver, text):

        try:
            sub_opt = (By.XPATH, "//android.widget.TextView[@text=\'" + text + "\']")
            check = CommonMethods.wait_for_element_visible(driver, sub_opt, 5)
            if check == True:
                logging.info("Element is visible ")
                CommonMethods.elementClick(driver, sub_opt)
            else:
                driver.find_element_by_android_uiautomator(
                    'new UiScrollable(new UiSelector().scrollable(true)).setAsHorizontalList().scrollIntoView(new UiSelector().textContains("' + text + '"))')
                CommonMethods.elementClick(driver, sub_opt)

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'math_tap')

        except:
            CommonMethods.exception(driver, featureFileName, 'math_tap')

    ''' sub_highlight_Verify  verifies highlight bar is present  '''

    def sub_highlight_Verify(self, driver, text):

        try:
            sub_opt = (By.XPATH, "//android.widget.TextView[@text=\'" + text + "\']")
            high = CommonMethods.getAttributeOfElement(driver, 'selected', sub_opt)
            print("########################" + high)
            if (high == "true"):
                logging.info("subject is highlighted ")
            else:
                logging.info('subject failed to highlight')
                pytest.fail("Failed due to Bookmark subject highlight")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'sub_highlight_Verify')

        except:
            CommonMethods.exception(driver, featureFileName, 'sub_highlight_Verify')

    ''' remove_bookmark  removes bookmark item '''

    def remove_bookmark(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.bookmark_icon)
            if check == False:
                logging.info("No Bookmarks items are present ")
            else:
                while check == True:
                    CommonMethods.elementClick(driver, self.bookmark_icon)
                    check = CommonMethods.isElementPresent(driver, self.bookmark_icon)

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'remove_bookmark')
        except:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'remove_bookmark')

    ''' bookmark_present   bookmark  item is present or not '''

    def bookmark_present(self, driver):
        try:
            check = CommonMethods.isElementPresent(driver, self.bookmark_icon)
            if check == True:
                logging.info(" Bookmarks items are present ")
            else:
                logging.info("bookmark items are not present")
                pytest.fail("Bookmark is not present ")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'bookmark_present')
        except:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'bookmark_present')

    def pause_video(self, driver):
        check = True
        wait_count = 0
        try:
            while check and wait_count < 15:
                wait_count += 1
                CommonMethods.elementClick(driver, self.videoFrame_id)
                CommonMethods.elementClick(driver, self.video_tab_PauseBtn_id)
                flag = CommonMethods.wait_for_element_visible(driver, self.video_tap_playicon, 2)
                check = not flag
        except:
            logging.info('Error in pausing the video')

    ''' check_bookmark   bookmark  is present or not '''

    def check_bookmark(self, driver):
        try:

            check = CommonMethods.isElementPresent(driver, self.bookmark_icon)
            if check == False:
                logging.info("No Bookmarks items are present ")
            else:
                logging.info("Bookmark content is present ")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'check_bookmark')
        except:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'check_bookmark')

    def check_nobookmark(self, driver, text):
        try:
            sub_opt = (By.XPATH, "//android.widget.TextView[@text=\'" + text + "\']")
            check = CommonMethods.isElementPresent(driver, sub_opt)
            if check == True:
                logging.info("No Bookmarks text is  present ")
            else:
                logging.info("Bookmark content is present ")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'check_nobookmark')
        except:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'check_nobookmark')

    ''' check_nobookmark_text  check nobookmark text is present or not '''

    def check_nobookmark_text(self, driver, text):
        try:
            sub_opt = (By.XPATH, ("//android.widget.TextView[@text=\'" + text + "\']"))
            # sub_opt = (By.XPATH,"//android.widget.TextView[@text=\'"+text+"\']")

            check = CommonMethods.isElementPresent(driver, sub_opt)
            if check == True:
                logging.info("No Bookmarks text is  present ")
                pytest.fail("Text no Bookmark is present")
            else:
                logging.info("Bookmark content is present ")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'check_nobookmark_text')
        except:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'check_nobookmark_text')

    ''' navigate_to_library  navigates to library screen from home screen '''

    def navigate_to_library(self, driver, sub):
        try:
            pythonSub_xpath = (By.XPATH, "//android.widget.TextView[@text=\'" + sub + "\']")
            CommonMethods.wait_for_locator(driver, pythonSub_xpath, 15)
            CommonMethods.elementClick(driver, pythonSub_xpath)
            if CommonMethods.isElementPresent(driver, self.personalizeScreen_xpath):
                pass
            else:
                for i in range(5):
                    CommonMethods.run('adb shell input touchscreen swipe 300 300 300 800')
                    check = CommonMethods.wait_for_element_visible(driver, self.librayBtn_id, 5)
                    if check == True:
                        break
                CommonMethods.wait_for_locator(driver, self.librayBtn_id, 10)
                CommonMethods.elementClick(driver, self.librayBtn_id)
                logging.info('successfully navigated to library')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'navigate_to_library')

        except:
            CommonMethods.exception(driver, featureFileName, 'navigate_to_library')

    ''' initial_remove_bookmark  removes existing bookmark from bookmark screen   '''

    def initial_remove_bookmark(self, driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.ham_btn_id, 5)
            CommonMethods.elementClick(driver, self.ham_btn_id)
            CommonMethods.wait_for_element_visible(driver, self.ham_bookmark, 3)
            CommonMethods.elementClick(driver, self.ham_bookmark)
            CommonMethods.wait_for_element_visible(driver, self.ham_bookmark, 3)
            check = CommonMethods.isElementPresent(driver, self.bookmark_icon)
            if check == False:
                logging.info("No Bookmarks items are present ")
                CommonMethods.click_on_device_back_btn(driver)
            else:
                while check == True:
                    CommonMethods.elementClick(driver, self.bookmark_icon)

                    check = CommonMethods.isElementPresent(driver, self.bookmark_icon)

                CommonMethods.click_on_device_back_btn(driver)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'initial_remove_bookmark')
        except:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'initial_remove_bookmark')

    ''' Bookmark_video  methods bookmarks video from library  '''

    def Bookmark_video(self, driver):
        try:
            self.navigate_to_library(driver, 'Mathematics')
            check = CommonMethods.isElementPresent(driver, self.first_video_mob)
            if check == True:
                CommonMethods.elementClick(driver, self.first_video_mob)
                # CommonMethods.wait_for_element_visible(driver, self.video_tab_list_close, 3)
                # CommonMethods.elementClick(driver, self.video_tab_list_close)
                check_initial = CommonMethods.isElementPresent(driver, self.video_initial_play)
                if check_initial == True:
                    CommonMethods.elementClick(driver, self.video_initial_play)
                    sleep(5)
                    # self.pause_video(driver)
                    CommonMethods.elementClick(driver, self.videoFrame_id)
                    CommonMethods.elementClick(driver, self.video_tab_PauseBtn_id)
                    CommonMethods.wait_for_element_visible(driver, self.Bookmark_tab, 5)
                    CommonMethods.elementClick(driver, self.Bookmark_tab)
                    while True:
                        if CommonMethods.isElementPresent(driver, self.analytics_icon):
                            logging.info('User is in Home screen')
                            break
                        else:
                            CommonMethods.click_on_device_back_btn(driver)
                            sleep(2)
                    # # CommonMethods.elementClick(driver,self.Bookmark_tab)
                    # CommonMethods.click_on_device_back_btn(driver)
                    # sleep(2)
                    # CommonMethods.click_on_device_back_btn(driver)

                else:

                    logging.info("video is playing ")
                    sleep(5)
                    # self.pause_video(driver)
                    CommonMethods.elementClick(driver, self.videoFrame_id)
                    CommonMethods.elementClick(driver, self.video_tab_PauseBtn_id)
                    CommonMethods.wait_for_element_visible(driver, self.Bookmark_tab, 5)
                    CommonMethods.elementClick(driver, self.Bookmark_tab)
                    while True:
                        if CommonMethods.isElementPresent(driver, self.analytics_icon):
                            logging.info('User is in Home screen')
                            break
                        else:
                            CommonMethods.click_on_device_back_btn(driver)
                            sleep(2)
                    # CommonMethods.click_on_device_back_btn(driver)
                    # sleep(2)
                    # CommonMethods.click_on_device_back_btn(driver)


            else:
                logging.info("failed to navigate to videolist screen ")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'Bookmark_video')

        except:
            CommonMethods.exception(driver, featureFileName, 'Bookmark_video')
