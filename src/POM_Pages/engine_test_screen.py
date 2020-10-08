from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Utilities.common_methods import CommonMethods
from Utilities.interrupt import *
from selenium.common.exceptions import NoSuchElementException
import logging
import pytest
from Constants.load_json import *
from Constants.constants import CONFIG_PATH, Login_Credentials, Test_data
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
import re
import random
import time
from PIL import Image, ImageChops
from io import BytesIO
import math

CommonMethods = CommonMethods()
data_file = CONFIG_PATH

# uncomment below line while executing via cmd
# f = open("../../Test_data/featureFileName.txt", "r")
# uncomment below line while executing via unit test
# f = open("Test_data/featureFileName.txt","r")
featureFileName = "Question Screen"


class EngineTestScreen():

    def __init__(self, driver):
        self.driver = driver

    hamburger_id = (By.ID, "com.byjus.thelearningapp.premium:id/backNav")
    toast_msg = (By.XPATH, "//android.widget.Toast")
    snackbar_text = (By.ID, "com.byjus.thelearningapp.premium:id/snackbar_text")
    allowbutton = (By.ID, "com.android.packageinstaller:id/permission_allow_button")
    denybutton = (By.ID, "com.android.packageinstaller:id/permission_deny_button")
    skipButton = (By.ID, "com.byjus.thelearningapp.premium:id/buttonSkip")
    grade8th = (By.XPATH, "//android.widget.Button[@text ='8th']")
    gms_cancel = (By.ID, "com.google.android.gms:id/cancel")
    btnRegister = (By.ID, "com.byjus.thelearningapp.premium:id/btnRegister")
    regscn_lgnbtn = (By.ID, "com.byjus.thelearningapp.premium:id/tvLoginBl")
    country_Code = (By.ID, "com.byjus.thelearningapp.premium:id/spnrCountry")
    phone_num = (By.ID, "com.byjus.thelearningapp.premium:id/etPhoneNumber")
    OtpTxtBx_id = (By.ID, "com.byjus.thelearningapp.premium:id/etOTP")
    badge = (By.ID, "com.byjus.thelearningapp.premium:id/lvBadgeEarnlottieAnim")
    closeBtn = (By.ID, "com.byjus.thelearningapp.premium:id/ivCloseBtn")
    loginBtn_id = (By.ID, "com.byjus.thelearningapp.premium:id/btnLogin")
    # analytics_icon=(By.ID,"com.byjus.thelearningapp.premium:id/home_analytics")
    analytics_icon = (By.ID, "com.byjus.thelearningapp.premium:id/iv_analysis")
    personalizeScreen_xpath = (By.XPATH, "//android.widget.Button[@text='Personalised']")
    librayBtn_id = (By.XPATH, "//android.widget.Button[@text='Library']")
    profile_header_id = (By.ID, "com.byjus.thelearningapp.premium:id/llHeaderTextParent")
    ibrayBtn_id = (By.ID, "com.byjus.thelearningapp.premium:id/optionalNav")
    testbtn = (By.ID, "com.byjus.thelearningapp.premium:id/chapter_list_item_test_txtvw")
    practicebtn = (By.ID, "com.byjus.thelearningapp.premium:id/practice_mode_bottom_txtvw")
    toggle_btn = (By.ID, "com.byjus.thelearningapp.premium:id/optionalNav")
    toggle_btn1 = (By.ID, "com.byjus.thelearningapp.premium:id/optionalNav2")
    secondaryActionBtn = (By.ID, "com.byjus.thelearningapp.premium:id/secondaryAction")
    primaryActionBtn = (By.ID, "com.byjus.thelearningapp.premium:id/primaryAction")
    header_title_text = (By.ID, "com.byjus.thelearningapp.premium:id/header_title_text")
    title = (By.ID, "com.byjus.thelearningapp.premium:id/title")
    subtitle1_text = (By.ID, "com.byjus.thelearningapp.premium:id/header_subtitle1_text")
    App_backBtn = (By.ID, "com.byjus.thelearningapp.premium:id/roundedNavButton")
    header_icon = (By.ID, "com.byjus.thelearningapp.premium:id/header_icon")
    chapter_title_view = (By.ID, "com.byjus.thelearningapp.premium:id/chapter_title_view")
    video_card_tab = (By.ID, "com.byjus.thelearningapp.premium:id/chapter_video_item_imgvw_thumbnail")
    video_card = (By.ID, "com.byjus.thelearningapp.premium:id/chapter_video_thumbnail_imgvw")
    current_grade = (By.ID, "com.byjus.thelearningapp.premium:id/home_drawer_txtvw_course")
    home_drawer_arrow_right = (By.ID, "com.byjus.thelearningapp.premium:id/home_drawer_imgvw_arrow_right")
    grade_drop_down = (By.ID, "com.byjus.thelearningapp.premium:id/tvGrade")
    account_details_title = (By.ID, "com.byjus.thelearningapp.premium:id/account_details_title")
    back_button_id = (By.ID, "com.byjus.thelearningapp.premium:id/backNav")
    profile_name_hamburger = (By.ID, "com.byjus.thelearningapp.premium:id/home_drawer_txtvw_profile_name")
    profile_mob_num = (By.ID, "com.byjus.thelearningapp.premium:id/mobile_number")
    allow_btn_id = (By.ID, "com.android.packageinstaller:id/permission_allow_button")
    none_of_the_above_id = (By.ID, "com.google.android.gms:id/cancel")
    loginPageVerify_id = (By.XPATH, "//android.widget.Button[@text='Login']")
    multiple_accounts_dialog = (By.ID, "com.byjus.thelearningapp.premium:id/dialog_linearlayout")
    user_profile_name = (By.ID, "com.byjus.thelearningapp.premium:id/tv_profile_name")
    profile_select_radio_button = (By.ID, "com.byjus.thelearningapp.premium:id/profile_select_radio_button")
    continue_button = (By.ID, "com.byjus.thelearningapp.premium:id/tv_submit")
    welcome_button = (By.ID, "com.byjus.thelearningapp.premium:id/welcomeButton")
    homescreen_corana_dialog_ok_btn = (By.ID, "com.byjus.thelearningapp.premium:id/tv_secondaryAction")
    homescreen_corana_dialog = (By.ID, "com.byjus.thelearningapp.premium:id/dialog_layout")
    free_live_classes = (By.XPATH, "//android.view.View[@content-desc='Free Live Classes']")
    bookmark_tag = (By.ID, "com.byjus.thelearningapp.premium:id/ivBookmarkTag")
    bookmark_ham_id = (By.XPATH, "//android.widget.TextView[@text ='Bookmarks']")
    user_name_profile_page = (By.ID, "com.byjus.thelearningapp.premium:id/tvUserName")
    # Test list screenlocators
    start_btn = (By.XPATH, "//android.widget.TextView[@text='Start']")
    analyse_btn = (By.XPATH, "//android.widget.TextView[@text='Analyse']")
    revise_btn = (By.XPATH, "//android.widget.TextView[@text='Revise']")
    questionId = (By.XPATH, "//android.view.View[@index='0']")
    retake_test = (By.ID, "com.byjus.thelearningapp.premium:id/retake_test")
    test_list_section = (By.ID, "com.byjus.thelearningapp.premium:id/rv_test_list_section")
    test_label = (By.ID, "com.byjus.thelearningapp.premium:id/chapter_tests_list_item_txtv_header")
    primaryText = (By.ID, "com.byjus.thelearningapp.premium:id/primaryText")
    chapter_list_title = (By.ID, "com.byjus.thelearningapp.premium:id/chapterlistTitle")
    resume_title = (By.ID, "com.byjus.thelearningapp.premium:id/resumeTitle")
    test_name_list = (By.ID, "com.byjus.thelearningapp.premium:id/chapter_tests_list_item_txtv_testname")
    objective_test_list_xpath = (By.XPATH,
                                 "//android.widget.LinearLayout[@index=1]//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_tests_list_item_txtv_testname']")
    subjective_test_list_xpath = (By.XPATH,
                                  "//android.widget.LinearLayout[@index=2]//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_tests_list_item_txtv_testname']")
    ncert_exemplars = (By.XPATH,
                       "//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_tests_list_item_txtv_testname'][contains(@text,'Exemplar')]")
    ncert_exercises = (By.XPATH,
                       "//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_tests_list_item_txtv_testname'][contains(@text,'Exercise')]")
    learn_testcard = (By.XPATH,
                      "//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/tvSubtopicName'][@text='Tests']")
    test_list_scn = (By.XPATH,
                     "//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/header_subtitle1_text'][@text='Test']")
    subjective_test = (By.XPATH,
                       "//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_tests_list_item_txtv_testname'][contains(@text,'Subjective')]")
    chapter_name = None
    objective_test_list = []
    subjective_test_list = []

    # Test instruction screen locators
    test_start_button = (By.ID, "com.byjus.thelearningapp.premium:id/test_start_button")
    test_question_icon = (By.ID, "com.byjus.thelearningapp.premium:id/iv_test_question")
    question_count = (By.ID, "com.byjus.thelearningapp.premium:id/test_question_count")
    test_time_icon = (By.ID, "com.byjus.thelearningapp.premium:id/iv_test_time")
    time_count = (By.ID, "com.byjus.thelearningapp.premium:id/test_time_count")
    backToTopClick = (By.ID, "com.byjus.thelearningapp.premium:id/backToTopClick")
    test_name = None

    # Test question screen locators
    pause_timer = (By.ID, "com.byjus.thelearningapp.premium:id/ivPauseTimer")
    timer = (By.ID, "com.byjus.thelearningapp.premium:id/tvTimer")
    questiontime = (By.ID, "com.byjus.thelearningapp.premium:id/tvQuestionTime")
    submitbtn = (By.XPATH, "//android.widget.Button[@text='Submit']")
    finish_btn = (By.XPATH, "//android.widget.Button[@text='Finish']")
    radio_button = (By.XPATH, "//android.widget.Image[@content-desc='tick']")
    radio_button1 = (By.XPATH, "//android.widget.Image[@text='tick']")
    report_an_issue = (By.ID, "com.byjus.thelearningapp.premium:id/ivReportIssue")
    previous_button_icon = (By.ID, "com.byjus.thelearningapp.premium:id/ivleftButtonIcon")
    previous_button = (By.ID, "com.byjus.thelearningapp.premium:id/tvLeftButtonText")
    next_button_icon = (By.ID, "com.byjus.thelearningapp.premium:id/ivRightButtonIcon")
    next_button = (By.ID, "com.byjus.thelearningapp.premium:id/tvRightButtonText")
    bookmark_icon = (By.ID, "com.byjus.thelearningapp.premium:id/ivBookmark")
    edit_text = (By.XPATH, "//android.widget.EditText")
    question_number = (By.ID, "com.byjus.thelearningapp.premium:id/tvTabText")
    question_number_tab = (By.ID, "com.byjus.thelearningapp.premium:id/rlTabs")
    bookmark_dot = (By.ID, "com.byjus.thelearningapp.premium:id/themedFlag")
    bookmark_id = (By.ID, "com.byjus.thelearningapp.premium:id/ivBookmark")
    question_one_id = (
        By.XPATH, "//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/tvTabText'][@text='1']")
    option_scn = (By.XPATH, "//android.webkit.WebView")
    image_class = (By.XPATH, "//android.widget.Image")
    image_view = (By.ID, "com.byjus.thelearningapp.premium:id/img")
    image_close_btn = (By.ID, "com.byjus.thelearningapp.premium:id/ic_close")
    submit_test = (By.XPATH,
                   "//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/dialog_title'][@text='Submit Test?']")
    dialog_image = (By.ID, "com.byjus.thelearningapp.premium:id/dialog_image")
    dialog_layout = (By.ID, "com.byjus.thelearningapp.premium:id/dialog_layout")
    design_bottom_sheet = (By.ID, "com.byjus.thelearningapp.premium:id/design_bottom_sheet")
    Chevron = (By.ID, "com.byjus.thelearningapp.premium:id/ivChevron")
    dialog_title = (By.ID, "com.byjus.thelearningapp.premium:id/dialog_title")
    dialog_message = (By.ID, "com.byjus.thelearningapp.premium:id/dialog_message")
    total_questions = 0
    color1 = set()
    color2 = set()
    question = None
    current_question_number = None
    image = None
    image2 = None
    option_selected = None
    time = None
    image_mobile = (By.XPATH, "//android.view.View[@content-desc=" "]")
    pause_image = (By.ID, "com.byjus.thelearningapp.premium:id/image")
    pause_right_arrow = (By.ID, "com.byjus.thelearningapp.premium:id/right_arrow")

    # Highlight screen locator
    view_solutions = (By.ID, "com.byjus.thelearningapp.premium:id/view_solutions")
    filter_icon = (By.XPATH, "//android.widget.FrameLayout[@index='2']")
    Bookmarked_filter = (By.XPATH, "//android.widget.TextView[@text ='Bookmarked']")

    # Report an Issue

    # This method is used to navigate to home screen
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

    def verify_home_screen(self, driver):
        try:
            if CommonMethods.wait_for_element_visible(driver, self.homescreen_corana_dialog, 10):
                CommonMethods.elementClick(driver, self.homescreen_corana_dialog_ok_btn)
            if CommonMethods.isElementPresent(driver, self.badge):
                CommonMethods.elementClick(driver, self.closeBtn)
            if CommonMethods.isElementPresent(driver, self.analytics_icon):
                logging.info('User is in Home screen')
                return True
            else:
                return False

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_home_screen')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_home_screen')

    # This method is used to check for subject, if subject not found it will switch to 8th grade
    def check_for_subject_and_tap(self, driver, sub):
        try:
            CommonMethods.wait_for_element_visible(driver, self.profile_header_id, 10)
            pythonSub_xpath = (By.XPATH, "//android.widget.TextView[@text=\'" + sub + "\']")
            while True:
                if CommonMethods.wait_for_element_visible(driver, pythonSub_xpath, 5):
                    CommonMethods.elementClick(driver, pythonSub_xpath)
                    break
                elif CommonMethods.scrollToElementAndClick(driver, sub):
                    break
                else:
                    self.switch_grade(driver, '8th Grade')
                    if CommonMethods.isElementPresent(driver, self.backToTopClick):
                        CommonMethods.elementClick(driver, self.backToTopClick)

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'check_for_subject_and_tap')

        except:
            CommonMethods.exception(driver, featureFileName, 'check_for_subject_and_tap')

        # This method is used to navigate to Library chapter list screen

    def navigate_to_library(self, driver, sub):
        try:
            self.check_for_subject_and_tap(driver, sub)
            while True:
                if CommonMethods.isElementPresent(driver, self.personalizeScreen_xpath):
                    break
                elif CommonMethods.isElementPresent(driver, self.chapter_list_title):
                    logging.info('User is in library chapter list screen')
                    break
                elif CommonMethods.isElementPresent(driver, self.librayBtn_id):
                    CommonMethods.elementClick(driver, self.librayBtn_id)
                elif CommonMethods.isElementPresent(driver, self.toggle_btn1):
                    CommonMethods.elementClick(driver, self.toggle_btn1)
                else:
                    CommonMethods.isElementPresent(driver, self.toggle_btn)
                    CommonMethods.elementClick(driver, self.toggle_btn)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'navigate_to_library')

        except:
            CommonMethods.exception(driver, featureFileName, 'navigate_to_library')

            # This method is used to tap on test option

    def tap_on_test_link(self, driver):
        try:
            CommonMethods.wait_for_locator(driver, self.chapter_title_view, 10)
            self.chapter_name = CommonMethods.getAttributeOfElement(driver, 'text', self.chapter_title_view)
            if CommonMethods.isElementPresent(driver, self.testbtn):
                CommonMethods.elementClick(driver, self.testbtn)
            elif CommonMethods.isElementPresent(driver, self.primaryText):
                text = CommonMethods.getTextOfElement(driver, self.primaryText)
                if text == 'Take Test':
                    CommonMethods.elementClick(driver, self.primaryText)
            else:
                logging.error('Failed to tap on test option')
                pytest.fail('Failed in method tap_on_test_link')


        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_test_link')

        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_test_link')

    # This method is used to verify user is in test list screen
    def verify_test_list_screen(self, driver):
        try:
            CommonMethods.wait_for_locator(driver, self.subtitle1_text, 20)
            if CommonMethods.isElementPresent(driver, self.subtitle1_text):
                pass
            else:
                logging.error('User is not in test list screen')
                pytest.fail('Failed to navigate to test list screen')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_test_list_screen')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_test_list_screen')

    # This method is used to verify various fields in the screen
    def verify_the_elements(self, driver, locator, Field):
        try:
            check = CommonMethods.isElementPresent(driver, locator)
            if check == True:
                logging.info(Field + ' is verified on the screen')

            else:
                logging.error('Failed to verify the ' + Field + ' on the screen')
                pytest.fail('Searching field ' + Field + ' is not found in the screen')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_the_elements')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_the_elements')

    def verify_app_back_button(self, driver):
        self.verify_the_elements(driver, self.App_backBtn, "App back button")

    def verify_header_icon(self, driver):
        self.verify_the_elements(driver, self.header_icon, "Chapter icon")

    # This method is used to verify the chapter name in test list screen
    def verify_chapter_name(self, driver):
        try:
            self.verify_the_elements(driver, self.header_title_text, "Chapter name")
            actual_text = CommonMethods.getTextOfElement(driver, self.header_title_text)
            result = CommonMethods.verifyTextMatch(actual_text, self.chapter_name)
            if result == False:
                logging.error('Chapter name is not verified')
                pytest.fail('Failed to verify chapter name')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_chapter_name')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_chapter_name')

    # This method is used to verify the text
    def verify_the_text(self, driver, text):
        try:
            if CommonMethods.findText(driver, text):
                logging.info('Found searching text "' + text + '"')

            elif CommonMethods.scrollToElement(driver, text):
                CommonMethods.findText(driver, text)
                logging.info('Found searching text "' + text + '"')

            else:
                logging.error('Failed to find the text "' + text + '" in method verifythetext')
                pytest.fail('Failed to find the text')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verifythetext')

        except:
            CommonMethods.exception(driver, featureFileName, 'verifythetext')

    # This method is used to verify objective test list
    def verify_objective_test_list(self, driver):
        try:
            check1 = CommonMethods.isElementPresent(driver, self.objective_test_list_xpath)
            check2 = CommonMethods.isElementPresent(driver, self.start_btn)
            check3 = CommonMethods.isElementPresent(driver, self.retake_test)
            if check1 == True and (check2 == True or check3 == True):
                logging.info('Objective test list is shown')
            else:
                logging.error('Objective test list is not shown')
                pytest.fail('Failed to show objective test list')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_objective_test_list')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_objective_test_list')

            # This method is used to verify subjective test list

    def verify_subjective_test_list(self, driver):
        try:
            check1 = CommonMethods.isElementPresent(driver, self.subjective_test_list_xpath)
            check2 = CommonMethods.isElementPresent(driver, self.revise_btn)
            if check1 == True and check2 == True:
                logging.info('Subjective test list is shown')
            else:
                logging.error('Subjective test list is not shown')
                pytest.fail('Failed to show Subjective test list')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_subjective_test_list')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_subjective_test_list')

            # This method is used to verify objective test card

    def verify_objective_test_card(self, driver):
        try:
            if CommonMethods.findText(driver, "Objective Tests "):
                elements = CommonMethods.getElements(driver, self.objective_test_list_xpath)
                for i in elements:
                    ob_test = i.get_attribute('text')
                    if self.chapter_name in str(ob_test):
                        pass
                    else:
                        logging.error('Chapter name is not found in objective test name')
                        pytest.fail('Chapter name is not found in objective test name')
                    self.objective_test_list.append(ob_test)
                logging.info('Found objective tests are ' + str(
                    len(self.objective_test_list)) + ' and these are the tests ' + str(self.objective_test_list))

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_objective_test_card')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_objective_test_card')

    # This method is used to verify subjective test card
    def verify_subjective_test_card(self, driver):
        try:
            if CommonMethods.findText(driver, "Subjective Tests "):
                elements = CommonMethods.getElements(driver, self.subjective_test_list_xpath)
                for i in elements:
                    sub_test = i.get_attribute('text')
                    if self.chapter_name in str(sub_test) and "Subjective Test" in str(sub_test):
                        pass
                    else:
                        logging.error('Chapter name is not found in subjective test name')
                        pytest.fail('Chapter name and "subjective test" are not found in subjective test name')
                    self.subjective_test_list.append(sub_test)
                logging.info('Found objective tests are ' + str(
                    len(self.subjective_test_list)) + ' and these are the tests ' + str(self.subjective_test_list))


        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_subjective_test_card')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_subjective_test_card')

    # This method is used verify that the tests objective tests are arranged in ascending order
    def check_obective_test_order(self, driver):
        try:
            list2 = self.objective_test_list.copy()
            self.objective_test_list.sort()
            if list2 == self.objective_test_list:
                logging.info('Objective tests are arranged in ascending order')
            else:
                logging.error('Objective tests are not arranged in ascending order')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'check_obective_test_order')

        except:
            CommonMethods.exception(driver, featureFileName, 'check_obective_test_order')

    # This method is used verify that the tests subjective tests are arranged in ascending order
    def check_subjective_test_order(self, driver):
        try:
            list2 = self.subjective_test_list.copy()
            self.subjective_test_list.sort()
            if list2 == self.subjective_test_list:
                logging.info('Subjective tests are arranged in ascending order')
            else:
                logging.error('Subjective tests are not arranged in ascending order')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'check_subective_test_order')

        except:
            CommonMethods.exception(driver, featureFileName, 'check_subective_test_order')

    # This method is used verify the star button on objective test card
    def verify_start_button(self, driver):
        try:
            if CommonMethods.isElementPresent(driver, self.start_btn):
                logging.info('Star button is shown on Objective test card')
            elif CommonMethods.isElementPresent(driver, self.retake_test):
                logging.error(' User has already taken the test')
            else:
                logging.error('Failed to find start button')
                pytest.fail('Start button not found')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_start_button')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_start_button')

    # This method is used verify the revise button on subjective test card
    def verify_revise_button(self, driver):
        try:
            if CommonMethods.isElementPresent(driver, self.revise_btn):
                logging.info('Revise button is shown on subjective test card')
            else:
                logging.error('Failed to find revise button')
                pytest.fail('Revise button not found')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_revise_button')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_revise_button')

    # This method is used for submitting the test
    def submit_test(self, driver):
        try:
            CommonMethods.wait_for_locator(driver, self.submitbtn, 10)
            CommonMethods.elementClick(driver, self.submitbtn)
            CommonMethods.wait_for_locator(driver, self.primaryActionBtn, 5)
            CommonMethods.elementClick(driver, self.primaryActionBtn)
            if CommonMethods.isElementPresent(driver, self.badge):
                CommonMethods.elementClick(driver, self.closeBtn)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'submit_test')

        except:
            CommonMethods.exception(driver, featureFileName, 'submit_test')

            # This method is used to tap on Test button on test instruction screen

    def tap_on_test_button_on_instruction_scn(self, driver):
        try:
            CommonMethods.wait_for_locator(driver, self.test_start_button, 20)
            CommonMethods.elementClick(driver, self.test_start_button)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_test_button_on_instruction_scn')

        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_test_button_on_instruction_scn')

            # This method is used to navigate to objective test instruction screen

    def navigate_to_test_instruction_screen(self, driver):
        try:
            CommonMethods.wait_for_locator(driver, self.objective_test_list_xpath, 20)
            self.test_name = CommonMethods.getAttributeOfElement(driver, 'text', self.objective_test_list_xpath)
            if CommonMethods.isElementPresent(driver, self.retake_test):
                CommonMethods.elementClick(driver, self.retake_test)
            elif CommonMethods.isElementPresent(driver, self.start_btn):
                CommonMethods.elementClick(driver, self.start_btn)
            else:
                logging.error('User failed to tap on retake or start option')
                pytest.fail('Failed to navigate to text instruction screen')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'navigate_to_test_instruction_screen')

        except:
            CommonMethods.exception(driver, featureFileName, 'navigate_to_test_instruction_screen')

    # This method is verify Analyse text
    def verify_analyse_option(self, driver):
        self.verify_the_elements(driver, self.analyse_btn, 'Analyse option')

    # This method is to verify retake icon
    def verify_retake_test_icon(self, driver):
        self.verify_the_elements(driver, self.retake_test, 'Retake icon')

    # This method is used to navigate back to test list screen
    def navigate_back_to_test_list_scn(self, driver):
        try:
            while True:
                if CommonMethods.isElementPresent(driver, self.test_list_scn):
                    break
                else:
                    CommonMethods.click_on_device_back_btn(driver)
                    sleep(2)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'navigate_back_to_test_list_scn')

        except:
            CommonMethods.exception(driver, featureFileName, 'navigate_back_to_test_list_scn')

    # This method is used to verify that user is in objective test instruction screen
    def verify_test_instruction_screen(self, driver):
        try:
            CommonMethods.wait_for_locator(driver, self.test_start_button, 20)
            if CommonMethods.isElementPresent(driver, self.test_start_button):
                logging.info('User is test instruction screen')
                if CommonMethods.isElementPresent(driver, self.question_count):
                    self.total_questions = CommonMethods.getAttributeOfElement(driver, 'text', self.question_count)
            else:
                logging.error('User is not in test instruction screen')
                pytest.fail('Failed to navigate test instruction screen')


        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_test_instruction_screen')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_test_instruction_screen')

    # This method is used to tap on retake_test_option
    def tap_on_retake_test_option(self, driver):
        try:
            if CommonMethods.isElementPresent(driver, self.retake_test):
                CommonMethods.elementClick(driver, self.retake_test)
                logging.info('User tapped on Retake test option ')
            elif CommonMethods.isElementPresent(driver, self.start_btn):
                CommonMethods.elementClick(driver, self.start_btn)
                self.tap_on_test_button_on_instruction_scn(driver)
                self.submit_test(driver)
                self.navigate_back_to_test_list_scn(driver)
                CommonMethods.wait_for_locator(driver, self.retake_test, 10)
                CommonMethods.elementClick(driver, self.retake_test)
                logging.info('User tapped on Retake test option ')
            else:
                logging.error('Failed to tap on Retake test option')
                pytest.fail('Failed in method tap_on_retake_test_option')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_retake_test_option')

        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_retake_test_option')

    # This method is used to verify that user is in objective test question screen
    def verify_test_question_screen(self, driver):
        try:
            CommonMethods.wait_for_locator(driver, self.submitbtn, 10)
            if CommonMethods.isElementPresent(driver, self.submitbtn):
                logging.info('User is objective test question screen')
            else:
                logging.error('User is not in test question screen')
                pytest.fail('Failed to navigate objective test question screen')


        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_test_question_screen')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_test_question_screen')

    # This method is used to navigate to learn chapter list screen
    def navigate_to_learn_screen(self, driver, sub):
        try:
            CommonMethods.wait_for_element_visible(driver, self.profile_header_id, 10)
            pythonSub_xpath = (By.XPATH, "//android.widget.TextView[@text=\'" + sub + "\']")
            CommonMethods.wait_for_element_visible(driver, pythonSub_xpath, 3)
            CommonMethods.elementClick(driver, pythonSub_xpath)
            if CommonMethods.isElementPresent(driver, self.librayBtn_id):
                pass
            elif CommonMethods.isElementPresent(driver, self.personalizeScreen_xpath):
                CommonMethods.elementClick(driver, self.personalizeScreen_xpath)

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'navigate_to_learn_screen')

        except:
            CommonMethods.exception(driver, featureFileName, 'navigate_to_learn_screen')

    # This method is used to tap on test card on learn screen
    def scroll_to_test_and_click(self, driver):
        try:
            driver.find_element_by_android_uiautomator(
                "new UiScrollable(new UiSelector().resourceId(\"com.byjus.thelearningapp.premium:id/rvSubtopic\")).setAsHorizontalList().scrollIntoView("
                + "new UiSelector().textContains(\"Tests\"))").click()
            return True
        except NoSuchElementException:
            logging.info("Test is not found")
            return False

        except:
            CommonMethods.exception(driver, featureFileName, 'scroll_to_test_and_click')

    # This method is used to tap on Analyse button on test list screen
    def tap_on_analyse_option(self, driver):
        try:
            if CommonMethods.isElementPresent(driver, self.analyse_btn):
                CommonMethods.elementClick(driver, self.analyse_btn)
                logging.info('User tapped on Analyse option ')
            elif CommonMethods.isElementPresent(driver, self.start_btn):
                CommonMethods.elementClick(driver, self.start_btn)
                self.tap_on_test_button_on_instruction_scn(driver)
                self.submit_test(driver)
                self.navigate_back_to_test_list_scn(driver)
                CommonMethods.wait_for_locator(driver, self.analyse_btn, 10)
                CommonMethods.elementClick(driver, self.analyse_btn)
                logging.info('User tapped on Analyse option ')
            else:
                logging.error('Failed to tap on Analyse option')
                pytest.fail('Failed in method tap_on_analyse_option')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_analyse_option')

        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_analyse_option')

    # This method is used verify that user is in highlights screen:
    def verify_highlights_screen(self, driver):
        try:
            if CommonMethods.isElementPresent(driver, self.primaryActionBtn):
                CommonMethods.click_on_device_back_btn(driver)
            CommonMethods.wait_for_locator(driver, self.subtitle1_text, 15)
            actual_text = CommonMethods.getAttributeOfElement(driver, 'text', self.header_title_text)
            result = CommonMethods.verifyTextMatch(actual_text, "Highlights")
            if result == False:
                logging.error('User is not in Highlights screen')
                pytest.fail('Failed to navigate to Highlights screen')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_highlights_screen')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_highlights_screen')

    # This method is used to to tap on 'Start' button on test list screen. If start button is not found in particular chapter,it will select next chapter.
    def tap_on_start_button(self, driver):
        try:
            count = 1
            while True:
                if CommonMethods.isElementPresent(driver, self.start_btn):
                    CommonMethods.elementClick(driver, self.start_btn)
                    break
                else:
                    self.app_backbtn(driver)
                    sleep(2)
                    if CommonMethods.isElementPresent(driver, self.testbtn):
                        elements = CommonMethods.getElements(driver, self.testbtn)
                        if count == len(elements):
                            CommonMethods.run('adb shell input touchscreen swipe 191 672 185 251')
                            elements = CommonMethods.getElements(driver, self.testbtn)
                            count = 0
                        elements[int(count)].click()
                        count = count + 1
                    else:
                        pytest.fail('Failed to find "Start" button')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_start_button')

        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_start_button')

    # This method is used to tap on app back button
    def app_backbtn(self, driver):
        try:
            CommonMethods.wait_for_locator(driver, self.App_backBtn, 20)
            CommonMethods.elementClick(driver, self.App_backBtn)

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'app_backbtn')

        except:
            CommonMethods.exception(driver, featureFileName, 'app_backbtn')

    # This method is used to tap on Video card on Library chapter list screen
    def tap_on_video_card(self, driver):
        try:
            sleep(2)
            if CommonMethods.elementClick(driver, self.video_card):
                logging.info('User tapped on Video card')
            elif CommonMethods.elementClick(driver, self.video_card_tab):
                logging.info('User tapped on Video card')
            else:
                logging.error('Failed to tap on video card')
                pytest.fail('Failed in method tap_on_video_card')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_video_card')

        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_video_card')

    # This method is used to tap test card on video list screen
    def tap_test_card_on_video_list(self, driver):
        try:
            chapter_title_2 = (By.ID, "com.byjus.thelearningapp.premium:id/chapter_title_2")
            CommonMethods.wait_for_locator(driver, chapter_title_2, 20)
            if CommonMethods.scrollToElementAndClick(driver, 'Test'):
                logging.info('User tapped on test card')
            else:
                logging.error('Failed to tap on test card')
                pytest.fail('Failed to scroll and tap on test card')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_video_card')

        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_video_card')

    # This method is used to verify library screen
    def verify_library_screen(self, driver):
        try:
            CommonMethods.wait_for_locator(driver, self.App_backBtn, 10)
            if CommonMethods.isElementPresent(driver, self.personalizeScreen_xpath):
                logging.info('User is in library screen')
            elif CommonMethods.isElementPresent(driver, self.chapter_list_title):
                logging.info('User is in library screen')
            else:
                logging.error('User is not in library screen')
                pytest.fail('Failed to navigate to library screen')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_library_screen')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_library_screen')

    # This method is used to verify learn screen
    def verify_learn_screen(self, driver):
        try:
            CommonMethods.wait_for_locator(driver, self.App_backBtn, 10)
            if CommonMethods.isElementPresent(driver, self.librayBtn_id):
                logging.info('User is in learn screen')
            elif CommonMethods.isElementPresent(driver, self.resume_title):
                logging.info('User is in learn screen')
            else:
                logging.error('User is not in learn screen')
                pytest.fail('Failed to navigate to learn screen')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_learn_screen')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_learn_screen')

    # This method is used for switch grade
    def switch_grade(self, driver, grade):
        try:
            switch_grade = (By.XPATH, "//android.widget.TextView[@text=\'" + grade + "\']")
            if CommonMethods.isElementPresent(driver, self.badge):
                CommonMethods.elementClick(driver, self.closeBtn)
            CommonMethods.isElementPresent(driver, self.hamburger_id)
            CommonMethods.elementClick(driver, self.hamburger_id)
            CommonMethods.wait_for_locator(driver, self.current_grade, 10)
            get_grade = CommonMethods.getTextOfElement(driver, self.current_grade)
            result = CommonMethods.verifyTextMatch(get_grade, grade)
            if result == True:
                logging.info('User is already in ' + grade)
                CommonMethods.click_on_device_back_btn(driver)
            else:
                CommonMethods.elementClick(driver, self.home_drawer_arrow_right)
                CommonMethods.wait_for_locator(driver, self.grade_drop_down, 10)
                CommonMethods.elementClick(driver, self.grade_drop_down)
                CommonMethods.wait_for_locator(driver, self.account_details_title, 10)
                self.scroll_till_text(driver, grade)
                CommonMethods.elementClick(driver, switch_grade)
                CommonMethods.wait_for_locator(driver, self.grade_drop_down, 30)
                CommonMethods.click_on_device_back_btn(driver)

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'switch_grade')

        except:
            CommonMethods.exception(driver, featureFileName, 'switch_grade')

    # This method is used to scroll till text is found
    def scroll_till_text(self, driver, grade):
        try:
            box_list = driver.find_element_by_xpath("//android.widget.RelativeLayout")
            switch_grade = (By.XPATH, "//android.widget.TextView[@text=\'" + grade + "\']")
            while True:
                if CommonMethods.isElementPresent(driver, switch_grade):
                    break
                else:
                    self.scroll_list(driver, box_list)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, ' scroll_till_text')

        except:
            CommonMethods.exception(driver, featureFileName, ' scroll_till_text')

            # This method is used to scroll bottom sheet dialog

    def scroll_list(self, driver, box_list):
        textlist = driver.find_elements_by_xpath("//android.widget.TextView")
        touch = TouchAction(driver)
        start_x = textlist[-1].location['x']
        start_y = textlist[-1].location['y']
        end_x = box_list.location['x']
        end_y = box_list.location['y']
        touch.press(x=start_x, y=start_y).wait(3000).move_to(x=end_x, y=end_y).release().perform()

        # This method is used to switch the network to offline mode

    def select_offline_mode(self, driver):
        try:
            set_connection_type(driver, 'OFFLINE')
            logging.info("enabled offline mode")
        except:
            logging.info("Failed in Method select_offline_mode")
            CommonMethods.takeScreenShot(driver, featureFileName)
            pytest.fail("Failed in method select_offline_mode")

    # This method is used to verify snackbar message
    def verify_snackbar_msg(self, driver, text):
        try:
            check = CommonMethods.isElementPresent(driver, self.snackbar_text)
            if check == True:
                act_txt = CommonMethods.getTextOfElement(driver, self.snackbar_text)
                logging.info('Found snackbar text ' + act_txt)
                assert act_txt == text, "Snackbar message is not matching"
            else:
                pytest.fail("Snackbar message verification failed ")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'snackbar_msg')
        except:
            CommonMethods.exception(driver, featureFileName, 'snackbar_msg')

    # This method is used to switch the network to online mode
    def select_online_mode(self, driver):
        try:
            set_connection_type(driver, "WIFI")
            logging.info("Enabled Online mode")
        except:
            logging.info("Failed in method select_online_mode")
            CommonMethods.takeScreenShot(driver, featureFileName)
            pytest.fail("Failed in method select_online_mode")

    # This method is used to tap on revise button
    def tap_on_revise_button(self, driver):
        try:
            CommonMethods.wait_for_locator(driver, self.revise_btn, 10)
            if CommonMethods.elementClick(driver, self.revise_btn):
                logging.info('User tapped on revise button')
            else:
                logging.error('Failed to tap revise button')
                pytest.fail('Failed in method tap_on_revise_button')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_revise_button')

        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_revise_button')

    # This method is used to verify Ncert Exemplars test list
    def verify_ncert_exemplars_test_list(self, driver):
        try:
            check1 = CommonMethods.isElementPresent(driver, self.ncert_exemplars)
            check2 = CommonMethods.isElementPresent(driver, self.revise_btn)
            if check1 == True and check2 == True:
                logging.info('Ncert Exemplars test list is shown')
            else:
                logging.error('Ncert Exemplars list is not shown')
                pytest.fail('Failed to show Ncert Exemplars test list')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_ncert_exemplars_test_list')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_ncert_exemplars_test_list')

    # This method is used to verify Ncert Exercises test list
    def verify_ncert_exercises_test_list(self, driver):
        try:
            check1 = CommonMethods.isElementPresent(driver, self.ncert_exercises)
            check2 = CommonMethods.isElementPresent(driver, self.revise_btn)
            if check1 == True and check2 == True:
                logging.info('Ncert Exercises test list is shown')
            else:
                logging.error('Ncert Exercises test list is not shown')
                pytest.fail('Failed to show Ncert Exercises test list')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_ncert_exercises_test_list')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_ncert_exercises_test_list')

    # This method is used to tap on device backbutton
    def tap_device_backbtn(self, driver):
        try:
            CommonMethods.click_on_device_back_btn(driver)
            logging.info('User tapped on back button')
        except:
            logging.error('Failed tap on device back button')
            pytest.fail('Failed in method tap_device_backbtn')

    # This method is used to verify the button
    def verify_the_button(self, driver, text):
        try:
            if CommonMethods.findButton(driver, text):
                logging.info('Found searching button "' + text + '"')
            else:
                logging.error('Failed to find the button "' + text + '" in method verifythebutton')
                pytest.fail('Failed to find the button')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verifythebutton')

        except:
            CommonMethods.exception(driver, featureFileName, 'verifythebutton')

    # This method is used to verify question icon,count and text in test instruction screen
    def verify_questions_and_icon(self, driver):
        self.verify_the_elements(driver, self.test_question_icon, "Question Icon")
        self.verify_the_elements(driver, self.question_count, "Question count")
        self.verify_the_text(driver, 'Questions')

    # This method is used to verify time icon ,count and text in test instruction screen
    def verify_time_and_icon(self, driver):
        self.verify_the_elements(driver, self.test_time_icon, "Time icon")
        self.verify_the_elements(driver, self.time_count, "Time count")
        self.verify_the_text(driver, 'Minutes')

    # This method is used to find text from data 'content-desc'
    def find_content_desc_text(self, driver, text):
        check = False
        locator = (By.XPATH, "//android.view.View")
        CommonMethods.wait_for_locator(driver, locator, 10)
        classlist1 = CommonMethods.getElements(driver, locator)
        for i in range(len(classlist1)):
            text2 = classlist1[i].get_attribute('content-desc')
            if str(text) in str(text2):
                check = True
                return check
            else:
                for i in range(len(classlist1)):
                    text2 = classlist1[i].get_attribute('text')
                    if str(text) in str(text2):
                        check = True
                        return check
        return False

    # This method is used to verify text from data 'content-desc'
    def verify_the_content_desc_text(self, driver, text):
        try:
            if self.find_content_desc_text(driver, text) == True:
                logging.info('Found searching text "' + text + '"')

            else:
                logging.error('Failed to find the text "' + text + '" in method verify_the_content_desc_text')
                pytest.fail('Failed to find the text')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_the_content_desc_text')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_the_content_desc_text')

    # This method is used to verify objective test insstuction 1
    def verify_objective_test_instruction1(self, driver, text):
        try:
            to_find_text = re.compile(
                r'(.*) mark is awarded for correct attempts and (.*) marks for incorrect attempts.')
            search_text = to_find_text.search(text)
            if search_text:
                found_text = search_text.group()
                logging.info('Found instruction1 is ' + found_text)
            else:
                logging.error('Failed to find the text "' + text + '" in method verify_objective_test_instruction1')
                pytest.fail('Failed to find the text')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_objective_test_instruction1')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_objective_test_instruction1')

    # This method is used to verify test instruction icons
    def verify_instruction_icons(self, driver):
        try:
            icon1 = (By.XPATH, "//android.widget.Image")
            icon2 = (By.XPATH,
                     "//android.widget.TextView/following-sibling::android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[@index=0]")
            if CommonMethods.isElementPresent(driver, icon1):
                icon = icon1
            elif CommonMethods.isElementPresent(driver, icon2):
                icon = icon2
            icons = CommonMethods.getElements(driver, icon)
            if len(icons) == 3:
                logging.info('Instruction icons are verified')
            else:
                logging.error('Instruction icons are not verified')
                pytest.fail('Failed verify Instruction icons ')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_instruction_icon')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_instruction_icon')

    # This method is used to verify that user is in test question screen
    def verify_finish_btn_on_test_question_screen(self, driver):
        try:
            CommonMethods.wait_for_locator(driver, self.finish_btn, 10)
            if CommonMethods.isElementPresent(driver, self.finish_btn):
                logging.info('User is test question screen')
            else:
                logging.error('User is not in test question screen')
                pytest.fail('Failed to navigate test question screen')


        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_finish_btn_on_test_question_screen')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_finish_btn_on_test_question_screen')

    # This method is used to navigate to Ncert Exercises test instruction screen
    def navigate_to_ncert_exercises_test_instruction_scn(self, driver):
        self.navigate_to_test_instruction_scn(driver, self.ncert_exercises, "Ncert Exercises ")

    # This method is used to navigate to Ncert Exemplars test instruction screen
    def navigate_to_ncert_examplar_test_instruction_scn(self, driver):
        self.navigate_to_test_instruction_scn(driver, self.ncert_exemplars, "Exemplar -")

    # This method is used to test name in instruction screen
    def verify_test_name_on_instruction_screen(self, driver):
        try:
            device = CommonMethods.get_device_type(driver)
            if device == 'tab':
                CommonMethods.wait_for_locator(driver, self.title, 10)
                test_name = CommonMethods.getAttributeOfElement(driver, 'text', self.title)
            elif device == 'mobile':
                CommonMethods.wait_for_locator(driver, self.header_title_text, 10)
                test_name = CommonMethods.getAttributeOfElement(driver, 'text', self.header_title_text)
            if self.test_name == test_name:
                pass
            else:
                logging.error('Found test name ' + test_name)
                pytest.fail('Failed to verify test name')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_test_name_on_instruction_screen')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_test_name_on_instruction_screen')

    # This method is used to navigate to subjective  test  instruction screen
    def navigate_to_subjective_test_instruction_scn(self, driver):
        self.navigate_to_test_instruction_scn(driver, self.subjective_test_list_xpath, "Subjective Tests ")

    # This method is used to navigate to test instruction screen
    def navigate_to_test_instruction_scn(self, driver, locator, test):
        try:
            CommonMethods.wait_for_locator(driver, self.revise_btn, 20)
            CommonMethods.scrollToElement(driver, test)
            self.test_name = CommonMethods.getAttributeOfElement(driver, 'text', locator)
            CommonMethods.elementClick(driver, locator)
            CommonMethods.wait_for_locator(driver, self.test_start_button, 20)
            if CommonMethods.isElementPresent(driver, self.test_start_button):
                logging.info('User is in ' + test + 'instruction screen')
            else:
                pytest.fail('Failed to navigate to ' + test + 'instruction screen')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'navigate_to_test_instruction_scn')

        except:
            CommonMethods.exception(driver, featureFileName, 'navigate_to_test_instruction_scn')

    # This method is used to navigate to question screen
    def navigate_to_objective_test_question_scn(self, driver):
        try:
            test = getdata(Test_data, 'Test_to_be_tested', 'Test')
            chapter = getdata(Test_data, test, 'Chapter')
            test_link1 = (By.XPATH,
                          "//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_title_view' and @text=\'" + chapter + "\']/parent::android.widget.LinearLayout/following-sibling::android.widget.LinearLayout/android.widget.TextView[@text='Test']")
            test_link2 = (By.XPATH,
                          "//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_title_view' and @text=\'" + chapter + "\']//ancestor::android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp.premium:id/chapter_view_group']//android.widget.Button[@text='Test']")
            self.switch_grade(driver, getdata(Test_data, test, 'Grade'))
            self.navigate_to_library(driver, getdata(Test_data, test, 'Subject'))
            CommonMethods.wait_for_locator(driver, self.App_backBtn, 10)
            CommonMethods.scrollToElement(driver, chapter)
            if CommonMethods.isElementPresent(driver, test_link1):
                CommonMethods.elementClick(driver, test_link1)
            elif CommonMethods.isElementPresent(driver, test_link2):
                CommonMethods.elementClick(driver, test_link2)
            else:
                CommonMethods.run('adb shell input touchscreen swipe 300 635 294 381')
                CommonMethods.elementClick(driver, test_link2)
            test_name = getdata(Test_data, test, 'Test_Name')
            test_locator = (By.XPATH,
                            "//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_tests_list_item_txtv_testname'][contains(@text,\'" + test_name + "\')]")
            CommonMethods.wait_for_locator(driver, test_locator, 20)
            CommonMethods.elementClick(driver, test_locator)
            self.tap_on_test_button_on_instruction_scn(driver)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'navigate_to_objective_test_question_scn')

        except:
            CommonMethods.exception(driver, featureFileName, 'navigate_to_objective_test_question_scn')

    # This method is used to verify previous button
    def verify_previous_button(self, driver):
        try:
            while True:
                if CommonMethods.isElementPresent(driver, self.previous_button):
                    logging.info('Previous button is verified')
                    break
                else:
                    CommonMethods.elementClick(driver, self.next_button)
            self.verify_the_elements(driver, self.previous_button_icon, 'previous button icon')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_previous_button')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_previous_button')

    def verify_next_button(self, driver):
        self.verify_the_elements(driver, self.next_button, 'Next button')
        self.verify_the_elements(driver, self.next_button_icon, 'Next button icon')

    def verify_countdown_timer(self, driver):
        self.verify_the_elements(driver, self.timer, 'Countdown Timer')

    def verify_pause_button(self, driver):
        self.verify_the_elements(driver, self.pause_timer, 'Pause button')

    def verify_question_count_up_timer(self, driver):
        self.verify_the_elements(driver, self.questiontime, 'Question count up timer')

    def verify_book_mark_icon(self, driver):
        self.verify_the_elements(driver, self.bookmark_icon, 'Bookmark icon')

    #
    #             input("Press Enter to start")
    #             start_time = time.time()
    #
    #             input("Press Enter to stop")
    #             end_time = time.time()
    #             time_lapsed = end_time - start_time
    #             time_convert(time_lapsed)
    # #
    # This method is used verify that selected question is highlighted
    def verify_question_number_highlighted(self, driver):
        try:
            CommonMethods.wait_for_locator(driver, self.question_number, 10)
            #             question_number= 1
            #             question_number_id=(By.XPATH,"//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/tvTabText'][@text=\'"+str(question_number)+"\']")
            self.verify_the_elements(driver, self.question_number, 'Question number')
            if self.question_highlighted(driver, self.question_one_id) == True:
                logging.info('Selected question is highlighted')
            CommonMethods.elementClick(driver, self.next_button)
            if self.question_highlighted(driver, self.question_one_id) == False:
                logging.info('Only Selected question is highlighted')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_question_number_highlighted')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_question_number_highlighted')

    # This method is to verify if the locator is selected or not
    def question_highlighted(self, driver, locator):
        element = CommonMethods.getElement(driver, locator)
        if element is not None:
            check = element.get_attribute("selected")
            if check == 'true':
                return True
            else:
                return False

    def verify_report_an_issue_option(self, driver):
        CommonMethods.run('adb shell input touchscreen swipe 300 635 294 381')
        self.verify_the_elements(driver, self.report_an_issue, "Report an issue")

    # This method is used to verify multiple choice question in the test
    def verify_multiple_choice_question(self, driver):
        try:
            while True:
                if CommonMethods.isElementPresent(driver,
                                                  self.radio_button) == False and CommonMethods.isElementPresent(
                    driver, self.edit_text) == False:
                    logging.info('Test has multiple choice question')
                    break
                elif CommonMethods.isElementPresent(driver, self.next_button) == False:
                    pytest.fail('Multiple choice question not found in the test')
                    break
                else:
                    CommonMethods.elementClick(driver, self.next_button)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_multiple_choice_question')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_multiple_choice_question')

    # This method is used to verify multiselect question in the test
    def verify_multi_select_question(self, driver):
        try:
            while True:
                if CommonMethods.isElementPresent(driver, self.radio_button) == True:
                    logging.info('Test has multiselect question')
                    break
                elif CommonMethods.isElementPresent(driver, self.radio_button1) == True:
                    logging.info('Test has multiselect question')
                    break
                elif CommonMethods.isElementPresent(driver, self.next_button) == False:
                    pytest.fail('Multi select question not found in the test')
                    break
                else:
                    CommonMethods.elementClick(driver, self.next_button)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_multi_select_question')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_multi_select_question')

    # This method is used to verify fill in the blanks question in the test
    def verify_fill_in_the_blanks_question(self, driver):
        try:
            while True:
                if CommonMethods.isElementPresent(driver, self.edit_text) == True:
                    logging.info('Test has fill in question')
                    break
                elif CommonMethods.isElementPresent(driver, self.next_button) == False:
                    pytest.fail('Fill in the blanks question not found in the test')
                    break
                else:
                    CommonMethods.elementClick(driver, self.next_button)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_fill_in_the_blanks_question')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_fill_in_the_blanks_question')

    # This method is used to bookmark question in test screen
    def book_mark_a_question(self, driver):
        try:
            CommonMethods.wait_for_locator(driver, self.bookmark_id, 5)
            CommonMethods.elementClick(driver, self.bookmark_id)
            sleep(2)
            toast_message = CommonMethods.getTextOfElement(driver, self.toast_msg)
            if toast_message == 'Bookmarked':
                logging.info('Question bookmarked')
            else:
                CommonMethods.elementClick(driver, self.bookmark_id)
            self.color2 = self.crop_screenshot_for_color(driver, self.bookmark_id)

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'book_mark_a_question')

        except:
            CommonMethods.exception(driver, featureFileName, 'book_mark_a_question')

        # This method is used remove bookmark question in test screen

    def remove_book_mark_in_qn_screen(self, driver):
        try:
            CommonMethods.wait_for_locator(driver, self.bookmark_id, 5)
            CommonMethods.elementClick(driver, self.bookmark_id)
            sleep(2)
            toast_message = CommonMethods.getTextOfElement(driver, self.toast_msg)
            if toast_message == 'Bookmark Removed':
                logging.info('Bookmark Removed')
            else:
                CommonMethods.elementClick(driver, self.bookmark_id)
            self.color2 = self.crop_screenshot_for_color(driver, self.bookmark_id)

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'remove_book_mark_in_qn_screen')

        except:
            CommonMethods.exception(driver, featureFileName, 'remove_book_mark_in_qn_screen')

    def verify_bookmarked_dot_on_qn_number(self, driver):
        if CommonMethods.isElementPresent(driver, self.bookmark_dot):
            logging.info('bookmaark dot is shown on question screen')
        else:
            pytest.fail('Bookmark dot is not shown')

    def verify_bookmarked_dot_removed(self, driver):
        if CommonMethods.isElementPresent(driver, self.bookmark_dot) == False:
            logging.info('Bookmark dot is not shown')
        else:
            pytest.fail('bookmaark dot is shown on question screen')

    def crop_screenshot_for_color(self, driver, locator):
        im = self.crop_element(driver, locator)
        # Quantize down to 2 colour palettised image using *"Fast Octree"* method:
        q = im.quantize(colors=2, method=2)
        # Now look at the first 2 colours, each 3 RGB entries in the palette:
        logging.info(q.getpalette()[:6])
        x = (q.getpalette()[:6])
        return x

    def crop_element(self, driver, locator):
        element = CommonMethods.getElement(driver, locator)
        location = element.location
        size = element.size
        png = driver.get_screenshot_as_png()
        im = Image.open(BytesIO(png))  # uses PIL library to open image in memory
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']
        im = im.crop((left, top, right, bottom))
        return im

    #
    def root_mean_square_error(self, rgb1, rgb2):
        sumof = (rgb1[0] - rgb2[0]) ** 2 + (rgb1[1] - rgb2[1]) ** 2 + (rgb1[2] - rgb2[2]) ** 2
        return math.sqrt(sumof / 3)

    def verify_bookmark_color(self):
        rgb_color_code1 = tuple(self.color1[:3])
        rgb_color_code2 = tuple(self.color2[3:])
        match = self.root_mean_square_error(rgb_color_code1, rgb_color_code2)
        logging.info(match)
        assert (match < 35), "Text color is not as expected"

    def get_subject_color(self, driver, sub):
        CommonMethods.wait_for_element_visible(driver, self.profile_header_id, 20)
        locator1 = (By.XPATH, "//android.widget.TextView[@text=\'" + sub + "\']/../*/android.widget.ImageView")
        locator2 = (By.XPATH, "//android.widget.TextView[@text=\'" + sub + "\']/..")
        if CommonMethods.isElementPresent(driver, locator1):
            locator = locator1
        elif CommonMethods.isElementPresent(driver, locator2):
            locator = locator2
        #         CommonMethods.wait_for_element_visible(driver, pythonSub_xpath, 3)
        self.color1 = self.crop_screenshot_for_color(driver, locator)

    def verify_gray_color(self, driver):
        device = CommonMethods.get_device_type(driver)
        if device == 'tab':
            rgb_color_code1 = tuple([187, 187, 187])
        elif device == 'mobile':
            rgb_color_code1 = tuple([153, 153, 153])
        rgb_color_code2 = tuple(self.color2[3:])
        match = self.root_mean_square_error(rgb_color_code1, rgb_color_code2)
        logging.info(match)
        assert (match < 5), "Text color is not as expected"

    def verify_question_number_tab(self, driver):
        self.verify_the_elements(driver, self.question_number, 'Question number')
        self.verify_the_elements(driver, self.question_number_tab, 'Question number tab')

    # This method will fetch a question and returns question
    def get_question(self, driver):
        try:
            test_question = (By.XPATH,
                             "//androidx.viewpager.widget.ViewPager//android.view.View[@resource-id='q']/android.view.View[@index=0]")
            count = 0
            elements = []
            elements = driver.find_elements_by_xpath("//android.view.View")
            if CommonMethods.isElementPresent(driver, test_question):
                question = CommonMethods.getAttributeOfElement(driver, 'text', test_question)
                return question
            else:
                while True:
                    question = elements[count].get_attribute('text')
                    if question == None or question == '':
                        count = count + 1
                    else:
                        break
                logging.info('Found Question is "' + question + '"')
                return question

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'get_question')

        except:
            CommonMethods.exception(driver, featureFileName, 'get_question')

        # This method is used to tap on previous button

    def tap_on_previous_button(self, driver):
        try:
            CommonMethods.wait_for_locator(driver, self.question_number, 10)
            if CommonMethods.isElementPresent(driver, self.previous_button):
                CommonMethods.elementClick(driver, self.previous_button)
            else:
                CommonMethods.elementClick(driver, self.next_button)
                CommonMethods.wait_for_locator(driver, self.questiontime, 10)
                self.question = self.get_question(driver)
                CommonMethods.elementClick(driver, self.previous_button)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_previous_button')

        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_previous_button')

    # This method is used to tap on next button
    def tap_on_next_button(self, driver):
        try:
            CommonMethods.wait_for_locator(driver, self.next_button, 10)
            CommonMethods.wait_for_locator(driver, self.questiontime, 10)
            self.question = self.get_question(driver)
            CommonMethods.elementClick(driver, self.next_button)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_next_button')

        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_next_button')

    # This method is used to verify user is in different question screen
    def user_in_different_qn_scn(self, driver):
        try:
            CommonMethods.wait_for_locator(driver, self.questiontime, 10)
            question1 = self.get_question(driver)
            if question1 != self.question:
                logging.info('User is in previous question screen')
            else:
                pytest.fail('User is not navigated to previous question screen')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'user_in_previous_qn_scn')

        except:
            CommonMethods.exception(driver, featureFileName, 'user_in_previous_qn_scn')

    # This method is used to remove bookmark in bookmrak home screen
    def remove_bookmark_in_book_mark_screen(self, driver):
        try:
            CommonMethods.isElementPresent(driver, self.analytics_icon)
            CommonMethods.elementClick(driver, self.hamburger_id)
            CommonMethods.wait_for_locator(driver, self.bookmark_ham_id, 10)
            CommonMethods.elementClick(driver, self.bookmark_ham_id)
            filter_btn = (By.XPATH, "//android.widget.Button[@text='Filter']")
            CommonMethods.wait_for_locator(driver, filter_btn, 10)
            while True:
                if CommonMethods.isElementPresent(driver, self.bookmark_tag):
                    CommonMethods.elementClick(driver, self.bookmark_tag)
                else:
                    CommonMethods.click_on_device_back_btn(driver)
                    break
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'remove_bookmark_in_book_mark_screen')

        except:
            CommonMethods.exception(driver, featureFileName, 'remove_bookmark_in_book_mark_screen')

    # This method is used to tap any question number passed to this method
    def tap_on_question_number(self, driver, question_number):
        try:
            CommonMethods.wait_for_locator(driver, self.questiontime, 20)
            self.question = self.get_question(driver)
            #             self.question_number_tab_scroll_click(driver,question_number)
            CommonMethods.scrollToElementAndClick(driver, str(question_number))
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_question_number')

        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_question_number')

    # This method is used to verify that the user is in particular question screen
    def verify_user_is_in_particular_qn_scn(self, driver, question_number):
        try:
            question_number_id = (By.XPATH,
                                  "//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/tvTabText'][@text=\'" + str(
                                      question_number) + "\']")
            CommonMethods.wait_for_locator(driver, question_number_id, 15)
            if self.question_highlighted(driver, question_number_id):
                self.user_in_different_qn_scn(driver)
                logging.info('User is in question screen of question number ' + str(self.current_question_number))
            else:
                pytest.fail('Failed to navigate to particular question')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_user_is_in_particular_qn_scn')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_user_is_in_particular_qn_scn')

    # This method is used to click on any random question from the text
    def navigate_to_particular_qn_screen(self, driver):
        logging.info('Total number of question in the test ' + self.total_questions)
        self.current_question_number = random.randint(2, int(self.total_questions))
        logging.info('Question number to click ' + str(self.current_question_number))
        #         CommonMethods.scrollToElementAndClick(driver,str(self.current_question_number))
        self.tap_on_question_number(driver, str(self.current_question_number))

    def verify_particular_qn_scn(self, driver):
        self.verify_user_is_in_particular_qn_scn(driver, self.current_question_number)

    def navigate_to_last_question(self, driver):
        CommonMethods.wait_for_locator(driver, self.questiontime, 20)
        self.question_number_tab_scroll_click(driver, self.total_questions)
        #         self.tap_on_question_number(driver, self.total_questions)
        self.verify_user_is_in_particular_qn_scn(driver, self.total_questions)

    # This method is used to verify user is in first question screen
    def user_is_in_first_question_scn(self, driver):
        try:
            CommonMethods.wait_for_locator(driver, self.question_number, 10)
            if self.question_highlighted(driver, self.question_one_id):
                logging.info('User is in first question screen')
            else:
                pytest.fail('User is not in First question screen')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'user_is_in_first_question_scn')

        except:
            CommonMethods.exception(driver, featureFileName, 'user_is_in_first_question_scn')

    # This method is used to verify that element is not shown on the screen
    def element_not_shown(self, driver, locator, text):
        try:
            if CommonMethods.isElementPresent(driver, locator) == False:
                logging.info(text + ' is not shown in the screen')
            else:
                pytest.fail(text + ' is shown in the screen')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'element_not_shown')

        except:
            CommonMethods.exception(driver, featureFileName, 'element_not_shown')

    def next_button_not_shown(self, driver):
        self.element_not_shown(driver, self.next_button, "Next button")

    def previous_button_not_shown(self, driver):
        self.element_not_shown(driver, self.previous_button, "Previous button")

    # This method is used to scroll question number tab
    def question_number_tab_scroll_click(self, driver, question_number):
        try:
            driver.find_element_by_android_uiautomator(
                "new UiScrollable(new UiSelector().resourceId(\"com.byjus.thelearningapp.premium:id/tabs\")).setAsHorizontalList().scrollIntoView("
                + "new UiSelector().textContains(\"" + str(question_number) + "\"))").click()

        except:
            CommonMethods.exception(driver, featureFileName, 'scroll_to_test_and_click')

    # This method is used to verify the keypad enabled
    def is_keypad_enabled(self, driver):
        check = CommonMethods.isKeyBoardShown(driver)
        if check == True:
            logging.info('Keypad is displayed')
        else:
            pytest.fail('Failed to show keypad in method is_keypad_enabled')

        # This method is used to tap on edit text field on fill the blanks question screen

    def tap_on_edit_text(self, driver):
        try:
            CommonMethods.wait_for_locator(driver, self.edit_text, 5)
            CommonMethods.elementClick(driver, self.edit_text)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_edit_text')

        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_edit_text')

    def verify_edit_text_field_on_scn(self, driver):
        self.verify_the_elements(driver, self.edit_text, 'Edit text')

    # This method is used to enter data on fill in the blanks edit text field
    def enter_answer(self, driver, Answer):
        try:
            self.image = self.crop_element(driver, self.option_scn)
            if CommonMethods.enterText(driver, Answer, self.edit_text):
                logging.info('You have entered answer ' + Answer)
            else:
                pytest.fail('Failed to enter answer ' + Answer)
            self.image2 = self.crop_element(driver, self.option_scn)

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'enter_answer')

        except:
            CommonMethods.exception(driver, featureFileName, 'enter_answer')

        # This method is used verify entered answer

    def verify_entered_answer(self, driver, Answer):
        try:
            if CommonMethods.getAttributeOfElement(driver, 'text', self.edit_text) == Answer:
                logging.info('Entered answer verified')
            elif CommonMethods.getAttributeOfElement(driver, 'content-desc', self.edit_text) == Answer:
                logging.info('Entered answer verified')
            else:
                pytest.fail('Entered text is not matching')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_entered_answer')

    # This method is used to verify options on question screen
    def verify_options_shown(self, driver):
        try:
            options = ["a.", "b.", "c.", "d."]
            for i in range(len(options)):
                option = options[i]
                option_content_desc = (By.XPATH, "//android.view.View[@content-desc=\'" + option + "\']/..")
                option_text = (By.XPATH, "//android.view.View[@text=\'" + option + "\']/..")
                locator = self.confirm_locator(driver, option_content_desc, option_text)
                if CommonMethods.isElementPresent(driver, locator) == True:
                    logging.info('Option found ' + option)
                elif option == "c." or option == "d.":
                    logging.info('Question type is True or False')
                else:
                    pytest.fail('Failed to verify options question screen')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_options_shown')

    # This method is used to verify radio buttons on multiselect question screen
    def verify_radio_buttons_on_question_Scn(self, driver):
        try:
            radio_buttons = CommonMethods.getElements(driver, self.radio_button)
            if len(radio_buttons) == 4:
                logging.info('Radio buttons are verified on the screen')
            else:
                pytest.fail(
                    'All radio buttons are not found on question screen and number of radio buttons found ' + str(
                        len(radio_buttons)))
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_radio_buttons_on_question_Scn')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_radio_buttons_on_question_Scn')

        # This method is used to select multiple choice question

    def select_multiple_choice_option(self, driver):
        try:
            ts = time.strftime("%Y_%m_%d_%H%M%S")

            options = ["a.", "b.", "c.", "d."]
            option = random.choice(options)
            option_content_desc = (By.XPATH, "//android.view.View[@content-desc=\'" + option + "\']/..")
            option_text = (By.XPATH, "//android.view.View[@text=\'" + option + "\']/..")
            self.option_selected = self.confirm_locator(driver, option_content_desc, option_text)
            self.image = self.crop_element(driver, self.option_selected)
            self.image.save(ts + "im1.png")
            CommonMethods.elementClick(driver, self.option_selected)
            sleep(2)
            self.image2 = self.crop_element(driver, self.option_selected)
            self.image2.save(ts + "im4.png")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'select_multiple_choice_option')

        except:
            CommonMethods.exception(driver, featureFileName, 'select_multiple_choice_option')

        # This method is used to compare multiple choice question screen

    def image_compare(self, driver):
        try:
            #             diff = ImageChops.difference(self.image,self.image2)
            #             if diff.getbbox()!=None:
            if list(self.image.getdata()) != list(self.image2.getdata()):
                logging.info('Option is selected')
            else:
                pytest.fail('Option is not selected')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'image_compare')

        except:
            CommonMethods.exception(driver, featureFileName, 'image_compare')

        # This method is used to confirm the locators in the screen

    def confirm_locator(self, driver, locator1, locator2):
        try:
            if CommonMethods.isElementPresent(driver, locator1):
                locator = locator1
            elif CommonMethods.isElementPresent(driver, locator2):
                locator = locator2
            return locator
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'confirm_locator')

        except:
            CommonMethods.exception(driver, featureFileName, 'confirm_locator')

        # This method is used to select options in multi select question screen

    def select_multi_select_options(self, driver):
        try:
            self.image = self.crop_element(driver, self.option_scn)
            number_of_option_to_select = random.randint(1, 4)
            logging.info(number_of_option_to_select)
            options = ["a.", "b.", "c.", "d."]
            option_list = random.sample(options, number_of_option_to_select)
            logging.info(option_list)
            for i in range(len(option_list)):
                option_content_desc = (By.XPATH, "//android.view.View[@content-desc=\'" + option_list[i] + "\']/..")
                option_text = (By.XPATH, "//android.view.View[@text=\'" + option_list[i] + "\']/..")
                locator = self.confirm_locator(driver, option_content_desc, option_text)
                CommonMethods.elementClick(driver, locator)
            sleep(2)
            self.image2 = self.crop_element(driver, self.option_scn)

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'select_multi_select_option')

        except:
            CommonMethods.exception(driver, featureFileName, 'select_multi_select_option')

        # This method is used to compare the multiselect question screen after the answer selection

    def image_compare_multiselect(self, driver):
        try:
            #             diff = ImageChops.difference(self.image,self.image2)
            # if diff.getbbox()!=None:
            if list(self.image.getdata()) != list(self.image2.getdata()):
                logging.info('Options are selected ')
            else:
                pytest.fail('Options are not selected')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'image_compare_multiselect')

        except:
            CommonMethods.exception(driver, featureFileName, 'image_compare_multiselect')

        # This method is to verify that the previously answered question answer is saved

    def answer_saved(self, driver, locator):
        try:
            im2 = self.crop_element(driver, locator)

            #             diff = ImageChops.difference(self.image2,im2)
            #             if diff.getbbox()!=None:
            if list(im2.getdata()) != list(self.image2.getdata()):
                pytest.fail('Previously saved answer is not shown')
            else:
                logging.info('Answer is saved')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'image_compare_multiselect')

        except:
            CommonMethods.exception(driver, featureFileName, 'image_compare_multiselect')

    def compare_multiple_choice_option(self, driver):
        self.answer_saved(driver, self.option_selected)

    def compare_question_screen(self, driver):
        self.answer_saved(driver, self.option_scn)

    # This method is used to navigate to image type questions
    def navigate_to_image_type_qn(self, driver):
        try:
            qn_number = getdata(Test_data, getdata(Test_data, 'Test_to_be_tested', 'Test'),
                                'Image_type_question_number')
            self.tap_on_question_number(driver, qn_number)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'navigate_to_image_type_qn')

        except:
            CommonMethods.exception(driver, featureFileName, 'navigate_to_image_type_qn')

    # This method is used to tap on Image on question screen
    def tap_on_image(self, driver):
        try:
            CommonMethods.wait_for_locator(driver, self.option_scn, 10)
            if CommonMethods.isElementPresent(driver, self.image_class):
                CommonMethods.elementClick(driver, self.image_class)
            elif CommonMethods.elementClick(driver, self.option_scn):
                logging.info('Tapped on image on question screen')
            else:
                pytest.fail('Failed to tap on the image on question screen')
            CommonMethods.wait_for_locator(driver, self.image_view, 10)
            self.image = self.crop_element(driver, self.image_view)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_image')

        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_image')

    def verify_image_view_screen(self, driver):
        self.verify_the_elements(driver, self.image_view, 'Image view screen')

    def verify_image_view_cls_btn(self, driver):
        self.verify_the_elements(driver, self.image_close_btn, 'Image view close button')

    # This method is used to tap on close button on image view screen
    def tap_on_close_btn(self, driver):
        try:
            CommonMethods.wait_for_locator(driver, self.image_close_btn, 5)
            CommonMethods.elementClick(driver, self.image_close_btn)

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_close_btn')

        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_close_btn')

    # This method is used to verify that Image view screen is dismissed
    def verify_image_view_dismissed(self, driver):
        try:
            if CommonMethods.isElementPresent(driver, self.image_view) == False:
                if CommonMethods.isElementPresent(driver, self.option_scn):
                    logging.info('Image view screen is dismissed')
            else:
                pytest.fail('Failed to dismiss Image view screen')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_image_view_dismissed')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_image_view_dismissed')

    def double_tap_on_image(self, driver):
        try:
            element = CommonMethods.getElement(driver, self.image_view)
            loc = element.rect
            x = loc['x']
            y = loc['y']
            height = loc['height']
            width = loc['width']
            x2 = (x + width) / 2
            y2 = (y + height) / 2
            action1 = TouchAction(driver)
            action1.press(x=x2, y=y2).release().perform().wait(100).press(x=x2, y=y2).release().perform()
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'double_tap_on_image')

        except:
            CommonMethods.exception(driver, featureFileName, 'double_tap_on_image')

    # This method is used to verify bottom sheet dialog
    def verify_bottomsheet_dialog_shown(self, driver, text):
        try:
            CommonMethods.wait_for_locator(driver, self.dialog_title, 5)
            if CommonMethods.findText(driver, text):
                logging.info("'" + text + "'" + " bottom sheet dialog is shown")
            else:
                pytest.fail("'" + text + "'" + " bottom sheet dialog is not shown")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_bottomsheet_dialog_shown')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_bottomsheet_dialog_shown')

    # This method is used to tap on submit button
    def tap_on_submit_button(self, driver):
        try:
            CommonMethods.wait_for_locator(driver, self.submitbtn, 10)
            if CommonMethods.elementClick(driver, self.submitbtn):
                logging.info('User tapped on submit button')
            else:
                pytest.fail('Failed to tap submit button')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_submit_button')

        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_submit_button')

    def verify_test_icon(self, driver):
        self.verify_the_elements(driver, self.dialog_image, "Dialog image")

    def verify_bottom_sheet_dialog_title(self, driver, text):
        try:
            if CommonMethods.getAttributeOfElement(driver, 'text', self.dialog_title) == text:
                logging.info("Title text '" + text + "' is verified")
            else:
                pytest.fail("Title text " + text + "' not found")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_bottom_sheet_dialog_title')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_bottom_sheet_dialog_title')

    def verify_bottom_sheet_dialog_message(self, driver, text):
        try:
            if CommonMethods.getAttributeOfElement(driver, 'text', self.dialog_message) == text:
                logging.info("Message ' " + text + "' is verified")
            else:
                pytest.fail("Message ' " + text + "' not found")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_bottom_sheet_dialog_message')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_bottom_sheet_dialog_message')

    # This method is used verify primary button
    def verify_primary_button(self, driver, text):
        try:
            if CommonMethods.getAttributeOfElement(driver, 'text', self.primaryActionBtn) == text:
                logging.info("Primary Action button ' " + text + "' is verified")
            else:
                pytest.fail("Primary Action button ' " + text + "' not found")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_primary_button')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_primary_button')

    # This method is used verify secondary button
    def verify_secondary_button(self, driver, text):
        try:
            if CommonMethods.getAttributeOfElement(driver, 'text', self.secondaryActionBtn) == text:
                logging.info("Secondary Action button ' " + text + "' is verified")
            else:
                pytest.fail("Secondary Action button ' " + text + "'not found")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_secondary_button')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_secondary_button')

    # This method is used to tap on primary action button
    def tap_on_primary_action_button(self, driver):
        try:
            if CommonMethods.elementClick(driver, self.primaryActionBtn):
                logging.info("User tappped on primary action button")
            else:
                pytest.fail("Failed to tap on primary action button")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_primary_action_button')

        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_primary_action_button')

    # This method is used to tap on secondary action button
    def tap_on_secondary_action_button(self, driver):
        try:
            if CommonMethods.elementClick(driver, self.secondaryActionBtn):
                logging.info("User tappped on secondary action button")
            else:
                pytest.fail("Failed to tap on secondary action button")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_secondary_action_button')

        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_secondary_action_button')

    # This method is used verify bottom sheet dialog is dismissed
    def bottomsheet_dailog_dismissed(self, driver):
        try:
            sleep(2)
            if CommonMethods.isElementPresent(driver, self.dialog_layout) == False:
                logging.info('Bottom sheet dialog is dismissed')
            elif CommonMethods.isElementPresent(driver, self.design_bottom_sheet) == False:
                logging.info('Bottom sheet dialog is dismissed')
            else:
                pytest.fail('Failed to dismiss the bottom sheet dialog')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'bottomsheet_dailog_dismissed')

        except:
            CommonMethods.exception(driver, featureFileName, 'bottomsheet_dailog_dismissed')

    # This method is used to verify submit test bottom sheet dialog text message
    def verify_submit_test_message(self, driver, text):
        try:
            to_find_text = re.compile(r'Hey (.*), are you sure you want to end this test?')
            search_text = to_find_text.search(text)
            if search_text:
                found_text = search_text.group()
                logging.info('Found message ' + found_text)
            else:
                pytest.fail('Failed to find the text message "' + text + '" in method verify_submit_test_message ')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_submit_test_message')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_submit_test_message')

    # This method is used to verify image is zoomed in
    def image_zoom_in(self, driver):
        try:
            sleep(2)
            self.image2 = self.crop_element(driver, self.image_view)
            #             diff = ImageChops.difference(self.image,self.image2)
            #             if diff.getbbox()!=None:
            if list(self.image.getdata()) != list(self.image2.getdata()):
                logging.info('Image is zoomed')
            else:
                pytest.fail('Failed to zoom the image')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'image_zoom_in')

        except:
            CommonMethods.exception(driver, featureFileName, 'image_zoom_in')

    # This method is used to verify image is zoomed out
    def image_zoom_out(self, driver):
        try:
            sleep(2)
            self.image2 = self.crop_element(driver, self.image_view)
            #             diff = ImageChops.difference(self.image,self.image2)
            #             if diff.getbbox()!=None:
            if list(self.image.getdata()) != list(self.image2.getdata()):
                pytest.fail('Failed to zoom out the image')
            else:
                logging.info('Image zoomed in')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'image_zoom_out')

        except:
            CommonMethods.exception(driver, featureFileName, 'image_zoom_out')

    def navigate_to_first_qn(self, driver):
        CommonMethods.scrollToElementAndClick(driver, '1')

    # This method is used to tap on Pause button
    def tap_on_pause_button(self, driver):
        try:
            CommonMethods.wait_for_locator(driver, self.pause_timer, 10)
            if CommonMethods.elementClick(driver, self.pause_timer):
                logging.info("User tappped on pause button")
            else:
                pytest.fail("Failed to tap on pause button")

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_pause_button')

        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_pause_button')

    # This method is used to tap on option on "Test Paused" bottom sheet dialog
    def tap_on_option(self, driver, text):
        try:
            locator = (By.XPATH, "//android.widget.TextView[@text=\'" + text + "\']")
            CommonMethods.wait_for_locator(driver, locator, 5)
            if CommonMethods.elementClick(driver, locator):
                logging.info('User tapped on ' + text + ' option')
            else:
                pytest.fail('Failed to tap on ' + text + ' option')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_option')

        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_option')

    # This method is used to verify option, icon and right arrow on Test Paused bottom sheet dialog
    def verify_option_icon_rightarrow(self, driver, text):
        try:
            option = (By.XPATH,
                      "//android.widget.ImageView/following-sibling::android.widget.RelativeLayout/android.widget.TextView[@text = \'" + text + "\']/following-sibling::android.widget.ImageView")
            icon = (By.XPATH,
                    "//descendant::android.widget.TextView[@text=\'" + text + "\']/parent::android.widget.RelativeLayout/preceding-sibling::android.widget.ImageView")
            right_arrow = (By.XPATH,
                           "//android.widget.ImageView/following-sibling::android.widget.RelativeLayout/android.widget.TextView[@text =\'" + text + "\']/following-sibling::android.widget.ImageView")
            self.verify_the_elements(driver, option, 'Option')
            self.verify_the_elements(driver, icon, 'icon')
            self.verify_the_elements(driver, right_arrow, 'right_arrow')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_option_icon_rightarrow')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_option_icon_rightarrow')

    # This method is used to verify countdown timer in question screen
    def verify_countdown_timer_time(self, driver):
        try:
            CommonMethods.wait_for_locator(driver, self.timer, 5)
            time1 = CommonMethods.getAttributeOfElement(driver, 'text', self.timer)
            time1 = self.time_to_sec(time1)
            logging.info(time1)
            sleep(5)
            time2 = CommonMethods.getAttributeOfElement(driver, 'text', self.timer)
            time2 = self.time_to_sec(time2)
            logging.info(time2)
            if int(time1) > int(time2):
                logging.info('Countdown timer started')
            else:
                logging.info('Timer1 is ' + str(time1) + ' and timer2 is ' + str(time2))
                pytest.fail('Countdown timer failed')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_countdown_timer_time')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_countdown_timer_time')

    # This method is used to convert time string into sec in integer value
    def time_to_sec(self, time_str):
        return sum(x * int(t) for x, t in zip([1, 60, 3600], reversed(time_str.split(":"))))

    # This method is to verify the timer count up for particular question
    def verify_countup_for_qn(self, driver):
        try:
            time1 = self.time_to_sec(self.time)
            logging.info(time1)
            sleep(5)
            time2 = CommonMethods.getAttributeOfElement(driver, 'text', self.questiontime)
            time2 = self.time_to_sec(time2)
            logging.info(time2)
            if int(time1) < int(time2):
                logging.info('Countup timer started')
            else:
                logging.info('Timer1 is ' + str(time1) + ' and timer2 is ' + str(time2))
                pytest.fail('Countup timer failed')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_countup_for_qn')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_countup_for_qn')

    # This method is to verify particular qn time start @ 00:00
    def get_qn_start_time(self, driver):
        try:
            time = self.get_qn_time(driver)
            time1 = self.time_to_sec(time)
            logging.info(time1)
            if int(time1) == 0 or int(time1) <= 2:
                logging.info('Countup timer started from 00:00')
            else:
                logging.info('Timer count is ' + str(time1))
                pytest.fail('Countup timer failed')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'get_qn_start_time')

        except:
            CommonMethods.exception(driver, featureFileName, 'get_qn_start_time')

    # This method is to verify particular qn time
    def get_qn_time(self, driver):
        try:
            CommonMethods.wait_for_locator(driver, self.questiontime, 5)
            self.time = CommonMethods.getAttributeOfElement(driver, 'text', self.questiontime)
            return self.time
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'get_qn_time')

        except:
            CommonMethods.exception(driver, featureFileName, 'get_qn_time')

        # This method is used to tap on report an issue icon

    def tap_on_report_an_issue_icon(self, driver):
        self.verify_report_an_issue_option(driver)
        CommonMethods.elementClick(driver, self.report_an_issue)

    # This method is used to verify option and right arrow on Report an Issue bottom sheet dialog
    def verify_option_rightarrow(self, driver, text):
        try:
            option = (By.XPATH, "//android.widget.TextView[@text=\'" + text + "\']")
            right_arrow = (
                By.XPATH,
                "//android.widget.TextView[@text=\'" + text + "\']/following-sibling::android.widget.ImageView")
            self.verify_the_elements(driver, option, 'Option')
            self.verify_the_elements(driver, right_arrow, 'right_arrow')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_option_icon_rightarrow')

        except:
            CommonMethods.exception(driver, featureFileName, 'verify_option_icon_rightarrow')

    #
