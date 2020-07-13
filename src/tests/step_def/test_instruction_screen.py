from time import sleep
import subprocess
from selenium.webdriver.common import keys
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from pytest_bdd import scenarios, given, when, then, parsers,scenario
from POM_Pages.engine_test_screen import EngineTestScreen
import pytest
import logging
import datetime
from Utilities.BasePage import BaseClass
browser = fixture = 'browser'


baseClass = BaseClass()
testinstructionscn = EngineTestScreen(browser)
featureFileName = 'Instruction Screen'


# baseClass.setupLogs(featureFileName)


"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""

scenarios('../features/' + featureFileName + '.feature')

@given('Launch the app online and navigate to Home screen')
@given('Launch the app and navigate to Home screen')
def loginapp(browser):
    testinstructionscn.navigate_to_home_screen(browser)
    
@given(parsers.parse('Navigate to "{Subject}" chapter list screen'))
def navigate_to_subject_library_scn(browser,Subject):
    testinstructionscn.navigate_to_library(browser, Subject) 
    
@then('Verify App back arrow icon should be shown')
def verify_app_back_button(browser):
    testinstructionscn.verify_app_back_button(browser) 

@when('Tap on "Continue" button in instruction screen')    
@when('Tap on "Test" button in instruction screen')    
def tap_on_test_button_on_instruction_scn(browser):
    testinstructionscn.tap_on_test_button_on_instruction_scn(browser)  
    
@when('Tap on app back button')
def tap_on_app_backbtn(browser):
    sleep(2)
    testinstructionscn.app_backbtn(browser)
    
@then('Verify that user lands on the "Test List" screen')
def verify_test_list_screen1(browser):
    testinstructionscn.verify_test_list_screen(browser)
    
@when('Navigate to Objective test instruction screen')
def navigate_to_test_instruction_screen(browser):
    testinstructionscn.tap_on_test_link(browser)
    testinstructionscn.navigate_to_test_instruction_screen(browser)
    testinstructionscn.verify_test_instruction_screen(browser)
    testinstructionscn.verify_the_button(browser,'Test')
    
@given('Navigate to Objective test instruction screen')
def navigate_to_test_instruction_screen1(browser):
    testinstructionscn.tap_on_test_link(browser)
    testinstructionscn.navigate_to_test_instruction_screen(browser)
    testinstructionscn.verify_test_instruction_screen(browser)
    testinstructionscn.verify_the_button(browser,'Test')
    
@when('Tap on device back button')
def tap_device_backbtn(browser):
    sleep(2)
    testinstructionscn.tap_device_backbtn(browser)
    
@then('connect device wifi/mobile data')
def connect_internet(browser):
    testinstructionscn.select_online_mode(browser)
    sleep(2)
    
@when('disconnect device wifi/mobile data')
def off_internet(browser):
    testinstructionscn.select_offline_mode(browser)
    sleep(2)
    
@then('Verify Test icon should be shown top right side of the screen')
def verify_chapter_icon(browser):
    testinstructionscn.verify_header_icon(browser)
    
@then(parsers.parse('Verify "{text}" label'))
def verify_the_text(browser,text):
    testinstructionscn.verify_the_text(browser,text)
    
@then(parsers.parse('Verify the "{text}" button'))
def verify_the_button(browser,text):
    testinstructionscn.verify_the_button(browser,text)
    
@then('Verify number of Questions with icon should shown along with "Questions" text')
def verify_questions_and_icon(browser):
    testinstructionscn.verify_questions_and_icon(browser)
    
@then('Verify Minutes with icon should shown along with "Minutes" text')
def verify_time_and_icon(browser):
    testinstructionscn.verify_time_and_icon(browser)
    
@then(parsers.parse('Verify instruction text "{text}"'))
def verify_the_content_desc_text(browser,text):
    testinstructionscn.verify_the_content_desc_text(browser,text)
    
@then(parsers.parse('Verify instruction "{text}" text should shown below the instruction label'))
def verify_objective_test_instruction1(browser,text):
    testinstructionscn.verify_objective_test_instruction1(browser,text)
    
@then('Verify instruction icons')
def verify_instruction_icons(browser):
    testinstructionscn.verify_instruction_icons(browser)
    
@then('Verify user should land on Objective test question screen')
def verify_test_question_screen(browser):
    testinstructionscn.verify_test_question_screen(browser)
    
@when('Navigate to Subjective test instruction screen')
def navigate_to_test_Subjective_instruction_screen(browser):
    testinstructionscn.tap_on_test_link(browser)
    testinstructionscn.navigate_to_subjective_test_instruction_scn(browser)    
    
@given('Navigate to Subjective test instruction screen')
def navigate_to_test_Subjective_instruction_screen1(browser):
    testinstructionscn.tap_on_test_link(browser)
    testinstructionscn.navigate_to_subjective_test_instruction_scn(browser)

@then('Verify user should land on Ncert Exercises test question screen')
@then('Verify user should land on Ncert Exemplars test question screen')    
@then('Verify user should land on Subjective test question screen')
def verify_finish_btn_on_test_question_screen(browser):
    testinstructionscn.verify_finish_btn_on_test_question_screen(browser)
    
@given('Navigate to Ncert Exercises test instruction screen')
def navigate_to_ncert_exercises_test_instruction_scn(browser):
    testinstructionscn.tap_on_test_link(browser)
    testinstructionscn.navigate_to_ncert_exercises_test_instruction_scn(browser)
    
@given('Navigate to Ncert Exemplars test instruction screen')
def navigate_to_ncert_examplar_test_instruction_scn(browser):
    testinstructionscn.tap_on_test_link(browser)
    testinstructionscn.navigate_to_ncert_examplar_test_instruction_scn(browser)
    
@then('Verify Chapter Name and test name should be shown on the screen') 
def verify_chapter_n_test_name_on_instruction_screen(browser):
    testinstructionscn.verify_chapter_n_test_name_on_instruction_screen(browser)
    
@when('Navigate to Ncert Exercises test instruction screen')
def navigate_to_ncert_exercises_test_instruction_scn1(browser):
    testinstructionscn.tap_on_test_link(browser)
    testinstructionscn.navigate_to_ncert_exercises_test_instruction_scn(browser)
    
@when('Navigate to Ncert Exemplars test instruction screen')
def navigate_to_ncert_examplar_test_instruction_scn1(browser):
    testinstructionscn.tap_on_test_link(browser)
    testinstructionscn.navigate_to_ncert_examplar_test_instruction_scn(browser)


    
    