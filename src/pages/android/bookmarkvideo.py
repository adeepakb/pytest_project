from appium import webdriver
import sys
import os
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import logging
import json
import logging
from constants.constants import CONFIG_PATH
from constants.load_json import *
from constants.constants import Hamburger_Options
from utilities.interrupt import *

from utilities.common_methods import CommonMethods
from constants.constants import CONFIG_PATH,Login_Credentials,Hamburger_Options
import logging
import pytest
from conftest import driver
from distutils.command.check import check


page_value = None
CommonMethods = CommonMethods()

data_file = CONFIG_PATH  

     
 
featureFileName = "Bookmarks"
 
 
class Bookmark_video():
    
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
    

        
    def verify_home_page(self, driver):
        try:
            if CommonMethods.wait_for_element_visible(driver, self.back_button_id, 3):
                CommonMethods.elementClick(driver, self.back_button_id)
                CommonMethods.elementClick(driver, self.profile_name_hamburger)
                CommonMethods.wait_for_locator(driver, self.user_name_profile_page, 5)
                account_text = CommonMethods.getTextOfElement(driver, self.account_details_title)
                CommonMethods.scrollToElement(driver, account_text)
                expected_mob_num = CommonMethods.getTextOfElement(driver, self.profile_mob_num)
                actual_mob_num = get_data(data_file, 'profile_credentials3', 'mobileNum')
                if CommonMethods.verifyTwoText(actual_mob_num, expected_mob_num):
                    CommonMethods.elementClick(driver, self.back_button_id)
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
                    CommonMethods.scrollToElementAndClick(driver, get_data(Login_Credentials, 'login_detail3'
                                                                           , 'country_code'))
                    CommonMethods.enterText(driver, get_data(Login_Credentials, 'login_detail3', 'mobile_no'), self.phone_num)
                    CommonMethods.wait_for_locator(driver,self.loginBtn_id,15)
                    CommonMethods.elementClick(driver,self.loginBtn_id)
                    CommonMethods.wait_for_locator(driver,self.OtpTxtBx_id,15)
                    CommonMethods.enterText(driver, get_data(Login_Credentials, 'login_detail3', 'OTP'), self.OtpTxtBx_id)
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
            CommonMethods.scrollToElementAndClick(driver, get_data(Login_Credentials, 'login_detail3', 'country_code'))
            CommonMethods.enterText(driver, get_data(Login_Credentials, 'login_detail3', 'mobile_no'), self.phone_num)
            # CommonMethods.scrollToElementAndClick(driver, 'Canada (+1)')
            # CommonMethods.enterText(driver, "9871234", self.profile_mob_num)
            CommonMethods.wait_for_locator(driver, self.loginBtn_id, 15)
            CommonMethods.elementClick(driver, self.loginBtn_id)
            CommonMethods.wait_for_locator(driver, self.OtpTxtBx_id, 15)
            CommonMethods.enterText(driver, get_data(Login_Credentials, 'login_detail3', 'OTP'), self.OtpTxtBx_id)
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
                
   
    '''  hamburger verify  will verify hamburger  options  is present in the home screen  ''' 
    def hamburger_verify(self,driver):
        try:
            if CommonMethods.wait_for_element_visible(driver, self.ham_btn_id,5):
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
            if CommonMethods.wait_for_element_visible( driver, self.ham_bookmark, 3):
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
                    #driver.back()
                    CommonMethods.click_on_device_back_btn(driver)
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
            
            
    ''' device back method taps on device back button  '''         
    def device_back(self,driver):
        try:
            sleep(5)
            CommonMethods.clickOnBackBtn( driver)
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'device_back')
        
        except:
            CommonMethods.exception(driver, featureFileName, 'device_back')
            
            
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
            
    ''' remove_bookmark method will remove bookmark from bookmarkscreen   '''                   
    def remove_bookmark(self,driver):
        try:
            check=CommonMethods.isElementPresent( driver, self.bookmark_icon)
            if check == False:
                logging.info("No Bookmarks items are present ")
            else:
                while  check==True:
                    
                    CommonMethods.elementClick(driver, self.bookmark_icon)
#                     CommonMethods.wait_for_element_visible(driver, self.Bookmark_snackbartxt, 5)
#                     act_txt=CommonMethods.getTextOfElement(driver,self.Bookmark_snackbartxt)
#                     print("#########################",act_txt)
#                     exp_txt= "Bookmark Removed "
#                     print("###########################",exp_txt)
#                     assert act_txt == exp_txt ," stack bar toast  text  failed "
                    check=CommonMethods.isElementPresent(driver, self.bookmark_icon)
                                       
                
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept( driver, featureFileName, 'remove_bookmark')
        except:
            CommonMethods.noSuchEleExcept( driver, featureFileName, 'remove_bookmark') 
            
             
            
    ''' videoplayer_back method click on player back button    '''                  
    def videoplayer_back(self,driver):
               
        try:
            sleep(5)
            CommonMethods.elementClick(driver,self.videoFrame_id)
            CommonMethods.elementClick(driver,self.video_tab_PauseBtn_id)
            check=CommonMethods.isElementPresent( driver, self.Videoplayer_appback)
            if check == True:
                CommonMethods.elementClick( driver, self.Videoplayer_appback)
                logging.info( "videoplayer app back button is clicked ")
            else:
                logging.info("Videoplayer app back button is not clicked ")
                
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept( driver, featureFileName, 'videoplayer_back')
        except:
            CommonMethods.noSuchEleExcept( driver, featureFileName, 'videoplayer_back') 
    
    
    ''' videoplayer_chaptername_verify method verifies video chaptername    '''                   
    def videoplayer_chaptername_verify(self,driver):
        try:
            if CommonMethods.wait_for_element_visible(driver, self.video_player_chaptername,5):
                logging.info('Videoplayer chapter name is verified')
                 
            else:
                logging.info("Videoplayer chapter name Not Found")
                pytest.fail("Videoplayer chapter name Not Found")
         
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'videoplayer_chaptername_verify')  
               
        except:
            CommonMethods.exception(driver, featureFileName, 'videoplayer_chaptername_verify')
            
            
    ''' videoplayer_shareicon_verify method verifies shareicon in player    '''         
    def videoplayer_shareicon_verify(self,driver):
        try:
            if CommonMethods.wait_for_element_visible(driver, self.videoplayer_shareicon,5):
                logging.info('Videoplayer share icon is verified')
                 
            else:
                logging.info("Videoplayer share icon Not Found")
                pytest.fail("Videoplayer share icon Not Found")
         
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'videoplayer_shareicon_verify')  
               
        except:
            CommonMethods.exception(driver, featureFileName, 'videoplayer_shareicon_verify')
            
            
    ''' videoplayer_listicon_verify method verifies listicon in player    '''             
    def videoplayer_listicon_verify(self,driver):
        try:
            if CommonMethods.wait_for_element_visible(driver, self.video_player_listicon,1):
                logging.info('Videoplayer list icon is verified')
                 
            else:
                logging.info("Videoplayer list icon Not Found")
                pytest.fail("Videoplayer list icon Not Found")
         
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'videoplayer_listicon_verify')  
               
        except:
            CommonMethods.exception(driver, featureFileName, 'videoplayer_listicon_verify')
            
            
    ''' These videoplayer_bookmark_verify will verify bookmark icon in player screen  '''   
    def videoplayer_bookmark_verify(self,driver):
        try:
            if CommonMethods.wait_for_element_visible(driver, self.video_player_tab_bookmark,5):
                logging.info('Videoplayer bookmark icon is verified')
                 
            else:
                logging.info("Videoplayer bookmark icon Not Found")
                pytest.fail("Videoplayer bookmark icon Not Found")
         
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'videoplayer_bookmark_verify')  
               
        except:
            CommonMethods.exception(driver, featureFileName, 'videoplayer_bookmark_verify')
            
    ''' These videoplayer_back_verify  videoplayer back icon      '''           
    def videoplayer_back_verify(self,driver):
        try:
            sleep(5)
            CommonMethods.elementClick(driver,self.videoFrame_id)
            CommonMethods.elementClick(driver,self.video_tab_PauseBtn_id)
            check=CommonMethods.isElementPresent( driver, self.Videoplayer_appback)
            if check ==True:
                
                logging.info('Videoplayer back button is verified')
                 
            else:
                logging.info("Videoplayer back button Not Found")
                pytest.fail("Videoplayer back button Not Found")
         
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'videoplayer_back_verify')  
               
        except:
            CommonMethods.exception(driver, featureFileName, 'videoplayer_back_verify')
            
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
            
            
    ''' These library_video_screen  will navigate from home to library video screen    '''    
    def library_video_screen(self,driver):
        try:
            self.navigate_to_library(driver, 'Mathematics')
            check=CommonMethods.isElementPresent(driver, self.third_video_tab)
            if check == True:
                CommonMethods.elementClick(driver,self.third_video_tab)
                CommonMethods.wait_for_element_visible( driver, self.video_tab_list_close, 3)
                CommonMethods.elementClick(driver,self.video_tab_list_close)
                check_initial=CommonMethods.isElementPresent(driver,self.video_initial_play)
                if check_initial== True:
                    CommonMethods.elementClick(driver,self.video_initial_play)
                    sleep(5)
                    #self.pause_video(driver)
                    CommonMethods.elementClick(driver,self.videoFrame_id)
                    CommonMethods.elementClick(driver,self.video_tab_PauseBtn_id)                                    
                else:
                    
                    logging.info("video is playing ")
                    sleep(5)
                    #self.pause_video(driver)
                    CommonMethods.elementClick(driver,self.videoFrame_id)
                    CommonMethods.elementClick(driver,self.video_tab_PauseBtn_id)
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'library_video_screen')  
               
        except:
            CommonMethods.exception(driver, featureFileName, 'library_video_screen') 
            
            
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
            
    ''' These verify_toast_msg  will  verify toast message  '''          
    def verify_toast_msg(self,driver,text):
        try:
            check=CommonMethods.isElementPresent( driver, self.toast_msg)
             
            if check == True:
                
                act_txt=CommonMethods.getTextOfElement(driver,self.toast_msg)
                exp_txt= text
                assert act_txt == exp_txt ,"toast  text  failed "
  
            else:
                logging.info("toast text verification failed ")
                pytest.fail("toast text verification failed ")
                
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'verify_toast_msg')    
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_toast_msg')
            
            
    ''' These unbookmark_video  will   unbookmark the video from video screen '''            
    def unbookmark_video(self,driver):               
        try:     
                
                check_initial=CommonMethods.isElementPresent(driver,self.video_initial_play)
                if check_initial== True:
                    CommonMethods.elementClick(driver,self.video_initial_play)
                    sleep(5)
                    #self.pause_video(driver)
                    CommonMethods.elementClick(driver,self.videoFrame_id)
                    CommonMethods.elementClick(driver,self.video_tab_PauseBtn_id)
                    CommonMethods.elementClick(driver,self.Bookmark_tab)
                   # CommonMethods.elementClick(driver,self.Bookmark_tab)        
                else:
                    
                    logging.info("video is playing ")

                    sleep(5)
                    #self.pause_video(driver)
                    CommonMethods.elementClick(driver,self.videoFrame_id)
                    CommonMethods.elementClick(driver,self.video_tab_PauseBtn_id)
                    CommonMethods.elementClick(driver,self.Bookmark_tab)           
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver,featureFileName,'unbookmark_video')
        
        except :
            CommonMethods.exception(driver,featureFileName,'unbookmark_video')  
            
            
    ''' These bookmark_video_removed  will remove existing bookmark from bookmark screen after tapping on videoplayer back  '''   
            
    def bookmark_video_removed(self,driver):
        try:
            CommonMethods.isElementPresent( driver, self.Videoplayer_appback)
            CommonMethods.elementClick(driver, self.Videoplayer_appback)
            check=CommonMethods.isElementPresent( driver, self.bmrkvideo_verify)
             
            if check == False:
                
                logging.info("Bookmark Video is removed ")
                CommonMethods.elementClick(driver,self.Bookmark_mathematics)
                CommonMethods.isElementPresent(driver,self.Nobookmart_text)
                
            else:
                logging.info("Bookmark Video is  not removed ")
                pytest.fail("Bookmark Video is  not removed ")
                
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'bookmark_video_removed')    
        except:
            CommonMethods.exception(driver, featureFileName, 'bookmark_video_removed')
            
    
    
    
    
    ''' These initial_remove_bookmark  will remove existing bookmark from bookmark screen   '''     
    def initial_remove_bookmark(self,driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.ham_btn_id,5)
            CommonMethods.elementClick(driver, self.ham_btn_id)
            CommonMethods.wait_for_element_visible( driver, self.ham_bookmark, 3)
            CommonMethods.elementClick( driver, self.ham_bookmark)
            CommonMethods.wait_for_element_visible( driver, self.ham_bookmark, 3)            
            check=CommonMethods.isElementPresent( driver, self.bookmark_icon)
            if check == False:
                logging.info("No Bookmarks items are present ")
                driver.back()
            else:
                while  check==True:
                    
                    CommonMethods.elementClick(driver, self.bookmark_icon)
                    
                    check=CommonMethods.isElementPresent(driver, self.bookmark_icon)
                
            
                driver.back()
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept( driver, featureFileName, 'initial_remove_bookmark')
        except:
            CommonMethods.noSuchEleExcept( driver, featureFileName, 'initial_remove_bookmark') 
            
            
            
               
    ''' These boolmark_stack_toast_msg will verify the message present in boolmark_stack_toast_msg  option  '''            
    def boolmark_stack_toast_msg(self,driver):
        
        try:
            check=CommonMethods.isElementPresent(driver, self.bookmark_icon)
            if check == False:
                logging.info("No Bookmarks items are present ")
                pytest.fail("No bookmark present")
            else:
                CommonMethods.elementClick(driver, self.bookmark_icon)
                CommonMethods.wait_for_element_visible(driver, self.Bookmark_snackbartxt, 5)
                act_txt=CommonMethods.getTextOfElement(driver,self.Bookmark_snackbartxt)
                act1_txt=CommonMethods.getTextOfElement(driver,self.Bookmark_snackbartbn)
                
                print("actual text.................",act_txt)
                exp_txt= "Bookmark Removed"
                print("Expected text ...............",exp_txt)
                assert act_txt == exp_txt ," stack bar toast  text  failed "
                 
                print("actual text......................",act1_txt)
                exp1_txt= "UNDO"
                print("expected text....................",exp1_txt)
                assert act1_txt == exp1_txt ," stack bar toast  text  failed "
                                    
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'boolmark_stack_toast_msg')    
        except:
            CommonMethods.exception(driver, featureFileName, 'boolmark_stack_toast_msg')  
            
            
            
    ''' These bookmark_toast_undo will tap on bookmark undo option  '''           
    def bookmark_toast_undo(self,driver):
        
        try:
            check=CommonMethods.isElementPresent(driver, self.bookmark_icon)
            if check == False:
                logging.info("No Bookmarks items are present ")
                pytest.fail("No bookmark present")
            else:
                CommonMethods.elementClick(driver, self.bookmark_icon)
                CommonMethods.wait_for_element_visible(driver, self.Bookmark_snackbartxt, 5)
                CommonMethods.elementClick(driver,self.Bookmark_snackbartbn)
                logging.info("clicked on undo button sucessfully")
                
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'bookmark_toast_undo')    
        except:
            CommonMethods.exception(driver, featureFileName, 'bookmark_toast_undo')  
            
                
    ''' These bookmark_video_verify method will verify bookmarked video is present in bookmark screen  '''                           
    def bookmark_video_verify(self,driver):
        try:
            
            check=CommonMethods.isElementPresent( driver, self.bmrkvideo_verify)
             
            if check == True:
                CommonMethods.elementClick(driver, self.Bookmark_mathematics)
                CommonMethods.isElementPresent( driver, self.bmrkvideo_verify)
                
                logging.info("undo Bookmark video is present  ")
  
            else:
                logging.info("undo Bookmark Video is not present ")
                pytest.fail("undo Bookmark Video is  not present ")
                
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'bookmark_video_verify')    
        except:
            CommonMethods.exception(driver, featureFileName, 'bookmark_video_verify')
            
    
    ''' These bookmark_subject_chapter_verify method will verify subjectand chapter name  '''                
    def bookmark_subject_chapter_verify(self,driver):
        try:           
            check=CommonMethods.isElementPresent( driver, self.Bookmarksub_title)
             
            if check == True:
                
                logging.info("subject and title is verified   ")
  
            else:
                logging.info("subject and title is is not present ")
                pytest.fail("subject and title is  not present ")
                
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'bookmark_subject_chapter_verify')    
        except:
            CommonMethods.exception(driver, featureFileName, 'bookmark_subject_chapter_verify')
            
            
    ''' These bookmark_videotitle_verify method will verify videotitle '''         
    def bookmark_videotitle_verify(self,driver):
        try:            
            check=CommonMethods.isElementPresent( driver, self.Bookmarkvideo_title)
             
            if check == True:
                
                logging.info("video title is verified   ")
  
            else:
                logging.info("Video title failed to verify ")
                pytest.fail("Video title failed to verify ")
                
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'bookmark_videotitle_verify')    
        except:
            CommonMethods.exception(driver, featureFileName, 'bookmark_videotitle_verify')
            
            
            
    ''' These bookmark_screen_bookmarkicon method will verify bookmark icon is present or not '''            
    def bookmark_screen_bookmarkicon(self,driver):
        try:           
            check=CommonMethods.isElementPresent( driver, self.bookmark_icon)
             
            if check == True:
                
                logging.info("Bookmark icon  is verified   ")
  
            else:
                logging.info("Bookmark icon failed to verify ")
                pytest.fail("Bookmark icon failed to verify ")
                
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'bookmark_screen_bookmarkicon')    
        except:
            CommonMethods.exception(driver, featureFileName, 'bookmark_screen_bookmarkicon')
        
              
        
    ''' These navigate_to_video_screen method will navigate to video screen and pause the video  '''       
    def navigate_to_video_screen(self,driver):
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
                    #CommonMethods.elementClick(driver,self.Bookmark_tab)
                   # CommonMethods.elementClick(driver,self.Bookmark_tab)
#                     driver.back()
#                     driver.back()
                    
                else:
                    
                    logging.info("video is playing ")               
                    sleep(5)
                    #self.pause_video(driver)
                    CommonMethods.elementClick(driver,self.videoFrame_id)
                    CommonMethods.elementClick(driver,self.video_tab_PauseBtn_id)
                    #CommonMethods.elementClick(driver,self.Bookmark_tab)
#                     driver.back()
#                     driver.back()
                
                 
            else:
                logging.info("failed to navigate to videolist screen ")    
           
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver,featureFileName,'navigate_to_video_screen')
        except:
            CommonMethods.exception(driver, featureFileName, 'navigate_to_video_screen')


    ''' These select_offline_mode method will offline the device  '''            
    def select_offline_mode(self, driver):        
        try:
            set_connection_type(driver, 'OFFLINE')
             
            logging.info("enabled offline mode")   
        except :
            logging.info("Failed in Method selectOfflineMode")

            pytest.fail("Failed Due to Locator in Journey map screen")

    
    ''' These offline_toast_verify will the offline toast message  '''     
    def offline_toast_verify(self,driver,text):                
        try:
            check=CommonMethods.isElementPresent(driver, self.Bookmarkvideo_title)
            if check == False:
                logging.info("No Bookmarks items are present ")
                pytest.fail("No bookmark present")
            else:
                CommonMethods.elementClick(driver, self.Bookmarkvideo_title)
                CommonMethods.wait_for_element_visible(driver, self.Bookmark_snackbartxt, 5)
                act_txt=CommonMethods.getTextOfElement(driver,self.Bookmark_snackbartxt)               
                print("Actual text..........",act_txt)
                exp_txt= text
                print("Expected text..........",exp_txt)
                assert act_txt == exp_txt ," stack bar toast  text  failed "
                                                  
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'offline_toast_verify')    
        except:
            CommonMethods.exception(driver, featureFileName, 'offline_toast_verify')  
                 

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
            
            
             
    ''' These verify_8thgrade method will verify user is in 8th grade '''                 
    def verify_8thgrade(self,driver):
        try:
            CommonMethods.wait_for_element_visible(driver, self.ham_btn_id,5)
            CommonMethods.elementClick(driver, self.ham_btn_id)
            CommonMethods.wait_for_element_visible( driver, self.prof_btn_id, 3)
            CommonMethods.elementClick( driver, self.prof_btn_id)
            CommonMethods.wait_for_element_visible( driver, self.dropdown_8thgrade,3)
            CommonMethods.isElementPresent( driver, self.dropdown_8thgrade)
            
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver,featureFileName,'verify8thgrade')
        
        except :
            CommonMethods.exception(driver,featureFileName,'verify8thgrade') 
            
            
    ''' These switchto_9thgrade methods switch from  current grade to 9th grade  '''          
    def switchto_9thgrade(self,driver):
        try:
            
            CommonMethods.wait_for_element_visible(driver, self.Grade_dropdown,5)
            CommonMethods.elementClick(driver,self.Grade_dropdown)
            CommonMethods.wait_for_element_visible(driver, self.dropdown_9thgrade,5)
            CommonMethods.elementClick(driver, self.dropdown_9thgrade)
            sleep(2)
            CommonMethods.wait_for_element_visible( driver, self.dropdown_9thgrade,3)
            CommonMethods.isElementPresent( driver, self.dropdown_9thgrade)
            driver.back()
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver,featureFileName,'switchto9thgrade')
        
        except :
            CommonMethods.exception(driver,featureFileName,'switchto9thgrade') 
            
            
    ''' These check_nobookmark  method  verifies nobookmark text   ''' 
    def check_nobookmark(self,driver,text):
        try:
            sub_opt = (By.XPATH,"//android.widget.TextView[@text=\'"+text+"\']")
            check=CommonMethods.isElementPresent( driver, sub_opt)
            if check == True:
                logging.info("No Bookmarks text is  present ")
            else:
                logging.info("Bookmark content is present ")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept( driver, featureFileName, 'check_nobookmark')
        except:
            CommonMethods.noSuchEleExcept( driver, featureFileName, 'check_nobookmark')
            
            
    ''' These switch_to_wifi  method  switches on the device wifi   '''            
    def switch_to_wifi(self, driver):     
        try:
            set_connection_type(driver, "WIFI_ONLY")
             
            logging.info("enabled wifi connection mode")   
        except :
            logging.info("Failed in Method selectOfflineMode")

            pytest.fail("Failed Due to Locator in Journey map screen") 
            
            
    ''' These fromjourneyto_homescreen  method  takes user from journey screen to home screen   '''   
    def fromjourneyto_homescreen(self,driver):
        try:          
            
            check=CommonMethods.isElementPresent( driver, self.Videoplayer_appback)
            if check == True:
                CommonMethods.elementClick( driver, self.Videoplayer_appback)
                sleep(1)
                #driver.back()
                CommonMethods.click_on_device_back_btn(driver)
                if CommonMethods.isElementPresent(driver, self.exit_journey):
                    
                    CommonMethods.elementClick(driver, self.exit_journey)
                    #driver.back()
                    CommonMethods.click_on_device_back_btn(driver)
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
            
    ''' These bmark_back  method verifies app back button is present in bookkmark screen   '''
    def bmark_back(self,driver):
        try:
            check=CommonMethods.wait_for_element_visible(driver, self.back_button_id,3)
            
            if check ==True:
                logging.info("Element is visible ")
            
            else:
                logging.info('back button    Not Found')
                pytest.fail("Failed due to Bookmark elements")
         
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'bmark_back')  
               
        except:
            CommonMethods.exception(driver, featureFileName, 'bmark_back')

    ''' These method verifies filter option is present or not in bookmarkscreen  ''' 
    def filter_option(self,driver):
        try:
            check=CommonMethods.wait_for_element_visible(driver, self.filter_txt,3)
            
            if check ==True:
                logging.info("Element is visible ")
            
            else:
                logging.info('Filter text   Not Found')
                pytest.fail("Failed due to Bookmark elements")
         
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'filter_option')  
               
        except:
            CommonMethods.exception(driver, featureFileName, 'filter_option') 
             
    
    ''' These method verifies all the subject text  present in bookmark screen with respect to Home page subjects  '''    
    def subject_txt(self,driver):
        try:
                        
            check=CommonMethods.wait_for_element_visible(driver, self.all_txt,5)
            
            if check ==True:
                logging.info("Element is visible and present  ")
            
            else:
                logging.info('All option is    Not Found')
                pytest.fail("Failed due to Bookmark elements")
            sub=CommonMethods.getElements( driver, self.all_bookmark_sub)
                
            ''' Bookmark list is taken from below code'''
            Blist=[]
            for ele in sub:
                sub_txt=ele.text
                print("sub text............."+sub_txt)
                Blist.append(sub_txt)
            print(Blist)
            Blist.pop(0)
            print(Blist)
            CommonMethods.elementClick( driver, self.back_button_id)
            sublist=CommonMethods.getElements(driver, self.all_sub)
            
            '''subject list is taken from home screen '''
            slist=[]
            for ele in sublist:
                sub_txt=ele.text
                print("subject list items.........."+sub_txt)
                slist.append(sub_txt)
            print(slist)
            print(slist)
            if Blist == slist:
                print("List are identical")
            else:
                print("list elements are not identical")
         
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'subject_txt')  
               
        except:
            CommonMethods.exception(driver, featureFileName, 'subject_txt')    
           