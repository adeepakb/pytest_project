import pytest
import sys
import os
import subprocess
from time import sleep
from pytest_bdd import scenarios, given, when, then, parsers,scenario
from selenium.webdriver.common import keys
from appium import webdriver
from POM_Pages.Hamburgermenu import Hamburger
from Utilities.BasePage import BaseClass

PATH = lambda p: os.path.abspath(
   os.path.join(os.path.dirname(__file__), p)
)

# sys.path.append(PATH('./Utilities/'))
# from Utilities.common_methods import CommonMethods
# from Utilities.BasePage import BaseClass
# 
# sys.path.append(PATH('../../../POM_Pages/'))
# from POM_Pages.Hamburgermenu import Hamburger

browser = fixture = 'browser'
base_class = BaseClass()
Hamburg = Hamburger(browser)

"""storing the feature file name"""
featureFileName = "Hamburger Menu"


# base_class.setupLogs(featureFileName)

"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""
scenarios('../features/'+featureFileName+'.feature')


@given('Launch the app online')
def loginapp(browser):
    Hamburg.navigate_to_home_screen(browser)
   

@given('User is in Hamburger menu')
def ham_verify(browser):
    Hamburg.hamburger_verify(browser)
    
    
@when('User taps on profile button')
def profile_verify(browser):
    Hamburg.profile_button(browser)


@then('Verify that user should  navigate to profilescreen') 
def profile_screen(browser):
    Hamburg.profilescreen_verify(browser)
    
@pytest.fixture 
@when(parsers.parse('user taps on "{text}" option'))
def bookmark_verify(browser,text):
    Hamburg.tap_hamburger_option(browser, text)
    yield text
    
    
@then('Verify that user should  navigate to Bookmarks Screen')
def bookmark_page(browser, bookmark_verify):
    Hamburg.Hamburger_page(browser, bookmark_verify)
       
@pytest.fixture 
@when(parsers.parse('user taps on "{text}" option'))
def Notification_verify(browser,text):
    Hamburg.tap_hamburger_option(browser, text)
    yield text
    
    
@then('Verify that user should  navigate to  Notification screen')
def Notification_page(browser, Notification_verify):
    Hamburg.Hamburger_page(browser, Notification_verify)
    
@pytest.fixture 
@when(parsers.parse('user taps on "{text}" option'))
def Badges_verify(browser,text):
    Hamburg.tap_hamburger_option(browser, text)
    yield text
    
    
@then('Verify that user should  navigate to  Badges screen')
def Badges_page(browser, Badges_verify):
    Hamburg.Hamburger_page(browser, Badges_verify)  
    
@pytest.fixture 
@when(parsers.parse('user taps on "{text}" option'))
def parent_verify(browser,text):
    Hamburg.tap_hamburger_option(browser, text)
    yield text
    
    
@then('Verify that user should  navigate to  Parent Connect screen')
def parent_page(browser, parent_verify):
    Hamburg.Hamburger_page(browser, parent_verify) 
    
@pytest.fixture 
@when(parsers.parse('user taps on "{text}" option'))
def quizzo_verify(browser,text):
    Hamburg.tap_hamburger_option(browser, text)
    yield text
    
    
@then('Verify that user should  navigate to  Quizzo screen')
def quizzo_page(browser, quizzo_verify):
    Hamburg.Hamburger_page(browser, quizzo_verify) 
    
@pytest.fixture 
@when(parsers.parse('user taps on "{text}" option'))
def share_verify(browser,text):
    Hamburg.tap_hamburger_option(browser, text)
    yield text
    
    
@then('Verify that user should  navigate to  share dialog')
def share_page(browser, share_verify):
    Hamburg.Hamburger_page(browser, share_verify)
    
    
@pytest.fixture 
@when(parsers.parse('user taps on "{text}" option'))
def contact_verify(browser,text):
    Hamburg.tap_hamburger_option(browser, text)
    yield text
    
    
@then('Verify that user should  navigate to  contact us screen')
def contact_page(browser, contact_verify):
    #Hamburg.Hamburger_page(browser, share_verify)
    Hamburg.scroll_hamburg_verify(browser, contact_verify)
    
    
@pytest.fixture 
@when(parsers.parse('user taps on "{text}" option'))
def Terms_verify(browser,text):
    Hamburg.tap_hamburger_option(browser, text)
    yield text
    
    
@then('Verify that user should  navigate to  Terms & Conditions screen')
def Terms_page(browser, Terms_verify):
    Hamburg.scroll_hamburg_verify(browser, Terms_verify)
    
    
@pytest.fixture 
@when(parsers.parse('user taps on "{text}" option'))
def subscribe_verify(browser,text):
    Hamburg.tap_hamburger_option(browser, text)
    yield text
    
    
@then('Verify that user should  navigate to  Subscribition  screen')
def subscribe_page(browser, subscribe_verify):
    Hamburg.scroll_hamburg_verify(browser, subscribe_verify)
    
    
@pytest.fixture 
@when(parsers.parse('user taps on "{text}" option'))
def Redeem_verify(browser,text):
    Hamburg.tap_hamburger_option(browser, text)
    yield text
    
    
@then('Verify that user should  navigate to  Redeem Voucher  screen')
def Redeem_page(browser, Redeem_verify):
    Hamburg.scroll_hamburg_verify(browser, Redeem_verify)
    
@pytest.fixture 
@when(parsers.parse('user taps on "{text}" option'))
def colgate_verify(browser,text):
    Hamburg.tap_hamburger_option(browser, text)
    yield text
    
    
@then('Verify that user should  navigate to  Colgate Scholarship  screen')
def colgate_page(browser, colgate_verify):
    Hamburg.scroll_hamburg_verify(browser, colgate_verify)
    
 
    
@when('User taps on Enquire Now option')
def r_homeDemo_verify(browser):
    Hamburg.hamburger_enquire_now(browser)
    
@then('Verify that user should  navigate to  Enquire Now screen') 
def home_demo_page(browser):
    Hamburg.enquire_now_page(browser)
    
    
@when('User taps on School Super League option')
def ssl_verify(browser):
    Hamburg.hamburger_spl(browser)
    
@then('Verify that user should  navigate to School Super League  screen') 
def ssl_page(browser):
    Hamburg.ssl_verify(browser)

    


     
     
   


