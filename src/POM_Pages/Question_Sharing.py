import time
from appium.webdriver.common.touch_action import TouchAction
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
import random
import re



CommonMethods = CommonMethods()
data_file = CONFIG_PATH

featureFileName = 'Question Sharing'

class QuestionSharing():
    
    def __init__(self, browser):
        self.browser = browser
        
        
    hamburger_id = (By.ID, "com.byjus.thelearningapp:id/backNav")
    bookmark_ham_id=(By.XPATH,"//android.widget.TextView[@text ='Bookmarks']")
    bookmark_id=(By.ID, "com.byjus.thelearningapp:id/ivBookmark")
    question_title= (By.ID, "com.byjus.thelearningapp:id/tvTitle")
    subject_chapter=(By.ID,"com.byjus.thelearningapp:id/tvSubject")
    bookmark_tag=(By.ID,"com.byjus.thelearningapp:id/ivBookmarkTag")   
    filter_id=(By.XPATH,"//android.widget.Button[@text ='Filter']")
    app_back=(By.ID,"com.byjus.thelearningapp:id/roundedNavButton")
    practice_bookmark=(By.ID,"com.byjus.thelearningapp:id/ivBookmarkButton")
    concept_name_id=(By.ID,"com.byjus.thelearningapp:id/conceptName")
    share_icon=(By.ID,"com.byjus.thelearningapp:id/ivShare")
    bookmark_icon=(By.ID,"com.byjus.thelearningapp:id/bookmark")               
    toast_msg= (By.XPATH, "//android.widget.Toast")
    android_title=(By.ID,"android:id/title")
    text_view= (By.XPATH, "//android.widget.TextView")
    share_resolver_list=(By.ID,"android:id/resolver_list")
    bottom_sheet_dialog=(By.ID,"com.byjus.thelearningapp:id/design_bottom_sheet")
    title=(By.ID,"com.byjus.thelearningapp:id/title")
    snackbar_action=(By.ID,"com.byjus.thelearningapp:id/snackbar_action")
    snackbar_text =(By.ID,"com.byjus.thelearningapp:id/snackbar_text")
    filter= (By.ID,"com.byjus.thelearningapp:id/rightNav")
    
    allowbutton =(By.ID,"com.android.packageinstaller:id/permission_allow_button")
    denybutton = (By.ID,"com.android.packageinstaller:id/permission_deny_button")
    skipButton = (By.ID,"com.byjus.thelearningapp:id/buttonSkip")
    grade8th =(By.XPATH,"//android.widget.Button[@text ='8th']")
    gms_cancel=(By.ID,"com.google.android.gms:id/cancel")
    btnRegister =(By.ID, "com.byjus.thelearningapp:id/btnRegister")
    regscn_lgnbtn=(By.ID,"com.byjus.thelearningapp:id/tvLoginBl")
    country_Code = (By.ID,"com.byjus.thelearningapp:id/spnrCountry")
    phone_num = (By.ID,"com.byjus.thelearningapp:id/etPhoneNumber")
    OtpTxtBx_id = (By.ID,"com.byjus.thelearningapp:id/etOTP")
    badge=(By.ID,"com.byjus.thelearningapp:id/lvBadgeEarnlottieAnim")
    closeBtn=(By.ID,"com.byjus.thelearningapp:id/ivCloseBtn")
    loginBtn_id =(By.ID,"com.byjus.thelearningapp:id/btnLogin")
    analytics_icon=(By.ID,"com.byjus.thelearningapp:id/home_analytics")
    personalizeScreen_xpath = (By.XPATH,"//android.widget.Button[@text='Personalised']")
    librayBtn_id=(By.XPATH,"//android.widget.Button[@text='Library']")
    profile_header_id = (By.ID,"com.byjus.thelearningapp:id/llHeaderTextParent")
    ibrayBtn_id = (By.ID,"com.byjus.thelearningapp:id/optionalNav")
    testbtn=(By.ID, "com.byjus.thelearningapp:id/chapter_list_item_test_txtvw")
    practicebtn=(By.ID,"com.byjus.thelearningapp:id/practice_mode_bottom_txtvw")
    start_btn=(By.XPATH,"//android.widget.TextView[@text='Start']" )
    test_start_button=(By.ID,"com.byjus.thelearningapp:id/test_start_button")
    submitbtn=(By.ID,"com.byjus.thelearningapp:id/rectangleNavButton")
    questionId=(By.XPATH, "//android.view.View[@index='0']")
    retake_test=(By.ID,"com.byjus.thelearningapp:id/retake_test")
    toggle_btn=(By.ID,"com.byjus.thelearningapp:id/optionalNav2")
    secondaryActionBtn =(By.ID,"com.byjus.thelearningapp:id/secondaryAction")
    primaryActionBtn=(By.ID,"com.byjus.thelearningapp:id/primaryAction")
    header_title_text =(By.ID,"com.byjus.thelearningapp:id/header_title_text")
    subtitle1_text=(By.ID,"com.byjus.thelearningapp:id/header_subtitle1_text")
    filter_icon =(By.XPATH, "//android.widget.FrameLayout[@index='2']")
    Bookmarked_filter=(By.XPATH,"//android.widget.TextView[@text ='Bookmarked']")
    start_practice= (By.ID,"com.byjus.thelearningapp:id/tvStartPractice")
    gmail_to=(By.ID,"com.google.android.gm:id/to")
    gmail_subject=(By.ID,"com.google.android.gm:id/subject")
    gmail_subject_content=(By.ID,"com.google.android.gm:id/subject_content")
    gmail_body=(By.XPATH,"//android.view.View[@index='0']")
    gmail_attachment=(By.ID,"com.google.android.gm:id/attachment_tile_subtitle")
    gmail_send=(By.ID,"com.google.android.gm:id/send")
    dialogBox_title =(By.ID,"com.byjus.thelearningapp:id/dialog_title")
    dialogBox_msg=(By.ID,"com.byjus.thelearningapp:id/dialog_message")
    dialogBox_image=(By.ID,"com.byjus.thelearningapp:id/dialog_image")
    whatsapp_contact_name=(By.ID,"com.whatsapp:id/contactpicker_row_name")
    whatsapp_send=(By.ID,"com.whatsapp:id/send")
    whatsapp_photo=(By.ID,"com.whatsapp:id/photo")
    whatsapp_content=(By.XPATH,"//*[contains(@content-desc, 'Check out this question')]")
    message_image_content=(By.ID,"com.android.mms:id/image_content")
    text_editor=(By.ID,"com.android.mms:id/embedded_text_editor")
    message_text=(By.ID,"com.google.android.apps.messaging:id/compose_message_text")
    question_xpath=(By.XPATH,"//*[contains(@text, 'Q. ')]")
    chapter_list_title=(By.ID,"com.byjus.thelearningapp:id/chapterlistTitle")
    homescreen_corana_dialog_ok_btn = (By.ID,"com.byjus.thelearningapp:id/tv_secondaryAction")
    homescreen_corana_dialog = (By.ID,"com.byjus.thelearningapp:id/dialog_layout")
    free_live_classes=(By.XPATH,"//android.view.View[@content-desc='Free Live Classes']")
    count =0
  


    

#This method is used to navigate to home screen         
    def navigate_to_home_screen(self, browser):
        try:
            if self.verify_home_screen(browser):
                pass
            else:
                if CommonMethods.isElementPresent(browser, self.allowbutton):
                    CommonMethods.elementClick(browser, self.allowbutton)
                    CommonMethods.elementClick(browser, self.allowbutton)
                if CommonMethods.isElementPresent(browser,self.skipButton):
                    CommonMethods.elementClick(browser, self.skipButton)
                if CommonMethods.isElementPresent(browser,self.grade8th):
                    CommonMethods.elementClick(browser, self.grade8th)
                    if CommonMethods.isElementPresent(browser, self.gms_cancel):
                        CommonMethods.elementClick(browser,self.gms_cancel)                 
                if CommonMethods.isElementPresent(browser,self.btnRegister):
                    CommonMethods.elementClick(browser,self.regscn_lgnbtn)
                    if CommonMethods.isElementPresent(browser, self.gms_cancel):
                        CommonMethods.elementClick(browser,self.gms_cancel)
                if CommonMethods.isElementPresent(browser, self.loginBtn_id):
                    CommonMethods.wait_for_locator(browser,self.country_Code,15)
                    CommonMethods.elementClick(browser,self.country_Code)
                    sleep(2)
                    CommonMethods.scrollToElementAndClick(browser,getdata(Login_Credentials,'login_detail4'
                                                                          , 'country_code'))
                    CommonMethods.enterText(browser,getdata(Login_Credentials,'login_detail4','mobile_no'),self.phone_num)
                    CommonMethods.wait_for_locator(browser,self.loginBtn_id,10)
                    CommonMethods.elementClick(browser,self.loginBtn_id)
                    CommonMethods.wait_for_locator(browser,self.OtpTxtBx_id,15)
                    CommonMethods.enterText(browser, getdata(Login_Credentials,'login_detail4','OTP'), self.OtpTxtBx_id)
                    sleep(10)
                self.verify_home_screen(browser)

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'navigate_to_home_screen')
                
        except:
            CommonMethods.exception(browser, featureFileName, 'navigate_to_home_screen')
    
    
    def verify_home_screen(self,browser):
        try:
            aerr_close=(By.ID,"android:id/aerr_close")
            if CommonMethods.isElementPresent(browser, aerr_close):
                CommonMethods.elementClick(browser, aerr_close)
            if CommonMethods.wait_for_element_visible(browser, self.homescreen_corana_dialog, 10):
                CommonMethods.elementClick(browser, self.homescreen_corana_dialog_ok_btn)
#             if CommonMethods.isElementPresent(browser, self.free_live_classes):
#                 CommonMethods.click_on_device_back_btn(browser)
            if CommonMethods.isElementPresent(browser,self.badge):
                    CommonMethods.elementClick(browser,self.closeBtn)
            if CommonMethods.isElementPresent(browser, self.analytics_icon):
                logging.info('User is in Home screen')
                return True
            else:
                return False
                
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_home_screen')
                
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_home_screen')
            
            
#This method is used to navigate to Library chapter list screen            
    def navigate_to_library(self, browser):
        try:
            subject_list = ["Mathematics", "Biology", "Physics","Chemistry"]
            sub=random.choice(subject_list)
            CommonMethods.wait_for_element_visible(browser, self.profile_header_id, 10)
            pythonSub_xpath =(By.XPATH,"//android.widget.TextView[@text=\'"+sub+"\']")
#             BookMarkQuestionScreen.subject_color=self.get_the_rgb_lst(browser,pythonSub_xpath)
            CommonMethods.wait_for_element_visible(browser, pythonSub_xpath, 3)
            CommonMethods.elementClick(browser,pythonSub_xpath)
            if CommonMethods.isElementPresent(browser, self.personalizeScreen_xpath):
                pass
            elif CommonMethods.isElementPresent(browser, self.chapter_list_title):
                pass
            elif CommonMethods.isElementPresent(browser,self.librayBtn_id):
                CommonMethods.elementClick(browser,self.librayBtn_id)
            
            elif CommonMethods.isElementPresent(browser,self.toggle_btn1):
                CommonMethods.elementClick(browser,self.toggle_btn1)
                if CommonMethods.isElementPresent(browser, self.personalizeScreen_xpath):
                    pass
                else:
                    CommonMethods.elementClick(browser,self.librayBtn_id)
            elif CommonMethods.isElementPresent(browser,self.toggle_btn):
                CommonMethods.elementClick(browser,self.toggle_btn)
                if CommonMethods.isElementPresent(browser, self.personalizeScreen_xpath):
                    pass
                else:
                    CommonMethods.elementClick(browser,self.librayBtn_id)
            else:
                pytest.fail('Failed in method navigate to library')
        
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'navigate_to_library')
                  
        except:
            CommonMethods.exception(browser, featureFileName, 'navigate_to_library')
            
#This method is used to navigate to Home screen from any other screen           
    def navigate_back_home_screen(self,browser):
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
#This method is used to navigate to bookmrak home screen   
    def navigate_to_book_mark_screen(self,browser):
        try:
            CommonMethods.isElementPresent(browser, self.analytics_icon)
            CommonMethods.elementClick(browser,self.hamburger_id)
            CommonMethods.wait_for_locator(browser, self.bookmark_ham_id, 5)
            CommonMethods.elementClick(browser,self.bookmark_ham_id)
            logging.info('User tapped on Bookmark option in Hamburger menu')
            self.verify_bookmark_homescreen(browser)
              
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'navigate_to_book_mark_screen')
                
        except:
            CommonMethods.exception(browser, featureFileName, 'navigate_to_book_mark_screen')            
            
        
                 
#This method is used to navigate to test instruction screen
    def bookmark_a_question_from_test(self,browser):
        try:
            CommonMethods.wait_for_locator(browser, self.testbtn, 10)
            CommonMethods.elementClick(browser,self.testbtn)
            if CommonMethods.isElementPresent(browser,self.start_btn):
                CommonMethods.elementClick(browser,self.start_btn)
            else:
                CommonMethods.elementClick(browser,self.retake_test)
            CommonMethods.wait_for_locator(browser, self.test_start_button,10)
            CommonMethods.elementClick(browser,self.test_start_button)
            CommonMethods.wait_for_locator(browser, self.bookmark_id,10)
            CommonMethods.elementClick(browser,self.bookmark_id)
            sleep(2)
            self.toast_message=CommonMethods.getTextOfElement(browser,self.toast_msg)
            if self.toast_message =='Bookmarked':
                logging.info('Question bookmarked')
            else:
                CommonMethods.elementClick(browser,self.bookmark_id)
            CommonMethods.click_on_device_back_btn(browser)
            sleep(2)
            CommonMethods.elementClick(browser, self.secondaryActionBtn)
              
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'bookmark_a_question_from_test')
                
        except:
            CommonMethods.exception(browser, featureFileName, 'bookmark_a_question_from_test')  



#This method is used to verify bookmark home screen    
    def verify_bookmark_homescreen(self,browser):
        try:
            sleep(2)
            title=CommonMethods.getAttributeOfElement(browser, 'text', self.header_title_text)
            if title =='Bookmarks':
                logging.info('User is in Bookmark home screen')
            else:
                logging.error('Failed to navigate to bookmark home screen')
                pytest.fail('Failed in method navigate_to_book_mark_screen')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_bookmark_homescreen')
                
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_bookmark_homescreen')

            
#This method is used to bookmark practice question    
    def bookmark_a_question_from_practice(self,browser):
        try:
            CommonMethods.wait_for_locator(browser, self.practicebtn,10)
            CommonMethods.elementClick(browser,self.practicebtn)
            if CommonMethods.isElementPresent(browser,self.start_practice):
                CommonMethods.elementClick(browser,self.start_practice)
                logging.info('User is in practice question screen')
                CommonMethods.elementClick(browser,self.start_practice)
                if CommonMethods.isElementPresent(browser, self.primaryActionBtn):
                    CommonMethods.elementClick(browser,self.primaryActionBtn)
            CommonMethods.wait_for_locator(browser, self.practice_bookmark,10)
            CommonMethods.elementClick(browser, self.practice_bookmark)
            sleep(2)
            self.toast_message=CommonMethods.getTextOfElement(browser,self.toast_msg)
            if self.toast_message=='Bookmarked':
                logging.info('Question bookmarked')
            else:
                CommonMethods.elementClick(browser, self.practice_bookmark)
            CommonMethods.click_on_device_back_btn(browser)
            sleep(2)
            CommonMethods.elementClick(browser, self.secondaryActionBtn)    

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'navigate_to_practice_qn_scn')
          
        except:
            CommonMethods.exception(browser,featureFileName,'navigate_to_practice_qn_scn')


#This method is used to make sure that question is bookmarked and is found in bookmark home screen
    def bookmarked_question_found_in_home_screen(self,browser):
        try:
            self.navigate_to_book_mark_screen(browser)
            sleep(2)
            if CommonMethods.isElementPresent(browser, self.question_xpath):
                logging.info('Question is found in bookmark home screen')
            else:
                self.navigate_back_home_screen(browser)
                self.navigate_to_library(browser)
                pick_one = ["Test", "Practice"]
                test_or_practice=random.choice(pick_one)
                logging.info('User will book mark a question from '+test_or_practice)
                if test_or_practice =="Test":
                    self.bookmark_a_question_from_test(browser)
                elif test_or_practice =="Practice":
                    self.bookmark_a_question_from_practice(browser) 
                else:
                    pytest.fail('Failed bookmark a question')
                self.navigate_back_home_screen(browser)
                self.navigate_to_book_mark_screen(browser)   
        
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'bookmarked_question_found_in_home_screen')
              
        except:
            CommonMethods.exception(browser,featureFileName,'bookmarked_question_found_in_home_screen')        
    
    
    #This method is used to navigate to bookmark question screen
    def navigate_to_bookmark_question_screen(self,browser):
        try:
            self.bookmarked_question_found_in_home_screen(browser)
            CommonMethods.wait_for_locator(browser,self.question_title, 5)
            CommonMethods.elementClick(browser, self.question_xpath)
            CommonMethods.wait_for_locator(browser,self.concept_name_id, 5)
            if CommonMethods.isElementPresent(browser, self.concept_name_id):
                logging.info('User navigated to question in bookmark screen')
            else:
                logging.error('User is not in bookmark question screen')
                pytest.fail('Failed in method navigate_to_bookmark_question_screen')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'navigate_to_bookmark_question_screen')

        except:
            CommonMethods.exception(browser,featureFileName,'navigate_to_bookmark_question_screen')       
    
    
    #This method is used to tap on share icon
    def tap_on_share_icon(self,browser):
        try:
            CommonMethods.wait_for_locator(browser, self.share_icon, 10)
            if CommonMethods.elementClick(browser, self.share_icon):
                self.count=self.count+1
#                 CommonMethods.wait_for_locator(browser, self.android_title, 10)
                logging.info('Tapped on share icon')
            else:
                logging.error('Failed to tap on share icon')
                pytest.fail('Failed in method tap_on_share_icon')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'tap_on_share_icon')

        except:
            CommonMethods.exception(browser,featureFileName,'tap_on_share_icon')
    
    
    #This method is used to verify "share with" bottom sheet dialog and list of sharing elements       
    def verify_share_with_popup_and_list(self,browser):
        try:
            if CommonMethods.isElementPresent(browser, self.android_title):
                actual_text=CommonMethods.getTextOfElement(browser, self.android_title)
                if actual_text=="Share with":
                    logging.info('Share with popup is shown')
                    if CommonMethods.isElementPresent(browser, self.share_resolver_list):
                        logging.info('sharing apps list is shown')
                    else:
                        logging.error('Failed to show sharing apps list')
                elif CommonMethods.isElementPresent(browser, self.bottom_sheet_dialog):
                    logging.error('User already shared 5 questions per day')
                    pytest.fail('Failed show Share with pop up due to share limit')
                else:
                    logging.error('Failed to display share with pop up')
                    pytest.fail('Failed in method verify_share_with_popup_and_list')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_share_with_popup_and_list')

        except:
            CommonMethods.exception(browser,featureFileName,'verify_share_with_popup_and_list')
    
    
    #This method is used to select sharing medium from share pop up
    def select_option_to_share(self,browser,option):
        try:
            CommonMethods.wait_for_locator(browser, self.android_title, 10)
            option_xpath =(By.XPATH,"//android.widget.TextView[@text=\'"+option+"\']")
            if CommonMethods.isElementPresent(browser, option_xpath):
                if CommonMethods.elementClick(browser, option_xpath):
                    logging.info('User tapped on '+option+ ' option')
                else:
                    logging.error('Failed to tap on '+option+ ' option')
                    pytest.fail('Failed in method select_option_to_share')
            else:
                logging.error(option+ ' option is not found in share popup')
            
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'select_option_to_share')

        except:
            CommonMethods.exception(browser,featureFileName,'select_option_to_share')
    
    
    #This method is used to enter_recipient mail id
    def enter_recipient_mail_id(self,browser,EmailId):
        try:
            CommonMethods.wait_for_locator(browser,self.gmail_to, 10)
            if CommonMethods.enterText(browser, EmailId,self.gmail_to):
                logging.info('Entered recipient mail id')
                CommonMethods.hideKeyboard(browser)
            else:
                logging.error('Failed to enter recipient mail id')
                pytest.fail('Failed in method enter_recipient_mail_id')
        
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'enter_recipient_mail_id')

        except:
            CommonMethods.exception(browser,featureFileName,'enter_recipient_mail_id')
    
    
    #This method is used to tap on gmail send option
    def tap_on_gmail_send_option(self,browser):
        try:
            if CommonMethods.elementClick(browser, self.gmail_send):
                logging.info('Tapped on send option in gmail')
            else:
                logging.error('Failed to tap on send option')
                pytest.fail('Failed in method tap_on_gmail_send_option')
        
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'tap_on_gmail_send_option')

        except:
            CommonMethods.exception(browser,featureFileName,'tap_on_gmail_send_option')
    
                
    #This method is used to verify toast message     
    def verify_toast_msg(self,browser,text):
        try:
            if CommonMethods.isElementPresent(browser, self.toast_msg):
                act_txt=CommonMethods.getTextOfElement(browser,self.toast_msg)
                if act_txt == text:
                    logging.info('Found toast message '+act_txt)
            else:
                pytest.fail("Toast text verification failed ")    
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_toast_msg')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_toast_msg')     
    
            
    #This method verify sending toast message of gmail
    def verify_mail_is_sent(self,browser):
            self.verify_toast_msg(browser,"Sending message...")
            
    
    #This method is used to verify user is in gmail compose mail screen
    def verify_gmail_compose_screen(self,browser):
        try:
            CommonMethods.wait_for_locator(browser, self.gmail_to, 10)
            if CommonMethods.isElementPresent(browser, self.gmail_send):
                logging.info('User is in gmail compose mail screen')
            else:
                logging.error('User is not in gmail compose screen')
                pytest.fail('Failed in method verify_gmail_compose_screen')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_gmail_compose_screen')
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_gmail_compose_screen') 
        
    #This method is used to verify the subject in compose mail screen
    def verify_subject_in_mailcompose_scn(self,browser,text):
        try:
            CommonMethods.wait_for_locator(browser, self.gmail_subject, 10)
            actual_text=CommonMethods.getAttributeOfElement(browser,'text', self.gmail_subject)
            if CommonMethods.verifyTwoText(actual_text,text):
                logging.info('Gmail subject is matched '+actual_text)
            else:
                logging.error('Gmail subject mismatch')
                pytest.fail('Failed in method verify_subject_in_mailcompose_scn ')
        
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_subject_in_mailcompose_scn')
        
        except: 
            CommonMethods.exception(browser, featureFileName, 'verify_subject_in_mailcompose_scn')
    
    
    #This method is used to verify text description and link in gmail        
    def verify_descriptiontext_and_link_in_a_mail(self,browser,text):
        try:
            link="https://app.byjus.com/staging_bookmark_question_share?referrer="
            actual_text=CommonMethods.getElement(browser,self.gmail_body).get_attribute('content-desc')
            if str(text) in str(actual_text):
                logging.info('Description text found in gmail body')
            else:
                logging.error('Description text mismatch')
                pytest.fail('Failed in method verify_body_text_in_a_mail')
            if str(link) in str(actual_text) :
                logging.info('Link to navigate to byjus app is found in the mail')
            else:
                logging.error('Failed to find the link')
                pytest.fail('Searching link is not found')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_body_text_in_a_mail')
        
        except: 
            CommonMethods.exception(browser, featureFileName, 'verify_body_text_in_a_mail')
    

    
    #This method is used to get share_limit_reached_btmsheet_dialog 
    def get_share_limit_reached_btmsheet_dialog(self,browser):
        try:
            self.tap_on_share_icon(browser)
            while True:
                if CommonMethods.isElementPresent(browser, self.bottom_sheet_dialog):
                    logging.info('bottom sheet dialog is shown')
                    if self.count>5:
                        logging.info('User tapped on share icon for '+str(self.count)+' times')
                    else:
                        logging.info('Bottom sheet dialog is shown before sharing five questions ')
                    break     
                else:
                    CommonMethods.click_on_device_back_btn(browser)
                    self.tap_on_share_icon(browser)
                    sleep(2)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'get_share_limit_reached_btmsheet_dialog')
        
        except: 
            CommonMethods.exception(browser, featureFileName, 'get_share_limit_reached_btmsheet_dialog')
    
    #This methpod is used to verify share limit bottom sheet dialog        
    def verify_bottom_sheet_dialog(self,browser,text):
        try: 
            check = CommonMethods.isElementPresent(browser, self.bottom_sheet_dialog)
            if check == True:
                logging.info('Bottom sheet dialog is shown')
                actual_text=CommonMethods.getTextOfElement(browser, self.dialogBox_title)
                CommonMethods.verifyTextMatch(actual_text, text)  
            else:
                logging.error('Failed to display bottom sheet dialog')
                pytest.fail('Bottom sheet dialog is not shown')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_bottom_sheet_dialog')
        
        except: 
            CommonMethods.exception(browser, featureFileName, 'verify_bottom_sheet_dialog')
        
#This method is used check the attachment in the mail
    def verify_attached_screenshot(self,browser):
        try:
            CommonMethods.hideKeyboard(browser)
            check = CommonMethods.isElementPresent(browser, self.gmail_attachment)
            if check == True:
                logging.info('Screensot is attached')
            else:
                logging.error('Attachment is not found')
                pytest.fail('Failed in method verify_attached_screenshot')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_attached_screenshot')
        
        except: 
            CommonMethods.exception(browser, featureFileName, 'verify_attached_screenshot')
               

    #This method is used to verify the button
    def verify_the_button(self,browser,text):
            try:
                if CommonMethods.findButton(browser, text):
                    logging.info('Found searching button "'+text+'"')
                else:
                    logging.error('Failed to find the button "'+text+'" in method verifythebutton')  
                    pytest.fail('Failed to find the button')
            
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(browser, featureFileName, 'verifythebutton')
                
            except:
                CommonMethods.exception(browser, featureFileName, 'verifythebutton')
    
    #This method is used to verify the text
    def verify_the_text(self,browser,text):
        try:
            actual_text=CommonMethods.getTextOfElement(browser,self.dialogBox_msg)
            if str(text) in str(actual_text):
                logging.info('Found searching text "'+text+'"')
                    
            else:
                logging.error('Failed to find the text "'+text+'" in method verifythetext')
                pytest.fail('Failed to find the text')
            
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verifythetext')
                
        except:
            CommonMethods.exception(browser, featureFileName, 'verifythetext')
    
    #This method is used verify hero image in bottom sheet dialog
    def verify_hero_image(self,browser):
        try:
            check=CommonMethods.isElementPresent(browser, self.dialogBox_image)
            if check == True:
                logging.info('Hero image is found')
            else:
                logging.error('Hero image not found')
                pytest.fail('Failed to verify hero image in bottom sheet dialog')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_hero_image')
                
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_hero_image')
    
         
         
#This method is used to verify the bottom sheet dialaog is dismissed             
    def bottom_sheet_dialog_dismissed(self,browser):
        try:
            CommonMethods.wait_for_element_visible(browser, self.share_icon, 10)
            check = CommonMethods.isElementPresent(browser, self.bottom_sheet_dialog)
            if check == False:
                logging.info('Bottom sheet dialog is not shown')
            else:
                logging.error('Bottom sheet dialog is showm')
                pytest.fail('Bottom sheet dialog is shown')
        
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'bottom_sheet_dialog_dismissed')
                    
        except:
            CommonMethods.exception(browser, featureFileName, 'bottom_sheet_dialog_dismissed')
            
#This method is used to tap on primary action button                     
    def tap_on_primaryActionBtn(self,browser):
        try:
            CommonMethods.elementClick(browser,self.primaryActionBtn)
             
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'tap_on_primaryActionBtn')    
 
        except:
            CommonMethods.exception(browser, featureFileName, 'tap_on_primaryActionBtn')

   
   
    def select_recipient_share_in_whatsapp(self,browser):
        try:
            CommonMethods.wait_for_locator(browser, self.whatsapp_contact_name, 10)
            CommonMethods.elementClick(browser, self.whatsapp_contact_name)
            CommonMethods.wait_for_locator(browser,self.whatsapp_send, 5)
            CommonMethods.elementClick(browser,self.whatsapp_send)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'tap_on_primaryActionBtn')    
 
        except:
            CommonMethods.exception(browser, featureFileName, 'tap_on_primaryActionBtn')
            
  
    
    def verify_descriptiontext_and_link_in_a_whatsapp(self,browser,text):
        try:
            link="https://app.byjus.com/staging_bookmark_question_share?referrer="
            actual_text=CommonMethods.getElement(browser,self.whatsapp_content).get_attribute('content-desc')
            if str(text) in str(actual_text):
                logging.info('Description text found in whats app message body')
            else:
                logging.error('Description text mismatch')
                pytest.fail('Failed in method verify_descriptiontext_and_link_in_a_whatsapp')
            if str(link) in str(actual_text) :
                logging.info('Link to navigate to byjus app is found in whats app')
            else:
                logging.error('Failed to find the link')
                pytest.fail('Searching link is not found')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_descriptiontext_and_link_in_a_whatsapp')
        
        except: 
            CommonMethods.exception(browser, featureFileName, 'verify_descriptiontext_and_link_in_a_whatsapp')
    
    def verify_attached_photo(self,browser):
        try:
            CommonMethods.hideKeyboard(browser)
            check = CommonMethods.isElementPresent(browser, self.whatsapp_photo)
            if check == True:
                logging.info('Screensot is attached in whats app')
            else:
                logging.error('Attachment is not found in whats app')
                pytest.fail('Failed in method verify_attached_screenshot')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_attached_photo')
        
        except: 
            CommonMethods.exception(browser, featureFileName, 'verify_attached_photo')
    
    def verify_attached_photo_sms(self,browser):
        try:
            CommonMethods.hideKeyboard(browser)
            check = CommonMethods.isElementPresent(browser, self.message_image_content)
            if check == True:
                logging.info('Screensot is attached in SMS')
            else:
                logging.error('Attachment is not found in SMS')
                pytest.fail('Failed in method verify_attached_screenshot')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_attached_photo_sms')
        
        except: 
            CommonMethods.exception(browser, featureFileName, 'verify_attached_photo_sms')
            
    def user_is_in_messages_screen(self,browser):
        try:
            check = CommonMethods.isElementPresent(browser, self.text_editor)
            if check == True:
                logging.info('User navigate to messages screen')
            else:
                logging.error('User is not in messages screen')
                pytest.fail('Failed in method user_is_in_messages_screen')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'user_is_in_messages_screen')
        
        except: 
            CommonMethods.exception(browser, featureFileName, 'user_is_in_messages_screen')
            
    def verify_descriptiontext_and_link_in_a_sms(self,browser,text):
        try:
            link="https://app.byjus.com/staging_bookmark_question_share?referrer="
            actual_text=CommonMethods.getAttributeOfElement(browser,text, self.text_editor)
            if str(text) in str(actual_text):
                logging.info('Description text found in SMS message body')
            else:
                logging.error('Description text mismatch')
                pytest.fail('Failed in method verify_descriptiontext_and_link_in_a_sms')
            if str(link) in str(actual_text) :
                logging.info('Link to navigate to byjus app is found in SMS')
            else:
                logging.error('Failed to find the link')
                pytest.fail('Searching link is not found')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_descriptiontext_and_link_in_a_sms')
        
        except: 
            CommonMethods.exception(browser, featureFileName, 'verify_descriptiontext_and_link_in_a_sms')
        
        