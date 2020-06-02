import pytest
import sys
import os
import subprocess
from time import sleep
from pytest_bdd import scenarios, given, when, then, parsers,scenario
from selenium.webdriver.common import keys
from appium import webdriver
from POM_Pages.bookMarkPage import BookMark
from POM_Pages.bookmarkFilter import Bookmark_filter
from Utilities.BasePage import BaseClass





browser = fixture = 'browser'
base_class = BaseClass()
bmrkfilter=Bookmark_filter(browser)

"""storing the feature file name"""
featureFileName = "Bookmark home screen filter slider"

"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""
scenarios('../features/'+featureFileName+'.feature')


@given('Launch the app online')
def loginapp(browser):
    bmrkfilter.navigate_to_home_screen(browser)
    
    
@given('Navigate to bookmark home screen')
def bmark_homescreen(browser):
    bmrkfilter.hamburger_verify(browser)
    bmrkfilter.bookmark_verify(browser)
    bmrkfilter.bookmark_screen(browser)
    
@when('Tap on Filter button')
def filter_click(browser):
    bmrkfilter.filter_tap(browser)
    
    
@then('Verify the Cross button')
def filter_close(browser):
    bmrkfilter.filter_close_verify(browser)
    
    
@then(parsers.parse('Verify the Label "{text}"'))
def filter_labelverify(browser,text):
    bmrkfilter.verify_filter_txt(browser,text)
    
    
@then('Verify below that Show All option with radio button')
def showalltxtbtn(browser):
    bmrkfilter.showalltxt_btn(browser)
    
    
@then('Verify below that Questions option with radio button')
def questiontxtbtn(browser):
    bmrkfilter.questiontxt_btn(browser)
    
    
@then('Verify below that Videos option with radio button')
def videotxtbtn(browser):
    bmrkfilter.videos_txt_btn(browser)
    
    
@when('Tap on Filter close button')
def filterclose(browser):
    bmrkfilter.filter_closebtn(browser)
    
    
@then('Verify that filter slider should disappear')
def filterscreen_check(browser):
    bmrkfilter.filterscreen_verify(browser)
    
    
@given('Bookmark any video')
def bookmark_video(browser):
    bmrkfilter.bookmark_video(browser)
    
    
@given('Bookmark any question')
def bookmark_question(browser):
    bmrkfilter.bookmark_question(browser)
    
    
@when('Verify show all option is selected')
def showall_btn_verify(browser):
    bmrkfilter.showall_selected(browser)
    
    
@when('Tap on show all')
def showall_btn_tap(browser):
    bmrkfilter.tap_showall(browser)
    
    
@then('Verify that all the bookmarked contents should display in bookmark home screen under All tab')
def bmrk_alltab(browser):
    bmrkfilter.all_highlight_Verify(browser)
    bmrkfilter.remove_bookmark(browser)
    
    
@when('Tap on videos option')
def video_tap(browser):
    bmrkfilter.tap_filter_video_btn(browser)
    
    
@then('Verify that only bookmarked videos should display in bookmark home screen under All tab')
def bmrk_videoverify_alltab(browser):
    bmrkfilter.Bookmark_video_verify(browser)
    bmrkfilter.remove_bookmark(browser)
    
    
@when('Tap on questions option')
def question_tap(browser):
    bmrkfilter.tap_filter_question_btn(browser)
    
    
@then('Verify that only bookmarked questions should display in bookmark home screen under All tab')
def bmrk_questionverify_alltab(browser):
    bmrkfilter.bookmark_question_verify(browser)
    bmrkfilter.remove_bookmark(browser)







