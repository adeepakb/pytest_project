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





driver = fixture = 'driver'
base_class = BaseClass()
bookMark=BookMark(driver)

"""storing the feature file name"""
featureFileName = "Bookmark Home screen"

"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""
scenarios('../features/'+featureFileName+'.feature')


@given('navigate to home screen')
def homescreen(driver):
    logging.info("implemented")
    pass
    


@given('Launch the app online')
def loginapp(driver):
    bookMark.navigate_to_home_screen(driver)
    

@given('User is in Hamburger menu')
def ham_verify(driver):
    bookMark.hamburger_verify(driver)
    
    
 
@when(parsers.parse('user taps on "{text}" option'))
def bookmark_verify(driver):
    bookMark.bookmark_verify(driver)
    
    
    
@then('Verify that user should  navigate to Bookmarks Screen')
def bookmark_page(driver):
    bookMark.bookmark_screen(driver)
    bookMark.remove_bookmark(driver)

    
    
    
@then('Verify that app back button at the top left corner of the screen should be present')
def bmark_back(driver):
    bookMark.bmark_back(driver)
    
@then(parsers.parse('verify "{text}" text'))
def no_bookmart(driver):
    bookMark.nobookmark_txt(driver)
    
@then(parsers.parse('Verify "{text}" option'))
def bmark_filter(driver):
    bookMark.filter_option(driver)
    
@then(parsers.parse('Verify  "{text}" text  followed by Subjects tab'))
def bmark_allsubj(driver):
    bookMark.subject_txt(driver)
      
      
@given('Navigate to bookmark home screen')
def bmark_homescreen(driver):
    bookMark.hamburger_verify(driver)
    bookMark.bookmark_verify(driver)
    bookMark.bookmark_screen(driver)
    
    
@when('tap on app back button')
def bmark_back_btn(driver):
    bookMark.bmark_back_btn_click(driver)
    
    
@then('Verify that user should navigate to home screen')
def home_screen_verify(driver):
    bookMark.homescreen_verify(driver)
    
    
@when('tap on device back button')
def device_back_verify(driver):
    bookMark.device_back(driver)
    
    
@when('navigate to bookmark home screen')
def bmark_screen(driver):
    bookMark.hamburger_verify(driver)
    bookMark.bookmark_verify(driver)
    bookMark.bookmark_screen(driver)
    
    
@then(parsers.parse('Tap on "{text}" subject'))
def bmrk_subtap(driver,text):
    bookMark.subject_tap(driver, text)
    
    
@then(parsers.parse('Verify that user should navigate to "{text}" tab'))
def bmrk_subverify(driver,text):
    bookMark.sub_highlight_Verify(driver,text)
    
    
@given('Remove existing bookmarks')
def bmrk_remove(driver):
    bookMark.remove_bookmark(driver)
    
    
@when('Check for bookmarked content')
def bmrk_check(driver):
    bookMark.check_bookmark(driver)
    
    
@then(parsers.parse('Verify "{text}" message should be shown when there are no bookmarks' ))
def bmrk_msg(driver,text):
     
    bookMark.check_nobookmark(driver, text)
    

@when('Bookmark any video')
def Bmrkvideo_back(driver):
    bookMark.initial_remove_bookmark(driver)
    bookMark.Bookmark_video(driver)
    
    
@when('navigate back to bookmark screen')
def bmrk_screen(driver):
    bookMark.hamburger_verify(driver)
    bookMark.bookmark_verify(driver)
    bookMark.bookmark_screen(driver)
    
    
@then('verify bookmark  is present')
def Bmrk_present(driver):
    bookMark.bookmark_present(driver)
    
    
@then(parsers.parse('Verify "{text}" message not shown in all tab' ))
def nobmrk_txt(driver,text):
    bookMark.check_nobookmark_text(driver, text)
    
    
    