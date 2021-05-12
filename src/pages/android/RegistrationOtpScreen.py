import time
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
from selenium.webdriver.common.by import By
from utilities.common_methods import CommonMethods
from selenium.common.exceptions import NoSuchElementException
import logging
import re
import pytest
from conftest import driver
from constants.load_json import *
from constants.constants import Registration_data

CommonMethods = CommonMethods()
data_file = Registration_data

featureFileName = 'Register OTP Verification Screen'

class RegOtpScreen():
    allowbutton =(By.ID,"com.android.packageinstaller:id/permission_allow_button")
    denybutton = (By.ID,"com.android.packageinstaller:id/permission_deny_button")
    skipButton = (By.ID,"com.byjus.thelearningapp:id/buttonSkip")
    grade8th =(By.XPATH,"//android.widget.Button[@text ='8th']")
    gms_cancel=(By.ID,"com.google.android.gms:id/cancel")
    header_greeting_text= (By.ID,"com.byjus.thelearningapp:id/header_greeting_text")
    header_title_text =(By.ID,"com.byjus.thelearningapp:id/header_title_text")
    nametextfield =(By.ID,"com.byjus.thelearningapp:id/etName")
    phonetextfield=(By.ID,"com.byjus.thelearningapp:id/etPhoneNumber")
    countrycodedrop_down_text_view =(By.ID, "com.byjus.thelearningapp:id/drop_down_text_view")
    countrycodedrop_down =(By.ID, "com.byjus.thelearningapp:id/spnrCountry")
    emailtextfield = (By.ID,"com.byjus.thelearningapp:id/etEmail")
    citytextfield = (By.ID,"com.byjus.thelearningapp:id/etCity")
    btnRegister =(By.ID, "com.byjus.thelearningapp:id/btnRegister")
    loginRegBtn =(By.ID,'com.byjus.thelearningapp:id/tvRegister')
    dialogBox_msg=(By.ID,"com.byjus.thelearningapp:id/dialog_message")
    otp_header_layout=(By.ID, "com.byjus.thelearningapp:id/header_layout")
    progressBar=(By.ID, "com.byjus.thelearningapp:id/progressBar")
    Countdowntimer=(By.ID, "com.byjus.thelearningapp:id/tvCountdown")
    loginPhoneNo=(By.ID,"com.byjus.thelearningapp:id/tvPhoneNo")
    loginCountryID=(By.ID,"com.byjus.thelearningapp:id/tvCountryID")
    otp=(By.ID,"com.byjus.thelearningapp:id/etOTP")
    ResendCallMe=(By.ID,"com.byjus.thelearningapp:id/tvResendCallMe")
    toast_msg= (By.XPATH, "//android.widget.Toast")
    countrycodedrop_down_text_view =(By.ID, "com.byjus.thelearningapp:id/drop_down_text_view")
    countrycodedrop_down =(By.ID, "com.byjus.thelearningapp:id/spnrCountry")
    loginBtn_id =(By.ID, "com.byjus.thelearningapp:id/btnLogin")
    PhoneErrorMsg =(By.ID,"com.byjus.thelearningapp:id/tvPhoneError")
    subtitle_text =(By.ID,"com.byjus.thelearningapp:id/header_subtitle_text")
    snackbar_text =(By.ID,"com.byjus.thelearningapp:id/snackbar_text")
    location_ok=(By.ID,"android:id/button1")
    countrycode = None
    phone_number = None
    reg_phone_number= None

    def __init__(self, driver):
        self.driver = driver
        
    def launch_the_app(self,driver):
        try:
            if CommonMethods.isElementPresent(driver, self.allowbutton):  
                CommonMethods.elementClick(driver, self.allowbutton)
                CommonMethods.elementClick(driver, self.allowbutton)
                sleep(3)
            if CommonMethods.isElementPresent(driver,self.loginRegBtn):
                if CommonMethods.isElementPresent(driver, self.gms_cancel):
                    CommonMethods.elementClick(driver,self.gms_cancel)
                CommonMethods.elementClick(driver, self.loginRegBtn)
            if CommonMethods.isElementPresent(driver,self.skipButton):
                logging.info('User is in onboarding screen')
                CommonMethods.elementClick(driver,self.skipButton)
            CommonMethods.elementClick(driver, self.grade8th)
            if CommonMethods.isElementPresent(driver, self.gms_cancel):
                CommonMethods.elementClick(driver,self.gms_cancel)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'launch_the_app')
                
        except:
            CommonMethods.exception(driver, featureFileName, 'launch_the_app')
        
    
    def navigate_to_reg_otp_screen(self,driver):
        try:
            if CommonMethods.isElementPresent(driver,self.nametextfield):
                CommonMethods.enterText(driver, get_data(data_file, 'user_details', 'name'), self.nametextfield)
                CommonMethods.enterText(driver, get_data(data_file, 'user_details', 'mobile'), self.phonetextfield)
                self.countrycode = CommonMethods.getAttributeOfElement(driver,'text', self.countrycodedrop_down_text_view)
                self.reg_phone_number=CommonMethods.getAttributeOfElement(driver,'text', self.phonetextfield)
                CommonMethods.enterText(driver, get_data(data_file, 'user_details', 'email'), self.emailtextfield)
                actual_text =CommonMethods.getAttributeOfElement(driver,'text', self.citytextfield)
                check = CommonMethods.verifyTextMatch(actual_text, 'City / Nearest location')
                if check == True:
                    self.tap_on_location_icon(driver)
                    if CommonMethods.isElementPresent(driver, self.location_ok):
                        CommonMethods.elementClick(driver, self.location_ok)
                        self.tap_on_location_icon(driver)
                    sleep(3)
#                 else: 
#                     CommonMethods.enterText(driver,get_data(data_file, 'user_details', 'city'), self.citytextfield)
                
                CommonMethods.elementClick(driver, self.btnRegister)
                CommonMethods.wait_for_locator(driver, self.otp_header_layout, 20)
                logging.info('Register OTP Verification Screen')
            else:
                logging.error('Failed to navigate to OTP verification screen')
        
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'navigate_to_reg_otp_screen')
                
        except:
            CommonMethods.exception(driver, featureFileName, 'navigate_to_reg_otp_screen')
        
        
    def verify_the_text(self,driver,text):
        try:
            if CommonMethods.findText(driver,text):
                logging.info('Found searching text "'+text+'"')
                 
            else:
                logging.error('Failed to find the text "'+text+'" in method verifythetext')
                pytest.fail('Failed to find the text')
         
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verifythetext')
             
        except:
            CommonMethods.exception(driver, featureFileName, 'verifythetext')
      
         
    def verify_the_button(self,driver,text):
        try:
            if CommonMethods.findButton(driver, text):
                logging.info('Found searching button "'+text+'"')
            else:
                logging.error('Failed to find the button "'+text+'" in method verifythebutton')  
                pytest.fail('Failed to find the button')
         
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verifythebutton')
             
        except:
            CommonMethods.exception(driver, featureFileName, 'verifythebutton')
               
         
    def verify_the_link(self,driver,text):
        try:
            if CommonMethods.findLink(driver, text):
                logging.info('Found searching link "'+text+'"')
            else:
                logging.error('Failed to find the link "'+text+'" in method verifythelink')
                pytest.fail('Failed to find the link')    
     
         
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verifythelink')
             
        except:
            CommonMethods.exception(driver, featureFileName, 'verifythelink')
    
    
    def verify_greeting_text(self,driver):
        try:
            actual_text =CommonMethods.getAttributeOfElement(driver,'text', self.header_title_text)
            check = CommonMethods.verifyTextMatch(actual_text, 'Verify')
            if check == True:
                logging.info('User is in OTP verification screen')
            else:
                logging.error('Failed to verify greeting text')
                pytest.fail('User is not in OTP verification screen')
                 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_greeting_text')
                     
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_greeting_text')        
    
         
    def verify_field(self,driver,locator,Field):
        try:
            check = CommonMethods.isElementPresent(driver, locator)
            if check == True:
                logging.info(Field+' is verified on register otp screen')    
            else:
                logging.error('Failed to verify the '+ Field)
                pytest.fail('Searching field '+Field +' is not found')
     
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verifyField')
                     
        except:
            CommonMethods.exception(driver, featureFileName, 'verifyField')
    
            
    def otp_bottom_sheet_dialog_shown(self,driver):
    
        check = CommonMethods.isElementPresent(driver, self.otp_header_layout)
        if check == True:
            logging.info('Bottom sheet dialog is shown')
        else:
            logging.error('Failed to display bottom sheet dialog')
            pytest.fail('Bottom sheet dialog is not shown,failed in method otp_bottom_sheet_dialog_shown')

    
    def verify_loading_spiner(self,driver):
        check = CommonMethods.isElementPresent(driver, self.progressBar)
        if check == True:
            logging.info('Progress bar is shown in bottom sheet dialog')
        else:
            logging.error('Failed to shown Progress bar in bottom sheet dialog')
            pytest.fail('Failed to shown Progress bar,failed in method verify_loading_spiner')
    
            
    def verify_count_down_timer(self,driver):
        check = CommonMethods.isElementPresent(driver, self.Countdowntimer)
        if check == True:
            logging.info('Count down timer is shown in bottom sheet dialog')
        else:
            logging.error('Failed to shown Count down time in bottom sheet dialog')
            pytest.fail('Failed to shown Count down timer,failed in method verify_count_down_timer')
    
            
    def tap_device_backbtn(self,driver):
        try:
            CommonMethods.click_on_device_back_btn(driver)
            logging.info('User tapped on back button')
        except:
            logging.error('Failed tap on device back button')
            pytest.fail('Failed in method tap_device_backbtn')
    
    
    def dismiss_otp_pop_up(self,driver):
        try:
            if CommonMethods.isElementPresent(driver,self.otp_header_layout):
                CommonMethods.click_on_device_back_btn(driver)
            else:
                logging.error('Failed to dismiss the pop up')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'dismiss_otp_pop_up')
                     
        except:
            CommonMethods.exception(driver, featureFileName, 'dismiss_otp_pop_up')
              
    
    def verify_otp_field(self,driver):
        self.verify_field(driver,self.otp,'OTP Field')
    
        
    def verify_phoneno_country_code(self,driver):
        self.verify_field(driver,self.loginPhoneNo,'Phone number Field')
        self.verify_field(driver,self.loginCountryID,'CountryCode')
    
    
    def verify_resend_call_button(self,driver,text):
        try:
            check = CommonMethods.isElementPresent(driver, self.ResendCallMe)
            if check == True:
                actual_text =CommonMethods.getAttributeOfElement(driver, 'text', self.ResendCallMe)
                if actual_text =="Resend":
                    logging.info('Resend button is shown')
                elif actual_text =="Call me":
                    logging.info('Call me button is shown')
                else:
                    logging.error('Failed to shown '+text)
                    pytest.fail("Failed to shown "+text+ " in method verify_resend_call_button")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_resend_call_button')
                     
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_resend_call_button')        
                
            
    def navigate_to_screen(self,driver,expectedText,locator):
        try:
            CommonMethods.wait_for_locator(driver,locator, 10)
            actual_text =CommonMethods.getAttributeOfElement(driver,'text', locator)
            check = CommonMethods.verifyTextMatch(actual_text, expectedText)
            if check == True:
                logging.info('User navigated to expected screen')
            else:
                logging.error('Failed to navigate to expected screen in method navigate_to_screen')
                pytest.fail('Failed in method "navigate_to_screen"')   
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'navigate_to_screen')
                
        except:
            CommonMethods.exception(driver, featureFileName, 'navigate_to_screen')    
    
    
    def verify_toast_msg(self,driver,text):
        try:
#             sleep(2)
            CommonMethods.wait_for_locator(driver, self.toast_msg, 10)
            check=CommonMethods.isElementPresent(driver, self.toast_msg)
            if check == True:
                act_txt=CommonMethods.getTextOfElement(driver,self.toast_msg)
                logging.info('Found toast message '+act_txt)
                exp_txt= text
                assert act_txt == exp_txt ,"Toast message is not matching"
            else:
                logging.info("toast text verification failed ")
                pytest.fail("toast text verification failed ")    
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'verify_toast_msg')    
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_toast_msg')
        
        
    def tap_edit_option(self,driver):
        try:
            if CommonMethods.isElementPresent(driver,self.otp_header_layout):
                CommonMethods.click_on_device_back_btn(driver)
            CommonMethods.wait_for_locator(driver, self.loginPhoneNo, 10)
            if CommonMethods.elementClick(driver,self.loginPhoneNo):
                logging.info('Tapped on edit option')
            else:
                logging.info("Failed to click on edit option")
                pytest.fail("Failed to click on edit option in method tap_edit_option")
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'tap_edit_option')    
        except:
            CommonMethods.exception(driver, featureFileName, 'tap_edit_option')
    
           
    def verify_mobile_number_field(self,driver):
        self.verify_field(driver,self.phonetextfield,'Mobile Number field')
    
        
    def phonenumber_autofill(self,driver):
        try:
            check =CommonMethods.getAttributeOfElement(driver,'text', self.phonetextfield)
            if check !='':
                logging.info('Phone number field is autofilled')
            else:
                logging.error('Phone number field is autofilled')
                pytest.fail('Failed in method phonenumber_autofill')
                    
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'phonenumber_autofill')
                
        except:
            CommonMethods.exception(driver, featureFileName, 'phonenumber_autofill')
    
            
    def verify_country_code_dropdown(self,driver):
        self.verify_field(driver,self.countrycodedrop_down_text_view,'Country code drop down')  
    
    
    def country_code_dropdown_click(self,driver):
        try:
            CommonMethods.elementClick(driver, self.countrycodedrop_down)
            logging.info('Clicked on country code drop down')
            
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'country_code_dropdown_click')    
             
        except:
            CommonMethods.exception(driver, featureFileName, 'country_code_dropdown_click')
            logging.error('Failed to click on country_code_dropdown')
        
        
    def select_country_code(self,driver,CountryName,CountryCode):
        try:
            if CommonMethods.elementClick(driver,(By.XPATH,"//*[contains(@text, \'"+CountryName+"\')]")):                             
                CommonMethods.wait_for_locator(driver, self.countrycodedrop_down_text_view,20)
                country_code =CommonMethods.getAttributeOfElement(driver,'text', self.countrycodedrop_down_text_view)
                CommonMethods.verifyTwoText(country_code, CountryCode)
                logging.info('Selected country is '+CountryName+' and the country code is '+country_code)
            else:
                logging.error('Failed to verify the country code')
                pytest.fail('Failed to verify the country code in method select_country_code') 
                 
            
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'select_country_code')    
             
        except:
            CommonMethods.exception(driver, featureFileName, 'select_country_code')
               
   
    def verify_country_code(self,driver):
        try:
            country_code =CommonMethods.getAttributeOfElement(driver,'text', self.countrycodedrop_down_text_view)
            if country_code ==self.countrycode:
                logging.info('Country is matching')
            else:
                logging.error('Mismatch in country code')
                pytest.fail('Failed to verify')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_country_code')    
             
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_country_code')
        
                    
    def tap_on_next_button(self,driver):
        try:
            if CommonMethods.elementClick(driver, self.btnRegister):
                logging.info('Clicked on Next button')
            else:
                pytest.fail('Failed to click on Next button')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_next_button')    
             
        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_next_button')
                
 
    def clear_mobile_number_field(self,driver):
            CommonMethods.enterText(driver,'', self.phonetextfield)  
    
            
    def phonenumber_field_errormessage(self,driver,text):
        try:
            phone_error = CommonMethods.getAttributeOfElement(driver,'text',self.PhoneErrorMsg)
            if CommonMethods.verifyTwoText( phone_error,text )== True:
                logging.info('The error message is '+  phone_error)
            else:
                logging.error("Failed to find '"+text+ "' error message")
                pytest.fail('Failed in method  phonenumber_field_errormessage')
            
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, ' phonenumber_field_errormessage')    
        except:
            CommonMethods.exception(driver, featureFileName, 'phonenumber_field_errormessage')      
    
    
    def navigate_to_edit_no_screen(self,driver):
        try:
            self.navigate_to_screen(driver,'Access',self.header_greeting_text)
            logging.info('User navigated to Edit number screen')
        except:
            CommonMethods.exception(driver, featureFileName, 'navigate_to_edit_no_screen')  
    
            
    def enter_mobile_number(self,driver,phone_number): 
        try:
            if CommonMethods.enterText(driver,phone_number,self.phonetextfield):
                logging.info('User entered  phone number '+ phone_number)
            else:    
                logging.error('failed to enter phone number')
            
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'enter_mobile_number')
                
        except:
            CommonMethods.exception(driver, featureFileName, 'enter_mobile_number') 
    
    
    def navigated_to_otp_verification_screen(self,driver):
        try:
            if CommonMethods.isElementPresent(driver,self.otp_header_layout):
                CommonMethods.click_on_device_back_btn(driver)
            self.navigate_to_screen(driver,'To complete registration',self.subtitle_text)
            logging.info('User navigated to OTP verification screen')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'navigated_to_otp_verification_screen')
                
        except:
            CommonMethods.exception(driver, featureFileName, 'navigated_to_otp_verification_screen') 
            

    def verify_entered_phone_number(self,driver,phone_number):
        try:
            phonenumber_otp =CommonMethods.getAttributeOfElement(driver,'text', self.loginPhoneNo)
            if phonenumber_otp ==phone_number:
                logging.info('The phone number in the edit number screen is same as phone number in otp verification')
            else:
                logging.error('Mismatch in Phone number')
                pytest.fail('Failed to match the phone number in method verify_entered_phone_number')
        
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_entered_phone_number')
                
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_entered_phone_number')
    
             
    def relaunch_the_app(self,driver,App):
        try:
            driver.activate_app(App)
            logging.info('App is launched')

        except:
            CommonMethods.exception(driver, featureFileName, 'relaunch_the_app')
    
            
    def verify_app_closed(self,driver,text):
        try:
            check = CommonMethods.isAppActive(driver,text)
            if check == 3:
                logging.info('App is closed')
            else:
                logging.error(" App is Not Closed")
                pytest.fail("App is not closed")
                 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver,featureFileName,'verifyAppIsClosed')
                     
        except :
            CommonMethods.exception(driver,featureFileName,'verifyAppIsClosed')
    
        
    def navigated_to_the_screen(self,driver,text):
        try:
            if CommonMethods.isElementPresent(driver, self.gms_cancel):
                CommonMethods.elementClick(driver,self.gms_cancel)
            self.navigate_to_screen(driver,text,self.header_title_text)
            logging.info('User is in ' +text + 'screen')
                
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'navigated_to_the_screen')    

        except:
            CommonMethods.exception(driver, featureFileName, 'navigated_to_the_screen')        
    
            
    def tap_on_link(self,driver,text):
        try:
            CommonMethods.elementClick(driver, (By.XPATH,"//android.widget.TextView[@text=\'"+text+"\']"))
            
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_link')    
             
        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_link')
            logging.error('Failed to click on "'+ text+ '"')     
    
        
    def click_on_resend_callme_btn(self,driver):
        try:
            CommonMethods.elementClick(driver, self.ResendCallMe)
            logging.info('Clicked on button Resend/ Call button')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'click_on_resend_callme_btn')    
             
        except:
            CommonMethods.exception(driver, featureFileName, 'click_on_resend_callme_btn')
    
            
    def verify_reg_otpscn_phone_number(self,driver):
        try:
            phonenumber_otp =CommonMethods.getAttributeOfElement(driver,'text', self.loginPhoneNo)
            if phonenumber_otp ==self.reg_phone_number:
                logging.info('The phone number on otp verification screen is same as phone number in registration screen')
            else:
                logging.error('Mismatch in Phone number')
                pytest.fail('Failed to match the phone number in method verify_reg_otpscn_phone_number')
        
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_reg_otpscn_phone_number')
                
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_reg_otpscn_phone_number')
    
            
    def enter_otp(self,driver,otp): 
        try:
            if CommonMethods.isElementPresent(driver, self.otp):
                CommonMethods.enterText(driver,otp,self.otp)
                logging.info('User entered otp is '+ otp)
            else:    
                logging.error('failed to enter otp')
                pytest.fail('failed to enter otp')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'enter_otp')
                
        except:
            CommonMethods.exception(driver, featureFileName, 'enter_otp')
    
    
    def wait_till_element(self,driver):
        try:
            CommonMethods.isElementPresent(driver,self.otp)
            pass
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'wait_till_element')
                
        except:
            CommonMethods.exception(driver, featureFileName, 'wait_till_element')
        
        
    def verify_snackbar_msg(self,driver,text):
        try:
            check=CommonMethods.isElementPresent(driver, self.snackbar_text)
            if check == True:
                act_txt=CommonMethods.getTextOfElement(driver,self.snackbar_text)
                logging.info('Found snackbar text '+act_txt)
                exp_txt= text
                assert act_txt == exp_txt ,"Snackbar message is not matching"
            else:
                logging.info("Snackbar message verification failed ")
                pytest.fail("Snackbar message verification failed ")    
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'verify_snackbar_msg')    
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_snackbar_msg')
    
            
    def two_line_toast_msg(self,driver,text):
        try:
            check=CommonMethods.isElementPresent(driver, self.toast_msg)
            if check == True:
                act_txt=CommonMethods.getTextOfElement(driver,self.toast_msg)
                logging.info('Found toast message '+act_txt)
                actual_text1 = act_txt.split()
                actual_text = " ".join(actual_text1)
                assert actual_text == text ,"Toast message is not matching"
            else:
                logging.info("toast text verification failed ")
                pytest.fail("toast text verification failed ")    
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(driver,featureFileName,'verify_toast_msg')    
        except:
            CommonMethods.exception(driver, featureFileName, 'verify_toast_msg')
            
    def tap_on_location_icon(self,driver):
        try:
            if CommonMethods.isElementPresent(driver,self.citytextfield):
                element =CommonMethods.getElement(driver,self.citytextfield)
                loc = element.rect   
                x = loc['x']
                y = loc['y']
                height = loc['height']
                width = loc['width']
                x2 = (x+width)-5
                y2 = (y+height)-5
                CommonMethods.run('adb shell input tap {} {}'.format(x2, y2)) 
            else:
                logging.error('Failed to tap on location icon')
                pytest.fail('Failed to tap on location icon')
                    
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_location_icon')    

        except:
            CommonMethods.exception(driver, featureFileName, 'tap_on_location_icon') 
        
    