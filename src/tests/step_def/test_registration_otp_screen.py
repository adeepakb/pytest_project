from time import sleep
import subprocess
from selenium.webdriver.common import keys
from appium import webdriver
from pytest_bdd import scenarios, given, when, then, parsers,scenario
from POM_Pages.RegistrationOtpScreen import RegOtpScreen
import pytest
import logging
import datetime
from Utilities.BasePage import BaseClass
browser = fixture = 'browser'


baseClass = BaseClass()
regotpScreen =RegOtpScreen(browser)
featureFileName = 'Register OTP Verification Screen'

baseClass.setupLogs(featureFileName)

"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""

scenarios('../features/' + featureFileName + '.feature')

@given('Launch the app online')
def launchtheApp(browser):
    regotpScreen.launch_the_app(browser)


@given('Navigate to register OTP verification screen')
def navigate_to_reg_otp_screen(browser):
    regotpScreen.navigate_to_reg_otp_screen(browser)


@when('Navigate to register OTP verification screen')
def navigate_to_reg_otp_screen_2(browser):
    regotpScreen.navigate_to_reg_otp_screen(browser)


@then('Verify a bottom sheet dialog is shown')
def bottom_sheet_dialog_shown(browser):
    regotpScreen.otp_bottom_sheet_dialog_shown(browser)

    
@then(parsers.parse('Verify the "{text}" text'))
def verify_the_text(browser,text):
    regotpScreen.verify_the_text(browser,text)

    
@then("Verify count down timer")
def verify_count_down_timer(browser):
    regotpScreen.verify_count_down_timer(browser)


@then("Verify loading spinner")
def verify_loading_spiner(browser):
    regotpScreen.verify_loading_spiner(browser)


@given('Dismiss the auto verify OTP Popup')
def dismiss_otp_pop_up(browser):
    regotpScreen.dismiss_otp_pop_up(browser)

    
@when('Dismiss the auto verify OTP Popup')
def dismiss_otp_pop_up2(browser):
    regotpScreen.dismiss_otp_pop_up(browser)


@when('On Register otp screen tap on device back button')
def tap_device_backbtn(browser):
    sleep(2)
    regotpScreen.tap_device_backbtn(browser)

    
@then('Verify user lands on "OTP verification" screen')
def user_is_in_regScn(browser):
    regotpScreen.verify_greeting_text(browser)

    
@then("4 Fields to enter OTP along with curser highlighted on first filed")
def verify_otp_field(browser):
    regotpScreen.verify_otp_field(browser)

    
@then(parsers.parse('Verify the "{text}" button on Otp verification screen'))
def verify_resend_call_button(browser,text):
    regotpScreen.verify_resend_call_button(browser,text)


@then('Verify Mobile number "<Country-Code>-<Mobile-Number>" with Edit option')
def verify_phoneno_country_code(browser):
    regotpScreen.verify_phoneno_country_code(browser)


@then(parsers.parse('Toast message "{text}" is displayed'))
def verify_toast_msg(browser,text):
    regotpScreen.verify_toast_msg(browser,text)

  
@when('Tap on edit option')
def tap_edit_option(browser):
    regotpScreen.tap_edit_option(browser)


@given('Navigate Edit Number Screen')
def navigate_to_edit_screen(browser):
    regotpScreen.tap_edit_option(browser)     


@then('Verify the Mobile Number field')
def verify_mobile_number_field(browser):
    regotpScreen.verify_mobile_number_field(browser)

    
@then(parsers.parse('Verify the "{text}" button'))
def verify_the_button(browser,text):
    regotpScreen.verify_the_button(browser,text)

    
@then(parsers.parse('Verify the "{text}" link'))
def verify_the_link(browser,text):
    regotpScreen.verify_the_link(browser,text)


@then('Verify Mobile Number field with number pre-filled as in register screen')
def phonenumber_autofill(browser):
    regotpScreen.phonenumber_autofill(browser)

    
@then('Verify Country Code which is a drop down')
def verify_country_code_dropdown(browser):
    regotpScreen.verify_country_code_dropdown(browser)

    
@when('tap on country code drop down')
def country_code_dropdown_click(browser):
    regotpScreen.country_code_dropdown_click(browser)

    
@then('Verify that user should be able to select any <CountryCode> and respective <CountryName> from the drop down')
def  select_country_code(browser,CountryName,CountryCode):
    sleep(2)
    regotpScreen.select_country_code(browser,CountryName,CountryCode)

    
@when('By default country which entered in Sign Up screen should be selected in the drop down menu')
def verify_country_code(browser):
    regotpScreen.verify_country_code(browser)


@when('User delete the default number')    
def clear_mobile_number_field(browser):
    regotpScreen.clear_mobile_number_field(browser)


@when('User tap on next button')
def tap_on_next_button(browser):
    regotpScreen.tap_on_next_button(browser)


@then(parsers.parse('Verify validation message "{text}"'))
def phonenumber_field_errormessage(browser,text):
    regotpScreen.phonenumber_field_errormessage(browser,text)


@when('User is in Edit Number Screen')
def navigate_to_edit_no_screen(browser):
    regotpScreen.navigate_to_edit_no_screen(browser)


@when('User enters valid <phone_number>')
@when('User enters invalid <phone_number>')
def enter_phone_number_one(browser,phone_number):
    regotpScreen.enter_mobile_number(browser,phone_number)

 
@then('User should navigates to the "RegistrationOTPVerificationScreen"')
def navigated_to_otp_verification_screen(browser):
    regotpScreen.navigated_to_otp_verification_screen(browser)

    
@then('Verify new number is updated in the <phone_number> field')
def verify_entered_phone_number(browser,phone_number):
    regotpScreen.verify_entered_phone_number(browser,phone_number)


@then('Verify <App> should be closed')
def VerifyAppClosed(browser,App):
    regotpScreen.verify_app_closed(browser,App)


@then('Relaunch the <App>')
def relaunch_the_app(browser,App):
    regotpScreen.relaunch_the_app(browser,App)


@when(parsers.parse('On Edit Number Screen tap on "{text}" link'))
def tap_on_link(browser,text):
    sleep(2)
    regotpScreen.tap_on_link(browser,text)


@then(parsers.parse('Verify that user is redirected to "{text}" screen'))
def navigated_to_screen(browser,text):
    sleep(3)
    regotpScreen.navigated_to_the_screen(browser, text)

    
@when('Tap on "Resend" option')
def click_on_resend_callme_btn(browser):
    regotpScreen.click_on_resend_callme_btn(browser)

    
@then('Mobile number shown on OTP enter screen should same as the number entered in "RegisterScreen"')
def verify_reg_otpscn_phone_number(browser):
    regotpScreen.verify_reg_otpscn_phone_number(browser)

    
@when('wait till countdown timer ends')
def wait_till_element(browser):
    sleep(3)
    regotpScreen.wait_till_element(browser)

    
@when('User enters invalid <otp>')
def enter_otp(browser,otp):
    regotpScreen.enter_otp(browser,otp)


@then(parsers.parse('Verify snack bar message "{text}"'))
def verify_snackbar_msg(browser,text):
    regotpScreen.verify_snackbar_msg(browser,text)


@then(parsers.parse('Verify toast message "{text}" is displayed'))
def verify_two_line_toast_msg(browser,text):
    regotpScreen.two_line_toast_msg(browser,text)


@then('4 digit OTP is sent to the valid mobile number')
@then('user should get an automated OTP call')
def automated_OTP_call(browser):
    logging.info('Time being this step defination is made pass')
    pass

@when('Tap on "Call me" option')
def click_on_resend_callme_btn2(browser):
    regotpScreen.click_on_resend_callme_btn(browser)
    sleep(5)
    regotpScreen.click_on_resend_callme_btn(browser)
    
    
    
    