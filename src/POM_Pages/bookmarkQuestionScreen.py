from time import sleep
from selenium.webdriver.common.by import By
from Utilities.common_methods import CommonMethods
from Utilities.interrupt import *
from selenium.common.exceptions import NoSuchElementException
import logging
import pytest
from conftest import browser
from Constants.load_json import *
from Constants.constants import CONFIG_PATH, Login_Credentials
import re
from PIL import Image
from io import BytesIO

CommonMethods = CommonMethods()
data_file = CONFIG_PATH

featureFileName = 'Bookmark questions'


class BookMarkQuestionScreen():

    def __init__(self, browser):
        self.browser = browser

    hamburger_id = (By.ID, "com.byjus.thelearningapp.premium:id/roundedNavButton")
    bookmark_ham_id = (By.XPATH, "//android.widget.TextView[@text ='Bookmarks']")
    bookmark_id = (By.ID, "com.byjus.thelearningapp.premium:id/ivBookmark")
    question_title = (By.ID, "com.byjus.thelearningapp.premium:id/tvTitle")
    subject_chapter = (By.ID, "com.byjus.thelearningapp.premium:id/tvSubject")
    bookmark_tag = (By.ID, "com.byjus.thelearningapp.premium:id/ivBookmarkTag")
    filter_id = (By.XPATH, "//android.widget.Button[@text ='Filter']")
    app_back = (By.ID, "com.byjus.thelearningapp.premium:id/roundedNavButton")
    practice_bookmark = (By.ID, "com.byjus.thelearningapp.premium:id/ivBookmarkButton")
    concept_name_id = (By.ID, "com.byjus.thelearningapp.premium:id/conceptName")
    share_icon = (By.ID, "com.byjus.thelearningapp.premium:id/ivShare")
    bookmark_icon = (By.ID, "com.byjus.thelearningapp.premium:id/bookmark")
    toast_msg = (By.XPATH, "//android.widget.Toast")
    title = (By.ID, "com.byjus.thelearningapp.premium:id/title")
    snackbar_action = (By.ID, "com.byjus.thelearningapp.premium:id/snackbar_action")
    sol_question = None
    snackbar_text = (By.ID, "com.byjus.thelearningapp.premium:id/snackbar_text")
    filter = (By.ID, "com.byjus.thelearningapp.premium:id/rightNav")
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

    exp_text = None
    personalizeScreen_xpath = (By.XPATH, "//android.widget.Button[@text='Personalised']")
    librayBtn_id = (By.XPATH, "//android.widget.Button[@text='Library']")
    profile_header_id = (By.ID, "com.byjus.thelearningapp.premium:id/llHeaderTextParent")
    ibrayBtn_id = (By.ID, "com.byjus.thelearningapp.premium:id/optionalNav")
    testbtn = (By.ID, "com.byjus.thelearningapp.premium:id/chapter_list_item_test_txtvw")
    practicebtn = (By.ID, "com.byjus.thelearningapp.premium:id/practice_mode_bottom_txtvw")
    start_btn = (By.XPATH, "//android.widget.TextView[@text='Start']")
    test_start_button = (By.ID, "com.byjus.thelearningapp.premium:id/test_start_button")
    submitbtn = (By.ID, "com.byjus.thelearningapp.premium:id/rectangleNavButton")
    questionId = (By.XPATH, "//android.view.View[@index='0']")
    retake_test = (By.ID, "com.byjus.thelearningapp.premium:id/retake_test")
    toggle_btn = (By.ID, "com.byjus.thelearningapp.premium:id/optionalNav")
    toggle_btn1 = (By.ID, "com.byjus.thelearningapp.premium:id/optionalNav2")
    secondaryActionBtn = (By.ID, "com.byjus.thelearningapp.premium:id/secondaryAction")
    primaryActionBtn = (By.ID, "com.byjus.thelearningapp.premium:id/primaryAction")
    header_title_text = (By.ID, "com.byjus.thelearningapp.premium:id/header_title_text")
    subtitle1_text = (By.ID, "com.byjus.thelearningapp.premium:id/header_subtitle1_text")
    view_solutions = (By.ID, "com.byjus.thelearningapp.premium:id/view_solutions")
    filter_icon = (By.XPATH, "//android.widget.FrameLayout[@index='2']")
    Bookmarked_filter = (By.XPATH, "//android.widget.TextView[@text ='Bookmarked']")
    start_practice = (By.ID, "com.byjus.thelearningapp.premium:id/tvStartPractice")
    solution = (By.XPATH, "//android.view.View[contains(@content-desc,'Solution']")
    CorrectAnswer = (By.XPATH, "//android.view.View[contains(@content-desc,'Correct Answer:']")
    option_a = (By.XPATH, "//android.view.View[contains(@content-desc,'a.']")
    chapter_list_title = (By.ID, "com.byjus.thelearningapp.premium:id/chapterlistTitle")
    homescreen_corana_dialog_ok_btn = (By.ID, "com.byjus.thelearningapp.premium:id/tv_secondaryAction")
    homescreen_corana_dialog = (By.ID, "com.byjus.thelearningapp.premium:id/dialog_layout")
    free_live_classes = (By.XPATH, "//android.view.View[@content-desc='Free Live Classes']")

    toast_message = None
    question = None
    chapter_name = None
    subject_color = set()
    bookmark_icon_color = set()

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
            if CommonMethods.isElementPresent(browser, self.profile_header_id):
                logging.info('User is in Home screen')
                return True
            else:
                return False

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_home_screen')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_home_screen')

    # This method is used to navigate to Library chapter list screen
    def navigate_to_library(self, browser, sub):
        try:
            CommonMethods.wait_for_element_visible(browser, self.profile_header_id, 20)
            pythonSub_xpath = (By.XPATH, "//android.widget.TextView[@text=\'" + sub + "\']")
            #             BookMarkQuestionScreen.subject_color=self.get_the_rgb_lst(browser,pythonSub_xpath)
            CommonMethods.wait_for_element_visible(browser, pythonSub_xpath, 3)
            CommonMethods.elementClick(browser, pythonSub_xpath)
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

        # This method is used to navigate to Home screen from any other screen

    def navigate_back_home_screen(self, browser):
        try:
            while True:
                if CommonMethods.isElementPresent(browser, self.analytics_icon):
                    logging.info('User is in Home screen')
                    break
                else:
                    CommonMethods.click_on_device_back_btn(browser)
                    sleep(2)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'navigate_back_home_screen')

        except:
            CommonMethods.exception(browser, featureFileName, 'navigate_back_home_screen')

        # This method is used to navigate to test instruction screen

    def navigate_to_test(self, browser):
        try:
            CommonMethods.isElementPresent(browser, self.testbtn)
            CommonMethods.elementClick(browser, self.testbtn)
            if CommonMethods.isElementPresent(browser, self.start_btn):
                CommonMethods.elementClick(browser, self.start_btn)
                logging.info('User is in instruction screen')
            elif CommonMethods.isElementPresent(browser, self.retake_test):
                CommonMethods.elementClick(browser, self.retake_test)
                logging.info('User is in instruction screen')
            else:
                logging.error('User is not in text instruction screen')
                pytest.fail('Failed to navigate to text instruction screen')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'navigate_to_test')

        except:
            CommonMethods.exception(browser, featureFileName, 'navigate_to_test')

        # This method is used to verify toast message

    def verify_toast_msg(self, browser, text):
        try:
            if CommonMethods.isElementPresent(browser, self.toast_msg):
                act_txt = CommonMethods.getTextOfElement(browser, self.toast_msg)
                if act_txt == text:
                    logging.info('Found toast message ' + act_txt)
            elif self.toast_message == text:
                logging.info('Toast message verified, toast message is ' + self.toast_message)
            else:
                pytest.fail("Toast text verification failed ")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_toast_msg')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_toast_msg')

    # This method is used to bookmark a question from test screen and to store the question in question
    def bookmark_qn_from_test(self, browser):
        try:
            self.navigate_to_test(browser)
            if CommonMethods.isElementPresent(browser, self.test_start_button):
                self.chapter_name = CommonMethods.getAttributeOfElement(browser, 'text', self.subtitle1_text)
                CommonMethods.elementClick(browser, self.test_start_button)
            if CommonMethods.isElementPresent(browser, self.submitbtn):
                self.book_mark_a_question(browser)
                self.submit_test(browser)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'bookmark_qn_from_test')

        except:
            CommonMethods.exception(browser, featureFileName, 'bookmark_qn_from_test')

        # This method is used to navigate to bookmrak home screen

    def navigate_to_book_mark_screen(self, browser):
        try:
            CommonMethods.isElementPresent(browser, self.analytics_icon)
            CommonMethods.elementClick(browser, self.hamburger_id)
            CommonMethods.wait_for_locator(browser, self.bookmark_ham_id, 10)
            CommonMethods.elementClick(browser, self.bookmark_ham_id)
            logging.info('User tapped on Bookmark option in Hamburger menu')
            self.verify_bookmark_homescreen(browser)

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'navigate_to_book_mark_screen')

        except:
            CommonMethods.exception(browser, featureFileName, 'navigate_to_book_mark_screen')

    # This method is used to verify bookmark home screen
    def verify_bookmark_homescreen(self, browser):
        try:
            filter_btn = (By.XPATH, "//android.widget.Button[@text='Filter']")
            CommonMethods.wait_for_locator(browser, filter_btn, 10)
            if CommonMethods.findText(browser, 'Bookmarks'):
                logging.info('User is in Bookmark home screen')
            else:
                logging.error('Failed to navigate to bookmark home screen')
                pytest.fail('Failed in method navigate_to_book_mark_screen')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_bookmark_homescreen')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_bookmark_homescreen')

    # This method is used to verify bookmarked question and the question in bookmark home screen
    def verify_question(self, browser):
        try:
            CommonMethods.isElementPresent(browser, self.question_title)
            question1 = CommonMethods.getAttributeOfElement(browser, 'text', self.question_title)
            question2 = question1.split(" ", 1)
            if question2[1] == self.question:
                logging.info('Question matched')
            else:
                text_to_search = re.compile(r'MCQ|FIB|MSQ')
                found_text = text_to_search.search(question1)
                if found_text:
                    question_type = found_text.group()
                    logging.info('found question type ' + question_type)
                    question3 = question1.split(" ", 4)
                    if question3[4] == self.question:
                        logging.info('Question matched')
                else:
                    question = "r'" + self.question
                    text_to_search = re.compile(question)
                    found_text = text_to_search.search(question1)
                    if found_text:
                        logging.info(found_text.group())
                        if found_text.group() == self.question:
                            logging.info('Question matched')
                        else:
                            logging.error('Failed to match question')
                            pytest.fail('Question mismatch')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_question')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_question')

    # This method is used verify subject and concept name in bookmark home screen
    def verify_subject_and_chapter_name(self, browser, subject):
        try:
            sub_con = CommonMethods.getAttributeOfElement(browser, 'text', self.subject_chapter)
            sub_con1 = sub_con.split("|")
            subject1 = sub_con1[0].rstrip()
            chapter = sub_con1[1].strip()
            logging.info(chapter)
            logging.info(self.chapter_name)
            if subject1 == subject and self.chapter_name == chapter:
                logging.info('Chapter name and subject name are verified')
            else:
                logging.error('Failed to verify Chapter name and subject name')
                pytest.fail('Failed in method verify_subject_and_concept_name')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_subject_and_concept_name')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_subject_and_concept_name')

    # This method is used to verify bookmark icon on bookmark home screen
    def is_bookmark_icon_shown(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.bookmark_tag)
            if check == True:
                logging.info('The bookmark icon is shown in test screen')
            else:
                pytest.fail('Book mark icon is not shown')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'is_bookmark_icon_shown')

        except:
            CommonMethods.exception(browser, featureFileName, 'is_bookmark_icon_shown')

    # This method is used to remove bookmark in bookmarkhome screen
    def remove_bookmark_inbookmark_scn(self, browser):
        try:
            CommonMethods.wait_for_locator(browser, self.bookmark_tag, 10)
            CommonMethods.elementClick(browser, self.bookmark_tag)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'remove_bookmark_inbookmark_scn')

        except:
            CommonMethods.exception(browser, featureFileName, 'remove_bookmark_inbookmark_scn')

    # This method is used to verify removed instruction in test instruction screen
    def istruction_notfound(self, browser, text):
        try:
            CommonMethods.wait_for_locator(browser, self.test_start_button, 20)
            if self.find_content_desc_text(browser, text) == False:
                logging.info('Instruction not found')
            else:
                logging.error('Instruction should be removed')
                pytest.fail('Failed in method istruction_notfound')
        except:
            CommonMethods.exception(browser, featureFileName, 'istruction_notfound')

        # This method is used to verify instruction in test instruction screen

    def istruction_found(self, browser, text):
        try:
            CommonMethods.wait_for_locator(browser, self.test_start_button, 20)
            if self.find_content_desc_text(browser, text):
                logging.info('Instruction found')
            else:
                logging.error('Instruction should be added')
                pytest.fail('Failed in method istruction_found')
        except:
            CommonMethods.exception(browser, featureFileName, 'istruction_found')

    # This method is used to navigate to test question screen
    def navigate_to_test_screen(self, browser):
        try:
            CommonMethods.wait_for_locator(browser, self.test_start_button, 10)
            CommonMethods.elementClick(browser, self.test_start_button)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'navigate_to_test_screen')

        except:
            CommonMethods.exception(browser, featureFileName, 'navigate_to_test_screen')

    # This method is used to verify bookmark icon on test question screen
    def verify_bookmark_icon_ontestscreen(self, browser):
        try:
            if CommonMethods.isElementPresent(browser, self.bookmark_id):
                logging.info('Book mark icon verified in test screen')
            else:
                logging.error('Failed to verify bookmark icon in test screen')
                pytest.fail('Failed in method verify_bookmark_icon_intestscreen')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'book_mark_a_question')

        except:
            CommonMethods.exception(browser, featureFileName, 'book_mark_a_question')

        # This method is used to bookmark question in test screen

    def book_mark_a_question(self, browser):
        try:
            CommonMethods.wait_for_locator(browser, self.bookmark_id, 5)
            CommonMethods.elementClick(browser, self.bookmark_id)
            sleep(2)
            self.toast_message = CommonMethods.getTextOfElement(browser, self.toast_msg)
            if self.toast_message == 'Bookmarked':
                logging.info('Question bookmarked')
            else:
                CommonMethods.elementClick(browser, self.bookmark_id)
                self.toast_message = CommonMethods.getTextOfElement(browser, self.toast_msg)
            self.question = self.get_question(browser)
        #             BookMarkQuestionScreen.bookmark_icon_color = self.get_the_rgb_lst(browser, self.bookmark_id)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'book_mark_a_question')

        except:
            CommonMethods.exception(browser, featureFileName, 'book_mark_a_question')

        # This method is used remove bookmark question in test screen

    def remove_book_mark_in_qn_screen(self, browser):
        try:
            CommonMethods.wait_for_locator(browser, self.bookmark_id, 5)
            CommonMethods.elementClick(browser, self.bookmark_id)
            sleep(2)
            self.toast_message = CommonMethods.getTextOfElement(browser, self.toast_msg)
            if self.toast_message == 'Bookmark Removed':
                logging.info('Bookmark Removed')
            else:
                CommonMethods.elementClick(browser, self.bookmark_id)
                self.toast_message = CommonMethods.getTextOfElement(browser, self.toast_msg)

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'remove_book_mark_in_qn_screen')

        except:
            CommonMethods.exception(browser, featureFileName, 'remove_book_mark_in_qn_screen')

        # this method is used to scroll till Chemistry

    def scroll_horizontal(self, browser, subject):
        try:
            if CommonMethods.scrollToElementAndClick(browser, subject):
                logging.info('Scrolled to subject ' + subject)
            else:
                pytest.fail('Failed to scroll till ' + subject)

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'scroll_horizontal')

        except:
            CommonMethods.exception(browser, featureFileName, 'scroll_horizontal')

    # This method is used for aborting the test
    def quit_inbtween(self, browser):
        try:
            CommonMethods.click_on_device_back_btn(browser)
            CommonMethods.wait_for_locator(browser, self.secondaryActionBtn, 5)
            CommonMethods.elementClick(browser, self.secondaryActionBtn)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'quit_inbtween')

        except:
            CommonMethods.exception(browser, featureFileName, 'quit_inbtween')

        # This method is used for submitting the test

    def submit_test(self, browser):
        try:
            CommonMethods.elementClick(browser, self.submitbtn)
            CommonMethods.wait_for_locator(browser, self.primaryActionBtn, 5)
            CommonMethods.elementClick(browser, self.primaryActionBtn)
            if CommonMethods.isElementPresent(browser, self.badge):
                CommonMethods.elementClick(browser, self.closeBtn)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'submit_test')

        except:
            CommonMethods.exception(browser, featureFileName, 'submit_test')

        # This method is used to verify question is removed from bookmark home screen

    def question_not_found(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.question_title)
            if check == False:
                logging.info('Question not found')
            else:
                question1 = CommonMethods.getAttributeOfElement(browser, 'text', self.question_title)
                question2 = question1.split(" ", 1)
                if question2[1] != self.question:
                    logging.info('Question not found')
                else:
                    text_to_search = re.compile(r'MCQ|FIB|MSQ')
                    found_text = text_to_search.search(question1)
                    if found_text:
                        question_type = found_text.group()
                        logging.info('found question type ' + question_type)
                        question3 = question1.split(" ", 4)
                        if question3[4] != self.question:
                            logging.info('Question not found')
                    else:
                        question = "r'" + self.question
                        text_to_search = re.compile(question)
                        found_text = text_to_search.search(question1)
                        if found_text:
                            logging.info(found_text.group())
                            if found_text.group() != self.question:
                                logging.info('Question not found')
                            else:
                                logging.error('Question found')
                                pytest.fail('Removed question found')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_question')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_question')

        # This method is used to tap on any option

    def tap_on_option(self, browser, locator, text):
        try:
            CommonMethods.wait_for_locator(browser, locator, 15)
            if CommonMethods.isElementPresent(browser, locator):
                CommonMethods.elementClick(browser, locator)
                logging.info('User tapped on ' + text + ' option')
            else:
                logging.error('Failed to tap on ' + text + ' option')
                pytest.fail('Failed to tap on expected option')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'tap_on_view_solutions')

        except:
            CommonMethods.exception(browser, featureFileName, 'tap_on_view_solutions')

    def tap_on_view_solutions(self, browser):
        self.tap_on_option(browser, self.view_solutions, '"View Solution"')

    def tap_on_filter_icon(self, browser):
        try:
            if CommonMethods.isElementPresent(browser, self.filter):
                CommonMethods.elementClick(browser, self.filter)
            elif CommonMethods.isElementPresent(browser, self.filter_icon):
                CommonMethods.elementClick(browser, self.filter_icon)
            else:
                pytest.fail('Failed to tap on filter icon')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'tap_on_filter_icon')

        except:
            CommonMethods.exception(browser, featureFileName, 'tap_on_filter_icon')

    def tap_on_Bookmarked_option(self, browser):
        self.tap_on_option(browser, self.Bookmarked_filter, '"Bookmarked"')
        sleep(2)

    # This method is used verify bookmarked question and question on solution screen
    def verify_qn_on_solutionscreen(self, browser):
        title = CommonMethods.getAttributeOfElement(browser, 'text', self.title)
        if title == 'Bookmarked':
            sol_question = self.get_question(browser)
            if self.question == sol_question:
                logging.info('Question verified in solution screen')
            else:
                pytest.fail('Failed to find the book marked question')
        else:
            pytest.fail('Failed in method verify_qn_on_solutionscreen')

    # This method is used to navigate to question screen
    def navigate_to_practice_qn_scn(self, browser):
        try:
            CommonMethods.isElementPresent(browser, self.practicebtn)
            CommonMethods.elementClick(browser, self.practicebtn)
            if CommonMethods.isElementPresent(browser, self.start_practice):
                self.chapter_name = CommonMethods.getAttributeOfElement(browser, 'text', self.header_title_text)
                CommonMethods.elementClick(browser, self.start_practice)
                if CommonMethods.isElementPresent(browser, self.primaryActionBtn):
                    CommonMethods.elementClick(browser, self.primaryActionBtn)
                logging.info('User is in practice question screen')
            else:
                logging.error('Failed to navigate to practice question screen')
                pytest.fail('Failed to navigate to practice')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'navigate_to_practice_qn_scn')

        except:
            CommonMethods.exception(browser, featureFileName, 'navigate_to_practice_qn_scn')

    # This method is used to bookmark in practice question screen
    def bookmark_practice_qn(self, browser):
        try:
            CommonMethods.wait_for_locator(browser, self.practice_bookmark, 30)
            CommonMethods.elementClick(browser, self.practice_bookmark)
            sleep(2)
            #             CommonMethods.wait_for_locator(browser, self.toast_msg, 5)
            self.toast_message = CommonMethods.getTextOfElement(browser, self.toast_msg)
            if self.toast_message == 'Bookmarked':
                logging.info('Question bookmarked')
            else:
                CommonMethods.elementClick(browser, self.practice_bookmark)
                self.toast_message = CommonMethods.getTextOfElement(browser, self.toast_msg)
            self.question = self.get_question(browser)
        #             BookMarkQuestionScreen.bookmark_icon_color = self.get_the_rgb_lst(browser, self.practice_bookmark)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'book_mark_a_question')

        except:
            CommonMethods.exception(browser, featureFileName, 'book_mark_a_question')

        # This method is used to remove bookmark in practice question screen

    def remove_book_mark_in_practiceqn_screen(self, browser):
        try:
            CommonMethods.wait_for_locator(browser, self.practice_bookmark, 30)
            CommonMethods.elementClick(browser, self.practice_bookmark)
            sleep(2)
            self.toast_message = CommonMethods.getTextOfElement(browser, self.toast_msg)
            if self.toast_message == 'Bookmark Removed':
                logging.info('Bookmark Removed')
            else:
                CommonMethods.elementClick(browser, self.practice_bookmark)
                self.toast_message = CommonMethods.getTextOfElement(browser, self.toast_msg)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'remove_book_mark_in_qn_screen')

        except:
            CommonMethods.exception(browser, featureFileName, 'remove_book_mark_in_qn_screen')

    # This method is used to tap on question on bookmark screen
    def tap_on_qn_in_bookmark_scn(self, browser):
        try:
            CommonMethods.wait_for_locator(browser, self.question_title, 5)
            if CommonMethods.elementClick(browser, self.question_title):
                logging.info('User tapped on question in bookmark screen')
            else:
                pytest.fail('Failed to click on question in bookmark screen')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'ap_on_qn_in_bookmark_scn')

        except:
            CommonMethods.exception(browser, featureFileName, 'ap_on_qn_in_bookmark_scn')

    # This method is used to verify user is on bookmark screen
    def verify_bookmark_qn_screen(self, browser):
        try:
            if CommonMethods.isElementPresent(browser, self.concept_name_id):
                logging.info('User is in bookmark question screen')
            else:
                logging.error('User is not in bookmark question screen')
                pytest.fail('Failed in method verify_bookmark_qn_screen')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_bookmark_qn_screen')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_bookmark_qn_screen')

    # This method is used to verify elements on screen
    def verify_elements_on_screen(self, browser, locator, text):
        try:
            check = CommonMethods.isElementPresent(browser, locator)
            if check == True:
                logging.info(text + ' is/are verified on the screen')

            else:
                logging.error('Failed to verify the ' + text)
                pytest.fail('Searching element ' + text + ' is not found')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_elements_on_screen')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_elements_on_screen')

    def verify_app_back_button(self, browser):
        self.verify_elements_on_screen(browser, self.app_back, 'App back button')

    def verify_share_icon(self, browser):
        self.verify_elements_on_screen(browser, self.share_icon, 'Share icon')

    def verify_Bookmark_icon(self, browser):
        self.verify_elements_on_screen(browser, self.bookmark_icon, 'Bookmark icon')

    def verify_chapter_label(self, browser):
        self.verify_elements_on_screen(browser, self.concept_name_id, 'Chapter label')

    # This method used to verify bookmarked question, solution and option on bookmark question screen
    def verify_qn_and_solution(self, browser):
        self.verify_elements_on_screen(browser, self.questionId, 'Question')
        if CommonMethods.isElementPresent(browser, self.option_a):
            logging.info('Qusetion options are displayed')
        else:
            CommonMethods.isElementPresent(browser, self.solution)
            CommonMethods.isElementPresent(browser, self.CorrectAnswer)
            logging.info('Solution and correct answer are displayed displayed')

    # This method used to tap on device back button
    def tap_device_backbtn(self, browser):
        try:
            CommonMethods.click_on_device_back_btn(browser)
            logging.info('User tapped on back button')
        except:
            logging.error('Failed tap on device back button')
            pytest.fail('Failed in method tap_device_backbtn')

    # This method used to tap on App back button
    def app_backbtn(self, browser):
        try:
            CommonMethods.wait_for_locator(browser, self.app_back, 10)
            CommonMethods.elementClick(browser, self.app_back)

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'app_backbtn')

        except:
            CommonMethods.exception(browser, featureFileName, 'app_backbtn')
            logging.error('Failed to click on app_back button')

    # This method is used to remove bookmark in Bookmark question screen
    def remove_bookmark_in_qnscn(self, browser):
        try:
            CommonMethods.wait_for_locator(browser, self.bookmark_icon, 10)
            CommonMethods.elementClick(browser, self.bookmark_icon)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'remove_bookmark_in_qnscn')

        except:
            CommonMethods.exception(browser, featureFileName, 'remove_bookmark_in_qnscn')

    # This method will fetch a question and returns question
    def get_question(self, browser):
        try:
            practice_question = (By.XPATH, "//android.view.View[@resource-id='q']/android.view.View/android.view.View")
            test_question = (By.XPATH,
                             "//androidx.viewpager.widget.ViewPager//android.view.View[@resource-id='q']/android.view.View[@index=0]")
            count = 0
            elements = []
            elements = browser.find_elements_by_xpath("//android.view.View")
            if CommonMethods.isElementPresent(browser, test_question):
                question = CommonMethods.getAttributeOfElement(browser, 'text', test_question)
                return question
            elif CommonMethods.isElementPresent(browser, practice_question):
                question = CommonMethods.getAttributeOfElement(browser, 'text', practice_question)
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

        except IndexError:
            while True:
                question = elements[count].get_attribute('text')
                if question == None or question == '':
                    count = count + 1
                else:
                    break
            logging.info('Found Question is "' + question + '"')
            return question

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'get_question')

        except:
            CommonMethods.exception(browser, featureFileName, 'get_question')

    # This method is used to verify UNDO snackbar action button
    def verify_snackbar_action_button(self, browser, text):
        try:
            check = CommonMethods.isElementPresent(browser, self.snackbar_action)
            if check == True:
                act_text = CommonMethods.getAttributeOfElement(browser, 'text', self.snackbar_action)
                ('Found snackbar action button ' + act_text)
                CommonMethods.verifyTextMatch(act_text, text)
            else:
                logging.error('Failed to find snackbar action button')
                pytest.fail("Failed to verify snackbar action button")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_snackbar_action_button')

        except:
            CommonMethods.exception(browser, featureFileName, 'verify_snackbar_action_button')

    # This method is used to verify snackbar msg
    def verify_snackbar_msg(self, browser, text):
        try:
            check = CommonMethods.isElementPresent(browser, self.snackbar_text)
            if check == True:
                act_txt = CommonMethods.getTextOfElement(browser, self.snackbar_text)
                logging.info('Found snackbar text ' + act_txt)
                exp_txt = text
                assert act_txt == exp_txt, "Snackbar message is not matching"
            else:
                logging.info("Snackbar message verification failed ")
                pytest.fail("Snackbar message verification failed ")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_snackbar_msg')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_snackbar_msg')

    # This method is used to tap on undo option
    def tap_on_undo_option(self, browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.snackbar_action)
            if check == True:
                CommonMethods.elementClick(browser, self.snackbar_action)
            else:
                logging.error('Failed to click on Undo option')
                pytest.fail('Failed in method tap_on_undo_option')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'tap_on_undo_option')
        except:
            CommonMethods.exception(browser, featureFileName, 'tap_on_undo_option')

    def rgb2hex(self, rgb):
        return '#%02x%02x%02x' % rgb

    def get_the_rgb_lst(self, browser, locator):
        try:
            s1 = set()
            CommonMethods.wait_for_element_visible(browser, locator, 10)
            element1 = CommonMethods.getElement(browser, locator)
            location = element1.location
            size = element1.size
            png = browser.get_screenshot_as_png()
            img = Image.open(BytesIO(png))
            left = location['x']
            top = location['y']
            right = location['x'] + size['width']
            bottom = location['y'] + size['height']
            im = img.crop((left, top, right, bottom))
            pix_val1 = list(dict.fromkeys(list(im.getdata())))
            for i in range(len(pix_val1)):
                rgb = list(pix_val1[i])
                rgb.pop(3)
                tup = tuple(rgb)
                result = self.rgb2hex(tup)
                s1.add(result)
            logging.info(s1)
            return s1
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'get_the_rgb_lst')

        except:
            CommonMethods.exception(browser, featureFileName, 'get_the_rgb_lst')

    def verify_subject_chapter_color(self, first, secound, count):
        result = first & secound
        if len(result) >= count:
            logging.info("both have same color")
        else:
            logging.info("both color not matching")

    def verify_bookmarkicon_with_subject_theme_color(self, browser):
        self.verify_subject_chapter_color(BookMarkQuestionScreen.subject_color,
                                          BookMarkQuestionScreen.bookmark_icon_color, 5)

        # This method is used to find text from data 'content-desc'

    def find_content_desc_text(self, browser, text):
        check = False
        locator = (By.XPATH, "//android.view.View")
        CommonMethods.wait_for_locator(browser, locator, 10)
        classlist1 = CommonMethods.getElements(browser, locator)
        for i in range(len(classlist1)):
            text2 = classlist1[i].get_attribute('text')
            if text2 == text:
                check = True
            elif str(text) in str(text2):
                check = True
            else:
                if CommonMethods.findText(browser, text):
                    check = True

        return check
