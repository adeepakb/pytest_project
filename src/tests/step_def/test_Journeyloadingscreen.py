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
from POM_Pages.Journeyloadingscreen import JourneyLoadingScreen
from Constants.constants import CONFIG_PATH, Login_Credentials
from Constants.load_json import getdata


browser = fixture = 'browser'
baseClass = BaseClass()
home = HomePage(browser)
journey_start=JourneyLoadingScreen(browser)
"""storing the feature file name"""
featureFileName = "Journey loading screen"

# baseClass.setupLogs(featureFileName)

"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""
scenarios('../features/' + featureFileName + '.feature')

# scenario 1
@given('Launch the app online')
def launch_app(browser):
    # journey_start.switch_to_wifi(browser)
    # code = getdata(Login_Credentials,'login_details2', 'code')
    # countrycode = getdata(Login_Credentials,'login_details2', 'country_code')
    # mobno = getdata(Login_Credentials,'login_details2', 'mobile_no')
    # otp = getdata(Login_Credentials,'login_details2','OTP')
    home.navigate_to_home_screen(browser)
    pass

@when('User is in journey loading Screen')
def personalized_chapter_screen(browser):
    home.select_subject_mathematics(browser)
#     journey_start.switch_to_twoG(browser)
    journey_start.verify_personaised_screen(browser)
    journey_start.click_on_journey_card(browser)


@then('Verify "Back arrow" on top left corner of the screen')
def back_arrow(browser):
    journey_start.verify_back_arrow(browser)


@then('Verify <Chapter name>')
def chapter_name(browser):
    journey_start.verify_chapter_name(browser)


@then('Verify image')
def image(browser):
    pass


@then('Verify "Hi <Username>! Analysing your learning profile to find the best path for you" text')
def msg(browser):
    journey_start.verify_msg(browser)


# scenario 2
@given('user is in journey loading screen')
def personalized_chapter_screen1(browser):
    home.select_subject_mathematics(browser)
#     journey_start.switch_to_twoG(browser)
    journey_start.click_on_journey_card(browser)
    journey_start.click_on_device_back_Btn(browser)


@when('User taps on back button')
def click_on_back(browser):
    # journey_loading.click_on_device_back_Btn(browser)
    pass


@then('Verify that user should be redirected to <PersonalisedChapterListScreen>')
def personalised_screen(browser):
    journey_start.verify_personaised_screen(browser)


# scenario 3
@given('User opens the journey for the first time')
def open_journey_first_time(browser):
    home.select_subject_mathematics(browser)
    journey_start.scroll_up_with_highlight_journey(browser)
    journey_start.click_on_new_journey_card(browser)


@when('User is in journey loading screen')
def journey_loading(browser):
    journey_start.verify_journey_loading_screen(browser)


@then('Verify that user should navigate to <JourneyMapScreen> after the loading screen')
def journey_map_screen(browser):
    journey_start.verify_journey_map_screen(browser)


@then('Verify formation of map should start')
def map_formation(browser):
    pass


@then('Verify the nodes appear with node names followed by node arrangement')
def node_names(browser):
    journey_start.nodes(browser)


# scenario 4
@given('Launch the app online.')
def app_online(browser):
#     journey_start.switch_to_wifi(browser)
    home.navigate_to_home_screen(browser)
    


@given('User opens already downloaded journey')
def already_loaded_journey(browser):
    home.select_subject_mathematics(browser)
    journey_start.scroll_up_with_highlight_journey(browser)
    journey_start.click_on_already_taken_journey_card(browser)


@then('Verify auto load the node which user need to continue to proceed the journey')
def auto_load_node(browser):
    journey_start.verify_resource_screen(browser)
    
    