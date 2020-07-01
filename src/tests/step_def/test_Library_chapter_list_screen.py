import pytest
from pytest_bdd import scenarios, given, when, then, parsers, scenario

import os
import sys
import subprocess
import logging
from time import sleep

from appium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from POM_Pages.homepage import HomePage
from POM_Pages.Librarychapterlistscreen import LibraryChapterListsScreen
from Utilities.BasePage import BaseClass
from POM_Pages.personalizedChapterList import PersonalizedChapterList
from Constants.constants import CONFIG_PATH, Login_Credentials
from Constants.load_json import getdata

browser = fixture = 'browser'
baseClass = BaseClass()
home = HomePage(browser)
library = LibraryChapterListsScreen(browser)
personalize = PersonalizedChapterList(browser)

"""storing the feature file name"""
featureFileName = "Library chapter list screen"

#baseClass.setupLogs(featureFileName)

"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""
scenarios('../features/' + featureFileName + '.feature')


# scenario 1
@given('Launch the app online')
def launch_app(browser):
    # code = getdata(Login_Credentials,'login_detail5_search', 'code')
    # countrycode = getdata(Login_Credentials,'login_detail5_search', 'country_code')
    # mobno = getdata(Login_Credentials,'login_detail5_search', 'mobile_no')
    # otp = getdata(Login_Credentials,'login_detail5_search','OTP')
    home.navigate_to_home_screen(browser)
    pass


@given('User is in Personalized Chapter list screen')
def personalized_chapter_screen(browser):
    home.select_subject_mathematics(browser)

    
@when('User taps on app back button')
def tap_on_back_button(browser):
    personalize.click_on_back_arrow(browser)


@then('Verify that user should be navigate to home screen')
def navigate_to_home(browser):
    personalize.verify_home_screen(browser)


# scenario 2
@then('Verify the App back button on top left corner of the screen')
def app_back_btn(browser):
    library.verify_app_back_arrow(browser)


@then(parsers.parse('Personalized button along with the text "{text}" at the top right of the screen.'))
def personalised_btn(browser,text):
    library.verify_personalise_btn(browser, text)


@then('Search button should be shown next to personalized button.')
def search_btn(browser):
    personalize.verify_search_button(browser)


@then('Subject Name followed by number of Videos and Tests')
def sub_videos_tests(browser):
    library.verify_chapters_heading(browser)


@then('Below the top layout, a label Chapters and list of chapters(Library carousel) below it')
def chapters_chapters_list(browser):
    library.chapter_name_with_total_video_count(browser)

# scenario 3
@when('User is in Library Chapter list screen')
def library_chapter_screen(browser):
    home.select_subject_mathematics(browser)
    library.verify_library_cha_screen(browser)
    

@when('User taps on personalized button')
def tep_on_personalized_button(browser):
    library.click_on_personlised_button(browser)


@then('Verify that user switches to personalized mode chapter list screen')
def navigate_to_personalized_screen(browser):
    library.verify_personalised_screen(browser)


# scenario 4
@then('Verify that chapter name and total number of video count')
def chapter_name_with_video_count(browser):
    library.chapter_name_with_total_video_count(browser)


@then('Video card with video thumbnail and Video Progression below the video thumbnail')
def verify_video_card_and_video_thumbail(browser):
    library.verify_video_thumbnail_progression_bar(browser)
    


@then('Test Button and Practice Button')
def practice_and_test(browser):
    library.verify_test_and_practice_btns(browser)


# scenario 5
@then('Verify that Chapter name should be displayed')
def chapter_names(browser):
#     library.chapter_names_without_video(browser)
    pass


@then('Test button and Practice button')
def practice(browser):
    library.verify_test_and_practice_for_empty_chapter(browser)


# scenario 7
@then('Verify that each chapter in the subject should have video carousel in Library chapter list screen.')
def video_carousel(browser):
    library.verify_video_corousel(browser)


# scenario 8
@when('User taps on video card in Library chapter list screen of particular chapter')
def tap_on_video(browser):
    library.click_on_video_card(browser)


@then('Verify that user should be navigates to video list screen of particular topic')
def verify_video(browser):
    library.verify_video_screen_of_perticular_chapter(browser)


# scenario 9
@when('User taps on test button on library chapter list screen of particular chapter')
def click_on_test(browser):
    library.click_on_test_button(browser)


@then('Verify that user should be navigates to test list screen of particular topic')
def verify_test(browser):
    library.verify_test_screen(browser)


# scenario 10
@when('User taps on practice button on library chapter list screen of particular chapter')
def tap_on_practice(browser):
    library.click_on_practice_button(browser)
    sleep(2)


@then('Verify that user should be navigates to practice list screen of particular topic')
def verify_practice(browser):
    library.verify_practice_screen(browser)


# scenario 11
@when('User taps on back button on library chapter list screen')
def tep_on_back_button(browser):
    sleep(2)
    library.click_on_back_arrow(browser)


@then('Verify that user should be navigate to home screen')
def verify_home(browser):
    sleep(2)
    library.verify_home_screen(browser)


# scenario 12
@when('User taps on same subject card')
def tep_on_subject_card(browser):
    home.select_subject_mathematics(browser)


@then('Verify that user should be navigate to library chapter list screen')
def navigate_to_library_chapter_list_screen(browser):
    library.verify_library_screen(browser)
