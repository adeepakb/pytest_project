import time
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
from selenium.webdriver.common.by import By
from Utilities.common_methods import CommonMethods
from selenium.common.exceptions import NoSuchElementException
import logging
import re
import pytest
from conftest import browser
from Constants.load_json import *
from Constants.constants import Registration_data

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

    def __init__(self, browser):
        self.browser = browser
        
    def launch_the_app(self,browser):
        try:
            if CommonMethods.isElementPresent(browser, self.allowbutton):  
                CommonMethods.elementClick(browser, self.allowbutton)
                CommonMethods.elementClick(browser, self.allowbutton)
                sleep(3)
            if CommonMethods.isElementPresent(browser,self.loginRegBtn):
                if CommonMethods.isElementPresent(browser, self.gms_cancel):
                    CommonMethods.elementClick(browser,self.gms_cancel)
                CommonMethods.elementClick(browser, self.loginRegBtn)
            if CommonMethods.isElementPresent(browser,self.skipButton):
                logging.info('User is in onboarding screen')
                CommonMethods.elementClick(browser,self.skipButton)
            CommonMethods.elementClick(browser, self.grade8th)
            if CommonMethods.isElementPresent(browser, self.gms_cancel):
                CommonMethods.elementClick(browser,self.gms_cancel)
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'launch_the_app')
                
        except:
            CommonMethods.exception(browser, featureFileName, 'launch_the_app')
        
    
    def navigate_to_reg_otp_screen(self,browser):
        try:
            if CommonMethods.isElementPresent(browser,self.nametextfield):
                CommonMethods.enterText(browser,getdata(data_file, 'user_details', 'name'), self.nametextfield)
                CommonMethods.enterText(browser,getdata(data_file, 'user_details', 'mobile'), self.phonetextfield)
                self.countrycode = CommonMethods.getAttributeOfElement(browser,'text', self.countrycodedrop_down_text_view)
                self.reg_phone_number=CommonMethods.getAttributeOfElement(browser,'text', self.phonetextfield)
                CommonMethods.enterText(browser,getdata(data_file, 'user_details', 'email'), self.emailtextfield)
                actual_text =CommonMethods.getAttributeOfElement(browser,'text', self.citytextfield)
                check = CommonMethods.verifyTextMatch(actual_text, 'City / Nearest location')
                if check == True:
                    self.tap_on_location_icon(browser)
                    if CommonMethods.isElementPresent(browser, self.location_ok):
                        CommonMethods.elementClick(browser, self.location_ok)
                        self.tap_on_location_icon(browser)
                    sleep(3)
#                 else: 
#                     CommonMethods.enterText(browser,getdata(data_file, 'user_details', 'city'), self.citytextfield)
                
                CommonMethods.elementClick(browser, self.btnRegister)
                CommonMethods.wait_for_locator(browser, self.otp_header_layout, 20)
                logging.info('Register OTP Verification Screen')
            else:
                logging.error('Failed to navigate to OTP verification screen')
        
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'navigate_to_reg_otp_screen')
                
        except:
            CommonMethods.exception(browser, featureFileName, 'navigate_to_reg_otp_screen')
        
        
    def verify_the_text(self,browser,text):
        try:
            if CommonMethods.findText(browser,text):
                logging.info('Found searching text "'+text+'"')
                 
            else:
                logging.error('Failed to find the text "'+text+'" in method verifythetext')
                pytest.fail('Failed to find the text')
         
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verifythetext')
             
        except:
            CommonMethods.exception(browser, featureFileName, 'verifythetext')
      
         
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
               
         
    def verify_the_link(self,browser,text):
        try:
            if CommonMethods.findLink(browser, text):
                logging.info('Found searching link "'+text+'"')
            else:
                logging.error('Failed to find the link "'+text+'" in method verifythelink')
                pytest.fail('Failed to find the link')    
     
         
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verifythelink')
             
        except:
            CommonMethods.exception(browser, featureFileName, 'verifythelink')
    
    
    def verify_greeting_text(self,browser):
        try:
            actual_text =CommonMethods.getAttributeOfElement(browser,'text', self.header_title_text)
            check = CommonMethods.verifyTextMatch(actual_text, 'Verify')
            if check == True:
                logging.info('User is in OTP verification screen')
            else:
                logging.error('Failed to verify greeting text')
                pytest.fail('User is not in OTP verification screen')
                 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_greeting_text')
                     
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_greeting_text')        
    
         
    def verify_field(self,browser,locator,Field):
        try:
            check = CommonMethods.isElementPresent(browser, locator)
            if check == True:
                logging.info(Field+' is verified on register otp screen')    
            else:
                logging.error('Failed to verify the '+ Field)
                pytest.fail('Searching field '+Field +' is not found')
     
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verifyField')
                     
        except:
            CommonMethods.exception(browser, featureFileName, 'verifyField')
    
            
    def otp_bottom_sheet_dialog_shown(self,browser):
    
        check = CommonMethods.isElementPresent(browser, self.otp_header_layout)
        if check == True:
            logging.info('Bottom sheet dialog is shown')
        else:
            logging.error('Failed to display bottom sheet dialog')
            pytest.fail('Bottom sheet dialog is not shown,failed in method otp_bottom_sheet_dialog_shown')

    
    def verify_loading_spiner(self,browser):
        check = CommonMethods.isElementPresent(browser, self.progressBar)
        if check == True:
            logging.info('Progress bar is shown in bottom sheet dialog')
        else:
            logging.error('Failed to shown Progress bar in bottom sheet dialog')
            pytest.fail('Failed to shown Progress bar,failed in method verify_loading_spiner')
    
            
    def verify_count_down_timer(self,browser):
        check = CommonMethods.isElementPresent(browser, self.Countdowntimer)
        if check == True:
            logging.info('Count down timer is shown in bottom sheet dialog')
        else:
            logging.error('Failed to shown Count down time in bottom sheet dialog')
            pytest.fail('Failed to shown Count down timer,failed in method verify_count_down_timer')
    
            
    def tap_device_backbtn(self,browser):
        try:
            CommonMethods.click_on_device_back_btn(browser)
            logging.info('User tapped on back button')
        except:
            logging.error('Failed tap on device back button')
            pytest.fail('Failed in method tap_device_backbtn')
    
    
    def dismiss_otp_pop_up(self,browser):
        try:
            if CommonMethods.isElementPresent(browser,self.otp_header_layout):
                CommonMethods.click_on_device_back_btn(browser)
            else:
                logging.error('Failed to dismiss the pop up')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'dismiss_otp_pop_up')
                     
        except:
            CommonMethods.exception(browser, featureFileName, 'dismiss_otp_pop_up')
              
    
    def verify_otp_field(self,browser):
        self.verify_field(browser,self.otp,'OTP Field')
    
        
    def verify_phoneno_country_code(self,browser):
        self.verify_field(browser,self.loginPhoneNo,'Phone number Field')
        self.verify_field(browser,self.loginCountryID,'CountryCode')
    
    
    def verify_resend_call_button(self,browser,text):
        try:
            check = CommonMethods.isElementPresent(browser, self.ResendCallMe)
            if check == True:
                actual_text =CommonMethods.getAttributeOfElement(browser, 'text', self.ResendCallMe)
                if actual_text =="Resend":
                    logging.info('Resend button is shown')
                elif actual_text =="Call me":
                    logging.info('Call me button is shown')
                else:
                    logging.error('Failed to shown '+text)
                    pytest.fail("Failed to shown "+text+ " in method verify_resend_call_button")
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_resend_call_button')
                     
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_resend_call_button')        
                
            
    def navigate_to_screen(self,browser,expectedText,locator):
        try:
            CommonMethods.wait_for_locator(browser,locator, 10)
            actual_text =CommonMethods.getAttributeOfElement(browser,'text', locator)
            check = CommonMethods.verifyTextMatch(actual_text, expectedText)
            if check == True:
                logging.info('User navigated to expected screen')
            else:
                logging.error('Failed to navigate to expected screen in method navigate_to_screen')
                pytest.fail('Failed in method "navigate_to_screen"')   
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'navigate_to_screen')
                
        except:
            CommonMethods.exception(browser, featureFileName, 'navigate_to_screen')    
    
    
    def verify_toast_msg(self,browser,text):
        try:
#             sleep(2)
            CommonMethods.wait_for_locator(browser, self.toast_msg, 10)
            check=CommonMethods.isElementPresent(browser, self.toast_msg)
            if check == True:
                act_txt=CommonMethods.getTextOfElement(browser,self.toast_msg)
                logging.info('Found toast message '+act_txt)
                exp_txt= text
                assert act_txt == exp_txt ,"Toast message is not matching"
            else:
                logging.info("toast text verification failed ")
                pytest.fail("toast text verification failed ")    
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_toast_msg')    
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_toast_msg')
        
        
    def tap_edit_option(self,browser):
        try:
            if CommonMethods.isElementPresent(browser,self.otp_header_layout):
                CommonMethods.click_on_device_back_btn(browser)
            CommonMethods.wait_for_locator(browser, self.loginPhoneNo, 10)
            if CommonMethods.elementClick(browser,self.loginPhoneNo):
                logging.info('Tapped on edit option')
            else:
                logging.info("Failed to click on edit option")
                pytest.fail("Failed to click on edit option in method tap_edit_option")
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(browser,featureFileName,'tap_edit_option')    
        except:
            CommonMethods.exception(browser, featureFileName, 'tap_edit_option')
    
           
    def verify_mobile_number_field(self,browser):
        self.verify_field(browser,self.phonetextfield,'Mobile Number field')
    
        
    def phonenumber_autofill(self,browser):
        try:
            check =CommonMethods.getAttributeOfElement(browser,'text', self.phonetextfield)
            if check !='':
                logging.info('Phone number field is autofilled')
            else:
                logging.error('Phone number field is autofilled')
                pytest.fail('Failed in method phonenumber_autofill')
                    
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'phonenumber_autofill')
                
        except:
            CommonMethods.exception(browser, featureFileName, 'phonenumber_autofill')
    
            
    def verify_country_code_dropdown(self,browser):
        self.verify_field(browser,self.countrycodedrop_down_text_view,'Country code drop down')  
    
    
    def country_code_dropdown_click(self,browser):
        try:
            CommonMethods.elementClick(browser, self.countrycodedrop_down)
            logging.info('Clicked on country code drop down')
            
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'country_code_dropdown_click')    
             
        except:
            CommonMethods.exception(browser, featureFileName, 'country_code_dropdown_click')
            logging.error('Failed to click on country_code_dropdown')
        
        
    def select_country_code(self,browser,CountryName,CountryCode):
        try:
            if CommonMethods.elementClick(browser,(By.XPATH,"//*[contains(@text, \'"+CountryName+"\')]")):                             
                CommonMethods.wait_for_locator(browser, self.countrycodedrop_down_text_view,20)
                country_code =CommonMethods.getAttributeOfElement(browser,'text', self.countrycodedrop_down_text_view)
                CommonMethods.verifyTwoText(country_code, CountryCode)
                logging.info('Selected country is '+CountryName+' and the country code is '+country_code)
            else:
                logging.error('Failed to verify the country code')
                pytest.fail('Failed to verify the country code in method select_country_code') 
                 
            
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'select_country_code')    
             
        except:
            CommonMethods.exception(browser, featureFileName, 'select_country_code')
               
   
    def verify_country_code(self,browser):
        try:
            country_code =CommonMethods.getAttributeOfElement(browser,'text', self.countrycodedrop_down_text_view)
            if country_code ==self.countrycode:
                logging.info('Country is matching')
            else:
                logging.error('Mismatch in country code')
                pytest.fail('Failed to verify')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_country_code')    
             
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_country_code')
        
                    
    def tap_on_next_button(self,browser):
        try:
            if CommonMethods.elementClick(browser, self.btnRegister):
                logging.info('Clicked on Next button')
            else:
                pytest.fail('Failed to click on Next button')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'tap_on_next_button')    
             
        except:
            CommonMethods.exception(browser, featureFileName, 'tap_on_next_button')
                
 
    def clear_mobile_number_field(self,browser):
            CommonMethods.enterText(browser,'', self.phonetextfield)  
    
            
    def phonenumber_field_errormessage(self,browser,text):
        try:
            phone_error = CommonMethods.getAttributeOfElement(browser,'text',self.PhoneErrorMsg)
            if CommonMethods.verifyTwoText( phone_error,text )== True:
                logging.info('The error message is '+  phone_error)
            else:
                logging.error("Failed to find '"+text+ "' error message")
                pytest.fail('Failed in method  phonenumber_field_errormessage')
            
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, ' phonenumber_field_errormessage')    
        except:
            CommonMethods.exception(browser, featureFileName, 'phonenumber_field_errormessage')      
    
    
    def navigate_to_edit_no_screen(self,browser):
        try:
            self.navigate_to_screen(browser,'Access',self.header_greeting_text)
            logging.info('User navigated to Edit number screen')
        except:
            CommonMethods.exception(browser, featureFileName, 'navigate_to_edit_no_screen')  
    
            
    def enter_mobile_number(self,browser,phone_number): 
        try:
            if CommonMethods.enterText(browser,phone_number,self.phonetextfield):
                logging.info('User entered  phone number '+ phone_number)
            else:    
                logging.error('failed to enter phone number')
            
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'enter_mobile_number')
                
        except:
            CommonMethods.exception(browser, featureFileName, 'enter_mobile_number') 
    
    
    def navigated_to_otp_verification_screen(self,browser):
        try:
            if CommonMethods.isElementPresent(browser,self.otp_header_layout):
                CommonMethods.click_on_device_back_btn(browser)
            self.navigate_to_screen(browser,'To complete registration',self.subtitle_text)
            logging.info('User navigated to OTP verification screen')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'navigated_to_otp_verification_screen')
                
        except:
            CommonMethods.exception(browser, featureFileName, 'navigated_to_otp_verification_screen') 
            

    def verify_entered_phone_number(self,browser,phone_number):
        try:
            phonenumber_otp =CommonMethods.getAttributeOfElement(browser,'text', self.loginPhoneNo)
            if phonenumber_otp ==phone_number:
                logging.info('The phone number in the edit number screen is same as phone number in otp verification')
            else:
                logging.error('Mismatch in Phone number')
                pytest.fail('Failed to match the phone number in method verify_entered_phone_number')
        
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_entered_phone_number')
                
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_entered_phone_number')
    
             
    def relaunch_the_app(self,browser,App):
        try:
            browser.activate_app(App)
            logging.info('App is launched')

        except:
            CommonMethods.exception(browser, featureFileName, 'relaunch_the_app')
    
            
    def verify_app_closed(self,browser,text):
        try:
            check = CommonMethods.isAppActive(browser,text)
            if check == 3:
                logging.info('App is closed')
            else:
                logging.error(" App is Not Closed")
                pytest.fail("App is not closed")
                 
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verifyAppIsClosed')
                     
        except :
            CommonMethods.exception(browser,featureFileName,'verifyAppIsClosed')
    
        
    def navigated_to_the_screen(self,browser,text):
        try:
            if CommonMethods.isElementPresent(browser, self.gms_cancel):
                CommonMethods.elementClick(browser,self.gms_cancel)
            self.navigate_to_screen(browser,text,self.header_title_text)
            logging.info('User is in ' +text + 'screen')
                
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'navigated_to_the_screen')    

        except:
            CommonMethods.exception(browser, featureFileName, 'navigated_to_the_screen')        
    
            
    def tap_on_link(self,browser,text):
        try:
            CommonMethods.elementClick(browser, (By.XPATH,"//android.widget.TextView[@text=\'"+text+"\']"))
            
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'tap_on_link')    
             
        except:
            CommonMethods.exception(browser, featureFileName, 'tap_on_link')
            logging.error('Failed to click on "'+ text+ '"')     
    
        
    def click_on_resend_callme_btn(self,browser):
        try:
            CommonMethods.elementClick(browser, self.ResendCallMe)
            logging.info('Clicked on button Resend/ Call button')
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'click_on_resend_callme_btn')    
             
        except:
            CommonMethods.exception(browser, featureFileName, 'click_on_resend_callme_btn')
    
            
    def verify_reg_otpscn_phone_number(self,browser):
        try:
            phonenumber_otp =CommonMethods.getAttributeOfElement(browser,'text', self.loginPhoneNo)
            if phonenumber_otp ==self.reg_phone_number:
                logging.info('The phone number on otp verification screen is same as phone number in registration screen')
            else:
                logging.error('Mismatch in Phone number')
                pytest.fail('Failed to match the phone number in method verify_reg_otpscn_phone_number')
        
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'verify_reg_otpscn_phone_number')
                
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_reg_otpscn_phone_number')
    
            
    def enter_otp(self,browser,otp): 
        try:
            if CommonMethods.isElementPresent(browser, self.otp):
                CommonMethods.enterText(browser,otp,self.otp)
                logging.info('User entered otp is '+ otp)
            else:    
                logging.error('failed to enter otp')
                pytest.fail('failed to enter otp')

        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'enter_otp')
                
        except:
            CommonMethods.exception(browser, featureFileName, 'enter_otp')
    
    
    def wait_till_element(self,browser):
        try:
            CommonMethods.isElementPresent(browser,self.otp)
            pass
        except NoSuchElementException:
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'wait_till_element')
                
        except:
            CommonMethods.exception(browser, featureFileName, 'wait_till_element')
        
        
    def verify_snackbar_msg(self,browser,text):
        try:
            check=CommonMethods.isElementPresent(browser, self.snackbar_text)
            if check == True:
                act_txt=CommonMethods.getTextOfElement(browser,self.snackbar_text)
                logging.info('Found snackbar text '+act_txt)
                exp_txt= text
                assert act_txt == exp_txt ,"Snackbar message is not matching"
            else:
                logging.info("Snackbar message verification failed ")
                pytest.fail("Snackbar message verification failed ")    
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_snackbar_msg')    
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_snackbar_msg')
    
            
    def two_line_toast_msg(self,browser,text):
        try:
            check=CommonMethods.isElementPresent(browser, self.toast_msg)
            if check == True:
                act_txt=CommonMethods.getTextOfElement(browser,self.toast_msg)
                logging.info('Found toast message '+act_txt)
                actual_text1 = act_txt.split()
                actual_text = " ".join(actual_text1)
                assert actual_text == text ,"Toast message is not matching"
            else:
                logging.info("toast text verification failed ")
                pytest.fail("toast text verification failed ")    
        except NoSuchElementException :
            CommonMethods.noSuchEleExcept(browser,featureFileName,'verify_toast_msg')    
        except:
            CommonMethods.exception(browser, featureFileName, 'verify_toast_msg')
            
    def tap_on_location_icon(self,browser):
        try:
            if CommonMethods.isElementPresent(browser,self.citytextfield):
                element =CommonMethods.getElement(browser,self.citytextfield)
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
            CommonMethods.noSuchEleExcept(browser, featureFileName, 'tap_on_location_icon')    

        except:
            CommonMethods.exception(browser, featureFileName, 'tap_on_location_icon') 
        
    