import pytest
import sys
import os
import subprocess
from time import sleep
from pytest_bdd import scenarios, given, when, then, parsers,scenario
from selenium.webdriver.common import keys
from appium import webdriver
from POM_Pages.bookmarkvideo import Bookmark_video
from Utilities.BasePage import BaseClass





browser = fixture = 'browser'
base_class = BaseClass()
bmrkvideo=Bookmark_video(browser)

"""storing the feature file name"""
featureFileName = "Bookmark videos"

"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""
scenarios('../features/'+featureFileName+'.feature')

@given('Launch the app online')
def loginapp(browser):
    bmrkvideo.navigate_to_home_screen(browser)
    
    
@given('Bookmark any video')
def bookmark_video(browser):
     bmrkvideo.initial_remove_bookmark(browser)
     bmrkvideo.bookmark_video(browser)
     
     
@given('Navigate to bookmark home screen')
def bmark_homescreen(browser):
    bmrkvideo.hamburger_verify(browser)
    bmrkvideo.bookmark_verify(browser)
    bmrkvideo.bookmark_screen(browser)
    
    
@when('Navigate to bookmark home screen')
def bmarkhomescreen(browser):
    bmrkvideo.hamburger_verify(browser)
    bmrkvideo.bookmark_verify(browser)
    bmrkvideo.bookmark_screen(browser)
    
    
@when('Tap on bookmarked video')
def bmrkvideo_tap(browser):
    bmrkvideo.bookmark_video_verify_tap(browser)
    
    
@when('Tap on device back button')
def device_back(browser):
    bmrkvideo.device_back(browser)
    
    
@then('Verify that user should navigate back  to bookmark home screen')
def verify_bookmarkscreen(browser):
    bmrkvideo.bookmark_screen(browser)
    bmrkvideo.remove_bookmark(browser)
    
    
@when('Tap on videoplayer back button')
def videoback_tap(browser):
    bmrkvideo.videoplayer_back(browser)
    
    
@then('Verify videoplayer back button')
def verify_videoplayer_back(browser):
    bmrkvideo.videoplayer_back_verify(browser)
    
    
@then('verify chaptername')
def verify_videoplayer_chaptername(browser):
    bmrkvideo.videoplayer_chaptername_verify(browser)
    
    
@then('verify share icon')
def verify_videoplayer_shareicon(browser):
    bmrkvideo.videoplayer_shareicon_verify(browser)
    
    
@then('verify videolist icon')
def verify_videoplayer_listicon(browser):
    bmrkvideo.videoplayer_listicon_verify(browser)
    
    
@then('verify Bookmark icon')
def verify_videoplayer_Bookmarkicon(browser):
    bmrkvideo.videoplayer_bookmark_verify(browser)
    
    
@then('Verify that user should navigate to bookmarked video screen')
def verify_videoplayer(browser):
    bmrkvideo.video_player_verify(browser)
    
    
@then(parsers.parse('verify "{text}" toast message displayed'))
def verify_toast(browser,text):
    bmrkvideo.verify_toast_msg(browser, text)
    
    
@then('tap on Bookmark icon')
def bookmarkvideoicon_tap(browser):
    bmrkvideo.video_player_bookmark_tap(browser)
    
    
@then('Verify that bookmark icon should be present in the video player overlay')
def bookmarkicon_verify(browser):
    bmrkvideo.bookmark_playericon_verify(browser)
    
    
@when('navigate to library video screen')
def bookmark_libvideo(browser):
    bmrkvideo.library_video_screen(browser)
    
    
@then(parsers.parse('verify that "{text}" toast message should be displayed at the bottom of the screen'))
def verify_toastmsg(browser,text):
    bmrkvideo.verify_toast_msg(browser, text)
    
    
@when('once again tap on same bookmark icon')
def unbookmark_video(browser):
    bmrkvideo.unbookmark_video(browser)
    
    
@then('Verify unbookmarked video should be removed from the bookmark home screen under All tab and subject tab')
def removedvideo_verify(browser):
    bmrkvideo.bookmark_video_removed(browser)
    
    
@given('remove existing bookmark')
def remove_initialbmrk(browser):
    bmrkvideo.initial_remove_bookmark(browser)
    
    
@when('unbookmark the video')
def unbookmark(browser):
    bmrkvideo.remove_bookmark(browser)
    
    
@then('Tap on undo option')
def tapundo(browser):
    bmrkvideo.undo_toast_msg(browser)
    
    
@then('Verify that Bookmark Removed undo  toast message should be shown on un unbookmark the video')
def stack_msg(browser):
    bmrkvideo.boolmark_stack_toast_msg(browser)
    
    
@then('Tap on the undo option after unbookmarking the bookmarked video')
def bookmark_undo(browser):
    bmrkvideo.bookmark_toast_undo(browser)
    
    
@then('Verify that removed video should reappear in the bookmark home screen')
def bookmarkvideo_verify(browser):
    bmrkvideo.bookmark_video_verify(browser)
    
    
@then('Verify that Video thumbnail should be present')
def videothumbnail(browser):
    bmrkvideo.bookmark_video_verify(browser)
    
    
@then('Verify Video name')
def videoname(browser):
    bmrkvideo.bookmark_videotitle_verify(browser)
    
    
@then('Verify subject name chapter name')
def video_subject_chapter(browser):
    bmrkvideo.bookmark_subject_chapter_verify(browser)
    
    
@then('Verify bookmark icon')
def bmrkscreen_icon(browser):
    bmrkvideo.bookmark_screen_bookmarkicon(browser)
    
    
@when('navigate to library video screen')
def videoscreen(browser):
    bmrkvideo.navigate_to_video_screen(browser)
    
    
@then('Verify that bookmark icon should be present in the video player overlay')
def playerbookmarkicon_verify(browser):
    bmrkvideo.bookmark_playericon_verify(browser)
    
    
@when('Switch off the device data')
def bookmarkvideo_offline(browser):
    bmrkvideo.select_offline_mode(browser)
    
    
@then(parsers.parse('Verify that user should get a toast message "{text}" on tapping on bookmarked video'))
def offline_toastmsg(browser,text):
    bmrkvideo.offline_toast_verify(browser, text)

@given('navigate to personalised mode')
def landon_personalisedscreen(browser):
    bmrkvideo.navigate_to_journey(browser)
    
    
@given('Tap on any journey')
def taponjourney(browser):
    bmrkvideo.first_journey(browser)
    
    
@when('Verify that bookmark icon should be present in the video player overlay')
def journeyplayerbookmarkicon_verify(browser):
    bmrkvideo.video_player_verify(browser)
    bmrkvideo.bookmark_playericon_verify(browser)
    
    
@when('tap on Bookmark icon')
def journeybookmarkvideoicon_tap(browser):
    bmrkvideo.video_player_bookmark_tap(browser)
    
    
@when('Navigate to profile screen verify user is in 8th grade')
def verify8thgrade(browser):
    bmrkvideo.verify_8thgrade(browser)
    
    
@when('switch to 9th grade')
def switchto9thgrade(browser):
    bmrkvideo.switchto_9thgrade(browser)
    
    
@then(parsers.parse('Verify "{text}" message should be shown when there are no bookmarks' ))
def bmrk_msg(browser,text):
    bmrkvideo.check_nobookmark(browser, text)
    
@then('Switch on the device data')
def bookmarkvideo_online(browser):
    bmrkvideo.switch_to_wifi(browser)
    
    
@when('Navigate back to home screen')
def journeytohome_screen(browser):
    bmrkvideo.fromjourneyto_homescreen(browser)
    

@when('unbookmark the video') 
def undobookmark_video(browser):
    bmrkvideo.video_player_bookmark_tap(browser) 
    
     
@given('bookmark a video from Journey') 
def bookmark_journey(browser):
    bmrkvideo.initial_remove_bookmark(browser)
    bmrkvideo.navigate_to_journey(browser)
    bmrkvideo.first_journey(browser)
    bmrkvideo.video_player_verify(browser)
    bmrkvideo.bookmark_playericon_verify(browser)
    bmrkvideo.video_player_bookmark_tap(browser)
    bmrkvideo.fromjourneyto_homescreen(browser)
    
    
@given('bookmark a video from Library')
def bookmark_videoplayer(browser):
    bmrkvideo.bookmark_video(browser)
    
    
@then('Verify that app back button at the top left corner of the screen should be present')
def bmark_back(browser):
    bmrkvideo.bmark_back(browser)
    
    
@then(parsers.parse('Verify "{text}" option'))
def bmark_filter(browser):
    bmrkvideo.filter_option(browser)
    
    
@then(parsers.parse('Verify  "{text}" text  followed by Subjects tab'))
def bmark_allsubj(browser):
    bmrkvideo.subject_txt(browser)
    
    
    
    
    

    




    