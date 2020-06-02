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
from POM_Pages.revisitScreen import RevisitScreen

browser = fixture = 'browser'
baseClass = BaseClass()
home = HomePage(browser)
revisit = RevisitScreen(browser)
"""storing the feature file name"""
featureFileName = "Revisit Screen"

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


@when('User is in Lets revisit screen')
def revisit_screen(browser):
    revisit.verify_revisit_screen(browser)


@then('Verify Card progress bars')
def progression_bar(browser):
    revisit.verify_progression_bar(browser)


@then('Verify "Close" icon below the progress bars')
def close_icon(browser):
    revisit.verify_close_icon(browser)


@then('Verify Lets revisit label')
def revisit_label(browser):
    revisit.verify_lets_revisit_label(browser)


@then('Verify Concept summary details Concepts name and Last learnt details')
def progression_bar_one(browser):
    revisit.verify_concepts_summary_details_and_count(browser)


@then(parsers.parse('Verify "{text}" text'))
def description_text(browser,text):
    revisit.verify_text_description(browser,text)


@then(parsers.parse('Verify "{text}" a text CTA with backward arrow icon'))
def swipe_to_start(browser,text):
    revisit.verify_text_swipe_to_start(browser,text)


# scenario 3
@given('User is in Lets revisit screen')
def revisit_screen1(browser):
    revisit.verify_revisit_screen(browser)


@when('User swipe "Swipe to start" text CTA')
def swipe_for_start(browser):
    revisit.swipe_for_swipe_to_start(browser)
    # revisit.swipe_till_practice_screen(browser)


@then('Verify that user should navigate to "Concept summary" screen')
def concept_summary(browser):
    revisit.verify_concept_summary_screen(browser)


# scenario 4
@when('User taps on "Close" button')
def click_close(browser):
    revisit.click_on_close_icon(browser)


@then('Verify that user should be redirected to journey map screen')
def journey_loading(browser):
    revisit.verify_journey_map_screen(browser)


# scenario 5
@when('User taps on device back button')
def click_device_back_btn(browser):
    sleep(5)
    revisit.click_on_device_back_btn(browser)


# scenario 6
@given('Users KG score of the concepts in the question node should be less than 60')
def kg_score_less_then_sixty(browser):
    pass


# scenario 7
@given('Users KG score of all concepts in the question node should be above or equal to 60')
def kg_score_greater_sixty(browser):
    pass


@then('Verify that user should navigate to <StartPracticeScreen>')
def practice_screen(browser):
    revisit.verify_practice_screen(browser)