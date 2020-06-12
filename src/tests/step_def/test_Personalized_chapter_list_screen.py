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
from Utilities.BasePage import BaseClass
from POM_Pages.personalizedChapterList import PersonalizedChapterList
from POM_Pages.Journeyloadingscreen import JourneyLoadingScreen
from POM_Pages.Journeymapscreen import JourneyMapScreen
from POM_Pages.Librarychapterlistscreen import LibraryChapterListsScreen
from Constants.constants import CONFIG_PATH, Login_Credentials
from Constants.load_json import getdata


browser = fixture = 'browser'
baseClass = BaseClass()
home = HomePage(browser)
personalize = PersonalizedChapterList(browser)
journey_map=JourneyMapScreen(browser)
journey_loading=JourneyLoadingScreen(browser)
library=LibraryChapterListsScreen(browser)    

"""storing the feature file name"""
featureFileName = "Personalized chapter list screen"

# baseClass.setupLogs(featureFileName)

"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""
scenarios('../features/' + featureFileName + '.feature')


# scenario 1
@given('Launch the app online')
def launch_app(browser):
    # journey_loading.switch_to_wifi(browser)
    # code = getdata(Login_Credentials,'login_detail5_search', 'code')
    # countrycode = getdata(Login_Credentials,'login_detail5_search', 'country_code')
    # mobno = getdata(Login_Credentials,'login_detail5_search', 'mobile_no')
    # otp = getdata(Login_Credentials,'login_detail5_search','OTP')
   # home.navigate_to_home_screen(browser,code ,countrycode, mobno, otp)
    pass

@when('User is in Personalized chapter list screen')
def personalized_chapter_screen_two(browser):
    home.select_subject_mathematics(browser)


@then('Verify that trending journey card should be highlighted')
def trending_journey(browser):
    personalize.verify_trending_journey_card_highlighted(browser)

# scenario 2
@given('User is new user')
def new_user(browser):
    pass


@given('User is in Personalized chapter list screen')
def personalized_chapter_screen(browser):
    home.select_subject_mathematics(browser)
    personalize.verify_personalised_chapter_list_screen(browser)
    personalize.go_up_with_respect_to_highlight_journey(browser)
    

# # scenario 3
@given('Device is white listed for search experiment')
def search_experiment(browser):
    pass


@when('User is in personalized chapter list screen.')
def personalised_chapter_3_line(browser):
    home.select_subject_mathematics(browser)
    personalize.verify_personalised_chapter_list_screen(browser)


@when('Trending journey card is highlighted after third row of chapter')
def trending_journey_card_after_third_row(browser):
    personalize.varify_trending_journey_in_third_or_below_row(browser)


@then('Verify back arrow on top left corner of the screen')
def varify_back_arrow(browser):
    personalize.varify_back_arrow_button(browser)


@then('Subject name center aligned')
def check_subject_name(browser):
    personalize.verify_subject_name_centre_allign(browser)


@then('back Button on top right corner of the screen')
def check_top_right_button(browser):
    personalize.varify_back_arrow_button(browser)


@then('Search button on top right corner of the screen')
def check_search_button(browser):
    personalize.verify_search_button(browser)


@then('Sticky card with recently taken chapter name followed by forward arrow')
def sticky_card_arrow(browser):
    personalize.verify_min_sticky_card_with_forward_arrow(browser)


# scenario 4
@when('Trending journey card is highlighted in first two rows of chapter')
def trending_journey_card(browser):
    personalize.varify_trending_journey_in_first_and_second_row(browser)


@then('Library button along with the text library at the top right side of the screen')
def library_button(browser):
    personalize.scroll_up_with_highlight_journey(browser)
    personalize.verify_library_button_and_text(browser)


@then('Verify that App back button on top left side of the screen')
def app_back_button(browser):
    personalize.varify_back_arrow_button(browser)


@then('Subject name followed by number of Chapters and Journeys')
def subject_name(browser):
    personalize.verify_subject_name_with_chapters_and_journeys(browser)


@then('Hero image')
def hero_image(browser):
    pass


@then('Below that resume where you left card with the journey/video name followed by forward icon(->)')
def recomanded_learning(browser):
    personalize.verify_resume_card_with_forward_icon(browser)


@then('Below that all the topics with respective journey cards ,test cards and practice cards')
def below_journey_cards(browser):
    personalize.verify_test_practice_and_journey_cards(browser)


@then('Ensure that each chapters in the journey screen should be separated by thin line')
def thin_line(browser):
    pass

# scenario 5

# scenario 6
@when('User taps on library button')
def click_on_personalized(browser):
    personalize.click_on_library_button(browser)


@then('Verify that user should be switched to library chapter list screen')
def library_chapter_screen(browser):
    personalize.verify_library_screen(browser)


# Scenario 7
@when('User taps on back arrow in personalized chapter list screen')
def click_on_back_button(browser):
    personalize.click_on_back_arrow(browser)


@then('Verify that user should be navigate back to home screen')
def display_home_screen(browser):
    personalize.verify_home_screen(browser)

# scenario 8    
@when('User taps on search button')
def tap_on_search(browser):
    personalize.click_on_search_button(browser)

@then('Verify that user should be navigate to <SearchScreen>')
def search_screen(browser):
    personalize.verify_search_screen(browser)


# @Scenario 9 
@when('User taps on resume where you left card')
def resume(browser):
    personalize.click_on_sticky_card(browser)


@then('Verify that user should be navigate to particular journey')
def verify_journey(browser):
#     personalize.verify_journey_name_with_respect_to_sticky_card(browser)
    journey_loading.verify_journey_map_screen(browser)

# scenario 10
@when('User taps on resume the practice card')
def resume_practice(browser):
    personalize.click_on_practice_card(browser)
    personalize.quit_inbtween(browser)


@then('Verify that user should be navigate to particular practice')
def practice_screen(browser):
    personalize.verify_practice_screen(browser)


# scenario 11
@when('User taps on resume the test card')
def resume_test(browser):
    personalize.click_on_test_card(browser)


@then('Verify that user should be navigate to particular test')
def ttest_screen(browser):
    personalize.verify_test_screen(browser)


# scenario 12
@when('User is in personalized chapter list screen')
def personalised_list(browser):
    home.select_subject_mathematics(browser)
    personalize.verify_personalised_chapter_list_screen(browser)
    personalize.go_up_with_respect_to_highlight_journey(browser)

@then('Verify that journey card should have journey icon and journey name')
def journey_icon_and_journey_name(browser):
    personalize.verify_journey_card_icon_and_name(browser)
    


# scenario 13  
@then('Verify that number of journey cards under each topic on personalized chapter list screen should be based on back end')
def total_journey_cards(browser):
#     personalize.journey_cards_in_each_chapters(browser)
    personalize.get_allchapter_names(browser)
    
  
    
# scenario 14
# @when('User is in Personalized chapter list screen.')
# def personalized_chapter_screen_one(browser):
#     home.select_subject_mathematics(browser)
#     sleep(3)
#     personalize.scroll_up_with_highlight_journey(browser)
#     personalize.verify_personalised_chapter_list_screen(browser)
    
# @then('Verify that each chapter should consists of tests and practices and should be based on back end')
# def check_test_and_practice(browser):
#     personalize.verify_test_and_practice(browser)

# scenario 15
@then('Verify that user should be able to see only chapter name and test card and practice card')
def chapter_name_test_practice(browser):
    personalize.go_up_with_respect_to_highlight_journey(browser)
    personalize.verify_test_practice_and_journey_cards(browser)
    
    
# scenario 16
@then('Verify that scrolling upwards the top label should be minimized')
def min_top_label(browser):
    personalize.verify_minimise_top_label(browser)


# scenario 17 
@when('User taps on journey card')
def tap_journey(browser):
    personalize.scroll_up_with_highlight_journey(browser)
    journey_loading.click_on_journey_card(browser)


@then('Verify that user navigates to journey loading screen first and then journey map screen of particular topic')
def verify_journey_loading_and_map_screen(browser):
    journey_loading.verify_journey_loading_screen(browser)
    personalize.verify_journey_map_screen(browser)


# scenario 18  
@given('User is in Offline')
def offline(browser):
    journey_map.select_offline_mode(browser)

@when('User taps on a journey card')
def tap_on_a_journey(browser):
    personalize.scroll_up_with_highlight_journey(browser)
    journey_loading.click_on_new_journey_card(browser)
#     journey_map.click_on_trending_journey_card(browser)

@then(parsers.parse('Verify that "{text}" toast message should be shown'))
def toast_msg(browser,text):
    personalize.verify_toast_message(browser, text)


@then('user should be navigate back to chapter list screen')
def chapter(browser):
    library.verify_personalised_screen(browser)
    journey_loading.switch_to_wifi(browser)


#  scenario 19
@when('User taps on test card')
def tap_test(browser):
    personalize.click_on_test_card(browser)


@then('Verify that user should be navigates to <TestScreen> of particular topic')
def verify_test(browser):
    personalize.verify_test_screen(browser)


#  scenario 20
@when('User taps on practice card')
def tap_practice_card(browser):
    personalize.click_on_practice_card(browser)


@then('Verify that user should be navigate to <PracticeScreen> of particular topic')
def verify_practice_card(browser):
    personalize.verify_practice_screen(browser)
    