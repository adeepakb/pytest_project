import pytest
import sys
import os
import subprocess
from time import sleep
from pytest_bdd import scenarios, given, when, then, parsers,scenario
from selenium.webdriver.common import keys
from appium import webdriver
from POM_Pages.bookMarkPage import BookMark
from Utilities.BasePage import BaseClass
import logging





browser = fixture = 'browser'
base_class = BaseClass()
bookMark=BookMark(browser)

"""storing the feature file name"""
featureFileName = "Bookmark Home screen"

"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""
scenarios('../features/'+featureFileName+'.feature')


@given('navigate to home screen')
def homescreen(browser):
    logging.info("implemented")
    pass
    


@given('Launch the app online')
def loginapp(browser):
    bookMark.navigate_to_home_screen(browser)
    

@given('User is in Hamburger menu')
def ham_verify(browser):
    bookMark.hamburger_verify(browser)
    
    
 
@when(parsers.parse('user taps on "{text}" option'))
def bookmark_verify(browser):
    bookMark.bookmark_verify(browser)
    
    
    
@then('Verify that user should  navigate to Bookmarks Screen')
def bookmark_page(browser):
    bookMark.bookmark_screen(browser)
    bookMark.remove_bookmark(browser)

    
    
    
@then('Verify that app back button at the top left corner of the screen should be present')
def bmark_back(browser):
    bookMark.bmark_back(browser)
    
@then(parsers.parse('verify "{text}" text'))
def no_bookmart(browser):
    bookMark.nobookmark_txt(browser)
    
@then(parsers.parse('Verify "{text}" option'))
def bmark_filter(browser):
    bookMark.filter_option(browser)
    
@then(parsers.parse('Verify  "{text}" text  followed by Subjects tab'))
def bmark_allsubj(browser):
    bookMark.subject_txt(browser)
      
      
@given('Navigate to bookmark home screen')
def bmark_homescreen(browser):
    bookMark.hamburger_verify(browser)
    bookMark.bookmark_verify(browser)
    bookMark.bookmark_screen(browser)
    
    
@when('tap on app back button')
def bmark_back_btn(browser):
    bookMark.bmark_back_btn_click(browser)
    
    
@then('Verify that user should navigate to home screen')
def home_screen_verify(browser):
    bookMark.homescreen_verify(browser)
    
    
@when('tap on device back button')
def device_back_verify(browser):
    bookMark.device_back(browser)
    
    
@when('navigate to bookmark home screen')
def bmark_screen(browser):
    bookMark.hamburger_verify(browser)
    bookMark.bookmark_verify(browser)
    bookMark.bookmark_screen(browser)
    
    
@then(parsers.parse('Tap on "{text}" subject'))
def bmrk_subtap(browser,text):
    bookMark.subject_tap(browser, text)
    
    
@then(parsers.parse('Verify that user should navigate to "{text}" tab'))
def bmrk_subverify(browser,text):
    bookMark.sub_highlight_Verify(browser,text)
    
    
@given('Remove existing bookmarks')
def bmrk_remove(browser):
    bookMark.remove_bookmark(browser)
    
    
@when('Check for bookmarked content')
def bmrk_check(browser):
    bookMark.check_bookmark(browser)
    
    
@then(parsers.parse('Verify "{text}" message should be shown when there are no bookmarks' ))
def bmrk_msg(browser,text):
     
    bookMark.check_nobookmark(browser, text)
    

@when('Bookmark any video')
def Bmrkvideo_back(browser):
    bookMark.initial_remove_bookmark(browser)
    bookMark.Bookmark_video(browser)
    
    
@when('navigate back to bookmark screen')
def bmrk_screen(browser):
    bookMark.hamburger_verify(browser)
    bookMark.bookmark_verify(browser)
    bookMark.bookmark_screen(browser)
    
    
@then('verify bookmark  is present')
def Bmrk_present(browser):
    bookMark.bookmark_present(browser)
    
    
@then(parsers.parse('Verify "{text}" message not shown in all tab' ))
def nobmrk_txt(browser,text):
    bookMark.check_nobookmark_text(browser, text)
    
    
    