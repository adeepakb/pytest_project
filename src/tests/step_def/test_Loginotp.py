import pytest
import sys
import os
import subprocess
from time import sleep
from pytest_bdd import scenarios, given, when, then, parsers,scenario
from selenium.webdriver.common import keys
from appium import webdriver
from POM_Pages.Loginotp import Loginoptscreen
from Utilities.BasePage import BaseClass
import logging
from Utilities.generic_methods import  GenericMethods











browser = fixture = 'browser'
base_class = BaseClass()
loginotp=Loginoptscreen(browser)

"""storing the feature file name"""
featureFileName = "Login OTP Verification Screen"

"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""
scenarios('../features/'+featureFileName+'.feature')

@given('Launch the app online')
def launchApp(browser):
    logging.info("implemented")
    
    
@given('Navigate to login screen')
def logscreen(browser):
   # loginotp.navigateToLoginPage(browser)
    GenericMethods.navigate_to_login_page(browser,'8th')
    
    
@given('User enters valid Mobile number')
def validnum(browser):
    loginotp.country_code(browser)
    loginotp.enterMobileNo(browser)
    
    
@given('tap on Login button on Login Screen')
def loginbtn_tap(browser):
    loginotp.click_on_next(browser)
    
    
@when('Tap on edit option')
def otp_edit(browser):
    loginotp.tap_on_edit(browser)
    
@then(parsers.parse('Toast message "{text}" is displayed'))
def verify_toast(browser,text):
    loginotp.verify_toast_msg(browser, text)
    
    
@then('user lands in LoginScreen')  
def login_verify(browser):
    loginotp.verify_loginpage(browser)
    
    
@when('Navigate to OTP screen')
def opt_verify(browser):
    loginotp.otp_screen_verify(browser)
    
    
@then('Mobile number shown on OTP enter screen should same as  the number  entered in LoginScreen')
def mobilenum_verify(browser):
    loginotp.verifynum(browser)
    
    
@when('tap on Login button')
def tap_login(browser):
    loginotp.click_on_next(browser)
    
@then(parsers.parse('A bottom sheet dialog should be displayed with the message "{text}"'))
def verify_bottomotp(browser,text):
    loginotp.verify_otp_bottomsheet(browser, text)
    
    
@then('verify count down timer')
def verify_countertime(browser):
    loginotp.verify_counter(browser)
    
    
@then('verify loader spinning')
def loader_verify(browser):
    loginotp.Verify_progressbar(browser)
    
    
@when('dismiss the auto verify OTP Popup')
def otp_bottomsheet_dismiss(browser):
    loginotp.otp_bottom_dismiss(browser)
    
    
@then(parsers.parse('OTP Entering Screen should be displayed with Label "{text}"'))
def otp_verify_txt(browser,text):
    loginotp.verify_all_otp_text(browser, text)
    
    
@then(parsers.parse('verify  text message "{text}"'))
def otp_txt(browser,text):
    loginotp.verifyotp_subtitle(browser,text)
    
    
@then(parsers.parse('verify text "{text}"'))
def otp_4digit(browser,text):
    loginotp.verify_all_otp_text(browser, text)
    
    
@then('verify country code')
def verify_countrycode(browser):
    loginotp.verify_country_code(browser)
    
    
@then('verify Mobile Number with Edit option')
def verify_mobnumfield(browser):
    loginotp.verify_mobilenum_field(browser)
    
    
@then('verify otp field')
def verify_otp_field(browser):
    loginotp.verify_otp_field(browser)
    
    
@then('Verify Resend button')
def verify_resend_btn(browser):
    loginotp.verify_resend_btn(browser)
    
    
@when('Tap on Resend Option')
def tap_resend(browser):
    loginotp.tap_resend_btn(browser)
    
    
@given('dismiss the auto verify OTP Popup')
def otp_dissmiss(browser):
    loginotp.otp_bottom_dismiss(browser)
    
    
@when('User enters incorrect OTP')
def invalid_otp(browser):
    loginotp.otp_invalid(browser)
    
    
@then(parsers.parse('Should displays error toast "{text}"' ))
def stack_msg(browser,text):
    loginotp.stackbar_toast_msg(browser, text)
 
