import pytest
import sys
import os
import subprocess
from time import sleep
from pytest_bdd import scenarios, given, when, then, parsers,scenario
from selenium.webdriver.common import keys
from appium import webdriver
from POM_Pages.bookmarkVideoSharing import BookmarkVideoSharing
from Utilities.BasePage import BaseClass





browser = fixture = 'browser'
base_class = BaseClass()
bmrk_video_share=BookmarkVideoSharing(browser)

"""storing the feature file name"""
featureFileName = "Bookmarkvideo Sharing"

"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""
scenarios('../features/'+featureFileName+'.feature')

@given('Launch the app online')
def loginapp(browser):
    bmrk_video_share.navigate_to_home_screen(browser)
    
@given('Bookmark any video')
def bookmark_video(browser):
    bmrk_video_share.initial_remove_bookmark(browser)
    bmrk_video_share.bookmark_video(browser)
    
    
@given('Navigate to bookmark home screen')
def bmark_homescreen(browser):
    bmrk_video_share.hamburger_verify(browser)
    bmrk_video_share.bookmark_verify(browser)
    bmrk_video_share.bookmark_screen(browser)
    
    
@when('Tap on bookmarked video')
def bmrkvideo_tap(browser):
    bmrk_video_share.bookmark_video_verify_tap(browser)
    
    
@when('Tap on Share option')
def bmrkshare_tap(browser):
    bmrk_video_share.shareicon_tap(browser)
    
    
@when('Select a mail option in Share with popup')
def tapon_gmail(browser):
    bmrk_video_share.gmail_verify_tap(browser)
    
    
@when('enter recipient mail ID')
def entermailid_gmail(browser):
    bmrk_video_share.to_mail_recipient_enter(browser)
    
    
@when('tap on send button')
def gmail_send(browser):
    bmrk_video_share.gmail_send_enter(browser)
    
    
@then('Verify that user should be able to share the video to the recipient mail id')
def video_share(browser):
    bmrk_video_share.video_share_tap(browser)
    
    
@then(parsers.parse('Verify the subject "{text}" should be pre filled'))
def verify_gsubject_text(browser,text):
    bmrk_video_share.verify_gmail_subject_text(browser, text)
    
    
@then(parsers.parse('Verify the description "{text}" verify link'))
def verify_gmailbody_text(browser,text):
    bmrk_video_share.verify_descriptiontext_and_link_in_a_mail(browser, text)
    
    
@then('Verify that user should navigate to compose mail screen')
def gmail_compose_verify(browser):
    bmrk_video_share.gmail_compose_verify(browser)
    
    
@when('Select a messaging option in Share with popup')
def tapon_message(browser):
    bmrk_video_share.messageverify_tap(browser)
    

@then(parsers.parse('Verify the description "{text}" verify  message link'))
def verify_messagebody_text(browser,text):
    bmrk_video_share.verify_descriptiontext_and_link_in_a_message(browser, text)
    
    
@given('bookmark a video from Journey') 
def bookmark_journey(browser):
    bmrk_video_share.initial_remove_bookmark(browser)
    bmrk_video_share.navigate_to_journey(browser)
    bmrk_video_share.first_journey(browser)
    bmrk_video_share.video_player_verify(browser)
    bmrk_video_share.bookmark_playericon_verify(browser)
    bmrk_video_share.video_player_bookmark_tap(browser)
    bmrk_video_share.fromjourneyto_homescreen(browser)
    
    
@then(parsers.parse('Verify the description "{text}" verify  journeymessage link'))
def verify_journeymessagebody_text(browser,text):
    bmrk_video_share.verify_journeydescriptiontext_and_link_in_a_message(browser, text)
    