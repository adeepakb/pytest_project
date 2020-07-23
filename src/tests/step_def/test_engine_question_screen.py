from time import sleep
import subprocess
from selenium.webdriver.common import keys
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from pytest_bdd import scenarios, given, when, then, parsers,scenario
from POM_Pages.engine_test_screen import EngineTestScreen
import pytest
import logging
from Utilities.BasePage import BaseClass
browser = fixture = 'browser'


baseClass = BaseClass()
testquestionscn = EngineTestScreen(browser)
featureFileName = 'Question Screen'
# baseClass.setupLogs(featureFileName)
"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""
scenarios('../features/' + featureFileName + '.feature')

@given('Launch the app online and navigate to Home screen')
@given('Launch the app and navigate to Home screen')
def loginapp(browser):
    testquestionscn.navigate_to_home_screen(browser)
    
@when('Navigate to objective test question screen')
def navigate_to_objective_test_question_scn(browser):
    testquestionscn.navigate_to_objective_test_question_scn(browser)
    
@given(parsers.parse('Navigate to "{Subject}" chapter list screen'))
def navigate_to_subject_library_scn(browser,Subject):
    testquestionscn.navigate_to_library(browser, Subject)
    
@then(parsers.parse('Verify the "{text}" button'))
def verify_the_button(browser,text):
    testquestionscn.verify_the_button(browser,text)
    
@given('Navigate to objective test question screen')
def navigate_to_obj_test_instruction_scn(browser):
    testquestionscn.tap_on_test_link(browser)
    testquestionscn.navigate_to_test_instruction_screen(browser)
    testquestionscn.verify_test_instruction_screen(browser)
    testquestionscn.tap_on_test_button_on_instruction_scn(browser)
    testquestionscn.verify_test_question_screen(browser)
    
@then('Verify "Previous" button')
def verify_previous_button(browser):
    testquestionscn.verify_previous_button(browser)

@then('Verify "Next" button')
def verify_next_button(browser):
    testquestionscn.verify_next_button(browser)
    
@then('Verify Countdown Timer should shown in the screen') 
def verify_countdown_timer(browser):
    testquestionscn.verify_countdown_timer(browser)
    
@then('Verify "Pause" button should shown in the screen') 
def verify_pause_button(browser):
    testquestionscn.verify_pause_button(browser)
    
@then('Verify Question number should be available with the current question highlighted') 
def verify_question_number_highlighted(browser):
    testquestionscn.verify_question_number_highlighted(browser)
    
@then('Verify Question count up timer should be shown') 
def  verify_question_count_up_timer(browser):
    testquestionscn.verify_question_count_up_timer(browser)
    
@then('Verify Bookmark icon') 
def verify_book_mark_icon(browser):
    testquestionscn.verify_book_mark_icon(browser)
    
@then('Verify Report an Issue icon should available along with the text "Report an issue" at the left bottom of the screen') 
def verify_report_an_issue_option(browser):
    testquestionscn.verify_report_an_issue_option(browser)
    
@then('Verify Question with options should appear in case of multiple choice question') 
def verify_multiple_choice_question(browser):
    testquestionscn.verify_multiple_choice_question(browser)

@then('Verify Question with answers along with radio button should appear in case of multi select question') 
def verify_multi_select_question(browser):
    testquestionscn.navigate_to_first_qn(browser)
    testquestionscn.verify_multi_select_question(browser)
    
@then('Verify Question with fillers should be available in case of Filler type question') 
def verify_fill_in_the_blanks_question(browser):
    testquestionscn.navigate_to_first_qn(browser)
    testquestionscn.verify_fill_in_the_blanks_question(browser)

@when('User is in objective test question screen')
@when('Verify that user is in objective test question screen')    
@then('Verify that user is in objective test question screen')
def verify_test_question_screen(browser):
    testquestionscn.verify_test_question_screen(browser)
    
@when('Bookmark a question')
def book_mark_a_question(browser):
    testquestionscn.book_mark_a_question(browser)
    

@when('Remove bookmark from question')
def remove_book_mark_in_qn_screen(browser):
    testquestionscn.remove_book_mark_in_qn_screen(browser)
    
@then('Verify dot should display above the Questions navigation bar')
def verify_bookmarked_dot_on_qn_number(browser):
    testquestionscn.verify_bookmarked_dot_on_qn_number(browser)
    

@then('Verify dot should be removed from the question navigation bar')
def verify_bookmarked_dot_removed(browser):
    testquestionscn.verify_bookmarked_dot_removed(browser)
    
@then('Verify current question should bookmarked with bookmark icon in subject theme color')
def verify_question_bookmarked(browser):
    testquestionscn.verify_bookmark_color()

@then('Verify current question bookmark should be removed')
def verify_bookmark_removed(browser):
    testquestionscn.verify_gray_color()
    
@given(parsers.parse('Get "{Subject}" subject theme color'))
def get_subject_color(browser,Subject):
    testquestionscn.remove_bookmark_in_book_mark_screen(browser)
    testquestionscn.get_subject_color(browser,Subject)

@then('Verify Question number along with question number tab should be shown')
def verify_question_number_tab(browser):
    testquestionscn.verify_question_number_tab(browser)

@when('Navigate back to previous fill in the blanks Question')  
@when('Tap on "Next" button')
def tap_on_next_button(browser):
    testquestionscn.tap_on_next_button(browser)

@when('Navigate back to previous Multi select Question') 
@when('Navigate back to previous Multiple choice Question')
@when('Navigate back to previous Question')
@when('Tap on "Previous" button')
def tap_on_previous_button(browser):
    testquestionscn.tap_on_previous_button(browser)
    
@then('Verify previous question should be shown')    
@then('Verify next question should be shown')
def user_in_different_qn_scn(browser):
    testquestionscn.user_in_different_qn_scn(browser)
    
@when('Tap on particular question number')
def navigate_to_particular_qn_screen(browser):
    testquestionscn.navigate_to_particular_qn_screen(browser)
    
@then('Verify that user should navigate to particular question screen')
def verify_particular_qn_scn(browser):
    testquestionscn.verify_particular_qn_scn(browser)
    
@when('User is in first question')
def user_is_in_first_question_scn(browser):
    testquestionscn.user_is_in_first_question_scn(browser)
    
@when('Navigate to last question')
def navigate_to_last_question(browser):
    testquestionscn.navigate_to_last_question(browser)
    
@then('Verify that "Next" button should not be shown')
def next_button_not_shown(browser):
    testquestionscn.next_button_not_shown(browser)
    
@then('Verify that "Previous" button should not be shown')
def previous_button_not_shown(browser):
    testquestionscn.previous_button_not_shown(browser)
    
@then("Verify keypad should appear on the user device")
def is_keyboadrd_shown(browser):
    testquestionscn.is_keypad_enabled(browser)
    
@when('Tap on the blank space')
def tap_on_edit_text(browser):
    testquestionscn.tap_on_edit_text(browser)

@when('Navigate to fill in the blanks question screen')
def navigate_to_fill_in_the_blanks_screen(browser):
    testquestionscn.navigate_to_objective_test_question_scn(browser)
    testquestionscn.verify_test_question_screen(browser)
    testquestionscn.verify_fill_in_the_blanks_question(browser)
    
@then('Verify Question on the screen')
def get_question(browser):
    testquestionscn.get_question(browser)
    
@then('Verify Edit text blank should be shown on the screen')
def verify_edit_text_field_on_scn(browser):
    testquestionscn.verify_edit_text_field_on_scn(browser)

@then(parsers.parse('Verify the instruction text "{text}"'))
@then(parsers.parse('Verify the text "{text}"'))
def verify_the_content_desc_text(browser,text):
    testquestionscn.verify_the_content_desc_text(browser,text)
    
@when('Enter the <Answer>')
def enter_answer(browser,Answer):
    testquestionscn.enter_answer(browser,Answer)
    
@then('Verify that user should able to enter <Answer> on fill in the blanks question screen')
def verify_entered_answer(browser,Answer):
    testquestionscn.verify_entered_answer(browser,Answer)
    
@when('Navigate to Multiple choice question screen')
def navigate_to_multiple_choice_question(browser):
    testquestionscn.verify_multiple_choice_question(browser)

@when('Navigate to Multi select question screen')
def navigate_to_multi_select_question(browser):
    testquestionscn.navigate_to_objective_test_question_scn(browser)
    testquestionscn.verify_test_question_screen(browser)
    testquestionscn.verify_multi_select_question(browser)
    
@then('Verify Multiple choice options on the screen')
@then('Verify Multi select options on the screen')
def verify_options_shown(browser):
    testquestionscn.verify_options_shown(browser)
    
@then('Verify that radio button on the screen')
def verify_radio_buttons_on_question_Scn(browser):
    testquestionscn.verify_options_shown(browser)
    
@when('Select an option to answer')
def select_multiple_choice_option(browser):
    testquestionscn.select_multiple_choice_option(browser)

@then('Verify that selected option is highlighted for answer')
def image_compare(browser):
    testquestionscn.image_compare(browser)
    
@when('Select options to answer the question')
def select_multi_select_options(browser):
    testquestionscn.select_multi_select_options(browser)
    
@then('Verify that selected options are highlighted for answer')
def image_compare_multiselect(browser):
    testquestionscn.image_compare_multiselect(browser)
    
@then('Verify that previously saved multiple choice answer is shown')
def compare_multiple_choice_option(browser):
    testquestionscn.compare_multiple_choice_option(browser)

@then('Verify that previously saved fill in the blanks answer is shown')
@then('Verify that previously saved multi select answer is shown')
def compare_question_screen(browser):
    testquestionscn.compare_question_screen(browser)
    
@when('Navigate to Image type question screen')
def navigate_to_image_type_qn(browser):
    testquestionscn.navigate_to_objective_test_question_scn(browser)
    testquestionscn.verify_test_question_screen(browser)
    sleep(2)
    testquestionscn.navigate_to_image_type_qn(browser)
    
@when('Tap on Image')
def tap_on_image(browser):
    testquestionscn.tap_on_image(browser)

@then('Verify that image should be shown in Image view screen')
def verify_image_view_screen(browser):
    testquestionscn.verify_image_view_screen(browser)
    
@then('Verify that "Close" button should be shown on Image view screen')
def verify_image_view_cls_btn(browser):
    testquestionscn.verify_image_view_cls_btn(browser)
    
@when('Tap on device back button')
def tap_device_backbtn(browser):
    sleep(2)
    testquestionscn.tap_device_backbtn(browser)
    
@when('Tap on "Close" button Image view screen')
def tap_on_close_btn(browser):
    testquestionscn.tap_on_close_btn(browser)

@then('Verify that "Image view screen" should be dismissed')
def verify_image_view_dismissed(browser):
    testquestionscn.verify_image_view_dismissed(browser)

@then('Double tap on image views screen')   
@when('Double tap on image views screen')
def double_tap_on_image(browser):
    testquestionscn.double_tap_on_image(browser)

@when(parsers.parse('Verify that "{text}" bottom sheet dialog is shown'))    
@then(parsers.parse('Verify that "{text}" bottom sheet dialog is shown'))
def verify_bottomsheet_dialog_shown(browser,text):
    testquestionscn.verify_bottomsheet_dialog_shown(browser,text)
    
@when('Tap "Submit" button')
def tap_on_submit_button(browser):
    testquestionscn.tap_on_submit_button(browser)

@then('Verify "Report an Issue Test" icon')
@then('Verify Test paused Test icon')
@then('Verify Submit Test icon')    
@then('Verify Abort Test icon')
def verify_test_icon(browser):
    testquestionscn.verify_test_icon(browser)
    
@then(parsers.parse('Verify "{text}" title'))
def verify_bottom_sheet_dialog_title(browser,text):
    testquestionscn.verify_bottom_sheet_dialog_title(browser,text)
    
@then(parsers.parse('Verify "{text}" message'))
def verify_bottom_sheet_dialog_message(browser,text):
    testquestionscn.verify_bottom_sheet_dialog_message(browser,text)
    
@then(parsers.parse('Verify "{text}" primary action button'))
def verify_primary_button(browser,text):
    testquestionscn.verify_primary_button(browser,text)
    
@then(parsers.parse('Verify "{text}" secondary action button'))
def verify_secondary_button(browser,text):
    testquestionscn.verify_secondary_button(browser,text)

@when('Tap on the "Cancel" button on "Submit Test?" bottom sheet dialog')    
@when('Tap on "Abort" button on "Abort" bottom sheet dialog')
def tap_on_secondary_action_button(browser):
    testquestionscn.tap_on_secondary_action_button(browser)

@when('Tap on "Got It" button on "Help" bottom sheet dialog')
@when('Tap on "Submit" button on "Submit Test?" bottom sheet dialog')    
@when('Tap on "Cancel" button on "Abort" bottom sheet dialog')
def tap_on_primary_action_button(browser):
    testquestionscn.tap_on_primary_action_button(browser)
    
@then('Verify that user lands on the "Test List" screen')
def verify_test_list_screen(browser):
    testquestionscn.verify_test_list_screen(browser)
    
@then('Verify that user should be redirected to "Highlights" screen')
def verify_highlights_screen(browser):
    testquestionscn.verify_highlights_screen(browser)

@then('Verify that "Report an Issue" bottom sheet dialog is dismissed')
@then('Verify that "Test paused" bottom sheet dialog is dismissed')
@then('Verify that "Help" bottom sheet dialog is dismissed') 
@then('Verify that "Submit Test?" bottom sheet dialog is dismissed')    
@then('Verify that "Abort" bottom sheet dialog is dismissed')
def bottomsheet_dailog_dismissed(browser):
    testquestionscn.bottomsheet_dailog_dismissed(browser)
    
@then(parsers.parse('Verify "{text}" message on "Submit Test?" bottom sheet dialog'))
def verify_submit_test_message(browser,text):
    testquestionscn.verify_submit_test_message(browser,text)

@then('Verify that image is zoomed')
def image_zoom_in(browser):
    testquestionscn.image_zoom_in(browser)
    
@then('Verify that image is zoom out')
def image_zoom_out(browser):
    testquestionscn.image_zoom_out(browser)
    
@when('Tap on Pause button')
def tap_on_pause_button(browser):
    testquestionscn.tap_on_pause_button(browser)
    
@when(parsers.parse('Tap on "{text}" option'))
def tap_on_option(browser,text):
    testquestionscn.tap_on_option(browser,text)
    
@then(parsers.parse('Verify instruction "{text}" text should be shown below the help label'))
def verify_objective_test_instruction1(browser,text):
    testquestionscn.verify_objective_test_instruction1(browser,text)
    
@then('Verify instruction icons')
def verify_instruction_icons(browser):
    testquestionscn.verify_instruction_icons(browser)
    
@then(parsers.parse('Verify "{text}" option along with icon and right arrow'))
def verify_option_icon_rightarrow(browser,text):
    testquestionscn.verify_option_icon_rightarrow(browser,text)
    
@then('Verify that timer countdown should start')
def verify_countdown_timer_time(browser):
    testquestionscn.verify_countdown_timer_time(browser)
    
@then('Verify that Timer should count up from 00:00')
def get_qn_start_time(browser):
    testquestionscn.get_qn_start_time(browser)

@then('Verify that Timer should count up from previous recorded time')
@then('Verify that timer should count up for particular question')
def verify_countup_for_qn(browser):
    testquestionscn.verify_countup_for_qn(browser)
    
@when('Note down particular question timer count')
def get_qn_time(browser):
    testquestionscn.get_qn_time(browser)
    
@when('Tap on "Report an Issue" icon')
def tap_on_report_an_issue_icon(browser):
    testquestionscn.tap_on_report_an_issue_icon(browser)
    
@then(parsers.parse('Verify "{text}" option along with right arrow'))
def verify_option_rightarrow(browser,text):
    testquestionscn.verify_option_rightarrow(browser,text)
    


    
     
    
