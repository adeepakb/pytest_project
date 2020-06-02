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
from POM_Pages.startPracticeScreen import StartPracticeScreen

browser = fixture = 'browser'
baseClass = BaseClass()
home = HomePage(browser)
cons = ConceptSummaryScreen(browser)
revisit=RevisitScreen(browser)
start=StartPracticeScreen(browser)

"""storing the feature file name"""
featureFileName = "Start Practice screen"

"""configuring the Logging Files"""
baseClass.setupLogs(featureFileName)

"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""
scenarios('../features/' + featureFileName + '.feature')

# scenario 1
@given('Launch the app')
def launch(browser):
    home.navigate_to_home_screen(browser)
    home.select_subject_mathematics(browser)
    revisit.click_on_revisit_journey_card(browser)


@when('User is in "Start Practice" screen')
def start_parctice(browser):
    revisit.swipe_for_swipe_to_start(browser)
    cons.scroll_concept(browser)


@then('Verify Practice icon')
def practice_icon(browser):
    revisit.verify_practice_screen(browser)


@then('Verify "Practice" label')
def practice_label(browser):
    start.verify_practice_label(browser)


@then(parsers.parse('Verify "{text}" text'))
def description(browser,text):
    start.verify_practice_description_text(browser,text)


@then('Verify "Start Practice" button')
def btn_practice(browser):
    start.verify_practice_button(browser)


# scenario 2
@given('User is in "Start Practice" screen')
def start_parctice_one(browser):
    revisit.swipe_for_swipe_to_start(browser)
    cons.scroll_concept(browser)


@when('User taps on "Start Practice" screen')
def click_on_practice(browser):
    start.click_on_practice_button(browser)


@then('Verify that user should be redirected to <QuestionScreen>')
def que_screen(browser):
    start.verify_question_screen(browser)