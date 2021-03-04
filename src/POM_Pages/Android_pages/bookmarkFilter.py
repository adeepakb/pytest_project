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
from Constants.constants import CONFIG_PATH,Login_Credentials,Hamburger_Options
import logging
import pytest
from conftest import driver
from distutils.command.check import check


page_value = None
CommonMethods = CommonMethods()

data_file = CONFIG_PATH  

     
 
featureFileName = "Bookmarks"
 
 
class Bookmark_filter():
    
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
    librayBtn_id = "com.byjus.thelearningapp:id/optionalNav"
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
    
    #subject  personalised  screen locators
    Library_btn=(By.XPATH,("//android.widget.Button[@text='Library']"))
    personalised_btn=(By.XPATH,("//android.widget.Button[@text='Personalised']"))
    first_video_tab=(By.XPATH,("//android.widget.FrameLayout[@resource-id='com.byjus.thelearningapp:id/chapter_view_group' and @index = 2]"))
    video_tab_list_close=(By.ID,("com.byjus.thelearningapp:id/video_list_close"))
    video_initial_play=(By.ID,("com.byjus.thelearningapp:id/ivPlay"))
    video_tap_playicon=(By.ID,("com.byjus.thelearningapp:id/exo_play"))
    videoFrame_id = (By.ID, ("com.byjus.thelearningapp:id/exo_subtitles"))
    video_tab_PauseBtn_id =(By.ID, ("com.byjus.thelearningapp:id/exo_pause" ))
    video_player_tab_bookmark=(By.ID,("com.byjus.thelearningapp:id/bookmark"))               
    Video_player_tab_backbtn=(By.ID,("com.byjus.thelearningapp:id/back"))
    personalizeScreen_xpath = (By.XPATH,("//android.widget.Button[@text='Personalised']"))
    
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
                
                
    ''' These hamburger_verify will verify hamburger menu in home screen and will click if it is present ''' 
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
            
    ''' bookmark_screen methods verifies Bookmark screen   '''
            
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
            
    ''' filter_tap methods verifies filter option and taps on it if present    '''
            
    def filter_tap(self,driver):
        try:
            
            if CommonMethods.wait_for_element_visible( driver, self.filter_txt, 3):
                CommonMethods.elementClick( driver, self.filter_txt)
            else:
                logging.info('Failed to click on filter ')
                pytest.fail("Failed to click on filter")
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'filter_tap')  
               
        except:
            CommonMethods.exception(driver, featureFileName, 'filter_tap')
            
    ''' filter_close_verify verifies filter close button in bookmarkscreen     '''
            
    def filter_close_verify(self,driver):
        try:
            if CommonMethods.wait_for_element_visible(driver, self.filter_close,5):
                logging.info('filter close verify')
                 
            else:
                logging.info('filter close Not Found')
                pytest.fail("Failed due to filter close")
         
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'filter_close_verify')  
               
        except:
            CommonMethods.exception(driver, featureFileName, 'filter_close_verify')
            
    ''' verify_filter_txt verifies filter text in  bookmarkscreen     '''
    
    def verify_filter_txt(self,driver,text):
        try:
            check=CommonMethods.isElementPresent( driver, self.filter_innertxt)
             
            if check == True:
                
                act_txt=CommonMethods.getTextOfElement(driver,self.filter_innertxt)
                print("actual text...........",act_txt)
                exp_txt= text
                print("expected text..........",exp_txt)
                assert act_txt == exp_txt ,"failed to verify filter text "
                
            else:
                logging.info("failed to verify filter text t")
                pytest.fail("failed to verify filter text  ")
                
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'verify_filter_txt')    
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_filter_txt')
            
    ''' showalltxt_btn verifies both text and button in the filter option    '''        
            
    def showalltxt_btn(self,driver):
        try:
            check=CommonMethods.isElementPresent( driver, self.Showall_txt)
                         
            if check == True:
                logging.info("showall option is present")
                CommonMethods.isElementPresent( driver, self.Showall_btn)
                logging.info("showallbtn  is present")
            else:
                logging.info("showall option is  not present")
                pytest.fail("failed to verify showall option  ")
                
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'showalltxt_btn')    
        except:
            CommonMethods.exception(driver, featureFileName, 'showalltxt_btn')
            
    ''' questiontxt_btn verifies both question  text and button in the filter option    ''' 
            
    def questiontxt_btn(self,driver):
        try:
            check=CommonMethods.isElementPresent( driver, self.questions_txt)
                         
            if check == True:
                logging.info("questions option is present")
                CommonMethods.isElementPresent( driver, self.questions_btn)
                logging.info("questionbtn  is present")
                
                
            else:
                logging.info("questions option is  not present")
                pytest.fail("failed to verify questions option  ")
                
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'questiontxt_btn')    
        except:
            CommonMethods.exception(driver, featureFileName, 'questiontxt_btn')
            
            
    ''' videos_txt_btn verifies both question  text and button in the filter option    '''           
    def videos_txt_btn(self,driver):
        try:
            check=CommonMethods.isElementPresent( driver, self.questions_txt)
                         
            if check == True:
                logging.info("questions option is present")
                CommonMethods.isElementPresent( driver, self.videos_btn)
                logging.info("video btn  is present")
                
            else:
                logging.info("questions option is  not present")
                pytest.fail("failed to verify questions option  ")
                
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'videos_txt_btn')    
        except:
            CommonMethods.exception(driver, featureFileName, 'videos_txt_btn')   
            
            
    ''' filter_closebtn verifies filter close btn and clicks if it is present     '''                    
    def filter_closebtn(self,driver):
        try:
            check=CommonMethods.isElementPresent( driver, self.filter_close)
                         
            if check == True:
                
                CommonMethods.elementClick( driver,self.filter_close )
                logging.info("clicked on filter closed ")
                
            else:
                logging.info("Filter close btn is  not present")
                pytest.fail("Filter close btn is  not present  ")
                
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'filter_closebtn')    
        except:
            CommonMethods.exception(driver, featureFileName, 'filter_closebtn')
            
            
    ''' filterscreen_verify verifies filter screen is present or not     '''                     
    def filterscreen_verify(self,driver):
        try:
            check=CommonMethods.isElementPresent( driver, self.filter_screen)
                         
            if check ==False:
                logging.info("filter screen is not present")
                
            else:
                logging.info("filter screen is present")
                pytest.fail("failed to verify filter  ")
                
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'filterscreen_verify')    
        except:
            CommonMethods.exception(driver, featureFileName, 'filterscreen_verify') 
            
    ''' navigate_to_library method will take user from home screen to library video screen     '''
    
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
            
                      

    ''' bookmark_video method will bookmark a library  video      '''

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
                    CommonMethods.elementClick(driver,self.Bookmark_tab)
                   # CommonMethods.elementClick(driver,self.Bookmark_tab)
                   # driver.back()
                    #driver.back()
                    CommonMethods.click_on_device_back_btn(driver)
                    CommonMethods.click_on_device_back_btn(driver)
                    
                else:
                    
                    logging.info("video is playing ")
                
                
                    sleep(5)
                    #self.pause_video(driver)
                    CommonMethods.elementClick(driver,self.videoFrame_id)
                    CommonMethods.elementClick(driver,self.video_tab_PauseBtn_id)
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
   
   
   
    ''' bookmark_question method will bookmark a question via library flow     '''
            
    def bookmark_question(self,driver):
        try:
            self.navigate_to_library(driver, 'Mathematics')
            check=CommonMethods.isElementPresent(driver, self.Library_test)
            if check == True:
                
                CommonMethods.elementClick(driver,self.Library_test)
                CommonMethods.wait_for_element_visible( driver, self.take_test, 3)
                CommonMethods.elementClick(driver,self.take_test)
                CommonMethods.wait_for_element_visible( driver, self.start_test, 3)
#                 check_initial=CommonMethods.isElementPresent(driver,self.start_test)
#                 if check_initial== True:
                CommonMethods.elementClick(driver,self.start_test)
                sleep(5)
                    
                CommonMethods.elementClick(driver,self.bookmark_question)
                driver.back()
                CommonMethods.wait_for_element_visible( driver, self.Abort_btn, 3)
                CommonMethods.elementClick(driver,self.Abort_btn)
                sleep(2)
                #driver.back()
                #driver.back()
                CommonMethods.click_on_device_back_btn(driver)
                CommonMethods.click_on_device_back_btn(driver)
                
                          
                    
            else:
                    
                logging.info("failed to bookmark question ")
                
                
                 
#             else:
#                 logging.info("failed to navigate to library list ")    
           
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver,featureFileName,'bookmark_question')
        
        except :
            CommonMethods.exception(driver,featureFileName,'bookmark_question')
            
            
    ''' Bookmark_video_verify method will verify bookmarked video is present in bookmark screen    '''                    
    def Bookmark_video_verify(self,driver):
        try:
            check=CommonMethods.isElementPresent(driver, self.bmrkvideo_verify)
            if check == True:
                logging.info("vedio verified sucessfully")
            else:
                logging.info("video is not present")
                pytest.fail("video is not present")
                
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver,featureFileName,'Bookmark_video_verify')
        
        except :
            CommonMethods.exception(driver,featureFileName,'Bookmark_video_verify')
            
            
    ''' bookmark_question_verify method will verify bookmarked question  is present in bookmark screen    '''                    
    def bookmark_question_verify(self,driver):
        try:
            check=CommonMethods.isElementPresent(driver, self.bmrkquestion_verify)
            if check == True:
                logging.info("question verified sucessfully")
            else:
                logging.info("question is not present")
                pytest.fail("question is not present")
                
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver,featureFileName,'bookmark_question_verify')
        
        except :
            CommonMethods.exception(driver,featureFileName,'bookmark_question_verify')
            
            
            
    ''' remove_bookmark method will remove the existing bookmars  in bookmark screen '''            
    def remove_bookmark(self,driver):
        try:
            check=CommonMethods.isElementPresent( driver, self.bookmark_icon)
            if check == False:
                logging.info("No Bookmarks items are present ")
            else:
                while  check==True:
                    
                    CommonMethods.elementClick(driver, self.bookmark_icon)
                    check=CommonMethods.isElementPresent(driver, self.bookmark_icon)
                
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept( driver, featureFileName, 'remove_bookmark')
        except:
            CommonMethods.noSuchEleExcept( driver, featureFileName, 'remove_bookmark')  
            
            
    ''' showall_selected method will verify showall button is selected '''           
    def showall_selected(self,driver):
        try:             
            high=CommonMethods.getAttributeOfElement( driver,'selected',self.showa11_btn ) 
            print("gives the status of high...."+high)
            if (high == "true"):
                logging.info("showall button is selected ")
            else:
                logging.info('showall button is not selected')
                pytest.fail("Failed due to showall button is not selected")
         
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'showall_selected')
        
        except:
            CommonMethods.exception(driver, featureFileName, 'showall_selected' )  
            
             
    ''' tap_showall method will verify  and tap on showwll option from filter  '''
    def tap_showall(self,driver):
        try:
            check=CommonMethods.isElementPresent( driver, self.Showall_btn)
                         
            if check == True:

                CommonMethods.elementClick( driver, self.Showall_btn)
                logging.info("showallbtn  is tapped")
            else:
                logging.info("showall button failed to tap")
                pytest.fail("failed to tap on showall button  ")
                
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'tap_showall')    
        except:
            CommonMethods.exception(driver, featureFileName, 'tap_showall')
            
            
    ''' tap_filter_video_btn method will verify  and tap on videos option from filter  '''            
    def tap_filter_video_btn(self,driver):
        try:
            check=CommonMethods.isElementPresent( driver, self.videos_btn)
                         
            if check == True:

                CommonMethods.elementClick( driver, self.videos_btn)
                logging.info("videobutton   is tapped")
            else:
                logging.info(" video button failed to tap")
                pytest.fail("failed to tap on video button  ")
                
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'tap_video')    
        except:
            CommonMethods.exception(driver, featureFileName, 'tap_video')
            
    ''' tap_filter_question_btn method will verify  and tap on question  option from filter  '''        
    def tap_filter_question_btn(self,driver):
        try:
            check=CommonMethods.isElementPresent( driver, self.questions_btn)
                         
            if check == True:

                CommonMethods.elementClick( driver, self.questions_btn)
                logging.info("question button    is tapped")
            else:
                logging.info(" question button  failed to tap")
                pytest.fail("failed to tap on question button   ")
                
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'tap_filter_question_btn')    
        except:
            CommonMethods.exception(driver, featureFileName, 'tap_filter_question_btn')
            
    ''' all_highlight_Verify method will verify  the highlight is present on the selected option  '''            
    def all_highlight_Verify(self,driver):        
        try:
            
            high=CommonMethods.getAttributeOfElement( driver, 'selected', self.all_txt)
            print("value of the high........"+high)
            if (high == "true"):
                logging.info("All is highlighted ")
                CommonMethods.isElementPresent(driver, self.bookmark_icon)
            else:
                logging.info('subject failed to highlight')
                pytest.fail("Failed due to Bookmark subject highlight")
         
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'all_highlight_Verify')
        
        except:
            CommonMethods.exception(driver, featureFileName, 'all_highlight_Verify')
            
            
    ''' Bookmark_video_removedverify method will verify  bookmarked video is removed in bookmarkscreen   '''            
    def Bookmark_video_removedverify(self,driver):
        try:
            check=CommonMethods.isElementPresent(driver, self.bmrkvideo_verify)
            if check == False:
                logging.info("video is removed sucessfully")
            else:
                logging.info("video is  present")
                pytest.fail("video is  present")
                
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver,featureFileName,'Bookmark_video_verify')
        
        except :
            CommonMethods.exception(driver,featureFileName,'Bookmark_video_verify')
            
 
            
