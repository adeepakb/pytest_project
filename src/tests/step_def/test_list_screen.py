from time import sleep
import subprocess
from selenium.webdriver.common import keys
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from pytest_bdd import scenarios, given, when, then, parsers,scenario
from POM_Pages.engine_test_list_screen import EngineTestListScreen
import pytest
import logging
import datetime
from Utilities.BasePage import BaseClass
browser = fixture = 'browser'


baseClass = BaseClass()
testlistscn = EngineTestListScreen(browser)
featureFileName = 'Test List Screen'


baseClass.setupLogs(featureFileName)


"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""

scenarios('../features/' + featureFileName + '.feature')


@given('Launch the app online and navigate to Home screen')
def loginapp(browser):
    testlistscn.navigate_to_home_screen(browser)


@given(parsers.parse('Navigate to "{Subject}" library screen'))
def navigate_to_subject_library_scn(browser,Subject):
    testlistscn.navigate_to_library(browser, Subject)    
    
    
@when('Tap on the "Test" option')
def tap_on_test_link(browser):
    testlistscn.tap_on_test_link(browser)

@when('Verify that user lands on the "Test List" screen')    
@then('Verify that user lands on the "Test List" screen')
def verify_test_list_screen(browser):
    testlistscn.verify_test_list_screen(browser)


@then('Verify App back arrow icon should be shown')
def verify_app_back_button(browser):
    testlistscn.verify_app_back_button(browser)

@then('Verify Chapter Name should shown in the header of the screen')
def verify_chapter_name(browser):
    testlistscn.verify_chapter_name(browser)

@then('Verify Chapter icon should be shown top right side of the screen')
def verify_chapter_icon(browser):
    testlistscn.verify_chapter_icon(browser)
    
@then(parsers.parse('Verify "{text}" label'))
def verify_the_text(browser,text):
    testlistscn.verify_the_text(browser,text)

@then('Verify Test cards should be display below the Tests label')    
@then('Verify Objective test card should be display below the objective test label')
def verify_objective_test_list(browser):
    testlistscn.verify_objective_test_list(browser)
    
@then('Verify Subjective test card should be display below the Subjective Test label')
def verify_subjective_test_list(browser):
    testlistscn.verify_subjective_test_list(browser)

@then('Verify objective tests should be named "Objective Test 0x"')
def objective_test_card(browser):
    testlistscn.verify_objective_test_card(browser)

    
@then('Verify where x being numbers in ascending order of objective test')
def check_obective_test_order(browser):
    testlistscn.check_obective_test_order(browser)
    
@then('Verify "Start" button should shown in front of objective test')
def verify_start_button(browser):
    testlistscn.verify_start_button(browser)

@then('Verify subjective tests should be named "Subjective Test 0x" format')
def verify_subjective_test_card(browser):
    testlistscn.verify_subjective_test_card(browser)

    
@then('Verify where x being numbers in ascending order of subjective test')
def check_subjective_test_order(browser):
    testlistscn.check_subjective_test_order(browser)
    
@then('Verify "Revise" button should be appear front of Subjective test')
def verify_revise_button(browser):
    testlistscn.verify_revise_button(browser)

@given('Verify that user lands on the "Test List" screen')
def verify_test_list_screen1(browser):
    testlistscn.verify_test_list_screen(browser)

@given('Tap on the "Test" option')
def tap_on_test_link1(browser):
    testlistscn.tap_on_test_link(browser)
    
@when('Tap on the "Start" option')
def navigate_to_test_instruction_screen(browser):
    testlistscn.navigate_to_test_instruction_screen(browser)

@then('Tap on "Test" button in instruction screen')    
@when('Take a test')
def tap_on_test_button_on_instruction_scn(browser):
    testlistscn.tap_on_test_button_on_instruction_scn(browser)
    
@when('Submit the test')
def submit_test(browser):
    testlistscn.submit_test(browser)
    
@then('Verify "Start" button should be replaced with "Analyse" text')
def verify_analyse_option(browser):
    testlistscn.navigate_back_to_test_list_scn(browser)
    testlistscn.verify_analyse_option(browser)

@then('Verify retake test icon should be shown before Analyse text with chevron icon')
def verify_retake_test_icon(browser):
    testlistscn.verify_retake_test_icon(browser)

@then('Tap on retake test icon')    
@when('Tap on retake test icon')
def tap_on_retake_test_option(browser):
    testlistscn.tap_on_retake_test_option(browser)
    
@then('Verify user should redirect to Instruction screen')
def verify_test_instruction_screen(browser):
    testlistscn.verify_test_instruction_screen(browser)
    
@then('Verify user redirect to objective test Question screen')
def verify_test_question_screen(browser):
    testlistscn.verify_test_question_screen(browser)
    
@given(parsers.parse('Navigate to "{Subject}" learn screen'))
def navigate_to_learn_screen(browser,Subject):
    testlistscn.navigate_to_learn_screen(browser, Subject)  
    
@when('Tap on the test card which is present in learn screen')
def scroll_to_test_and_click(browser):
    testlistscn.scroll_to_test_and_click(browser)

@then('Tap on Analyse button')    
@when('Tap on Analyse button')
def tap_on_analyse_option(browser):
    testlistscn.tap_on_analyse_option(browser)
    
@then('Verify that user should redirect to the highlights screen')
def verify_highlights_screen(browser):
    testlistscn.verify_highlights_screen(browser)

@then('Tap on Start button')
@when('Tap on Start button')
def tap_on_start_button(browser):
    testlistscn.tap_on_start_button(browser)
    
@when('Tap on video card')
def tap_on_video_card(browser):
    testlistscn.tap_on_video_card(browser)
    
@when('Tap on Test list card on video list screen')
def tap_test_card_on_video_list(browser):
    testlistscn.tap_test_card_on_video_list(browser)
    
@when('Tap on app back button')
def tap_on_app_backbtn(browser):
    sleep(2)
    testlistscn.app_backbtn(browser)
    
@then('Verify that user is in Library chapter list screen')
def verify_library_screen(browser):
    testlistscn.verify_library_screen(browser)
    
@then('Verify that user is in Learn chapter list screen')
def verify_learn_screen(browser):
    testlistscn.verify_learn_screen(browser)
    
@given(parsers.parse('Switch the grade to "{grade}"'))
def switch_grade(browser,grade):
    testlistscn.switch_grade(browser,grade) 
    
@when('disconnect device wifi/mobile data')
def off_internet(browser):
    testlistscn.select_offline_mode(browser)
    sleep(2)

    
@then(parsers.parse('Verify text message "{text}" shown at the bottom of the test list screen'))
def verify_snackbar_msg(browser,text):
    testlistscn.verify_snackbar_msg(browser,text)


@then('connect device wifi/mobile data')
def connect_internet(browser):
    testlistscn.select_online_mode(browser)
    sleep(2)

@then('Tap on Revise button')    
@when('Tap on Revise button')
def tap_on_revise_button(browser):
    testlistscn.tap_on_revise_button(browser)
    
@then('Verify Ncert Exemplars test card should be display below the Ncert Exemplars label')
def verify_ncert_exemplars_test_list(browser):
    testlistscn.verify_ncert_exemplars_test_list(browser)
    
@then('Verify Ncert Exercises card should be display below the Ncert Exercises label')
def verify_ncert_exercises_test_list(browser):
    testlistscn.verify_ncert_exercises_test_list(browser)




