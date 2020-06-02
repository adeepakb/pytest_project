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
featureFileName = "Question screen"

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


@when('User is Question Screen')
def click_on_practice(browser):
    revisit.swipe_for_swipe_to_start(browser)
    cons.scroll_concept(browser)
    start.verify_question_screen(browser)


@then('Verify Summary Progress bars on top of the screen')
def progress_bar(browser):
    pass


@then('Verify "Close icon" on top left corner  of the screen')
def close_icon(browser):
    pass


@then('Verify "Practice" label on top header of the screen')
def practice_label(browser):
    pass


@then('Verify "Question" label and Question description')
def que_label(browser):
    pass


@then('Verify Options should be displayed below the Question')
def options(browser):
    pass


@then('Verify <CurrentQuestionNumber/TotalNumberofQuestions> at bottom right corner of the screen')
def total_ques(browser):
    pass

