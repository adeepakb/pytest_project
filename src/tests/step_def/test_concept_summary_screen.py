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
from POM_Pages.ConceptSummaryScreen import ConceptSummaryScreen
from POM_Pages.revisitScreen import RevisitScreen

browser = fixture = 'browser'
baseClass = BaseClass()
home = HomePage(browser)
cons = ConceptSummaryScreen(browser)
revisit=RevisitScreen(browser)
"""storing the feature file name"""
featureFileName = "Concept Summary Screen"

"""configuring the Logging Files"""
baseClass.setupLogs(featureFileName)

"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""
scenarios('../features/' + featureFileName + '.feature')

# scenario 1
@given('Launch the app')
def launch_app(browser):
    home.navigate_to_home_screen(browser)
    home.select_subject_mathematics(browser)
    revisit.click_on_revisit_journey_card(browser)


@given('User is in Lets revisit screen')
def revisit_screen(browser):
    revisit.verify_revisit_screen(browser)
    sleep(3)


@when('User swipe "Swipe to start" text CTA')
def swipe(browser):
    revisit.swipe_for_swipe_to_start(browser)
    # revisit.swipe_till_practice_screen(browser)


@then('Verify that concept summary screen should be shown for two concepts')
def two_concepts(browser):
    cons.for_two_concepts(browser)


# scenario 3
@when('User is in Concept summary screen')
def concept_screen(browser):
    revisit.swipe_for_swipe_to_start(browser)
    sleep(3)
    revisit.verify_concept_summary_screen(browser)


@then('Verify Summary Progress bars on top of the screen')
def progress_bar(browser):
    revisit.verify_progression_bar(browser)


@then('Verify "Close" icon on top left corner  of the screen')
def close(browser):
    revisit.verify_close_icon(browser)


@then('Verify <ConceptName> on top header of the screen')
def concept_name(browser):
    print(dir(cons))
    cons.verify_chapter_name(browser)


@then('Verify Video Card')
def video_card(browser):
    cons.verify_video_player(browser)


# scenario 4
@given('User is in Concept summary screen')
def concept(browser):
    revisit.swipe_for_swipe_to_start(browser)
    sleep(3)
    revisit.verify_concept_summary_screen(browser)


@when('User taps on "Close" button')
def close_one(browser):
    revisit.click_on_close_icon(browser)


@then('Verify that user should be redirected to <JourneyMapScreen>')
def journey(browser):
    revisit.verify_journey_map_screen(browser)


# scenario 5
@given('User is in Concept summary Screen')
def concept1(browser):
    revisit.swipe_for_swipe_to_start(browser)


@when('User swipe "Concept Summary" card')
def scroll_till_practice(browser):
    cons.scroll_concept(browser)


@then('Verify that user should be redirected to "Start Practice" screen')
def practice_screen(browser):
    revisit.verify_practice_screen(browser)


# scenario 6
@when('User taps on device back button')
def back(browser):
    revisit.click_on_device_back_btn(browser)


# scenario 7
@when('User taps on video card')
def tap_on_video(browser):
    # cons.click_on_video_card(browser)
    pass


@then('Verify that tapping on video card video should be played')
def played_video(browser):
    cons.check_video_played(browser)