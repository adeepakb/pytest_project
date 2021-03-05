import time
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
from selenium.webdriver.common.by import By
from utilities.common_methods import CommonMethods
from utilities.interrupt import *
from selenium.common.exceptions import NoSuchElementException
import logging
import re
from PIL import Image
from pytesseract import image_to_string
import pytest
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from conftest import driver
from constants.load_json import *
from constants.constants import Registration_data



CommonMethods = CommonMethods()
data_file = Registration_data

featureFileName = 'Register Screen'

class RegScreen():

        #Locator ID
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
        AlreadyHaveAccount=(By.ID,"com.byjus.thelearningapp:id/tvAlreadyHaveAccountBl")
        LoginBtnLink=(By.ID,"com.byjus.thelearningapp:id/tvLoginBl")
        PrivacyPolicyBtn = (By.ID,"com.byjus.thelearningapp:id/tvPrivacyPolicyBl")
        Andtext = (By.ID,"com.byjus.thelearningapp:id/tvAndBl")
        TermsAndConditionsBtn = (By.ID,"com.byjus.thelearningapp:id/tvTermsAndConditionsBl")
        PhoneErrorMsg =(By.ID,"com.byjus.thelearningapp:id/tvPhoneError")
        permission_message=(By.ID,"com.android.packageinstaller:id/permission_message")
        App_backBtn=(By.ID,"com.byjus.thelearningapp:id/roundedNavButton")
        secondaryActionBtn =(By.ID,"com.byjus.thelearningapp:id/secondaryAction")
        primaryActionBtn=(By.ID,"com.byjus.thelearningapp:id/primaryAction")
        dialogBox_title =(By.ID,"com.byjus.thelearningapp:id/dialog_title")
        dialogBox_msg=(By.ID,"com.byjus.thelearningapp:id/dialog_message")
        textViewXpath=(By.ID,"//android.widget.TextView")
        loginBtn =(By.ID,"com.byjus.thelearningapp:id/btnLogin")
        loginRegBtn =(By.ID,'com.byjus.thelearningapp:id/tvRegister')
        permission_message=(By.ID,'com.android.packageinstaller:id/permission_message')
        header_subtitle_text =(By.ID,"com.byjus.thelearningapp:id/header_subtitle_text")
        hint_element_list =(By.XPATH,"//android.widget.TextView[@resource-id='com.google.android.gms:id/credential_primary_label']")
        snackbar_text =(By.ID,"com.byjus.thelearningapp:id/snackbar_text")
        location_ok=(By.ID,"android:id/button1")
        regscn_lgnbtn=(By.ID,"com.byjus.thelearningapp:id/tvLoginBl")
        email_xpath =(By.XPATH,"//*[contains(@text, '.com')]")
        google_account =None
        hint_dialog= None   
        
        def __init__(self, driver):
            self.driver = driver  
            
        phone_number = None
        email = None
        
        def allow_permissions(self,driver):
            try:
                if CommonMethods.isElementPresent(driver, self.allowbutton):  
                    CommonMethods.elementClick(driver, self.allowbutton)
                    logging.info('Allowed device Location permission')
                    CommonMethods.elementClick(driver, self.allowbutton)
                    logging.info('Allowed device contacts permission')
                
                elif self.find_os_version(driver)<'6':
                    logging.info('Os version of the device is below 6, hence permission pop up will not be shown')
                
                else:
                    logging.error('Failed to allow the the permissions in method allow_permissions')
                    pytest.fail('Permissions are not allowed')

            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'allow_permissions')
                
            except:
                CommonMethods.exception(driver, featureFileName, 'allow_permissions')
                
                
        def deny_permissions(self,driver):
            try:
                if CommonMethods.isElementPresent(driver, self.denybutton):
                    CommonMethods.elementClick(driver, self.denybutton)
                    logging.info('Denied device Location permission')
                    CommonMethods.elementClick(driver, self.denybutton)
                    logging.info('Denied device contacts permission')
                
                elif self.find_os_version(driver)<'6':
                    logging.info('Os version of the device is below 6, hence permission pop up will not be shown')
                else:
                    logging.error('Failed to deny the the permissions in method deny_permissions')
                    pytest.fail('Permissions are not Denied')
            
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'deny_permissions')
                
            except:
                CommonMethods.exception(driver, featureFileName, 'deny_permissions')
                

        def navigate_to_reg_screen(self,driver):
            try:
                sleep(2)
                if CommonMethods.isElementPresent(driver,self.loginRegBtn):
                    if CommonMethods.isElementPresent(driver, self.gms_cancel):
                        CommonMethods.elementClick(driver,self.gms_cancel)
                    CommonMethods.elementClick(driver, self.loginRegBtn)
                if CommonMethods.isElementPresent(driver,self.skipButton):
                    logging.info('User is in onboarding screen')
                    CommonMethods.elementClick(driver, self.skipButton)
                CommonMethods.elementClick(driver, self.grade8th)
                if CommonMethods.isElementPresent(driver, self.gms_cancel):
                    CommonMethods.elementClick(driver,self.gms_cancel)
                logging.info('User navigated to registration screen') 
       
                
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'navigateToRegScreen')
                
            except:
                CommonMethods.exception(driver, featureFileName, 'navigateToRegScreen')
                pytest.fail('Failed to navigate to registration screen')
                

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
                actual_text =CommonMethods.getAttributeOfElement(driver,'text', self.header_greeting_text)
                check = CommonMethods.verifyTextMatch(actual_text, 'Access')
                if check == True:
                    logging.info('User is in registration screen')
                else:
                    logging.error('Failed to verify greeting text')
                    pytest.fail('User is not in registration screen')
            
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_greeting_text')
                
            except:
                CommonMethods.exception(driver, featureFileName, 'verify_greeting_text')        
                
        
        def verify_field(self,driver,locator,Field):
            try:
                check = CommonMethods.isElementPresent(driver, locator)
                if check == True:
                    logging.info(Field+' is verified on register screen')
                
                else:
                    logging.error('Failed to verify the '+ Field)
                    pytest.fail('Searching field '+Field +' is not found')

            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'verifyField')
                
            except:
                CommonMethods.exception(driver, featureFileName, 'verifyField')
                
                
        def verify_name_field(self,driver):
            self.verify_field(driver,self.nametextfield,'Name Field')
        
                
        def verify_mobile_number_field(self,driver):
            self.verify_field(driver,self.phonetextfield,'Mobile Number field')
        
            
        def verfy_email_field(self,driver):
            self.verify_field(driver,self.emailtextfield,'Email ID field')
        
            
        def verfy_city_field(self,driver):
            self.verify_field(driver,self.emailtextfield,'The City / Nearest Location field')
        
            
        def email_field_is_empty(self,driver):
            try:
                actual_text =CommonMethods.getAttributeOfElement(driver,'text', self.emailtextfield)
                check = CommonMethods.verifyTextMatch(actual_text, 'Email')
                if check == True:
                    logging.info('Email field is empty')
                elif self.google_account==True:
                    logging.error('Email field is not empty')
                    logging.error('Goggle account is added in the device')
                else:
                    logging.error('Email field is not empty')
                    pytest.fail('Failed in method "email_field_is_empty"')
                    
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'email_field_is_empty')
                
            except:
                CommonMethods.exception(driver, featureFileName, 'email_field_is_empty')
                
                
        def city_field_is_empty(self,driver):
            try:
                actual_text =CommonMethods.getAttributeOfElement(driver,'text', self.citytextfield)
                check = CommonMethods.verifyTextMatch(actual_text, 'City / Nearest location')
                if check == True:
                    logging.info('City field is empty')
                else:
                    logging.error('city field is not empty')
                    pytest.fail('Failed in method "city_field_is_empty"') 

            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'city_field_is_empty')
                
            except:
                CommonMethods.exception(driver, featureFileName, 'city_field_is_empty')
                
                
        def click_on_name_field(self,driver):
            try:
                CommonMethods.elementClick(driver, self.nametextfield)
                logging.info('User tapped on name field in method "click_on_name_field"')
            
            except:
                logging.error('Failed to click on name field in method "click_on_name_field"')
                pytest.fail('Failed to click on the filed')
            
   
        def enter_name(self,driver,Characters):
            try:
                check =Characters.isalpha() or ' ' in Characters
                if check == True:
                    CommonMethods.enterText(driver, Characters, self.nametextfield)
                    logging.info('You have entered name '+ Characters)
                else:   
                    logging.error('Only characters are allowed to enter in name field and you are trying to enter '+ Characters)
                    
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'enter_name')
                
            except:
                CommonMethods.exception(driver, featureFileName, 'enter_name')
                
            
        def tap_device_backbtn(self,driver):
            try:
                CommonMethods.click_on_device_back_btn(driver)
                logging.info('User tapped on back button')
            except:
                logging.error('Failed tap on device back button')
                pytest.fail('Failed in method tap_device_backbtn')


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
               
                
        def navigate_to_course_selection_screen(self,driver):
            self.navigate_to_screen(driver,'Choose',self.header_greeting_text)
            logging.info('User navigated to "CourseSelectionScreen"')
        
            
        def check_google_account(self,driver):
            check = self.verify_google_account(driver)
            if check == True:
                logging.info('Google account is added in the device')
            else:
                logging.error('Google account is not registered')
#                 pytest.fail('Google account is not registered')
            #CommonMethods.terminate_settings(driver)
            driver.activate_app('com.byjus.thelearningapp')
        
        
        def google_account_not_added(self,driver):
            check = self.verify_google_account(driver)
            if check == False:
                logging.info('Google account is not added in the device')
            else:
                logging.error('Google account is added in the device')
#                 pytest.fail('Google account is added in the device')
            driver.activate_app('com.byjus.thelearningapp')     
        
                
        def check_email_address(self,driver):
            try:
                CommonMethods.wait_for_locator(driver,self.emailtextfield, 10)
                check =CommonMethods.getAttributeOfElement(driver,'text', self.emailtextfield)
                if check != 'Email':
                    logging.info('Email field is auto filled')
                elif self.find_os_version(driver)>='8':
                    logging.info('Os version of the device is above 8, Email field is empty')
                elif self.google_account ==False:
                    logging.error('Google account is not added in the device')
                else:
                    logging.error('Email field is not auto filled')
                    pytest.fail('Email field is empty. Either app is failing to auto fill or google account is not added in the device')
                    
                
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'check_email_address')
                
            except:
                CommonMethods.exception(driver, featureFileName, 'check_email_address')

                
        def check_city(self,driver):
            try:
                actual_text =CommonMethods.getAttributeOfElement(driver,'text', self.citytextfield)
                check = CommonMethods.verifyTextMatch(actual_text, 'City / Nearest location')
                if check == True:
                    self.tap_on_location_icon(driver)
                    if CommonMethods.isElementPresent(driver, self.location_ok):
                        CommonMethods.elementClick(driver, self.location_ok)
                        self.tap_on_location_icon(driver)
                    sleep(3)
                check =CommonMethods.getAttributeOfElement(driver,'text', self.citytextfield)
                if check != 'City / Nearest location':
                    logging.info('City field auto filled')
                    
                else:
                    logging.error('Failed to verify the address')
                    pytest.fail('Failed in method check_city')
                    
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'check_city')
                
            except:
                CommonMethods.exception(driver, featureFileName, 'check_city')
                               
                        
        def click_mobile_num_field(self,driver):
            try:
                CommonMethods.clearData(driver, self.phonetextfield)
                CommonMethods.elementClick(driver, self.phonetextfield)
                logging.info('User tapped on mobile number field in method "click_mobile_num_field"')
            
            except:
                logging.error('Failed to click on mobile number in method "click_mobile_num_field"')
                pytest.fail('Failed in method "click_mobile_num_field"')
        
         
        def is_keypad_enabled(self,driver):
                check =CommonMethods.isKeyBoardShown(driver)
                if check == True:
                    pass
                else:
                    logging.error('Failed to show keypad in method is_keypad_enabled')

                
        def enter_mobile_number(self,driver,phone_number): 
            try:
                check=phone_number.isdigit()
                if check == True: 
                    CommonMethods.enterText(driver,phone_number,self.phonetextfield)
                    logging.info('User entered  phone number '+ phone_number)
                else:
                    logging.error('Only numerics are allowed to enter in phone number field and you have entered '+ phone_number)
            
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'enter_mobile_number')
                
            except:
                CommonMethods.exception(driver, featureFileName, 'enter_mobile_number')
                
                
        def tap_on_regbtn(self,driver):
            try:
                CommonMethods.elementClick(driver, self.btnRegister)  
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_regbtn')
                
            except:
                CommonMethods.exception(driver, featureFileName, 'tap_on_regbtn')
                logging.error('Failed to tap on register button')  
         

         
        def name_field_toast_Msg(self,driver):
            try:
                CommonMethods.run('adb shell input touchscreen swipe 537 483 537 1000')
                CommonMethods.hideKeyboard(driver)
                CommonMethods.wait_for_locator(driver, self.nametextfield, 5)
                CommonMethods.elementClick(driver,self.nametextfield)
                CommonMethods.hideKeyboard(driver)
                self.extracting_text_from_image(driver,r'Please enter your name.','Please enter your name.')
                
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'name_field_toast_Msg')   
            

        def phonenumber_field_errormessage(self,driver):
            try:
                phone_error = CommonMethods.getAttributeOfElement(driver,'text',self.PhoneErrorMsg)
                if CommonMethods.verifyTwoText( phone_error, 'Please enter your mobile number')== True:
                    logging.info('The error message is '+  phone_error)
                else:
                    logging.error("Failed to find 'Please enter your mobile number'")
                    pytest.fail('Failed in method  phonenumber_field_errormessage')
            
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, ' phonenumber_field_errormessage')    
            except:
                CommonMethods.exception(driver, featureFileName, 'phonenumber_field_errormessage')
   
                
        def verify_city_toastmsg(self,driver):
            try:
                CommonMethods.wait_for_locator(driver, self.citytextfield, 5)
                CommonMethods.elementClick(driver,self.citytextfield)
                CommonMethods.hideKeyboard(driver)
                self.extracting_text_from_image(driver,r'Please enter your city','Please enter your city')

            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_city_toastmsg')    
             
            except:
                CommonMethods.exception(driver, featureFileName, 'verify_city_toastmsg')

         
        def emailfield_toastmsg_verification(self,driver):
            try:
                CommonMethods.wait_for_locator(driver, self.emailtextfield, 5)
                CommonMethods.elementClick(driver,self.emailtextfield)
                CommonMethods.hideKeyboard(driver)
                self.extracting_text_from_image(driver,r'Please enter your email address','Please enter your email address')
                 
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'emailfield_toastmsg_verification')    
             
            except:
                CommonMethods.exception(driver, featureFileName, 'emailfield_toastmsg_verification')
                
                
        def country_code_dropdown(self,driver):
            try:
                CommonMethods.isElementPresent(driver, self.countrycodedrop_down)
                actual_text =CommonMethods.getAttributeOfElement(driver,'text', self.countrycodedrop_down_text_view)
                check = CommonMethods.verifyTextMatch(actual_text, '+91')
                if check == True:
                    logging.info('On Register screen "+91" is displayed by default under mobile number country code drop down')

            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'country_code_dropdown')    
             
            except:
                CommonMethods.exception(driver, featureFileName, 'country_code_dropdown')
        
                
        def country_code_dropdown_click(self,driver):
            try:
                CommonMethods.wait_for_locator(driver, self.countrycodedrop_down, 10)
                CommonMethods.elementClick(driver, self.countrycodedrop_down)
                logging.info('Clicked on country code drop down')
            
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'country_code_dropdown_click')    
             
            except:
                CommonMethods.exception(driver, featureFileName, 'country_code_dropdown_click')
                logging.error('Failed to click on country_code_dropdown')
        
        
        def select_country_code(self,driver,CountryName,CountryCode):
            try:
                CommonMethods.elementClick(driver,(By.XPATH,"//*[contains(@text, \'"+CountryName+"\')]"))                             
                CommonMethods.wait_for_locator(driver, self.countrycodedrop_down_text_view,10)
                country_code =CommonMethods.getAttributeOfElement(driver,'text', self.countrycodedrop_down_text_view)
                CommonMethods.verifyTwoText(country_code, CountryCode)
                logging.info('Selected country is '+CountryName+' and the country code is '+country_code) 
            
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'select_country_code')    
             
            except:
                CommonMethods.exception(driver, featureFileName, 'select_country_code')
                logging.error('Failed to verify the country code')    

            
        def get_country_list_and_verify(self,driver):
            try:
                count = 0
                previous_text = str()
                country_list =[]
                while True:
                    textlist = driver.find_elements_by_xpath("//android.widget.TextView")
                    for i in textlist:
                        country =i.get_attribute('text')
                        if country not in country_list:
                            country_list.append(country)
                    self.scroll_list(driver, textlist)
                    if previous_text == textlist[-1].get_attribute('text'):
                        count += 1
                    else:
                        previous_text = textlist[-1].get_attribute('text')
                    if count == 1:
                        break     
                element2 =['India (+91)', 'UAE (+971)', 'Bahrain(+973)', 'Kuwait (+965)', 'Oman (+968)', 'Qatar (+974)', 'Saudi Arabia (+966)', 'United Arab Emirates (+971)', 'Afghanistan (+93)', 'Albania (+355)', 'Algeria (+213)', 'Andorra (+376)', 'Angola (+244)', 'Anguilla (+264)', 'Antigua and Barbuda (+268)', 'Argentina (+54)', 'Armenia (+374)', 'Aruba (+297)', 'Ascension Island (+247)', 'Australia (+61)', 'Austria (+0)', 'Azerbaijan (+994)', 'Bahamas (+242)', 'Bangladesh (+880)', 'Barbados (+246)', 'Belarus (+375)', 'Belgium (+32)', 'Belize (+501)', 'Benin (+229)', 'Bermuda (+441)', 'Bhutan (+975)', 'Bolivia (+591)', 'Bosnia (+387)', 'Botswana (+267)', 'Brazil (+55)', 'Brunei (+673)', 'Bulgaria (+359)', 'Burkina Faso (+226)', 'Burundi (+257)', 'Cambodia (+855)', 'Cameroon (+237)', 'Canada (+1)', 'Cape Verde Islands (+238)', 'Cayman Islands (+345)', 'Central Africa Republic (+236)', 'Chad (+235)', 'Chile (+56)', 'China (+86)', 'Columbia (+57)', 'Comoros Island (+269)', 'Congo (+242)', 'Cook Islands (+682)', 'Costa Rica (+506)', 'Croatia (+385)', 'Cuba (+53)', 'Cyprus (+357)', 'Czech Republic (+420)', 'Democratic Republic of Congo (Zaire) (+243)', 'Denmark (+45)', 'Diego Garcia (+246)', 'Djibouti (+253)', 'Dominica Islands (+767)', 'Dominican Republic (+809)', 'Ecuador (+593)', 'Egypt (+20)', 'El Salvador (+503)', 'Equatorial Guinea (+240)', 'Eritrea (+291)', 'Estonia (+372)', 'Ethiopia (+251)', 'Faeroe Islands (+298)', 'Falkland Islands (+500)', 'Fiji Islands (+679)', 'Finland (+358)', 'France (+33)', 'French Guiana\\xa0 (+594)', 'French Polynesia (+689)', 'Gabon (+241)', 'Georgia (+995)', 'Germany (+49)', 'Ghana (+233)', 'Gibraltar (+350)', 'Greece (+30)', 'Greenland (+299)', 'Grenada (+473)', 'Guadeloupe (+590)', 'Guam (+671)', 'Guatemala (+502)', 'Guinea Bissau (+245)', 'Guinea Republic (+224)', 'Guyana (+592)', 'Haiti (+509)', 'Honduras (+503)', 'Hong Kong (+852)', 'Hungary (+36)', 'Iceland (+354)', 'Indonesia (+62)', 'Iran (+98)', 'Iraq (+964)', 'Ireland (+353)', 'Israel (+972)', 'Italy (+39)', 'Ivory Coast (+225)', 'Jamaica (+876)', 'Japan (+81)', 'Jordan (+962)', 'Kazakhstan (+7)', 'Kenya (+254)', 'Kiribati (+686)', 'Korea, North (+850)', 'Korea, South (+82)', 'Kyrgyzstan (+996)', 'Laos (+856)', 'latvia (+371)', 'Lebanon (+961)', 'Lesotho (+266)', 'Liberia (+231)', 'Libya (+218)', 'Liechtenstein (+423)', 'Lithuania (+370)', 'Luxembourg (+352)', 'Macau (+853)', 'Macedonia (Fyrom) (+389)', 'Madagascar (+261)', 'Malawi (+265)', 'Malaysia (+60)', 'Maldives Republic (+960)', 'Mali (+223)', 'Malta (+356)', 'Mariana Islands (+670)', 'Marshall Islands (+692)', 'Martinique (+596)', 'Mauritius (+230)', 'Mayotte Islands (+269)', 'Mexico (+52)', 'Micronesia (+691)', 'Moldova (+373)', 'Monaco (+377)', 'Mongolia (+976)', 'Montserrat (+664)', 'Morocco (+212)', 'Mozambique (+258)', 'Myanmar (Burma) (+95)', 'Namibia (+264)', 'Nauru (+674)', 'Nepal (+977)', 'Netherlands (+31)', 'Netherlands Antilles (+599)', 'New Caledonia (+687)', 'New Zealand (+64)', 'Nicaragua (+505)', 'Niger (+227)', 'Nigeria (+234)', 'Niue Island (+683)', 'Norfolk Island (+672)', 'Norway (+47)', 'Pakistan (+92)', 'Palau (+680)', 'Palestine (+970)', 'Panama (+507)', 'Papua New Guinea (+675)', 'Paraguay (+595)', 'Peru (+51)', 'Philippines (+63)', 'Poland (+48)', 'Portugal (+351)', 'Puerto Rico (+787)', 'Reunion Island (+262)', 'Romania (+40)', 'Russia (+7)', 'Rwanda (+250)', 'Samoa (American) (+684)', 'Samoa (Western) (+685)', 'San Marino (+378)', 'Sao Tome & Principe (+239)', 'Senegal (+221)', 'Serbia (+381)', 'Seychelles (+248)', 'Sierra Leone (+232)', 'Singapore (+65)', 'Slovak Republic (+421)', 'Slovenia (+386)', 'Solomon Islands (+677)', 'Somalia (+252)', 'South Africa (+27)', 'Spain (+34)', 'Sri Lanka (+94)', 'St Helena (+290)', 'St Kitts & Nevia (+869)', 'St Lucia (+758)', 'Sudan (+249)', 'Surinam (+597)', 'Swaziland (+268)', 'Sweden (+46)', 'Switzerland (+41)', 'Syria (+963)', 'Taiwan (+886)', 'Tajikistan (+992)', 'Tanzania (+255)', 'Thailand (+66)', 'The Gambia (+220)', 'Togo (+228)', 'Tonga (+676)', 'Trinidad & Tobago (+868)', 'Tunisia (+216)', 'Turkey (+90)', 'Turkmenistan (+993)', 'Turks & Caicos Islands (+649)', 'Tuvalu (+688)', 'Uganda (+256)', 'Ukraine (+380)', 'United Kingdom (+44)', 'Uruguay (+598)', 'USA (+1)', 'Uzbekistan (+998)', 'Vanuatu (+678)', 'Venezuela (+58)', 'Vietnam (+84)', 'Wallis & Futuna Islands (+681)', 'Yemen Arab Republic (+967)', 'Zambia (+260)', 'Zimbabwe (+263)']
                self.compareElementsInList(country_list, element2)
                logging.info('The country list and country code is verified and first 8 countries and their code are ' + str(country_list[:8]))
             
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'get_country_list_and_verify')    
             
            except:
                CommonMethods.exception(driver, featureFileName, 'get_country_list_and_verify')
                logging.error('Failed to verify the country list')       
            
            
        def verify_phonenumber_valid_error_msg(self,driver,phone_number):
            try:
                actual_num = CommonMethods.getAttributeOfElement(driver,'text', self.phonetextfield)
                if len(actual_num)>15 or len(actual_num)<7:
                    if CommonMethods.isElementPresent(driver, self.PhoneErrorMsg):
                        errorMessage= CommonMethods.getAttributeOfElement(driver,'text', self.PhoneErrorMsg)
                        logging.info(errorMessage)
                        CommonMethods.verifyTwoText(errorMessage,"Please enter valid mobile number")
                        logging.info('User has entered ' + str(len(actual_num))+ ' digit number.Please enter a valid mobile number ')
                        CommonMethods.clearData(driver, self.phonetextfield)
                else:
                    logging.info('User has entered phone number within the range')  
            
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_phonenumber_valid_error_msg')    
             
            except:
                CommonMethods.exception(driver, featureFileName, 'verify_phonenumber_valid_error_msg')
                logging.error('"Please enter a valid mobile number" error message is not shown')              
                

                
        def enter_emailaddress(self,driver,EmailId):
            try:
                CommonMethods.enterText(driver, EmailId,self.emailtextfield)
                
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'enter_emailaddress')    
             
            except:
                CommonMethods.exception(driver, featureFileName, 'enter_emailaddress')
                logging.error('Failed to enter email address')    
        
                       
        def verify_invalid_emailid_toastmsg(self,driver):
            try:
                CommonMethods.elementClick(driver,self.emailtextfield)
                CommonMethods.hideKeyboard(driver)
                sleep(3)
                self.extracting_text_from_image(driver,r'Please enter (.*)','Please enter valid email address')
    
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_invalid_emailid_toastmsg')    
             
            except:
                CommonMethods.exception(driver, featureFileName, 'verify_invalid_emailid_toastmsg')
                logging.error('Failed to find the toast message Please enter valid email address ')   
            

        def tap_on_link(self,driver,text):
            try:
                CommonMethods.elementClick(driver, (By.XPATH,"//android.widget.TextView[@text=\'"+text+"\']"))
            
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_link')    
             
            except:
                CommonMethods.exception(driver, featureFileName, 'tap_on_link')
                logging.error('Failed to click on "'+ text+ '"')  
            
                
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
         

        def app_backbtn(self,driver):
            try:
                CommonMethods.wait_for_locator(driver, self.App_backBtn, 10)
                CommonMethods.elementClick(driver, self.App_backBtn)
            
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'app_backbtn')    
             
            except:
                CommonMethods.exception(driver, featureFileName, 'app_backbtn')
                logging.error('Failed to click on app_back button')     
        
        
        def navigate_back_reg_scrn(self,driver): 
            try:
                self.navigate_to_screen(driver,'5000+ Engaging Videos',self.header_title_text)
                logging.info('User is in registration screen')
            
            except:
                logging.error('Failed to navigate to registration screen')
                pytest.fail('User failed to navigate back to registration screen')
        
                
        def screenshot(self,driver):
            ts = time.strftime("%Y_%m_%d_%H%M%S")
            activityname = driver.current_activity
            filename = activityname + ts
            ScrnShotpath="./ScreenShots/"+ filename + ".png"
            driver.save_screenshot(ScrnShotpath)
            return ScrnShotpath

        
        def extracting_text_from_image(self,driver,rtext,expected):
            sleep(3)
            open_image = Image.open(self.screenshot(driver))
            img_to_text = image_to_string(open_image)
            to_find_text = re.compile(rtext)
            search_text = to_find_text.search(img_to_text)
            if search_text:
                found_text= search_text.group()
                logging.info('We found your searching text '+found_text)
                CommonMethods.verifyTextMatch(found_text,expected) 
            else:
                logging.error('Text not found')
                pytest.fail('Failed to find the text')
        
            
        def scroll_list(self,driver,textlist):
            touch = TouchAction(driver) 
            box_list =driver.find_element_by_xpath("//android.widget.ListView")
            start_x = textlist[-1].location['x']
            start_y = textlist[-1].location['y']
            end_x = box_list.location['x']
            end_y = box_list.location['y']
            touch.press(x=start_x, y=start_y).wait(3000).move_to(x=end_x, y=end_y).release().perform()  
        
        
        def clear_mobile_number_field(self,driver):
            CommonMethods.enterText(driver,'', self.phonetextfield)
        
        
        def compareElementsInList(self,element1, element2):
            for i in range(len(element2)):
                if element1[i] != element2[i]:
                    print('The', element1[i], 'is not matching with',element2[i])  
                    
            
        def find_os_version(self,driver):
            Check =CommonMethods.run('adb shell getprop ro.build.version.release')
            print(Check)
            Check = Check[0].decode().strip('\r\n')
            logging.info('The OS version of the device is '+ Check)
            return Check

        
        def verify_google_account(self,driver):
            driver.start_activity('com.android.settings', 'com.android.settings.Settings')
            CommonMethods.scrollToElement(driver, 'Google')
            CommonMethods.elementClick(driver,(By.XPATH,"//android.widget.TextView[@text='Google']"))
            if CommonMethods.findButton(driver, 'Sign in to your Google Account'):
                logging.info('Google account is not added')
                self.google_account = False
            elif CommonMethods.findButton(driver,'Manage your Google Account'):
                CommonMethods.elementClick(By.ID,"com.google.android.gms:id/account_spinner")
                sleep(3)
                list1 = []
                acc = driver.find_elements_by_xpath("//*[contains(@text, '.com')]")
                for i in range(len(acc)):
                    list1.append((acc[i]).get_attribute('text'))
                logging.info(list1)
                self.google_account = True  
            else:
                logging.error('User is not in accounts screen')
            return self.google_account
                
            
        def device_gps_location(self,driver):
            try:
                lat_la = driver.location
                xl =(lat_la["latitude"],lat_la["longitude"])
                geolocator = Nominatim(user_agent="Byjus")
                location = geolocator.reverse(str(xl[0]) + ', '+ str(xl[1]))
                device_location=location.address
                return device_location
            except GeocoderTimedOut:
                return self.device_gps_location(driver)
        
                  
        def verify_current_location(self,driver):
            sleep(2)
            app_location=CommonMethods.getAttributeOfElement(driver, 'text', self.citytextfield)
            device_location = self.device_gps_location(driver)
            logging.info(app_location)
            logging.info(device_location)
            try:
                if device_location==app_location:
                    logging.info('Current GPS location is verified')
                elif device_location!=app_location:
                    find_pincode = re.compile(r'\d{6}')
                    found_pincode1 = find_pincode.search(app_location)
                    found_pincode2 = find_pincode.search(device_location)
                    if found_pincode1 and found_pincode2:
                        if found_pincode1.group()==found_pincode2.group():
                            logging.info('Current GPS location is verified')
                    else:
                        location_one = str(app_location).split()
                        location_two = str(device_location).split()
                        logging.info(location_one)
                        logging.info(location_two)
                        compare_location = (set(location_one)).intersection(set(location_two)) 
                        logging.info(compare_location)
                        assert len(compare_location) >=2, "Location is not accurate"
                        logging.info('Current GPS location is verified')                        
                else:
                    logging.error('Failed to verify current location')
                    pytest.fail('Gps app location is not matching with current device location')
            
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_current_location')    

            except:
                CommonMethods.exception(driver, featureFileName, 'verify_current_location')
         
                
        def tap_on_locationfield(self,driver):
            try:
                CommonMethods.elementClick(driver, self.citytextfield)
                logging.info('User tapped on location field')
            
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_locationfield')    

            except:
                CommonMethods.exception(driver, featureFileName, 'tap_on_locationfield') 
        
               
        def enter_location_manually(self,driver,Location):
            try:
                if CommonMethods.enterText(driver, Location, self.citytextfield):
                    logging.info('Entered location '+Location)
                else:
                    logging.error('Failed to enter location'+ Location)
                    pytest.fail('Failed to enter location manually')
            
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'enter_location_manually')    

            except:
                CommonMethods.exception(driver, featureFileName, 'enter_location_manually')
        
            
        def tap_on_allow_button(self,driver): 
            try:
                CommonMethods.elementClick(driver, self.allowbutton) 
            
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_allow_button')    

            except:
                CommonMethods.exception(driver, featureFileName, 'tap_on_allow_button')
        
                
        def verify_location_permission(self,driver):
            try:
                if CommonMethods.isElementPresent(driver,self.allowbutton):
                    actualText= CommonMethods.getAttributeOfElement(driver, 'text', self.permission_message)
                    CommonMethods.verifyTextMatch(actualText, "Allow BYJU'S The Learning App to access this device's location?")
                    logging.info('Location pop up is shown')
                else:
                    logging.error('Failed to see the location permission pop up')
                    pytest.fail('location permission dialog is not shown in  Registration screen')     
            
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_location_permission')    

            except:
                CommonMethods.exception(driver, featureFileName, 'verify_location_permission')    
        
        
        def tap_on_location_icon1(self,driver):
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
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_location_icon1')    

            except:
                CommonMethods.exception(driver, featureFileName, 'tap_on_location_icon1')
                
        def tap_on_location_icon(self,driver):
            try:
                self.tap_on_location_icon1(driver)
                if CommonMethods.isElementPresent(driver, self.location_ok):
                    CommonMethods.elementClick(driver, self.location_ok)
                    self.tap_on_location_icon1(driver)
                sleep(3)
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_location_icon')    

            except:
                CommonMethods.exception(driver, featureFileName, 'tap_on_location_icon')


        def tap_on_deny_button(self,driver): 
            try:
                CommonMethods.elementClick(driver, self.denybutton)
                if CommonMethods.isElementPresent(driver, self.secondaryActionBtn):
                    CommonMethods.elementClick(driver, self.secondaryActionBtn) 
                
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_deny_button')    

            except:
                CommonMethods.exception(driver, featureFileName, 'tap_on_deny_button')

               
        def select_grade(self,driver):
            try:
                CommonMethods.isElementPresent(driver,self.grade8th)
                CommonMethods.elementClick(driver,self.grade8th)
                if CommonMethods.isElementPresent(driver, self.gms_cancel):
                    CommonMethods.elementClick(driver,self.gms_cancel)
            
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'select_grade')    

            except:
                CommonMethods.exception(driver, featureFileName, 'select_grade')
                
                
        def bottom_sheet_dialog_shown(self,driver):

            check = CommonMethods.isElementPresent(driver, self.dialogBox_msg)
            if check == True:
                logging.info('Bottom sheet dialog is shown')
            else:
                logging.error('Failed to display bottom sheet dialog')
                pytest.fail('Bottom sheet dialog is not shown')
        
            
        def bottom_sheet_dialog_dismissed(self,driver):
            check = CommonMethods.isElementPresent(driver, self.dialogBox_msg)
            if check == False:
                logging.info('Bottom sheet dialog is not shown')
            else:
                logging.error('Bottom sheet dialog is shown')
                pytest.fail('Bottom sheet dialog is shown')
        
                
        def tap_on_primaryActionBtn(self,driver):
            try:
                CommonMethods.elementClick(driver,self.primaryActionBtn)
            
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_primaryActionBtn')    

            except:
                CommonMethods.exception(driver, featureFileName, 'tap_on_primaryActionBtn')
                
        def check_phone_number(self,driver,phone_number):
            try:    
                check =CommonMethods.getAttributeOfElement(driver,'text', self.phonetextfield)
                if check == phone_number:
                    logging.info('Phone number is auto filled')       
                else:
                    logging.error('Phone number field is empty')
                    pytest.fail('Failed in method check_phone_number')
                    
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'check_phone_number')
                
            except:
                CommonMethods.exception(driver, featureFileName, 'check_phone_number')
        
        def navigate_to_otp_verification_scn(self,driver):
            try:
                self.navigate_to_screen(driver,'To complete registration',self.header_subtitle_text)
                logging.info('User navigated to "OTP verification Screen"') 
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'navigate_to_otp_verification_scn')
                
            except:
                CommonMethods.exception(driver, featureFileName, 'navigate_to_otp_verification_scn')    

                
        def launch_app(self,driver):
            try:
                sleep(5)
                self.tap_device_backbtn(driver)
                self.tap_device_backbtn(driver)

            except:
                CommonMethods.exception(driver, featureFileName, 'launch_app')
                
                
        def allow_location_settings_permission(self,driver):
            try:
                CommonMethods.elementClick(driver,(By.XPATH,"//android.widget.TextView[@text='Permissions']"))
                CommonMethods.elementClick(driver,(By.XPATH,"//android.widget.TextView[@text='Location']"))
               
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'allow_location_settings_permission')    
             
            except:
                CommonMethods.exception(driver, featureFileName, 'allow_location_settings_permission')
        
        
        def hint_dialog_shown(self,driver):
            try:
                Check1 =CommonMethods.isElementPresent(driver, self.gms_cancel)
                Check2=CommonMethods.isElementPresent(driver,self.email_xpath)
                if Check1 == True and Check2 ==False:
                    logging.info('Phone number Hint requset pop up is shown')
                elif Check2 ==True and  Check1== True:
                    if CommonMethods.isElementPresent(driver, self.gms_cancel):
                        CommonMethods.elementClick(driver, self.gms_cancel)
                    CommonMethods.wait_for_locator(driver,self.regscn_lgnbtn, 10)
                    CommonMethods.elementClick(driver,self.regscn_lgnbtn)
                    CommonMethods.wait_for_locator(driver, self.loginRegBtn, 10)
                    CommonMethods.enterText(driver, '',self.phonetextfield)
                    CommonMethods.elementClick(driver,self.loginRegBtn)
                    CommonMethods.wait_for_locator(driver, self.grade8th,10)
                    CommonMethods.elementClick(driver,self.grade8th)
                    sleep(2)
                    if CommonMethods.isElementPresent(driver, self.gms_cancel):
                        logging.info('Hint requset pop up is shown')
                elif self.verify_google_account(driver)==False:
                    driver.activate_app('com.byjus.thelearningapp')
                    logging.error('Google account is not added in the device, hence hint pop up is not shown')
                    self.hint_dialog =False

                else:
                    pytest.fail('Hint requset pop up is not shown')
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'hint_dialog_shown')    
             
            except:
                CommonMethods.exception(driver, featureFileName, 'hint_dialog_shown')
                
        def hint_dialog_shown_mail(self,driver):
            try:
                Check =CommonMethods.isElementPresent(driver, self.gms_cancel)
                if Check == True:
                    CommonMethods.isElementPresent(driver,self.email_xpath)
                    logging.info('Email hint dialog is shown')
                elif self.google_account==False:
                    logging.error('Google account is not added in the device, hence hint pop up is not shown')
                    self.hint_dialog =False
                    
                else:
                    logging.error('Email Hint dialog is not shown')
            
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'hint_dialog_shown_mail')    
             
            except:
                CommonMethods.exception(driver, featureFileName, 'hint_dialog_shown_mail')

        def hint_dialog_notshown(self,driver):
            try:
                if CommonMethods.isElementPresent(driver, self.gms_cancel):
                    logging.error('Hint request pop up is shown since the device email id is registered with other application')
                
                elif self.verify_google_account(driver)==True:
                    driver.activate_app('com.byjus.thelearningapp')
                    logging.error('Google account is added in the device, hence hint pop up is shown')
                    self.hint_dialog =True
#                     pytest.fail('Hint request pop up is shown')  
                else:
                    logging.info('Hint request pop up is not shown')
                    
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'hint_dialog_notshown')    
             
            except:
                CommonMethods.exception(driver, featureFileName, 'hint_dialog_notshown')
                    
        
        def select_phonenumber_from_hint_dialog(self,driver):
            try:
                if self.hint_dialog ==False:
                    logging.info('Hint dialog not shown')
                else:
                    ele =CommonMethods.getElements(driver, self.hint_element_list)
                    phone_number = ele[0].get_attribute('text')
                    res= re.findall(r'\d', phone_number)
                    self.phone_number=''.join(res)
                    ele[0].click()
            
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'Tap_number_hint_dialog')    
             
            except:
                CommonMethods.exception(driver, featureFileName, 'Tap_number_hint_dialog')
                
        
        def verify_mobileno_from_hint(self,driver):
            try:
                if self.hint_dialog ==False:
                    logging.info('Hint dialog not shown')
                else:
                    mobile_number = CommonMethods.getAttributeOfElement(driver, 'text',self.phonetextfield)
                    if self.phone_number[0]=='0':
                        self.phone_number=self.phone_number[1:]
                    if mobile_number ==self.phone_number:
                        logging.info('Mobile number is verified dialog')
                    else:
                        logging.error('Failed to verifiy the number')
                        pytest.fail('Failed to match the mobile number from hint dialog')
            
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_mobileno_from_hint')    
             
            except:
                CommonMethods.exception(driver, featureFileName, 'verify_mobileno_from_hint')
        
                
        def verify_email_from_hint(self,driver):
            try:
                if self.hint_dialog ==False:
                    logging.info('Hint dialog not shown')
                else:
                    email = CommonMethods.getAttributeOfElement(driver, 'text',self.emailtextfield)
                    logging.info(self.email)
                    if email ==self.email:
                        logging.info('email is verified from hint dialog')
                    else:
                        logging.error('Failed to verify the email')
                        pytest.fail('Failed to match the email id from hint dialog')
                
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'verify_email_from_hint')    
             
            except:
                CommonMethods.exception(driver, featureFileName, 'verify_email_from_hint')        
        
        
        def navigate_reg_for_hint_dialog(self,driver):
            try:
                if CommonMethods.isElementPresent(driver,self.skipButton):
                    logging.info('User is in onboarding screen')
                    CommonMethods.elementClick(driver, self.skipButton)
                if CommonMethods.isElementPresent(driver,self.loginRegBtn):
                    if CommonMethods.isElementPresent(driver, self.gms_cancel):
                        CommonMethods.elementClick(driver,self.gms_cancel)
                    CommonMethods.elementClick(driver, self.loginRegBtn)
                CommonMethods.elementClick(driver, self.grade8th)
            
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'navigate_reg_for_hint_dialog')    
             
            except:
                CommonMethods.exception(driver, featureFileName, 'navigate_reg_for_hint_dialog')
        
                
        def select_emailfrom_hint_dialog(self,driver):
            try:
                if self.hint_dialog ==False:
                    logging.info('Hint dialog not shown')
                else:
                    ele =CommonMethods.getElements(driver, self.hint_element_list)
                    email1 =driver.find_elements_by_xpath("//*[contains(@text, '.com')]")
                    self.email =email1[0].get_attribute('text')
                    ele[0].click()
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'select_emailfrom_hint_dialog')    
             
            except:
                CommonMethods.exception(driver, featureFileName, 'select_emailfrom_hint_dialog')
        
        
        def tap_on_deny_button_loc(self,driver): 
            try:
                CommonMethods.elementClick(driver, self.denybutton)
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'tap_on_deny_button_loc')    
             
            except:
                CommonMethods.exception(driver, featureFileName, 'tap_on_deny_button_loc') 
                
                
        def enter_user_phone_email_name(self,driver):
            try:
                CommonMethods.enterText(driver,getdata(data_file, 'user_details', 'name'), self.nametextfield)
                CommonMethods.enterText(driver,getdata(data_file, 'user_details', 'mobile'), self.phonetextfield)
                CommonMethods.enterText(driver,getdata(data_file, 'user_details', 'email'), self.emailtextfield)
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'enter_user_phone_email_name')    
             
            except:
                CommonMethods.exception(driver, featureFileName, 'enter_user_phone_email_name') 
                
        def enter_city_phone_name(self,driver):
            try:
                CommonMethods.enterText(driver,getdata(data_file, 'user_details', 'name'), self.nametextfield)
                CommonMethods.enterText(driver,getdata(data_file, 'user_details', 'mobile'), self.phonetextfield)
                CommonMethods.enterText(driver,getdata(data_file, 'user_details', 'city'), self.citytextfield)
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'enter_city_phone_name')    
             
            except:
                CommonMethods.exception(driver, featureFileName, 'enter_city_phone_name')    
        
        def enter_email_name(self,driver):
            try:
                CommonMethods.enterText(driver,getdata(data_file, 'user_details', 'name'), self.nametextfield)
                CommonMethods.enterText(driver,getdata(data_file, 'user_details', 'email'), self.emailtextfield)
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver, featureFileName, 'enter_email_name')    
             
            except:
                CommonMethods.exception(driver, featureFileName, 'enter_email_name')     
                
        def select_offline_mode(self, driver):
            try:
                set_connection_type(driver, 'OFFLINE')
                logging.info("enabled offline mode")   
            except :
                logging.info("Failed in Method select_offline_mode")
                CommonMethods.takeScreenShot(driver, featureFileName)
                pytest.fail("Failed in Method select_offline_mode")
            
        def verify_snackbar_msg(self,driver,text):
            try:
                check=CommonMethods.isElementPresent(driver, self.snackbar_text)
                if check == True:
                    act_txt=CommonMethods.getTextOfElement(driver,self.snackbar_text)
                    logging.info('Found snackbar text '+act_txt)
                    assert act_txt ==text ,"Snackbar message is not matching"
                else:
                    pytest.fail("Snackbar message verification failed ")    
            except NoSuchElementException:
                CommonMethods.noSuchEleExcept(driver,featureFileName,'snackbar_msg')    
            except:
                CommonMethods.exception(driver, featureFileName, 'snackbar_msg')
        
        def select_online_mode(self, driver):
            try:
                set_connection_type(driver, "WIFI")
                logging.info("enabled Online mode")   
            except :
                logging.info("Failed in Method select_online_mode")
                CommonMethods.takeScreenShot(driver, featureFileName)
                pytest.fail("Failed in Method select_online_mode")  
                
        def activate_app(self,driver):
            driver.activate_app('com.byjus.thelearningapp')  
