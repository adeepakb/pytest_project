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

from utilities.common_methods import CommonMethods
from constants.constants import CONFIG_PATH,Login_Credentials,Hamburger_Options
import logging
import pytest
from conftest import driver
from distutils.command.check import check

page_value = None
CommonMethods = CommonMethods()

data_file = CONFIG_PATH  

     
 
featureFileName = "Login OTP Verification Screen"

class Loginoptscreen():
    def __init__(self,driver):
        self.driver=driver
        
        
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
    Btn_next_id = (By.ID, "com.byjus.thelearningapp:id/btnLogin")
    txt_phoneNum_id = (By.ID, "com.byjus.thelearningapp:id/etPhoneNumber")
   
    toast_msg= (By.XPATH, "//android.widget.Toast")

    otp_stackbar=(By.ID,"com.byjus.thelearningapp:id/snackbar_text")
    snackbar_text=(By.XPATH,"//android.widget.TextView[@text='Bookmark Removed']")
    snackbar_btn=(By.XPATH,"//android.widget.Button[@text='UNDO']")
    otp_country_id=(By.ID,"com.byjus.thelearningapp:id/tvCountryID")
    otp_phno=(By.ID,"com.byjus.thelearningapp:id/tvPhoneNo")
    otp_verify_text=(By.XPATH, "//android.widget.TextView[@text='Verify']")
    otp_subtitle_text=(By.ID,"com.byjus.thelearningapp:id/header_subtitle_text")
    otp_4digit_txt=(By.XPATH, "//android.widget.TextView[@text='We have sent a 4 digit OTP to']")
    otp_sms_txt=(By.ID,"com.byjus.thelearningapp:id/tvRetryMSG")
    otp_resent_txt=(By.ID,"//android.widget.TextView[@text='Resend']")
    otp_enter=(By.ID,"com.byjus.thelearningapp:id/etOTP")
    bottomsheet_progressbar=(By.ID,"com.byjus.thelearningapp:id/progressBar")
    timer_check=(By.ID,"com.byjus.thelearningapp:id/tvCountdown")
    #otp_bottomsheet_txt=(By.ID,"com.byjus.thelearningapp:id/tvOTPSent")
    otp_bottomsheet_txt=(By.XPATH,"//android.widget.TextView[@text='Please wait, while we autoverify your OTP']")
    otp_callme_txt=(By.ID,"com.byjus.thelearningapp:id/tvResendCallMe")
    otp_trouble_text=(By.XPATH,"//android.widget.TextView[@text='Still having trouble?']")
    otp_resend_txt=(By.XPATH,"//android.widget.TextView[@text='Resend']")
    
    #login_title=(By.ID,"com.byjus.thelearningapp:id/header_title_text")
    


    
    
    def allowPopUp(self,driver):
        try:
            if CommonMethods.wait_for_element_visible(driver, self.allow_btn_id, 3):
                CommonMethods.elementClick(driver, self.allow_btn_id)
                logging.info('Allowed device Location')
                CommonMethods.elementClick(driver, self.allow_btn_id)
                logging.info('Allowed your Contacts')  
            elif CommonMethods.wait_for_element_visible(driver, self.noneOftheAbove_xpath, 3):
                CommonMethods.elementClick(driver, self.noneOftheAbove_xpath)  
            else:
                logging.info('Permission are not allowed') 
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'allowPopUp')    
        except:
            CommonMethods.exception(driver, featureFileName, 'allowPopUp')
    
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
            
    def navigateToLoginPage(self, driver):
        try:
            if CommonMethods.wait_for_element_visible(driver, self.loginPageVerify_id, 3):
                logging.info('App Navigated to Login Screen Successfully')
            elif CommonMethods.wait_for_element_visible(driver, self.allow_btn_id, 3):
                CommonMethods.elementClick(driver, self.allow_btn_id)
                CommonMethods.elementClick(driver, self.allow_btn_id)
                check = CommonMethods.wait_for_element_visible(driver, self.loginPageVerify_id, 3)
                if check == True:
                    logging.info('App Navigated to Login Screen Successfully')   
            elif CommonMethods.wait_for_element_visible(driver, self.back_button_id, 3):
                CommonMethods.run('adb shell pm clear com.byjus.thelearningapp')
                CommonMethods.run('adb shell am start -n com.byjus.thelearningapp/com.byjus.app.onboarding.activity.SplashActivity')
                self.navigateToLoginPage(driver)
            else:
                CommonMethods.run('adb shell pm clear com.byjus.thelearningapp')
                CommonMethods.run('adb shell am start -n com.byjus.thelearningapp/com.byjus.app.onboarding.activity.SplashActivity')
                self.navigateToLoginPage(driver)
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'navigateToLoginPage')    
        except:
            CommonMethods.exception(driver, featureFileName, 'navigateToLoginPage')   
            
    def verify_loginpage(self,driver):
        try:
            if CommonMethods.wait_for_element_visible(driver, self.loginPageVerify_id, 3):
                logging.info(' Navigated to Login Screen Successfully')
            else:
                logging.info("Failed to find Login text")
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'verify_loginpage')    
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_loginpage')
             
            
    def country_code(self,driver): 
        CommonMethods.wait_for_locator(driver,self.country_Code,15)
        CommonMethods.elementClick(driver,self.country_Code)
        sleep(2)
        CommonMethods.scrollToElementAndClick(driver, get_data(Login_Credentials, 'login_detail3'
                                                               , 'country_code'))
            
    def enterMobileNo(self,driver):
        CommonMethods.enterText(driver, get_data(Login_Credentials, 'login_detail3', 'mobile_no'), self.phone_num)

 
    
    def verifynum(self,driver):
        try:            
            expected_number = get_data(Login_Credentials, 'login_detail3', 'mobile_no')
            print("Expected num..........",expected_number)
            
            act_num= CommonMethods.getAttributeOfElement(driver,'text',self.otp_phno)
   
            #act_num=CommonMethods.getTextOfElement( driver, self.txt_phoneNum_id)
            print("Actual num...........",act_num)
            
            if act_num==expected_number:
                logging.info("Numbers are equal")
            else:
                logging.info("Numbers are not equal")
                pytest.fail("numbers are not eqaul ")
        
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'verifynum')    
        except:
            CommonMethods.exception(driver, featureFileName, 'verifynum')
            

            
    def tap_on_edit(self,driver):
        try:
            check = CommonMethods.wait_for_element_visible(driver, self.otp_phno, 15)
            sleep(5)
            if check == True:
                CommonMethods.elementClick( driver, self.otp_phno)
                logging.info("clicked on phone number field")
            else:
                logging.info("failed to clicked on phoneno  field")
                pytest.fail("failed to clicked on phoneno  field ")
                
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'tap_on_edit')    
        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_edit')
            
            
    def verifyotp_subtitle(self,driver,text):
        try:
            check=CommonMethods.isElementPresent( driver, self.otp_subtitle_text)
             
            if check == True:
                
                act_txt=CommonMethods.getTextOfElement(driver,self.otp_subtitle_text)
                print("Actual text...........",act_txt)
                exp_txt= text
                print("Expected text........",exp_txt)
                assert act_txt == exp_txt ,"failed to verify otp subtitle txt "
                
            else:
                logging.info("failed to verify otp subtitle txt")
                pytest.fail("failed to verify otp subtitle txt ")
                
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'verifyotp_subtitle')    
        except:
            CommonMethods.exception(driver, featureFileName, 'verifyotp_subtitle') 
            
    
    
    
    
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
            
            
    def stackbar_toast_msg(self,driver,text):
        try:
            sleep(1)
            check=CommonMethods.isElementPresent( driver, self.otp_stackbar)
             
            if check == True:
                
                act_txt=CommonMethods.getTextOfElement(driver,self.otp_stackbar)
                print("Actual Text..........",act_txt)
                exp_txt= text
                print("Expected text.........",exp_txt)
                assert act_txt == exp_txt ," stack bar toast  text  failed " 
            else:
                logging.info("stack bar toast text verification failed ")
                pytest.fail("stack bar toast text failed ")
                
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'stackbar_toast_msg')    
        except:
            CommonMethods.exception(driver, featureFileName, 'stackbar_toast_msg')  
            
    
    def otp_invalid(self,driver):
        try:           
            check = CommonMethods.wait_for_element_visible(driver, self.OtpTxtBx_id, 15)
            sleep(5)
            if check == True:
                CommonMethods.isElementPresent( driver, self.OtpTxtBx_id)
                CommonMethods.enterText(driver, "0000", self.OtpTxtBx_id)
                logging.info("Otp entered  verified ")
            else:
                logging.info("Not in otp screen")
                pytest.fail("Otp verification failed") 
                
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'otp_invalid')    
        except:
            CommonMethods.exception(driver, featureFileName, 'otp_invalid')
        
            
        
                
    def otp_screen_verify(self,driver):
        try:           
            check = CommonMethods.wait_for_element_visible(driver, self.otp_4digit_txt, 15)
            sleep(5)
            if check == True:
                CommonMethods.isElementPresent( driver, self.otp_4digit_txt)
                logging.info("Otp screen verified ")
            else:
                logging.info("Not in otp screen")
                pytest.fail("Otp verification failed") 
                
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'otp_screen_verify')    
        except:
            CommonMethods.exception(driver, featureFileName, 'otp_screen_verify')  
            
            
    def verify_otp_bottomsheet(self,driver,text):
        try:
            CommonMethods.isElementPresent( driver,self.otp_bottomsheet_txt )
              
            act_txt= CommonMethods.getAttributeOfElement(driver,'text', self.otp_bottomsheet_txt)
            print("Actual text.............",act_txt)
            exp_txt=text
            
            print("Expected text............",exp_txt)
            
            assert act_txt == exp_txt ,"Bottom sheet text failed to match"
            
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'verify_otp_bottomsheet')    
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_otp_bottomsheet')   
            
             
               
    def Verify_progressbar(self,driver):
        try:
            check = CommonMethods.wait_for_element_visible(driver, self.bottomsheet_progressbar, 1)
            sleep(5)
            if check == True:
                CommonMethods.isElementPresent( driver, self.bottomsheet_progressbar)
                logging.info("progress bar   verified ")
            else:
                logging.info(" progress bar is not present ")
                pytest.fail("progress bar is not present") 
                
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'Verify_progressbar')    
        except:
            CommonMethods.exception(driver, featureFileName, 'Verify_progressbar') 
            
    def verify_counter(self,driver):
        try:
            check = CommonMethods.wait_for_element_visible(driver, self.timer_check, 3)
            sleep(5)
            if check == True:
                CommonMethods.isElementPresent( driver, self.timer_check)
                logging.info("counter is verified ")
            else:
                logging.info(" counter is not present ")
                pytest.fail("Counter is not  present") 
                
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'verify_counter')    
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_counter') 
            
    def otp_bottom_dismiss(self,driver):
        sleep(5)
        CommonMethods.click_on_device_back_btn(driver)
        

            
            
            
    def verify_all_otp_text(self,driver,text):             
        try:
            sleep(2)
            if "Receive SMS?" in text:
                sub_opt = (By.XPATH,"//android.widget.TextView[contains(@text,'Receive SMS?')]")
            else:
                sub_opt = (By.XPATH,"//android.widget.TextView[@text=\'"+text+"\']")
            act_txt=CommonMethods.getAttributeOfElement(driver, 'text', sub_opt)
            print("actual text.............",act_txt)
            exp_txt=text
            print("expected text..........",exp_txt)           
            assert act_txt == exp_txt,"text failed to match"
   
        except NoSuchElementException :
                CommonMethods.noSuchEleExcept(driver,featureFileName,'verify_all_otp_text') 
        except:
                CommonMethods.exception(driver, featureFileName, 'verify_all_otp_text') 
                
   
    def verify_country_code(self,driver):
        try:
            check = CommonMethods.wait_for_element_visible(driver, self.otp_country_id, 1)
            sleep(5)
            if check == True:
                CommonMethods.isElementPresent( driver, self.otp_country_id)
                logging.info("country code  is verified ")
            else:
                logging.info(" country code is not present ")
                pytest.fail("country codeis not  present") 
                
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'verify_country_code')    
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_country_code') 
    
   
    def verify_mobilenum_field(self,driver):
        try:
            check = CommonMethods.wait_for_element_visible(driver, self.otp_phno, 1)
            sleep(5)
            if check == True:
                CommonMethods.isElementPresent( driver, self.otp_phno)
                logging.info("mobilenum field   is verified ")
            else:
                logging.info(" mobilenum field is not present ")
                pytest.fail("cmobilenum field is not  present") 
                
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'verify_mobilenum_field')    
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_mobilenum_field') 
    
    
    def verify_otp_field(self,driver):
        try:
            check = CommonMethods.wait_for_element_visible(driver, self.OtpTxtBx_id, 1)
            sleep(5)
            if check == True:
                CommonMethods.isElementPresent( driver, self.OtpTxtBx_id)
                logging.info("otp  field   is verified ")
            else:
                logging.info(" otp field is not present ")
                pytest.fail("otp field is not  present") 
                
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'verify_otp_field')    
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_otp_field')  
    
    def verify_resend_btn(self,driver):
        try:
            check = CommonMethods.wait_for_element_visible(driver, self.otp_resend_txt, 1)
            sleep(5)
            if check == True:
                CommonMethods.isElementPresent( driver, self.otp_resend_txt)
                logging.info("Resend button    is verified ")
            else:
                logging.info(" Resend button is not present ")
                pytest.fail("Resend button is not  present") 
                
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'verify_resend_btn')    
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_resend_btn')
            
      
              
    def tap_resend_btn(self,driver):
        try:
            check = CommonMethods.wait_for_element_visible(driver, self.otp_resend_txt, 1)
            sleep(5)
            if check == True:
                CommonMethods.elementClick( driver, self.otp_resend_txt)
                logging.info("Resend button    is verified ")
            else:
                logging.info(" Resend button is not present ")
                pytest.fail("Resend button is not  present") 
                
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'tap_resend_btn')    
        except:
            CommonMethods.exception(driver, featureFileName, 'tap_resend_btn')

    def click_on_next(self,driver):
        CommonMethods.elementClick(driver,self.Btn_next_id)