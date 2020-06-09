from time import sleep
from selenium.webdriver.common.by import By
from Utilities.common_methods import CommonMethods
from Utilities.interrupt import *
from selenium.common.exceptions import NoSuchElementException
import logging
import pytest
from Constants.load_json import *
from Constants.constants import CONFIG_PATH, Login_Credentials, Test_data
from appium.webdriver.common.touch_action import TouchAction
import re
import random
import time

CommonMethods = CommonMethods()
data_file = CONFIG_PATH

f = open("../../Test_data/featureFileName.txt", "r")
featureFileName = f.read()


class EngineTestScreen:

    def __init__(self, browser):
        self.browser = browser

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
    homescreen_corana_dialog_ok_btn = (By.ID, "com.byjus.thelearningapp.premium:id/tv_secondaryAction")
    homescreen_corana_dialog = (By.ID, "com.byjus.thelearningapp.premium:id/dialog_layout")
    free_live_classes = (By.XPATH, "//android.view.View[@content-desc='Free Live Classes']")

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
                                  "//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_tests_list_item_txtv_testname'][contains(@text,'Subjective')]")
    ncert_exemplars = (By.XPATH,
                       "//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_tests_list_item_txtv_testname'][contains(@text,'Exemplar')]")
    ncert_exercises = (By.XPATH,
                       "//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_tests_list_item_txtv_testname'][contains(@text,'Exercise')]")
    learn_testcard = (
        By.XPATH,
        "//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/tvSubtopicName'][@text='Tests']")
    test_list_scn = (By.XPATH,
                     "//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/header_subtitle1_text'][@text='Test']")

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
    report_an_issue = (By.ID, "com.byjus.thelearningapp.premium:id/ivReportIssue")
    previous_button_icon = (By.ID, "com.byjus.thelearningapp.premium:id/ivleftButtonIcon")
    previous_button = (By.ID, "com.byjus.thelearningapp.premium:id/tvLeftButtonText")
    next_button_icon = (By.ID, "com.byjus.thelearningapp.premium:id/ivRightButtonIcon")
    next_button = (By.ID, "com.byjus.thelearningapp.premium:id/tvRightButtonText")
    bookmark_icon = (By.ID, "com.byjus.thelearningapp.premium:id/ivBookmark")
    edit_text = (By.XPATH, "//android.widget.EditText")
    fill_in_the_blank_text = (By.XPATH, "//android.view.View[@content-desc='Tap the blank to answer']")
    question_number = (By.ID, "com.byjus.thelearningapp.premium:id/tvTabText")
    total_questions = 0

    # Highlight screen locator
    view_solutions = (By.ID, "com.byjus.thelearningapp.premium:id/view_solutions")
    filter_icon = (By.XPATH, "//android.widget.FrameLayout[@index='2']")
    Bookmarked_filter = (By.XPATH, "//android.widget.TextView[@text ='Bookmarked']")

    # Report an Issue

    # This method is used to navigate to home screen
    def navigate_to_home_screen(self, browser):
        try:
            if self.verify_home_screen(browser):
                pass
            else:
                if CommonMethods.isElementPresent(browser, self.allowbutton):
                    CommonMethods.elementClick(browser, self.allowbutton)
                    CommonMethods.elementClick(browser, self.allowbutton)
                if CommonMethods.isElementPresent(browser, self.skipButton):
                    CommonMethods.elementClick(browser, self.skipButton)
                if CommonMethods.isElementPresent(browser, self.grade8th):
                    CommonMethods.elementClick(browser, self.grade8th)
                    if CommonMethods.isElementPresent(browser, self.gms_cancel):
                        CommonMethods.elementClick(browser, self.gms_cancel)
                if CommonMethods.isElementPresent(browser, self.btnRegister):
                    CommonMethods.elementClick(browser, self.regscn_lgnbtn)
                    if CommonMethods.isElementPresent(browser, self.gms_cancel):
                        CommonMethods.elementClick(browser, self.gms_cancel)
                if CommonMethods.isElementPresent(browser, self.loginBtn_id):
                    CommonMethods.wait_for_locator(browser, self.country_Code, 15)
                    CommonMethods.elementClick(browser, self.country_Code)
                    sleep(2)
                    CommonMethods.scrollToElementAndClick(browser, getdata(Login_Credentials, 'login_detail4'
                                                                           , 'country_code'))
                    CommonMethods.enterText(browser, getdata(Login_Credentials, 'login_detail4', 'mobile_no'),
                                            self.phone_num)
                    CommonMethods.wait_for_locator(browser, self.loginBtn_id, 10)
                    CommonMethods.elementClick(browser, self.loginBtn_id)
                    CommonMethods.wait_for_locator(browser, self.OtpTxtBx_id, 15)
                    CommonMethods.enterText(browser, getdata(Login_Credentials, 'login_detail4', 'OTP'),
                                            self.OtpTxtBx_id)
                    sleep(10)
                self.verify_home_screen(browser)

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'navigate_to_home_screen')

        except:
            CommonMethods.exception(browser, featureFileName, 'navigate_to_home_screen')

    def verify_home_screen(self, browser):
        try:
            # if CommonMethods.wait_for_element_visible(browser, self.homescreen_corana_dialog, 10):
            #     CommonMethods.elementClick(browser, self.homescreen_corana_dialog_ok_btn)
            if CommonMethods.isElementPresent(browser, self.badge):
                CommonMethods.elementClick(browser, self.closeBtn)
            if CommonMethods.isElementPresent(browser, self.analytics_icon):
                logging.info('User is in Home screen')
                return True
            else:
                return False

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_home_screen')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_home_screen')

    # This method is used to check for subject, if subject not found it will switch to 8th grade
    def check_for_subject_and_tap(self, browser, sub):
        try:
            CommonMethods.wait_for_element_visible(browser, self.profile_header_id, 10)
            pythonSub_xpath = (By.XPATH, "//android.widget.TextView[@text=\'" + sub + "\']")
            while True:
                if CommonMethods.wait_for_element_visible(browser, pythonSub_xpath, 5):
                    CommonMethods.elementClick(browser, pythonSub_xpath)
                    break
                elif CommonMethods.scrollToElementAndClick(browser, sub):
                    break
                else:
                    self.switch_grade(browser, '8th Grade')
                    if CommonMethods.isElementPresent(browser, self.backToTopClick):
                        CommonMethods.elementClick(browser, self.backToTopClick)

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'check_for_subject_and_tap')

        except:
            CommonMethods.exception(browser, featureFileName, 'check_for_subject_and_tap')

        # This method is used to navigate to Library chapter list screen

    def navigate_to_library(self, browser, sub):
        try:
            self.check_for_subject_and_tap(browser, sub)
            while True:
                if CommonMethods.isElementPresent(browser, self.personalizeScreen_xpath):
                    break
                elif CommonMethods.isElementPresent(browser, self.chapter_list_title):
                    logging.info('User is in library chapter list screen')
                    break
                elif CommonMethods.isElementPresent(browser, self.librayBtn_id):
                    CommonMethods.elementClick(browser, self.librayBtn_id)
                elif CommonMethods.isElementPresent(browser, self.toggle_btn1):
                    CommonMethods.elementClick(browser, self.toggle_btn1)
                else:
                    CommonMethods.isElementPresent(browser, self.toggle_btn)
                    CommonMethods.elementClick(browser, self.toggle_btn)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'navigate_to_library')

        except:
            CommonMethods.exception(browser, featureFileName, 'navigate_to_library')

            # This method is used to tap on test option

    def tap_on_test_link(self, browser):
        try:
            CommonMethods.wait_for_locator(browser, self.chapter_title_view, 10)
            self.chapter_name = CommonMethods.getAttributeOfElement(browser, 'text', self.chapter_title_view)
            if CommonMethods.isElementPresent(browser, self.testbtn):
                CommonMethods.elementClick(browser, self.testbtn)
            elif CommonMethods.isElementPresent(browser, self.primaryText):
                text = CommonMethods.getTextOfElement(browser, self.primaryText)
                if text == 'Test':
                    CommonMethods.elementClick(browser, self.primaryText)
            else:
                logging.error('Failed to tap on test option')
                pytest.fail('Failed in method tap_on_test_link')


        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'tap_on_test_link')

        except:
            CommonMethods.exception(browser, featureFileName, 'tap_on_test_link')

    # This method is used to verify user is in test list screen
    def verify_test_list_screen(self, browser):
        try:
            CommonMethods.wait_for_locator(browser, self.subtitle1_text, 20)
            if CommonMethods.getAttributeOfElement(browser, 'text', self.subtitle1_text) == 'Test':
                #             if CommonMethods.findText(browser, 'Test'):
                pass
            else:
                logging.error('User is not in test list screen')
                pytest.fail('Failed to navigate to test list screen')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_test_list_screen')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_test_list_screen')

    # This method is used to verify various fields in the screen
    def verify_the_elements(self, browser, locator, Field):
        try:
            check = CommonMethods.isElementPresent(browser, locator)
            if check == True:
                logging.info(Field + ' is verified on the screen')

            else:
                logging.error('Failed to verify the ' + Field + ' on the screen')
                pytest.fail('Searching field ' + Field + ' is not found in the screen')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_the_elements')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_the_elements')

    def verify_app_back_button(self, browser):
        self.verify_the_elements(browser, self.App_backBtn, "App back button")

    def verify_header_icon(self, browser):
        self.verify_the_elements(browser, self.header_icon, "Chapter icon")

    # This method is used to verify the chapter name in test list screen
    def verify_chapter_name(self, browser):
        try:
            self.verify_the_elements(browser, self.header_title_text, "Chapter name")
            actual_text = CommonMethods.getTextOfElement(browser, self.header_title_text)
            result = CommonMethods.verifyTextMatch(actual_text, self.chapter_name)
            if result == False:
                logging.error('Chapter name is not verified')
                pytest.fail('Failed to verify chapter name')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_chapter_name')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_chapter_name')

    # This method is used to verify the text
    def verify_the_text(self, browser, text):
        try:
            if CommonMethods.findText(browser, text):
                logging.info('Found searching text "' + text + '"')

            elif CommonMethods.scrollToElement(browser, text):
                CommonMethods.findText(browser, text)
                logging.info('Found searching text "' + text + '"')

            else:
                logging.error('Failed to find the text "' + text + '" in method verifythetext')
                pytest.fail('Failed to find the text')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verifythetext')

        except:
            CommonMethods.exception(browser, featureFileName, 'verifythetext')

    # This method is used to verify objective test list
    def verify_objective_test_list(self, browser):
        try:
            check1 = CommonMethods.isElementPresent(browser, self.objective_test_list_xpath)
            check2 = CommonMethods.isElementPresent(browser, self.start_btn)
            check3 = CommonMethods.isElementPresent(browser, self.retake_test)
            if check1 == True and (check2 == True or check3 == True):
                logging.info('Objective test list is shown')
            else:
                logging.error('Objective test list is not shown')
                pytest.fail('Failed to show objective test list')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_objective_test_list')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_objective_test_list')

            # This method is used to verify subjective test list

    def verify_subjective_test_list(self, browser):
        try:
            check1 = CommonMethods.isElementPresent(browser, self.subjective_test_list_xpath)
            check2 = CommonMethods.isElementPresent(browser, self.revise_btn)
            if check1 == True and check2 == True:
                logging.info('Subjective test list is shown')
            else:
                logging.error('Subjective test list is not shown')
                pytest.fail('Failed to show Subjective test list')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_subjective_test_list')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_subjective_test_list')

            # This method is used to verify objective test card

    def verify_objective_test_card(self, browser):
        try:
            if CommonMethods.findText(browser, "Objective Tests "):
                elements = CommonMethods.getElements(browser, self.objective_test_list_xpath)
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
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_objective_test_card')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_objective_test_card')

    # This method is used to verify subjective test card
    def verify_subjective_test_card(self, browser):
        try:
            if CommonMethods.findText(browser, "Subjective Tests "):
                elements = CommonMethods.getElements(browser, self.subjective_test_list_xpath)
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
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_subjective_test_card')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_subjective_test_card')

    # This method is used verify that the tests objective tests are arranged in ascending order
    def check_obective_test_order(self, browser):
        try:
            list2 = self.objective_test_list.copy()
            self.objective_test_list.sort()
            if list2 == self.objective_test_list:
                logging.info('Objective tests are arranged in ascending order')
            else:
                logging.error('Objective tests are not arranged in ascending order')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'check_obective_test_order')

        except:
            CommonMethods.exception(browser, featureFileName, 'check_obective_test_order')

    # This method is used verify that the tests subjective tests are arranged in ascending order
    def check_subjective_test_order(self, browser):
        try:
            list2 = self.subjective_test_list.copy()
            self.subjective_test_list.sort()
            if list2 == self.subjective_test_list:
                logging.info('Subjective tests are arranged in ascending order')
            else:
                logging.error('Subjective tests are not arranged in ascending order')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'check_subective_test_order')

        except:
            CommonMethods.exception(browser, featureFileName, 'check_subective_test_order')

    # This method is used verify the star button on objective test card
    def verify_start_button(self, browser):
        try:
            if CommonMethods.isElementPresent(browser, self.start_btn):
                logging.info('Star button is shown on Objective test card')
            elif CommonMethods.isElementPresent(browser, self.retake_test):
                logging.error(' User has already taken the test')
            else:
                logging.error('Failed to find start button')
                pytest.fail('Start button not found')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_start_button')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_start_button')

    # This method is used verify the revise button on subjective test card
    def verify_revise_button(self, browser):
        try:
            if CommonMethods.isElementPresent(browser, self.revise_btn):
                logging.info('Revise button is shown on subjective test card')
            else:
                logging.error('Failed to find revise button')
                pytest.fail('Revise button not found')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_revise_button')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_revise_button')

    # This method is used for submitting the test
    def submit_test(self, browser):
        try:
            CommonMethods.wait_for_locator(browser, self.submitbtn, 10)
            CommonMethods.elementClick(browser, self.submitbtn)
            CommonMethods.wait_for_locator(browser, self.primaryActionBtn, 5)
            CommonMethods.elementClick(browser, self.primaryActionBtn)
            if CommonMethods.isElementPresent(browser, self.badge):
                CommonMethods.elementClick(browser, self.closeBtn)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'submit_test')

        except:
            CommonMethods.exception(browser, featureFileName, 'submit_test')

            # This method is used to tap on Test button on test instruction screen

    def tap_on_test_button_on_instruction_scn(self, browser):
        try:
            CommonMethods.wait_for_locator(browser, self.test_start_button, 20)
            CommonMethods.elementClick(browser, self.test_start_button)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'tap_on_test_button_on_instruction_scn')

        except:
            CommonMethods.exception(browser, featureFileName, 'tap_on_test_button_on_instruction_scn')

            # This method is used to navigate to objective test instruction screen

    def navigate_to_test_instruction_screen(self, browser):
        try:
            CommonMethods.wait_for_locator(browser, self.objective_test_list_xpath, 20)
            self.test_name = CommonMethods.getAttributeOfElement(browser, 'text', self.objective_test_list_xpath)
            if CommonMethods.isElementPresent(browser, self.start_btn):
                CommonMethods.elementClick(browser, self.start_btn)
            elif CommonMethods.isElementPresent(browser, self.retake_test):
                CommonMethods.elementClick(browser, self.retake_test)
            else:
                logging.error('User failed to tap on retake or start option')
                pytest.fail('Failed to navigate to text instruction screen')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'navigate_to_test_instruction_screen')

        except:
            CommonMethods.exception(browser, featureFileName, 'navigate_to_test_instruction_screen')

    # This method is verify Analyse text
    def verify_analyse_option(self, browser):
        self.verify_the_elements(browser, self.analyse_btn, 'Analyse option')

    # This method is to verify retake icon
    def verify_retake_test_icon(self, browser):
        self.verify_the_elements(browser, self.retake_test, 'Retake icon')

    # This method is used to navigate back to test list screen
    def navigate_back_to_test_list_scn(self, browser):
        try:
            while True:
                if CommonMethods.isElementPresent(browser, self.test_list_scn):
                    break
                else:
                    CommonMethods.click_on_device_back_btn(browser)
                    sleep(2)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'navigate_back_to_test_list_scn')

        except:
            CommonMethods.exception(browser, featureFileName, 'navigate_back_to_test_list_scn')

    # This method is used to verify that user is in objective test instruction screen
    def verify_test_instruction_screen(self, browser):
        try:
            CommonMethods.wait_for_locator(browser, self.test_start_button, 20)
            if CommonMethods.isElementPresent(browser, self.test_start_button):
                logging.info('User is test instruction screen')
                if CommonMethods.isElementPresent(browser, self.question_count):
                    self.total_question = CommonMethods.getAttributeOfElement(browser, 'text', self.question_count)
            else:
                logging.error('User is not in test instruction screen')
                pytest.fail('Failed to navigate test instruction screen')


        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_test_instruction_screen')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_test_instruction_screen')

    # This method is used to tap on retake_test_option
    def tap_on_retake_test_option(self, browser):
        try:
            if CommonMethods.isElementPresent(browser, self.retake_test):
                CommonMethods.elementClick(browser, self.retake_test)
                logging.info('User tapped on Retake test option ')
            elif CommonMethods.isElementPresent(browser, self.start_btn):
                CommonMethods.elementClick(browser, self.start_btn)
                self.tap_on_test_button_on_instruction_scn(browser)
                self.submit_test(browser)
                self.navigate_back_to_test_list_scn(browser)
                CommonMethods.wait_for_locator(browser, self.retake_test, 10)
                CommonMethods.elementClick(browser, self.retake_test)
                logging.info('User tapped on Retake test option ')
            else:
                logging.error('Failed to tap on Retake test option')
                pytest.fail('Failed in method tap_on_retake_test_option')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'tap_on_retake_test_option')

        except:
            CommonMethods.exception(browser, featureFileName, 'tap_on_retake_test_option')

    # This method is used to verify that user is in objective test question screen
    def verify_test_question_screen(self, browser):
        try:
            CommonMethods.wait_for_locator(browser, self.submitbtn, 10)
            if CommonMethods.isElementPresent(browser, self.submitbtn):
                logging.info('User is objective test question screen')
            else:
                logging.error('User is not in test question screen')
                pytest.fail('Failed to navigate objective test question screen')


        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_test_question_screen')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_test_question_screen')

    # This method is used to navigate to learn chapter list screen
    def navigate_to_learn_screen(self, browser, sub):
        try:
            CommonMethods.wait_for_element_visible(browser, self.profile_header_id, 10)
            pythonSub_xpath = (By.XPATH, "//android.widget.TextView[@text=\'" + sub + "\']")
            CommonMethods.wait_for_element_visible(browser, pythonSub_xpath, 3)
            CommonMethods.elementClick(browser, pythonSub_xpath)
            if CommonMethods.isElementPresent(browser, self.librayBtn_id):
                pass
            elif CommonMethods.isElementPresent(browser, self.personalizeScreen_xpath):
                CommonMethods.elementClick(browser, self.personalizeScreen_xpath)

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'navigate_to_learn_screen')

        except:
            CommonMethods.exception(browser, featureFileName, 'navigate_to_learn_screen')

    # This method is used to tap on test card on learn screen
    def scroll_to_test_and_click(self, browser):
        try:
            browser.find_element_by_android_uiautomator(
                "new UiScrollable(new UiSelector().resourceId(\"com.byjus.thelearningapp.premium:id/rvSubtopic\")).setAsHorizontalList().scrollIntoView("
                + "new UiSelector().textContains(\"Tests\"))").click()
            return True
        except NoSuchElementException:
            logging.info("Test is not found")
            return False

        except:
            CommonMethods.exception(browser, featureFileName, 'scroll_to_test_and_click')

    # This method is used to tap on Analyse button on test list screen
    def tap_on_analyse_option(self, browser):
        try:
            if CommonMethods.isElementPresent(browser, self.analyse_btn):
                CommonMethods.elementClick(browser, self.analyse_btn)
                logging.info('User tapped on Analyse option ')
            elif CommonMethods.isElementPresent(browser, self.start_btn):
                CommonMethods.elementClick(browser, self.start_btn)
                self.tap_on_test_button_on_instruction_scn(browser)
                self.submit_test(browser)
                self.navigate_back_to_test_list_scn(browser)
                CommonMethods.wait_for_locator(browser, self.analyse_btn, 10)
                CommonMethods.elementClick(browser, self.analyse_btn)
                logging.info('User tapped on Analyse option ')
            else:
                logging.error('Failed to tap on Analyse option')
                pytest.fail('Failed in method tap_on_analyse_option')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'tap_on_analyse_option')

        except:
            CommonMethods.exception(browser, featureFileName, 'tap_on_analyse_option')

    # This method is used verify that user is in highlights screen:
    def verify_highlights_screen(self, browser):
        try:
            if CommonMethods.isElementPresent(browser, self.primaryActionBtn):
                CommonMethods.click_on_device_back_btn(self, browser)
            CommonMethods.wait_for_locator(browser, self.subtitle1_text, 10)
            actual_text = CommonMethods.getAttributeOfElement(browser, 'text', self.header_title_text)
            result = CommonMethods.verifyTextMatch(actual_text, "Highlights")
            if result == False:
                logging.error('User is not in Highlights screen')
                pytest.fail('Failed to navigate to Highlights screen')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_highlights_screen')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_highlights_screen')

    # This method is used to to tap on 'Start' button on test list screen. If start button is not found in particular chapter,it will select next chapter.
    def tap_on_start_button(self, browser):
        try:
            count = 1
            while True:
                if CommonMethods.isElementPresent(browser, self.start_btn):
                    CommonMethods.elementClick(browser, self.start_btn)
                    break
                else:
                    self.app_backbtn(browser)
                    sleep(2)
                    if CommonMethods.isElementPresent(browser, self.testbtn):
                        elements = CommonMethods.getElements(browser, self.testbtn)
                        if count == len(elements):
                            CommonMethods.run('adb shell input touchscreen swipe 191 672 185 251')
                            elements = CommonMethods.getElements(browser, self.testbtn)
                            count = 0
                        elements[int(count)].click()
                        count = count + 1
                    else:
                        pytest.fail('Failed to find "Start" button')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'tap_on_start_button')

        except:
            CommonMethods.exception(browser, featureFileName, 'tap_on_start_button')

    # This method is used to tap on app back button
    def app_backbtn(self, browser):
        try:
            CommonMethods.wait_for_locator(browser, self.App_backBtn, 20)
            CommonMethods.elementClick(browser, self.App_backBtn)

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'app_backbtn')

        except:
            CommonMethods.exception(browser, featureFileName, 'app_backbtn')

    # This method is used to tap on Video card on Library chapter list screen
    def tap_on_video_card(self, browser):
        try:
            sleep(2)
            if CommonMethods.elementClick(browser, self.video_card):
                logging.info('User tapped on Video card')
            elif CommonMethods.elementClick(browser, self.video_card_tab):
                logging.info('User tapped on Video card')
            else:
                logging.error('Failed to tap on video card')
                pytest.fail('Failed in method tap_on_video_card')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'tap_on_video_card')

        except:
            CommonMethods.exception(browser, featureFileName, 'tap_on_video_card')

    # This method is used to tap test card on video list screen
    def tap_test_card_on_video_list(self, browser):
        try:
            chapter_title_2 = (By.ID, "com.byjus.thelearningapp.premium:id/chapter_title_2")
            CommonMethods.wait_for_locator(browser, chapter_title_2, 20)
            if CommonMethods.scrollToElementAndClick(browser, 'Test'):
                logging.info('User tapped on test card')
            else:
                logging.error('Failed to tap on test card')
                pytest.fail('Failed to scroll and tap on test card')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'tap_on_video_card')

        except:
            CommonMethods.exception(browser, featureFileName, 'tap_on_video_card')

    # This method is used to verify library screen
    def verify_library_screen(self, browser):
        try:
            CommonMethods.wait_for_locator(browser, self.App_backBtn, 10)
            if CommonMethods.isElementPresent(browser, self.personalizeScreen_xpath):
                logging.info('User is in library screen')
            elif CommonMethods.isElementPresent(browser, self.chapter_list_title):
                logging.info('User is in library screen')
            else:
                logging.error('User is not in library screen')
                pytest.fail('Failed to navigate to library screen')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_library_screen')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_library_screen')

    # This method is used to verify learn screen
    def verify_learn_screen(self, browser):
        try:
            CommonMethods.wait_for_locator(browser, self.App_backBtn, 10)
            if CommonMethods.isElementPresent(browser, self.librayBtn_id):
                logging.info('User is in learn screen')
            elif CommonMethods.isElementPresent(browser, self.resume_title):
                logging.info('User is in learn screen')
            else:
                logging.error('User is not in learn screen')
                pytest.fail('Failed to navigate to learn screen')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_learn_screen')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_learn_screen')

    # This method is used for switch grade
    def switch_grade(self, browser, grade):
        try:
            switch_grade = (By.XPATH, "//android.widget.TextView[@text=\'" + grade + "\']")
            if CommonMethods.isElementPresent(browser, self.badge):
                CommonMethods.elementClick(browser, self.closeBtn)
            CommonMethods.isElementPresent(browser, self.hamburger_id)
            CommonMethods.elementClick(browser, self.hamburger_id)
            CommonMethods.wait_for_locator(browser, self.current_grade, 10)
            get_grade = CommonMethods.getTextOfElement(browser, self.current_grade)
            result = CommonMethods.verifyTextMatch(get_grade, grade)
            if result == True:
                logging.info('User is already in ' + grade)
                CommonMethods.click_on_device_back_btn(browser)
            else:
                CommonMethods.elementClick(browser, self.home_drawer_arrow_right)
                CommonMethods.wait_for_locator(browser, self.grade_drop_down, 10)
                CommonMethods.elementClick(browser, self.grade_drop_down)
                CommonMethods.wait_for_locator(browser, self.account_details_title, 10)
                self.scroll_till_text(browser, grade)
                CommonMethods.elementClick(browser, switch_grade)
                CommonMethods.wait_for_locator(browser, self.grade_drop_down, 30)
                CommonMethods.click_on_device_back_btn(browser)

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'switch_grade')

        except:
            CommonMethods.exception(browser, featureFileName, 'switch_grade')

    # This method is used to scroll till text is found
    def scroll_till_text(self, browser, grade):
        try:
            box_list = browser.find_element_by_xpath("//android.widget.RelativeLayout")
            switch_grade = (By.XPATH, "//android.widget.TextView[@text=\'" + grade + "\']")
            while True:
                if CommonMethods.isElementPresent(browser, switch_grade):
                    break
                else:
                    self.scroll_list(browser, box_list)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, ' scroll_till_text')

        except:
            CommonMethods.exception(browser, featureFileName, ' scroll_till_text')

            # This method is used to scroll bottom sheet dialog

    def scroll_list(self, browser, box_list):
        textlist = browser.find_elements_by_xpath("//android.widget.TextView")
        touch = TouchAction(browser)
        start_x = textlist[-1].location['x']
        start_y = textlist[-1].location['y']
        end_x = box_list.location['x']
        end_y = box_list.location['y']
        touch.press(x=start_x, y=start_y).wait(3000).move_to(x=end_x, y=end_y).release().perform()

        # This method is used to switch the network to offline mode

    def select_offline_mode(self, browser):
        try:
            set_connection_type(browser, 'OFFLINE')
            logging.info("enabled offline mode")
        except:
            logging.info("Failed in Method select_offline_mode")
            CommonMethods.takeScreenShot(browser, featureFileName)
            pytest.fail("Failed in method select_offline_mode")

    # This method is used to verify snackbar message
    def verify_snackbar_msg(self, browser, text):
        try:
            check = CommonMethods.isElementPresent(browser, self.snackbar_text)
            if check == True:
                act_txt = CommonMethods.getTextOfElement(browser, self.snackbar_text)
                logging.info('Found snackbar text ' + act_txt)
                assert act_txt == text, "Snackbar message is not matching"
            else:
                pytest.fail("Snackbar message verification failed ")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'snackbar_msg')
        except:
            CommonMethods.exception(browser, featureFileName, 'snackbar_msg')

    # This method is used to switch the network to online mode
    def select_online_mode(self, browser):
        try:
            set_connection_type(browser, "WIFI")
            logging.info("Enabled Online mode")
        except:
            logging.info("Failed in method select_online_mode")
            CommonMethods.takeScreenShot(browser, featureFileName)
            pytest.fail("Failed in method select_online_mode")

    # This method is used to tap on revise button
    def tap_on_revise_button(self, browser):
        try:
            CommonMethods.wait_for_locator(browser, self.revise_btn, 10)
            if CommonMethods.elementClick(browser, self.revise_btn):
                logging.info('User tapped on revise button')
            else:
                logging.error('Failed to tap revise button')
                pytest.fail('Failed in method tap_on_revise_button')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'tap_on_revise_button')

        except:
            CommonMethods.exception(browser, featureFileName, 'tap_on_revise_button')

    # This method is used to verify Ncert Exemplars test list
    def verify_ncert_exemplars_test_list(self, browser):
        try:
            check1 = CommonMethods.isElementPresent(browser, self.ncert_exemplars)
            check2 = CommonMethods.isElementPresent(browser, self.revise_btn)
            if check1 == True and check2 == True:
                logging.info('Ncert Exemplars test list is shown')
            else:
                logging.error('Ncert Exemplars list is not shown')
                pytest.fail('Failed to show Ncert Exemplars test list')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_ncert_exemplars_test_list')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_ncert_exemplars_test_list')

    # This method is used to verify Ncert Exercises test list
    def verify_ncert_exercises_test_list(self, browser):
        try:
            check1 = CommonMethods.isElementPresent(browser, self.ncert_exercises)
            check2 = CommonMethods.isElementPresent(browser, self.revise_btn)
            if check1 == True and check2 == True:
                logging.info('Ncert Exercises test list is shown')
            else:
                logging.error('Ncert Exercises test list is not shown')
                pytest.fail('Failed to show Ncert Exercises test list')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_ncert_exercises_test_list')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_ncert_exercises_test_list')

    # This method is used to tap on device backbutton
    def tap_device_backbtn(self, browser):
        try:
            CommonMethods.click_on_device_back_btn(browser)
            logging.info('User tapped on back button')
        except:
            logging.error('Failed tap on device back button')
            pytest.fail('Failed in method tap_device_backbtn')

    # This method is used to verify the button
    def verify_the_button(self, browser, text):
        try:
            if CommonMethods.findButton(browser, text):
                logging.info('Found searching button "' + text + '"')
            else:
                logging.error('Failed to find the button "' + text + '" in method verifythebutton')
                pytest.fail('Failed to find the button')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verifythebutton')

        except:
            CommonMethods.exception(browser, featureFileName, 'verifythebutton')

    # This method is used to verify question icon,count and text in test instruction screen
    def verify_questions_and_icon(self, browser):
        self.verify_the_elements(browser, self.test_question_icon, "Question Icon")
        self.verify_the_elements(browser, self.question_count, "Question count")
        self.verify_the_text(browser, 'Questions')

    # This method is used to verify time icon ,count and text in test instruction screen
    def verify_time_and_icon(self, browser):
        self.verify_the_elements(browser, self.test_time_icon, "Time icon")
        self.verify_the_elements(browser, self.time_count, "Time count")
        self.verify_the_text(browser, 'Minutes')

    # This method is used to find text from data 'content-desc'
    def find_content_desc_text(self, browser, text):
        check = False
        locator = (By.XPATH, "//android.view.View")
        CommonMethods.wait_for_locator(browser, locator, 10)
        classlist1 = CommonMethods.getElements(browser, locator)
        for i in range(len(classlist1)):
            text2 = classlist1[i].get_attribute('content-desc')
            if str(text) in str(text2):
                check = True
            else:
                for i in range(len(classlist1)):
                    text2 = classlist1[i].get_attribute('text')
                    if str(text) in str(text2):
                        check = True
        return check

    # This method is used to verify text from data 'content-desc'
    def verify_the_content_desc_text(self, browser, text):
        try:
            if self.find_content_desc_text(browser, text) == True:
                logging.info('Found searching text "' + text + '"')

            else:
                logging.error('Failed to find the text "' + text + '" in method verify_the_content_desc_text')
                pytest.fail('Failed to find the text')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_the_content_desc_text')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_the_content_desc_text')

    # This method is used to verify objective test insstuction 1
    def verify_objective_test_instruction1(self, browser, text):
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
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_objective_test_instruction1')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_objective_test_instruction1')

    # This method is used to verify test instruction icons
    def verify_instruction_icons(self, browser):
        try:
            icon = (By.XPATH, "//android.widget.Image")
            icons = CommonMethods.getElements(browser, icon)
            if len(icons) == 3:
                logging.info('Instruction icons are verified')
            else:
                logging.error('Instruction icons are not verified')
                pytest.fail('Failed verify Instruction icons ')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_instruction_icon')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_instruction_icon')

    # This method is used to verify that user is in test question screen
    def verify_finish_btn_on_test_question_screen(self, browser):
        try:
            CommonMethods.wait_for_locator(browser, self.finish_btn, 10)
            if CommonMethods.isElementPresent(browser, self.finish_btn):
                logging.info('User is test question screen')
            else:
                logging.error('User is not in test question screen')
                pytest.fail('Failed to navigate test question screen')


        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_finish_btn_on_test_question_screen')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_finish_btn_on_test_question_screen')

    # This method is used to navigate to Ncert Exercises test instruction screen
    def navigate_to_ncert_exercises_test_instruction_scn(self, browser):
        self.navigate_to_test_instruction_scn(browser, self.ncert_exercises, "Ncert Exercises ")

    # This method is used to navigate to Ncert Exemplars test instruction screen
    def navigate_to_ncert_examplar_test_instruction_scn(self, browser):
        self.navigate_to_test_instruction_scn(browser, self.ncert_exemplars, "Ncert Exemplars ")

    # This method is used to verify chapter name and test name in instruction screen
    def verify_chapter_n_test_name_on_instruction_screen(self, browser):
        try:
            CommonMethods.wait_for_locator(browser, self.header_title_text, 10)
            test_name = CommonMethods.getAttributeOfElement(browser, 'text', self.header_title_text)
            if CommonMethods.findText(browser, self.chapter_name):
                pass
            else:
                pytest.fail('Failed to verify chapter name')
            if self.test_name == test_name:
                pass
            else:
                logging.error('Found test name ' + test_name)
                pytest.fail('Failed to verify test name')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_chapter_n_test_name_on_instruction_screen')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_chapter_n_test_name_on_instruction_screen')

    # This method is used to navigate to subjective  test  instruction screen
    def navigate_to_subjective_test_instruction_scn(self, browser):
        self.navigate_to_test_instruction_scn(browser, self.subjective_test_list_xpath, "Subjective Tests ")

    # This method is used to navigate to test instruction screen
    def navigate_to_test_instruction_scn(self, browser, locator, test):
        try:
            CommonMethods.wait_for_locator(browser, self.revise_btn, 20)
            CommonMethods.scrollToElement(browser, test)
            self.test_name = CommonMethods.getAttributeOfElement(browser, 'text', locator)
            CommonMethods.elementClick(browser, locator)
            CommonMethods.wait_for_locator(browser, self.test_start_button, 20)
            if CommonMethods.isElementPresent(browser, self.test_start_button):
                logging.info('User is in ' + test + 'instruction screen')
            else:
                pytest.fail('Failed to navigate to ' + test + 'instruction screen')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'navigate_to_test_instruction_scn')

        except:
            CommonMethods.exception(browser, featureFileName, 'navigate_to_test_instruction_scn')

    # This method is used to navigate to question screen
    def navigate_to_objective_test_question_scn(self, browser):
        try:
            test_list = getdata(Test_data, 'Test_list_for_different_types_of_questions', 'list')
            test = random.choice(test_list)
            chapter = getdata(Test_data, test, 'Chapter')
            test_link = (By.XPATH,
                         "//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_title_view' and @text=\'" + chapter + "\']/parent::android.widget.LinearLayout/following-sibling::android.widget.LinearLayout/android.widget.TextView[@text='Test']")
            self.switch_grade(browser, getdata(Test_data, test, 'Grade'))
            self.navigate_to_library(browser, getdata(Test_data, test, 'Subject'))
            CommonMethods.wait_for_locator(browser, self.App_backBtn, 10)
            CommonMethods.scrollToElement(browser, chapter)
            CommonMethods.wait_for_locator(browser, test_link, 10)
            CommonMethods.elementClick(browser, test_link)
            test_name = getdata(Test_data, test, 'Test_Name')
            test_locator = (By.XPATH,
                            "//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/chapter_tests_list_item_txtv_testname'][contains(@text,\'" + test_name + "\')]")
            CommonMethods.wait_for_locator(browser, test_locator, 20)
            CommonMethods.elementClick(browser, test_locator)
            self.tap_on_test_button_on_instruction_scn(browser)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'navigate_to_objective_test_question_scn')

        except:
            CommonMethods.exception(browser, featureFileName, 'navigate_to_objective_test_question_scn')

    # This method is used to verify previous button
    def verify_previous_button(self, browser):
        try:
            while True:
                if CommonMethods.isElementPresent(browser, self.previous_button):
                    logging.info('Previous button is verified')
                    break
                else:
                    CommonMethods.elementClick(browser, self.next_button)
            self.verify_the_elements(browser, self.previous_button_icon, 'previous button icon')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_previous_button')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_previous_button')

    def verify_next_button(self, browser):
        self.verify_the_elements(browser, self.next_button, 'Next button')
        self.verify_the_elements(browser, self.next_button_icon, 'Next button icon')

    def verify_countdown_timer(self, browser):
        self.verify_the_elements(browser, self.timer, 'Countdown Timer')

    def verify_pause_button(self, browser):
        self.verify_the_elements(browser, self.pause_timer, 'Pause button')

    def verify_question_count_up_timer(self, browser):
        self.verify_the_elements(browser, self.questiontime, 'Question count up timer')

    def verify_book_mark_icon(self, browser):
        self.verify_the_elements(browser, self.bookmark_icon, 'Bookmark icon')

    def time_convert(self, sec):
        mins = sec // 60
        sec = sec % 60
        hours = mins // 60
        mins = mins % 60
        logging.info("Time Lapsed = {0}:{1}:{2}".format(int(hours), int(mins), sec))

    #             input("Press Enter to start")
    #             start_time = time.time()
    #
    #             input("Press Enter to stop")
    #             end_time = time.time()
    #             time_lapsed = end_time - start_time
    #             time_convert(time_lapsed)
    # #
    # This method is used verify that selected question is highlighted
    def verify_question_number_highlighted(self, browser):
        try:
            question_number = 1
            question_number_id = (By.XPATH,
                                  "//android.widget.TextView[@resource-id='com.byjus.thelearningapp.premium:id/tvTabText'][@text=\'" + str(
                                      question_number) + "\']")
            self.verify_the_elements(browser, self.question_number, 'Question number')
            if self.question_highlighted(browser, question_number_id) == True:
                logging.info('Selected question is highlighted')
            CommonMethods.elementClick(browser, self.next_button)
            if self.question_highlighted(browser, question_number_id) == False:
                logging.info('Only Selected question is highlighted')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_question_number_highlighted')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_question_number_highlighted')

    # This method is to verify if the locator is selected or not
    def question_highlighted(self, browser, locator):
        element = CommonMethods.getElement(browser, locator)
        if element is not None:
            check = element.get_attribute("selected")
            if check == 'true':
                return True
            else:
                return False

    def verify_report_an_issue_option(self, browser):
        CommonMethods.scrollToElement(browser, "Report an issue")
        self.verify_the_elements(browser, self.report_an_issue, "Report an issue")

    # This method is used to verify multiple choice question in the test
    def verify_multiple_choice_question(self, browser):
        try:
            CommonMethods.scrollToElementAndClick(browser, '1')
            while True:
                if CommonMethods.isElementPresent(browser,
                                                  self.radio_button) == False and CommonMethods.isElementPresent(
                    browser, self.edit_text) == False:
                    logging.info('Test has multiple choice question')
                    break
                elif CommonMethods.isElementPresent(browser, self.next_button) == False:
                    logging.info('Multiple choice question not found in the test')
                    break
                else:
                    CommonMethods.elementClick(browser, self.next_button)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_multiple_choice_question')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_multiple_choice_question')

    # This method is used to verify multiselect question in the test
    def verify_multi_select_question(self, browser):
        try:
            CommonMethods.scrollToElementAndClick(browser, '1')
            while True:
                if CommonMethods.isElementPresent(browser, self.radio_button) == True:
                    logging.info('Test has multiselect question')
                    break
                elif CommonMethods.isElementPresent(browser, self.next_button) == False:
                    logging.info('Multi select question not found in the test')
                    break
                else:
                    CommonMethods.elementClick(browser, self.next_button)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_multi_select_question')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_multi_select_question')

    # This method is used to verify fill in the blanks question in the test
    def verify_fill_in_the_blanks_question(self, browser):
        try:
            CommonMethods.scrollToElementAndClick(browser, '1')
            while True:
                if CommonMethods.isElementPresent(browser, self.edit_text) == True:
                    logging.info('Test has fill in question')
                    break
                elif CommonMethods.isElementPresent(browser, self.next_button) == False:
                    pytest.fail('Fill in the blancks question not found in the test')
                    break
                else:
                    CommonMethods.elementClick(browser, self.next_button)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_fill_in_the_blanks_question')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_fill_in_the_blanks_question')
