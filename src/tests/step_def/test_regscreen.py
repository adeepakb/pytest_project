from time import sleep
import subprocess
from selenium.webdriver.common import keys
from appium import webdriver
from pytest_bdd import scenarios, given, when, then, parsers,scenario
from POM_Pages.RegScreen import RegScreen
import pytest
import logging
import datetime
from Utilities.BasePage import BaseClass
browser = fixture = 'browser'


baseClass = BaseClass()
regScreen =RegScreen(browser)
featureFileName = 'Register Screen'


baseClass.setupLogs(featureFileName)

"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""

scenarios('../features/' + featureFileName + '.feature')

@given('Launch the app online')
def launchtheApp(browser):
    pass
#     regScreen.clear_app_data(browser)

@given('Deny all the permission')
def deny_permissions(browser):
    regScreen.deny_permissions(browser)


@when('Navigate to Register Screen')
def navigate_to_reg_screen(browser):
    regScreen.navigate_to_reg_screen(browser)

    
@then('Verify that user lands on RegisterScreen')
def user_is_in_regScn(browser):
    regScreen.verify_greeting_text(browser)

@then(parsers.parse('Verify the "{text}" text'))
def verify_the_text(browser,text):
    regScreen.verify_the_text(browser,text)

    
@then('Verify the Name field')
def verify_name_field(browser):
    regScreen.verify_name_field(browser)


@then('Verify the Mobile Number field')
def verify_mobile_number_field(browser):
    regScreen.verify_mobile_number_field(browser)

 
@then('Verify the Email ID field')
def verfy_email_field(browser):
    regScreen.verfy_email_field(browser)  

    
@then('Verify the City / Nearest Location field') 
def verfy_city_field(browser):
    regScreen.verfy_city_field(browser)  

    
@then(parsers.parse('Verify the "{text}" button'))
def verify_the_button(browser,text):
    regScreen.verify_the_button(browser,text)

    
@then(parsers.parse('Verify the "{text}" link'))
def verify_the_link(browser,text):
    regScreen.verify_the_link(browser,text)


@then('On Register screen verify "Email" field is not auto  filled')
@then('Verify email field should be blank')
def email_field_is_empty(browser):
    regScreen.email_field_is_empty(browser)

    
@then('On Register screen verify "City" fields is not auto  filled')
def city_field_is_empty(browser):
    regScreen.city_field_is_empty(browser)

@given('Navigate to Register Screen')
def navigatetoRegisterScreen(browser):
    regScreen.navigate_to_reg_screen(browser)

    
@when('On Register screen tap on Name field')
def click_on_name_field(browser):
    regScreen.click_on_name_field(browser)


@then("Verify that keypad is displayed at bottom")
def is_keyboadrd_shown(browser):
    regScreen.is_keypad_enabled(browser)


@when('On Register screen enter valid <Characters> in name field')  
@then('Verify user is able to enter only <Characters>')
def verify_enter_name(browser, Characters):
    regScreen.enter_name(browser, Characters)


@given('Allow all the permission')
def allow_permissions(browser):
    regScreen.allow_permissions(browser)


@when('On Register screen tap on device back button')
def tap_device_backbtn(browser):
    sleep(2)
    regScreen.tap_device_backbtn(browser)

    
@then('Verify user lands on "CourseSelectionScreen"')
def navigate_to_course_selection_screen(browser):
    regScreen.navigate_to_course_selection_screen(browser)


@given('Google account id registered in device')    
def verify_goggle_account(browser):
    regScreen.check_google_account(browser)
    sleep(3)


@then('On Register screen verify "Email" field is auto filled')
def verify_email_address(browser):
    regScreen.check_email_address(browser)


@then('Verify "city" field is auto filled')
def verify_city_address(browser):
    regScreen.check_city(browser)

    
@when('On Register screen tap on Mobile Number field')
def click_on_phone_numfield(browser):
    regScreen.click_mobile_num_field(browser)    
   

@when('Tap on "Register" button')
def tap_on_regbtn(browser):
    regScreen.tap_on_regbtn(browser)


@then('Verify alert message  "Please enter your name" should be displayed')
def name_field_toast_Msg(browser):
    sleep(3)
    regScreen.name_field_toast_Msg(browser) 


@when('Clear mobile number field if already number is shown')
def clear_mobile_number_field(browser):
    regScreen.clear_mobile_number_field(browser)
    
 
@then('Verify alert message "Please enter your mobile number" should be displayed below mobile number field')   
def mobilenum_field_error_Msg(browser):
    regScreen.phonenumber_field_errormessage(browser)


@then('Verify error alert message "Please enter your city" is displayed under city field')
def verify_city_toastmsg(browser):
    regScreen.verify_city_toastmsg(browser)
    

@when('On Register screen verify "+91" is displayed by default under mobile number country code drop down')
def country_code_dropdown(browser):
    regScreen.country_code_dropdown(browser)


@when('tap on country code drop down')
def country_code_dropdown_click(browser):
    regScreen.country_code_dropdown_click(browser)

    
@then('Verify that user should be able to select any <CountryCode> and respective <CountryName> from the drop down')
def  select_country_code(browser,CountryName,CountryCode):
    regScreen.select_country_code(browser,CountryName,CountryCode)


@then('Verify GCC countries should be displayed first in the dropdown and other countries apart from 8 should be displayed in Alphabetical order')
def get_country_list_and_verify(browser):
    sleep(2)
    regScreen.get_country_list_and_verify(browser)


@then("verify user is able to enter only <phone_number>")
@when('Enter already registered <phone_number> in Mobile number field')
@when('Enter <phone_number>')
def enter_phone_number_one(browser,phone_number):
    regScreen.enter_mobile_number(browser,phone_number)


@then('Verify error  text message "Please enter a valid mobile number"  should be displayed  below the mobile number field')
def verify_phone_valid_error_msg(browser,phone_number):
    regScreen.verify_phonenumber_valid_error_msg(browser,phone_number)
    

@when('Enter valid email id <EmailId>')
@when('Enter in valid email id <EmailId>')
def enter_emailaddress(browser,EmailId):
    regScreen.enter_emailaddress(browser,EmailId)


@then('Verify error toast message "Please enter valid email address" should be displayed below email id field')
def verify_invalid_emailid_toastmsg(browser):
    regScreen.verify_invalid_emailid_toastmsg(browser)


@then('Verify error alert message "Please enter your email address" is displayed below email id field')
def emailfield_toastmsg_verification(browser):
    regScreen.emailfield_toastmsg_verification(browser)

    
@when(parsers.parse('On Register screen tap on "{text}" link'))
def tap_on_link(browser,text):
    regScreen.tap_on_link(browser, text)


@then(parsers.parse('Verify that user is redirected to "{text}" screen'))
def navigated_to_screen(browser,text):
    sleep(3)
    regScreen.navigated_to_the_screen(browser, text)


@when('Tap on app back button')
def tap_on_app_backbtn(browser):
    sleep(3)
    regScreen.app_backbtn(browser)


@then('Verify that user is redirected to "Register" screen')
def navigate_back_reg_scrn(browser):
    regScreen.navigate_back_reg_scrn(browser)

    
@given('Google account is not added in the device')
def google_account_not_added(browser):
    regScreen.google_account_not_added(browser)


@then('Verify on Register Screen city field is auto filled with user current Location')
def verify_gps_location(browser):
    sleep(3)
    regScreen.verify_current_location(browser)

    
@when ('Tap on Location field')
def tap_on_locationfield(browser):
    regScreen.tap_on_locationfield(browser)

    
@then('Verify that user should enter the <Location> in location field')
def enter_location_manually(browser,Location):
    regScreen.enter_location_manually(browser,Location)

    
@when('Tap on Location icon')
def tap_on_location_icon(browser):
    regScreen.tap_on_location_icon(browser)  


@when('Verify that user is able to see location dialog')
def verify_location_permission(browser):
    regScreen.verify_location_permission(browser)

    
@when ('Tap on allow button')
def tap_on_allow_button(browser):
    regScreen.tap_on_allow_button(browser) 

    
@when ('Tap on deny button')
def tap_on_deny_button(browser):
    regScreen.tap_on_deny_button(browser)  

    
@when('On course selection screen tap on any "grade"')
def select_grade(browser):
    regScreen.select_grade(browser)


@when('Verify bottom sheet dialog is shown')    
@then('Verify bottom sheet dialog is shown')
def bottom_sheet_dialog_shown(browser):
    regScreen.bottom_sheet_dialog_shown(browser)

    
@then('Verify bottom sheet dialog should disappear') 
def bottom_sheet_dialog_dismissed(browser):
    regScreen.bottom_sheet_dialog_dismissed(browser)


@when('Go to device settings by tapping on "Allow" button in Location permission is necessary bottom sheet dialog')    
@when('Tap on "Login" button')
def tap_on_primaryActionBtn(browser):
    regScreen.tap_on_primaryActionBtn(browser)


@then('Verify that <phone_number> field is auto filled') 
def check_phone_number(browser,phone_number):
    regScreen.check_phone_number(browser,phone_number)   

    
@then('Verify user is Redirected to Register "OTP Verification" screen')
def navigate_to_otp_verification_scn(browser):
    sleep(10)
    regScreen.navigate_to_otp_verification_scn(browser)


@when('Allow the location permission in settings screen')
def allow_location_settings_permission(browser):
    regScreen.allow_location_settings_permission(browser)


@when('Launch the app back')    
def launch_app(browser):
    regScreen.launch_app(browser)
    sleep(3)

    
@then('Verify that on Register screen Hint dialog should not be shown')
def hint_dialog_notshown(browser):
    regScreen.hint_dialog_notshown(browser)


@when('Verify that Mobile number hint dialog is displayed')
def hint_dialog_shown(browser):
    regScreen.hint_dialog_shown(browser)


@given('User is not  registered in any other apps for ex:Zomato,Swiggy etc')
def not_reg_in_other_app(browser):
    logging.info('Make sure that user is not  registered in any other apps')
    pass


@given('User is already registered in any other apps for ex:Zomato,Swiggy etc.Launch the app online')
def reg_in_other_app(browser):
    logging.info('Make sure that user is registered in any other apps')
    pass

   
@when('Tap on any mobile number in Hint dialog')
def select_phonenumber_from_hint_dialog(browser):
    regScreen.select_phonenumber_from_hint_dialog(browser)

     
@then('Verify that email id hint dialog is displayed')
def hint_dialog_shown1(browser):
    sleep(2)
    regScreen.hint_dialog_shown_mail(browser)

 
@then('Tap on any email id in Hint dialog')
def select_emailIdfrom_hint_dialog(browser):
    regScreen.select_emailfrom_hint_dialog(browser)

     
@then('Verify selected email should be filled in email field')
def verify_email_from_hint(browser):
    regScreen.verify_email_from_hint(browser)
    
    
@then('Verify selected number should be filled in Mobile Number field')
def verify_mobileno_from_hint(browser):
    regScreen.verify_mobileno_from_hint(browser)
    
     
@when('Navigate to register Screen without dismissing the hint pop up')
def navigate_reg_for_hint_dialog(browser):
    regScreen.navigate_reg_for_hint_dialog(browser)  
     
    
@when('Tap on deny button on reg screen')
def tap_on_deny_button_loc(browser):
    regScreen.tap_on_deny_button_loc(browser)


@when('On Register screen enter valid name, mobile number and email id')
def enter_user_phone_email_name(browser):
    regScreen.enter_user_phone_email_name(browser)


@when('On Register screen enter valid name,mobile number,city')
def enter_city_phone_name(browser):
    regScreen.enter_city_phone_name(browser)


@when('On Register screen enter name and email')
def enter_email_name(browser):
    regScreen.enter_email_name(browser)


@when('disconnect device wifi/mobile data')
def off_internet(browser):
    regScreen.select_offline_mode(browser)
    sleep(2)

    
@then(parsers.parse('Verify text message "{text}" shown at the bottom of the Register screen'))
def verify_snackbar_msg(browser,text):
    regScreen.verify_snackbar_msg(browser,text)


@then('connect device wifi/mobile data')
def connect_internet(browser):
    regScreen.select_online_mode(browser)

      

     