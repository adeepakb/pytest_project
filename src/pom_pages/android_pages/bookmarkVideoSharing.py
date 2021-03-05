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
from Utilities.interrupt import *

from Utilities.common_methods import CommonMethods
from Constants.constants import CONFIG_PATH,Login_Credentials,Hamburger_Options
import logging
import pytest
from conftest import driver
from distutils.command.check import check


page_value = None
CommonMethods = CommonMethods()

data_file = CONFIG_PATH  

     
 
featureFileName = "Bookmarkvideo Sharing"
 
 
class BookmarkVideoSharing():
    
    def __init__(self,driver):
        self.driver=driver
        
        
        
        
        
    phone_num = (By.ID,"com.byjus.thelearningapp:id/etPhoneNumber")
    country_Code = "com.byjus.thelearningapp:id/spnrCountry"
    video = "//android.widget.ImageView[@instance='2']"
    Btn_test="com.byjus.thelearningapp:id/chapter_list_item_test_txtvw"
    Btn_practice="com.byjus.thelearningapp:id/practice_mode_bottom_txtvw"
    Btn_play_pause="//android.widget.ImageView[@instance='3']"
    loginBtn_id ="com.byjus.thelearningapp:id/btnLogin"
    OtpTxtBx_id = "com.byjus.thelearningapp:id/etOTP"
    librayBtn_id =(By.ID, "com.byjus.thelearningapp:id/optionalNav")
    first_videoLnk_xpath = "//android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp:id/chapter_view_group' and @index=1]/androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp:id/chapter_videos_lstvw']/android.widget.LinearLayout[@resource-id='com.byjus.thelearningapp:id/chapter_video_list_cardview' and @index = 0]"
    videoFrame_id = "com.byjus.thelearningapp:id/exo_subtitles"
    #videoPauseBtn_id = "com.byjus.thelearningapp:id/exo_pause"
    #videoPlayBtn_id = "com.byjus.thelearningapp:id/exo_play"
    videoPlayingNow_xpath = "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp:id/video_list_view']//android.widget.LinearLayout[@index=0]//android.widget.TextView[@resource-id='com.byjus.thelearningapp:id/chapter_video_subitem_name_txtv' and @selected = 'true']"
    google_termsBtn_id = "com.android.chrome:id/terms_accept"
    nextBtn_id = "com.android.chrome:id/next_button"
    negativeBtn_id = "com.android.chrome:id/negative_button"
    progressTime_id = "com.byjus.thelearningapp:id/exo_position"
    remaingTime_id = "com.byjus.thelearningapp:id/exo_duration"
    tenSecFwdBtn_id = "com.byjus.thelearningapp:id/exo_ffwd"
    tenSecBkwdBtn_id = "com.byjus.thelearningapp:id/exo_rew"
    byjusAppPackage ="com.byjus.thelearningapp"
    skipBtn_id = "com.byjus.thelearningapp:id/buttonSkip"
    allow_btn_id = "com.android.packageinstaller:id/permission_allow_button"
    skipBtn_id = "com.byjus.thelearningapp:id/buttonSkip"
    Videoplayer_appback= (By.ID,"com.byjus.thelearningapp:id/back")
    #     Login Locators
    #com.byjus.thelearningapp:id/backNav
    back_button_id = (By.ID,"com.byjus.thelearningapp:id/backNav")
    profile_name_hamburger = (By.ID,"com.byjus.thelearningapp:id/home_drawer_txtvw_profile_name")
    account_details_title = (By.ID,"com.byjus.thelearningapp:id/account_details_title")
    profile_mob_num = (By.ID,"com.byjus.thelearningapp:id/mobile_number")
    country_Code = (By.ID, "com.byjus.thelearningapp:id/spnrCountry")
    loginBtn_id = (By.ID, "com.byjus.thelearningapp:id/btnLogin")
    OtpTxtBx_id = (By.ID, "com.byjus.thelearningapp:id/etOTP")
    allow_btn_id = (By.ID, "com.android.packageinstaller:id/permission_allow_button")
    none_of_the_above_id = (By.ID,"com.google.android.gms:id/cancel")
    loginPageVerify_id = (By.XPATH, "//android.widget.TextView[@text='Login']")
    phone_num = (By.ID, "com.byjus.thelearningapp:id/etPhoneNumber")
    user_name_profile_page = (By.ID,"com.byjus.thelearningapp:id/tvUserName") 
    ham_btn_id = (By.ID, "com.byjus.thelearningapp:id/roundedNavButton")  
    all_subjects=(By.XPATH,"//android.widget.GridLayout//android.widget.FrameLayout[@resource-id='com.byjus.thelearningapp:id/home_subject_cardview']")
    all_bookmark_sub=(By.XPATH,"//android.widget.HorizontalScrollView//android.widget.LinearLayout//android.widget.TextView")
    toast_msg= (By.XPATH, "//android.widget.Toast")
    #subject  personalised  screen locators
    Library_btn=(By.XPATH,("//android.widget.Button[@text='Library']"))
    personalised_btn=(By.XPATH,("//android.widget.Button[@text='Personalised']"))
    first_video_tab=(By.XPATH,("//android.widget.FrameLayout[@resource-id='com.byjus.thelearningapp:id/chapter_view_group' and @index = 2]"))
    video_tab_list_close=(By.ID,("com.byjus.thelearningapp:id/video_list_close"))
    video_initial_play=(By.ID,("com.byjus.thelearningapp:id/ivPlay"))
    video_tap_playicon=(By.ID,("com.byjus.thelearningapp:id/exo_play"))
    videoFrame_id = (By.ID, ("com.byjus.thelearningapp:id/exo_subtitles"))
    video_tab_PauseBtn_id =(By.ID, ("com.byjus.thelearningapp:id/exo_pause" ))
    #video_player_tab_bookmark=(By.ID,("com.byjus.thelearningapp:id/bookmark"))               
    Video_player_tab_backbtn=(By.ID,("com.byjus.thelearningapp:id/back"))
    personalizeScreen_xpath = (By.XPATH,("//android.widget.Button[@text='Personalised']"))
    third_video_tab=(By.XPATH,("//android.widget.FrameLayout[@resource-id='com.byjus.thelearningapp:id/chapter_view_group' and @index = 3]"))
    
    #Bookmarks
    
   
    filter_txt=(By.XPATH,"//android.widget.Button[@text='Filter']")
    
    mathematics_txt=(By.XPATH,"//android.widget.TextView[@text='Mathematics']")
    physics_txt=(By.XPATH,"//android.widget.TextView[@text='Physics']")
    chemistry_txt=(By.XPATH,("//android.widget.TextView[@text='Chemistry']"))
    all_txt=(By.XPATH,("//android.widget.TextView[@text='All']"))
    biology_txt=(By.XPATH,("//android.widget.TextView[@text='Biology']"))
    comp_exam_txt=(By.XPATH,("//android.widget.TextView[@text='Competitive Exam - Mocks']"))
    previous_txt=(By.XPATH,("//android.widget.TextView[@text='Previous Years Papers']"))
    all_sub=(By.ID,("com.byjus.thelearningapp:id/home_subject_name_txtvw"))
    ham_bookmark=(By.XPATH,("//android.widget.TextView[@text='Bookmarks']"))
    #ham_page=(By.XPATH,("//android.widget.TextView[@text='Bookmarks']"))
    bookmark_icon=(By.XPATH,("//androidx.recyclerview.widget.RecyclerView//android.widget.RelativeLayout[@index=0]//android.widget.ImageView[@resource-id='com.byjus.thelearningapp:id/ivBookmarkTag']"))
    no_bookmark=(By.XPATH,("//android.widget.TextView[@text='No Bookmarks']"))
    Bookmark_tab=(By.ID,("com.byjus.thelearningapp:id/bookmark"))
    
    #Bookmark Filter
    filter_close=(By.ID,"com.byjus.thelearningapp:id/closeFilter")
    filter_innertxt=(By.XPATH,"//android.widget.TextView[@text='Filter']")
    Showall_txt=(By.XPATH,"//android.widget.TextView[@text='Show all']")
    questions_txt=(By.XPATH,"//android.widget.TextView[@text='Questions']")
    videos_txt=(By.XPATH,"//android.widget.TextView[@text='Videos']")
    Showall_btn=(By.XPATH,"//android.widget.RelativeLayout[@index=0]//android.widget.ImageView[@resource-id='com.byjus.thelearningapp:id/bookmarkFilterRadioButton']")
    questions_btn=(By.XPATH,"//android.widget.RelativeLayout[@index=1]//android.widget.ImageView[@resource-id='com.byjus.thelearningapp:id/bookmarkFilterRadioButton']")
    videos_btn=(By.XPATH,"//android.widget.RelativeLayout[@index=2]//android.widget.ImageView[@resource-id='com.byjus.thelearningapp:id/bookmarkFilterRadioButton']")
    filter_screen=(By.ID,"com.byjus.thelearningapp:id/bookmarkFilterLayout")
    
    #questionscreen
    Library_test=(By.XPATH,"//android.widget.FrameLayout[@resource-id='com.byjus.thelearningapp:id/chapter_view_group' and @index = 2]//android.widget.TextView[@text='Test']")
    take_test=(By.XPATH,"//android.widget.LinearLayout[@index=1]//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp:id/rv_test_list_section']//android.widget.RelativeLayout[@index=0]//android.widget.RelativeLayout[@index=0]")
    start_test=(By.XPATH,"//android.widget.Button[@text='Test']")
    
   # Bookmark_icon=(By.ID,"//com.byjus.thelearningapp:id/ivBookmark")
    bookmark_question=(By.ID,"com.byjus.thelearningapp:id/ivBookmark")
  
    Abort_btn=(By.ID,"com.byjus.thelearningapp:id/secondaryAction")
    bmrkquestion_verify=(By.XPATH,"//android.widget.TextView[contains(@text,'Q.')]")
    bmrkvideo_verify=(By.XPATH,"//android.widget.ImageView[@resource-id='com.byjus.thelearningapp:id/ivVideoCover']")
    Videoplayer_appback= (By.ID,"com.byjus.thelearningapp:id/back")
    videoplayer_shareicon=(By.ID,"com.byjus.thelearningapp:id/share")
    video_player_tab_bookmark=(By.ID,("com.byjus.thelearningapp:id/bookmark"))   
    video_player_chaptername=(By.ID,"com.byjus.thelearningapp:id/tvVideoName") 
    video_player_listicon=(By.ID,"com.byjus.thelearningapp:id/video_list")
    snackbar_text=(By.XPATH,"//android.widget.TextView[@text='Bookmark Removed']")
    snackbar_btn=(By.XPATH,"//android.widget.Button[@text='UNDO']")
    snackbar_btn1=(By.ID,"com.byjus.thelearningapp:id/snackbar_action")
    Bookmark_snackbartxt=(By.ID,"com.byjus.thelearningapp:id/snackbar_text")
    Bookmark_snackbartbn=(By.ID,"com.byjus.thelearningapp:id/snackbar_action")
    otp_stackbar=(By.ID,"com.byjus.thelearningapp:id/snackbar_text")
    Bookmarksub_title=(By.XPATH,"//android.widget.TextView[@resource-id='com.byjus.thelearningapp:id/tvSubject']") 
    Bookmarkvideo_title=(By.XPATH,"//android.widget.TextView[@resource-id='com.byjus.thelearningapp:id/tvTitle']")  
    Bookmark_mathematics=(By.XPATH,"//android.widget.TextView[@text='Mathematics']")
    Nobookmart_text=(By.XPATH,"//android.widget.TextView[@text='No Bookmarks']")
    #first journey
    first_journey_card = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp:id/rvChapterList']/android.widget.LinearLayout[@index=1]//androidx.recyclerview.widget.RecyclerView[@resource-id='com.byjus.thelearningapp:id/rvSubtopic']/android.widget.RelativeLayout[@index=0]")
    subjectName_id = (By.ID, "com.byjus.thelearningapp:id/header_title_text")
    
    #Switch grade

    Grade_dropdown=(By.ID, "com.byjus.thelearningapp:id/tvGrade")
    dropdown_9thgrade=(By.XPATH,"//android.widget.TextView[@text='9th Grade']")
    dropdown_8thgrade=(By.XPATH,"//android.widget.TextView[@text='8th Grade']")
    prof_btn_id = (By.ID, "com.byjus.thelearningapp:id/home_drawer_imgvw_arrow_right")
    
    exit_journey=(By.ID, "com.byjus.thelearningapp:id/secondaryAction")
    
   # Sharing_locators
    videoplayer_shareicon=(By.ID,"com.byjus.thelearningapp:id/share")
    Gmail_text=(By.XPATH,"//android.widget.TextView[@text='Gmail']")
    Gmail_to=(By.XPATH,"//android.widget.MultiAutoCompleteTextView")
    Gmail_send=(By.XPATH,'//android.widget.TextView[@content-desc="Send"]')
    Gmail_compose_txt=(By.XPATH,"//android.widget.TextView[@text='Compose']")
    Gmail_subject_text=(By.XPATH,'//android.widget.EditText[@text="BYJU\'S The Learning App"]')
    Gmail_tosend=(By.XPATH,"//android.widget.MultiAutoCompleteTextView[@resource-id='com.google.android.gm:id/to']")
    Gmail_compose_txt=(By.XPATH,"//android.widget.TextView[@text='Compose']")
    Gmail_body_text=(By.XPATH,'//*[contains(@resource-id, "wc_body_layout")]//android.widget.EditText')
    message_txt=(By.ID,"com.android.mms:id/embedded_text_editor")
    Sms_messaging_txt=(By.XPATH,"//android.widget.TextView[@text='Messaging']")
    
    
    
    
    
    
    
    ''' verify_home_page method will verify home page and verifies the profile screen '''     
    def verify_home_page(self, driver):
        try:
            if CommonMethods.wait_for_element_visible(driver, self.back_button_id, 3):
                CommonMethods.elementClick(driver, self.back_button_id)
                CommonMethods.elementClick(driver, self.profile_name_hamburger)
                CommonMethods.wait_for_locator(driver, self.user_name_profile_page, 5)
                account_text = CommonMethods.getTextOfElement(driver, self.account_details_title)
                CommonMethods.scrollToElement(driver, account_text)
                expected_mob_num = CommonMethods.getTextOfElement(driver, self.profile_mob_num)
                actual_mob_num = getdata(data_file, 'profile_credentials3', 'mobileNum')
                if CommonMethods.verifyTwoText(actual_mob_num, expected_mob_num):
                    CommonMethods.elementClick(driver, self.back_button_id)
                    logging.info("condition pass")
                    pass
                
                
                else:
                    CommonMethods.run('adb shell pm clear com.byjus.thelearningapp')
                    CommonMethods.run('adb shell am start -n com.byjus.thelearningapp/com.byjus.app.onboarding.activity.SplashActivity')
                    # sleep(2)
                    CommonMethods.accept_notification(driver, self.allow_btn_id)
                    CommonMethods.accept_notification(driver, self.allow_btn_id)
                    CommonMethods.click_none_of_the_above(driver,self.none_of_the_above_id)
                    CommonMethods.wait_for_locator(driver,self.country_Code,15)
                    CommonMethods.elementClick(driver,self.country_Code)
                    sleep(2)
                    CommonMethods.scrollToElementAndClick(driver,getdata(Login_Credentials,'login_detail3'
                                                                          , 'country_code'))
                    CommonMethods.enterText(driver,getdata(Login_Credentials,'login_detail3','mobile_no'),self.phone_num)
                    CommonMethods.wait_for_locator(driver,self.loginBtn_id,15)
                    CommonMethods.elementClick(driver,self.loginBtn_id)
                    CommonMethods.wait_for_locator(driver,self.OtpTxtBx_id,15)
                    CommonMethods.enterText(driver, getdata(Login_Credentials,'login_detail3','OTP'), self.OtpTxtBx_id)
                    sleep(15)
                    return True
            else:
                logging.info('user is not in Home page')
                return False
        except:
            logging.info('Error in Verifing Home Page')
            
    
    def verify_to_login_page(self, driver):
        if CommonMethods.wait_for_element_visible(driver, self.allow_btn_id, 6):
            CommonMethods.accept_notification(driver, self.allow_btn_id)
            CommonMethods.accept_notification(driver, self.allow_btn_id)
            CommonMethods.click_none_of_the_above(driver,self.none_of_the_above_id)
            CommonMethods.wait_for_locator(driver,self.country_Code,15)
            CommonMethods.elementClick(driver,self.country_Code)
            sleep(1)
            CommonMethods.scrollToElementAndClick(driver, getdata(Login_Credentials, 'login_detail3', 'country_code'))
            CommonMethods.enterText(driver, getdata(Login_Credentials, 'login_detail3', 'mobile_no'), self.phone_num)
            # CommonMethods.scrollToElementAndClick(driver, 'Canada (+1)')
            # CommonMethods.enterText(driver, "9871234", self.profile_mob_num)
            CommonMethods.wait_for_locator(driver, self.loginBtn_id, 15)
            CommonMethods.elementClick(driver, self.loginBtn_id)
            CommonMethods.wait_for_locator(driver, self.OtpTxtBx_id, 15)
            CommonMethods.enterText(driver, getdata(Login_Credentials, 'login_detail3', 'OTP'), self.OtpTxtBx_id)
        else:
            logging.info('User verified Login page')
            
         
    def navigate_to_home_screen(self, driver):
            try:
                self.verify_home_page(driver)
                self.verify_to_login_page(driver)
                
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver,featureFileName,'navigateToHomeScreen')

            except :
                CommonMethods.exception(driver,featureFileName,'navigateToHomeScreen')
   
    
                
                
    ''' navigate_to_library method will take user from home screen to library screen   '''                    
    def navigate_to_library(self,driver,sub):
        try:
            pythonSub_xpath =(By.XPATH,"//android.widget.TextView[@text=\'"+sub+"\']")
            CommonMethods.wait_for_locator(driver,pythonSub_xpath,15)
            CommonMethods.elementClick(driver,pythonSub_xpath)
            if CommonMethods.isElementPresent(driver, self.personalizeScreen_xpath):
                pass
            else:
                CommonMethods.wait_for_locator(driver,self.librayBtn_id,3)
                CommonMethods.elementClick(driver,self.librayBtn_id)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver,featureFileName,'navigate_to_library')
        
        except :
            CommonMethods.exception(driver,featureFileName,'navigate_to_library') 
            
            
    ''' hamburger_verify methods verifies hamburger menu and clicks on it  '''       
    def hamburger_verify(self,driver):
        try:
            if CommonMethods.wait_for_element_visible(driver, self.ham_btn_id,15):
                CommonMethods.elementClick(driver, self.ham_btn_id)
                 
            else:
                logging.info('Hamburger menu Not Found')
                pytest.fail("Failed due to Hamburger Menu")
         
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'hamburger_verify')  
               
        except:
            CommonMethods.exception(driver, featureFileName, 'hamburger_verify')
            
            
    ''' bookmark_verify methods verifies Bookmarks options is present in the  hamburger  '''        
    def bookmark_verify(self,driver):
        try:
            if CommonMethods.wait_for_element_visible( driver, self.ham_bookmark, 10):
                CommonMethods.elementClick( driver, self.ham_bookmark)
            else:
                logging.info('Hamburger menu Not Found')
                pytest.fail("Failed due to Hamburger Menu")
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'bookmark_verify')  
               
        except:
            CommonMethods.exception(driver, featureFileName, 'bookmark_verify')
            
    ''' bookmark_screen methods verifies Bookmarks screen   '''         
    def bookmark_screen(self,driver):
        try:
            check=CommonMethods.wait_for_element_visible( driver, self.ham_bookmark, 3)
            
            if check== True:
                logging.info("Bookmark present ")
                
            else:
                logging.info('page Not Found')
                pytest.fail("Failed due to Hamburger Menu")
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'bookmark_screen')  
               
        except:
            CommonMethods.exception(driver, featureFileName, 'bookmark_screen')
    
    ''' video_share_tap methods verifies share icon in videoplayer and taps on it   '''            
    def video_share_tap(self,driver):
        try:
            if CommonMethods.wait_for_element_visible( driver, self.videoplayer_shareicon, 3):
                CommonMethods.elementClick( driver, self.videoplayer_shareicon)
            else:
                logging.info('shareicon not found ')
                pytest.fail("failed due to player shareicon")
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'video_share_tap')  
               
        except:
            CommonMethods.exception(driver, featureFileName, 'video_share_tap')
            
            
    ''' gmail_verify_tap methods verifies gmail icon in share bottomsheet dialog  and taps on it   '''         
    def gmail_verify_tap(self,driver):
        try:
            if CommonMethods.wait_for_element_visible( driver, self.Gmail_text, 3):
                CommonMethods.elementClick( driver, self.Gmail_text)
            else:
                logging.info('Gmail option  not found ')
                pytest.fail("Failed due to gmail option is not present in bottomsheet")
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'gmail_verify_tap')  
               
        except:
            CommonMethods.exception(driver, featureFileName, 'gmail_verify_tap')
    
    
    ''' to_mail_recipient_enter methods verifies to address field and enters email id   '''         
    def to_mail_recipient_enter(self,driver):
        try:
            if CommonMethods.wait_for_element_visible( driver, self.Gmail_tosend, 10):
                CommonMethods.enterText( driver, "test123@gmail.com", self.Gmail_tosend)
            else:
                logging.info('Gmail to address failed to find ')
                pytest.fail("Gmail to address failed to enter")
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'to_mail_recipient_enter')  
               
        except:
            CommonMethods.exception(driver, featureFileName, 'to_mail_recipient_enter')
    
            
    ''' gmail_send_enter methods verifies send option and clicks on it   '''         
    def gmail_send_enter(self,driver):
        try:
            if CommonMethods.wait_for_element_visible( driver, self.Gmail_send, 10):
                CommonMethods.elementClick(driver, self.Gmail_send)
            else:
                logging.info('Gmail to address failed to find ')
                pytest.fail("Gmail to address failed to enter")
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'gmail_send_enter')  
               
        except:
            CommonMethods.exception(driver, featureFileName, 'gmail_send_enter')
            
            
    ''' These initial_remove_bookmark  will remove existing bookmark from bookmark screen   '''     
    def initial_remove_bookmark(self,driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.ham_btn_id,10)
            CommonMethods.elementClick(driver, self.ham_btn_id)
            CommonMethods.wait_for_element_visible( driver, self.ham_bookmark, 3)
            CommonMethods.elementClick( driver, self.ham_bookmark)
            CommonMethods.wait_for_element_visible( driver, self.ham_bookmark, 5)            
            check=CommonMethods.isElementPresent( driver, self.bookmark_icon)
            if check == False:
                logging.info("No Bookmarks items are present ")
                #driver.back()
                CommonMethods.click_on_device_back_btn(driver)
            else:
                while  check==True:
                    
                    CommonMethods.elementClick(driver, self.bookmark_icon)
                    
                    check=CommonMethods.isElementPresent(driver, self.bookmark_icon)           
                driver.back()
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept( driver, featureFileName, 'initial_remove_bookmark')
        except:
            CommonMethods.noSuchEleExcept( driver, featureFileName, 'initial_remove_bookmark') 
            
    ''' bookmark_video  methods bookmarks video from library  '''                    
    def bookmark_video(self,driver):
        try:
            self.navigate_to_library(driver, 'Mathematics')
            check=CommonMethods.isElementPresent(driver, self.first_video_tab)
            if check == True:
                CommonMethods.elementClick(driver,self.first_video_tab)
                CommonMethods.wait_for_element_visible( driver, self.video_tab_list_close, 3)
                CommonMethods.elementClick(driver,self.video_tab_list_close)
                check_initial=CommonMethods.isElementPresent(driver,self.video_initial_play)
                if check_initial== True:
                    CommonMethods.elementClick(driver,self.video_initial_play)
                    sleep(5)
                    #self.pause_video(driver)
                    CommonMethods.elementClick(driver,self.videoFrame_id)
                    CommonMethods.elementClick(driver,self.video_tab_PauseBtn_id)
                    CommonMethods.wait_for_element_visible(driver, self.Bookmark_tab, 5)
                    CommonMethods.elementClick(driver,self.Bookmark_tab)
                   #CommonMethods.elementClick(driver,self.Bookmark_tab)
                    #driver.back()
                    CommonMethods.click_on_device_back_btn(driver)
                    #driver.back()
                    CommonMethods.click_on_device_back_btn(driver)
                    
                else:
                    
                    logging.info("video is playing ")              
                    sleep(5)
                    #self.pause_video(driver)
                    CommonMethods.elementClick(driver,self.videoFrame_id)
                    CommonMethods.elementClick(driver,self.video_tab_PauseBtn_id)
                    CommonMethods.wait_for_element_visible(driver, self.Bookmark_tab, 5)
                    CommonMethods.elementClick(driver,self.Bookmark_tab)
                    #driver.back()
                    #driver.back()
                    CommonMethods.click_on_device_back_btn(driver)
                    CommonMethods.click_on_device_back_btn(driver)                
                 
            else:
                logging.info("failed to navigate to videolist screen ")    
           
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver,featureFileName,'bookmark_video')
        
        except :
            CommonMethods.exception(driver,featureFileName,'bookmark_video')
            
            
    ''' bookmark_video_verify_tap method verifies bookmark video is present and taps on it if it is present  '''                    
    def bookmark_video_verify_tap(self,driver):
        try:
            check=CommonMethods.isElementPresent(driver, self.bmrkvideo_verify)
            if check == True:
                logging.info("vedio verified sucessfully")
                CommonMethods.elementClick( driver, self.bmrkvideo_verify)
                
            else:
                logging.info("video is not present")
                pytest.fail("video is not present")
                
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver,featureFileName,'bookmark_video_verify_tap')
        
        except :
            CommonMethods.exception(driver,featureFileName,'bookmark_video_verify_tap')    
            
            
    def shareicon_tap(self,driver):        
        try:     
                
                check_initial=CommonMethods.isElementPresent(driver,self.video_initial_play)
                if check_initial== True:
                    CommonMethods.elementClick(driver,self.video_initial_play)
                    sleep(5)
                    #self.pause_video(driver)
                    CommonMethods.elementClick(driver,self.videoFrame_id)
                    CommonMethods.elementClick(driver,self.video_tab_PauseBtn_id)
                    CommonMethods.wait_for_element_visible(driver, self.videoplayer_shareicon, 5)
                    CommonMethods.elementClick(driver,self.videoplayer_shareicon)
                          
                else:
                    
                    logging.info("video is playing ")

                    sleep(5)
                    #self.pause_video(driver)
                    CommonMethods.elementClick(driver,self.videoFrame_id)
                    CommonMethods.elementClick(driver,self.video_tab_PauseBtn_id)
                    CommonMethods.wait_for_element_visible(driver, self.videoplayer_shareicon, 5)
                    CommonMethods.elementClick(driver,self.videoplayer_shareicon)
                              
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver,featureFileName,'shareicon_tap')  
            
            
            
    ''' These check_nobookmark  method  verifies nobookmark text   '''    
    def verify_gmail_subject_text(self,driver,text):
        try:
            exp_txt=text
            CommonMethods.wait_for_element_visible(driver, self.Gmail_subject_text, 10)
            act_txt=CommonMethods.getTextOfElement(driver, self.Gmail_subject_text)
            print("actual text ............",act_txt)
            
            assert act_txt == exp_txt ,"subject text failed to match "
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept( driver, featureFileName, 'verify_gmail_subject_text')
        except:
            CommonMethods.noSuchEleExcept( driver, featureFileName, 'verify_gmail_subject_text')
    
            
    ''' These verify_descriptiontext_and_link_in_a_mail  method  verifies text and link in gmail   '''           
    def verify_descriptiontext_and_link_in_a_mail(self,driver,text):
        try:
            text2="I am having fun learning Linear Equations in One Variable on the BYJU'S app. Download the app for free now and take a look at it."
            link="https://app.byjus.com/staging_video_share"
            actual_text=CommonMethods.getTextOfElement(driver, self.Gmail_body_text)
            if str(text) in str(actual_text):
                logging.info('Description text found in gmail body')
            elif str(text2) in str(actual_text):
                logging.info('Description1st text found in gmail body')
            else:
                
                print("actual text................",actual_text)
                logging.error('Description text mismatch')
                pytest.fail('Failed in method verify_body_text_in_a_mail')
            
            if str(link) in str(actual_text) :
                logging.info('Link to navigate to byjus app is found in the mail')
            else:
                logging.error('Failed to find the link')
                pytest.fail('Searching link is not found')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_body_text_in_a_mail')
            
    ''' These gmail_compose_verify method  verifies Compose text is present  in a mail window   '''           
    def gmail_compose_verify(self,driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.Gmail_compose_txt, 5)
            check=CommonMethods.isElementPresent(driver, self.Gmail_compose_txt)
            if check == True:
                logging.info("Gmail compose is opened ")
                                
            else:
                logging.info("Gmail compose failed to open")
                pytest.fail("gmail compose is not found ")
                
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver,featureFileName,'gmail_compose_verify')
        
        except :
            CommonMethods.exception(driver,featureFileName,'gmail_compose_verify') 
            
    ''' messagingverify_tap methods verifies gmail icon in share bottomsheet dialog  and taps on it   '''         
    def messageverify_tap(self,driver):
        try:
            if CommonMethods.wait_for_element_visible( driver, self.Sms_messaging_txt, 3):
                CommonMethods.elementClick( driver, self.Sms_messaging_txt)
            else:
                logging.info('Messaging option  not found ')
                pytest.fail("Failed due to Messaging option is not present in bottomsheet")
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'messageverify_tap')  
               
        except:
            CommonMethods.exception(driver, featureFileName, 'messageverify_tap')
    
    ''' These verify_descriptiontext_and_link_in_a_message method  verifies text and link in sms   '''            
    def verify_descriptiontext_and_link_in_a_message(self,driver,text):
        try:
            text2="I am having fun learning Linear Equations in One Variable on the BYJU'S app. Download the app for free now and take a look at it."
            link="https://app.byjus.com/staging_video_share"
            actual_text=CommonMethods.getTextOfElement(driver, self.message_txt)
            if str(text) in str(actual_text):
                logging.info('Description text found in gmail body')
            elif str(text2) in str(actual_text):
                logging.info('Description1st text found in gmail body')
            else:
                
                print("actual text.............",actual_text)
                logging.error('Description text mismatch')
                pytest.fail('Failed in method verify_body_text_in_a_mail')
            
            if str(link) in str(actual_text) :
                logging.info('Link to navigate to byjus app is found in the mail')
            else:
                logging.error('Failed to find the link')
                pytest.fail('Searching link is not found')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_body_text_in_a_mail')
    
    ''' These navigate_to_journey will switch to journey screen  '''             
    def navigate_to_journey(self,driver):
        try:
            sub='Mathematics'
            pythonSub_xpath =(By.XPATH,"//android.widget.TextView[@text=\'"+sub+"\']")
            CommonMethods.wait_for_locator(driver,pythonSub_xpath,15)
            CommonMethods.elementClick(driver,pythonSub_xpath)
            if CommonMethods.isElementPresent(driver, self.personalizeScreen_xpath):
                CommonMethods.elementClick(driver,self.personalizeScreen_xpath)
                
            else:
                CommonMethods.wait_for_locator(driver,self.librayBtn_id,10)
                pass
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver,featureFileName,'navigate_to_journey')
        
        except :
            CommonMethods.exception(driver,featureFileName,'navigate_to_journey') 
            
    ''' These first_journey will scroll the chapterlist from bottom to top and tap on first journey '''     
    def first_journey(self,driver):
        try:
            sleep(5)    
            check=CommonMethods.isElementPresent(driver,self.first_journey_card)
            display_sub=CommonMethods.isElementPresent(driver,self.subjectName_id)
            if check==True:
                #CommonMethods.elementClick( driver,self.first_journey_card)
                
                while display_sub==False:
                    
                    nodeCrd = CommonMethods.getElement(driver, self.first_journey_card)
                    n = nodeCrd.location_in_view
                    driver.swipe(n['x'], n['y'], n['x'], n['y'] + 350)
                    #print(n['x'],n['y'])
                    display_sub = CommonMethods.isElementPresent(driver, self.subjectName_id)
                    
                CommonMethods.elementClick( driver,self.first_journey_card)
                  
            else:
                CommonMethods.elementClick( driver,self.first_journey_card)       
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver,featureFileName,'first_journey')
        
        except :
            CommonMethods.exception(driver,featureFileName,'first_journey')
            
    ''' These video_player_verify  will click on pause icon     '''    
    def video_player_verify(self,driver):
        try:
            sleep(5)
            CommonMethods.wait_for_element_visible( driver, self.videoFrame_id, 15)
            #CommonMethods.is_element_visible(self, driver, locator)
            CommonMethods.elementClick(driver,self.videoFrame_id)
            CommonMethods.elementClick(driver,self.video_tab_PauseBtn_id)
            CommonMethods.wait_for_element_visible(driver, self.video_tap_playicon,2)
            
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'video_player_verify')  
               
        except:
            CommonMethods.exception(driver, featureFileName, 'video_player_verify')
            
    ''' These bookmark_playericon_verify  will  verify player icon in the video player screen   '''     
    def bookmark_playericon_verify(self,driver):
        try:
            CommonMethods.wait_for_element_visible( driver, self.Bookmark_tab, 15)
            check=CommonMethods.isElementPresent(driver, self.Bookmark_tab)
            if check == True:
                logging.info("Bookmark icon is present")                                                   
            else:                    
                    logging.info("Bookmark icon is not present ")
                    
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'bookmark_playericon_verify')  
               
        except:
            CommonMethods.exception(driver, featureFileName, 'bookmark_playericon_verify') 
            
            
    ''' These verify_toast_msg  will  verify toast message  '''    
    def video_player_bookmark_tap(self,driver):
        try:
            check=CommonMethods.isElementPresent(driver, self.Bookmark_tab)
            if check == True:
                CommonMethods.elementClick(driver,self.Bookmark_tab)
                logging.info("Bookmark icon is selected")
                sleep(2)                                                   
            else:                    
                    logging.info("Bookmark icon is not present ")
                    
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'video_player_bookmark_tap')  
               
        except:
            CommonMethods.exception(driver, featureFileName, 'video_player_bookmark_tap')
            
            
    ''' These fromjourneyto_homescreen  method  takes user from journey screen to home screen   ''' 
    def fromjourneyto_homescreen(self,driver):
        try:                        
            check=CommonMethods.isElementPresent( driver, self.Videoplayer_appback)
            if check == True:
                CommonMethods.elementClick( driver, self.Videoplayer_appback)
                sleep(1)
                driver.back()
                if CommonMethods.isElementPresent(driver, self.exit_journey):
                    
                    CommonMethods.elementClick(driver, self.exit_journey)
                    driver.back()
#                 driver.back()
#                 driver.back()
                else:
                    #driver.back()
                    CommonMethods.click_on_device_back_btn(driver)
                    
                    logging.info( "Navigated to home screen  ")              
                
            else:
                logging.info("Videoplayer app back button is not clicked ")
                
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept( driver, featureFileName, 'fromjourneyto_homescreen')
        except:
            CommonMethods.noSuchEleExcept( driver, featureFileName, 'fromjourneyto_homescreen') 
            
    ''' These verify_journeydescriptiontext_and_link_in_a_message method  verifies text and link in sms   ''' 
    def verify_journeydescriptiontext_and_link_in_a_message(self,driver,text):
        
        try:
            text2="I am having fun learning Rational Numbers on the BYJU'S app. Download the app for free now and take a look at it."
            link="https://app.byjus.com/staging_video_share"
            actual_text=CommonMethods.getTextOfElement(driver, self.message_txt)
            if str(text) in str(actual_text):
                logging.info('Description text found in gmail body')
            elif str(text2) in str(actual_text):
                logging.info('Description1st text found in gmail body')
            else:
                
                print("actual text...............",actual_text)
                logging.error('Description text mismatch')
                pytest.fail('Failed in method verify_body_text_in_a_mail')
            
            if str(link) in str(actual_text) :
                logging.info('Link to navigate to byjus app is found in the mail')
            else:
                logging.error('Failed to find the link')
                pytest.fail('Searching link is not found')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_body_text_in_a_mail')
    
               
    