from time import sleep
from pytest_bdd import scenarios, given, when, then, parsers
from pages.android.engine_test_screen import EngineTestScreen
from utilities.base_page import BaseClass
driver = fixture = 'driver'


baseClass = BaseClass()
testquestionscn = EngineTestScreen(driver)
featureFileName = 'Question Screen'
# baseClass.setupLogs(featureFileName)
"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""
scenarios('../features/' + featureFileName + '.feature')

@given('Launch the app online and navigate to Home screen')
@given('Launch the app and navigate to Home screen')
def loginapp(driver):
    testquestionscn.navigate_to_home_screen(driver)
    
@when('Navigate to objective test question screen')
def navigate_to_objective_test_question_scn(driver):
    testquestionscn.navigate_to_objective_test_question_scn(driver)
    
@given(parsers.parse('Navigate to "{Subject}" chapter list screen'))
def navigate_to_subject_library_scn(driver,Subject):
    testquestionscn.navigate_to_library(driver, Subject)
    
@then(parsers.parse('Verify the "{text}" button'))
def verify_the_button(driver,text):
    testquestionscn.verify_the_button(driver,text)
    
@given('Navigate to objective test question screen')
def navigate_to_obj_test_instruction_scn(driver):
    testquestionscn.tap_on_test_link(driver)
    testquestionscn.navigate_to_test_instruction_screen(driver)
    testquestionscn.verify_test_instruction_screen(driver)
    testquestionscn.tap_on_test_button_on_instruction_scn(driver)
    testquestionscn.verify_test_question_screen(driver)
    
@then('Verify "Previous" button')
def verify_previous_button(driver):
    testquestionscn.verify_previous_button(driver)

@then('Verify "Next" button')
def verify_next_button(driver):
    testquestionscn.verify_next_button(driver)
    
@then('Verify Countdown Timer should shown in the screen') 
def verify_countdown_timer(driver):
    testquestionscn.verify_countdown_timer(driver)
    
@then('Verify "Pause" button should shown in the screen') 
def verify_pause_button(driver):
    testquestionscn.verify_pause_button(driver)
    
@then('Verify Question number should be available with the current question highlighted') 
def verify_question_number_highlighted(driver):
    testquestionscn.verify_question_number_highlighted(driver)
    
@then('Verify Question count up timer should be shown') 
def  verify_question_count_up_timer(driver):
    testquestionscn.verify_question_count_up_timer(driver)
    
@then('Verify Bookmark icon') 
def verify_book_mark_icon(driver):
    testquestionscn.verify_book_mark_icon(driver)
    
@then('Verify Report an Issue icon should available along with the text "Report an issue" at the left bottom of the screen') 
def verify_report_an_issue_option(driver):
    testquestionscn.verify_report_an_issue_option(driver)
    
@then('Verify Question with options should appear in case of multiple choice question') 
def verify_multiple_choice_question(driver):
    testquestionscn.verify_multiple_choice_question(driver)

@then('Verify Question with answers along with radio button should appear in case of multi select question') 
def verify_multi_select_question(driver):
    testquestionscn.navigate_to_first_qn(driver)
    testquestionscn.verify_multi_select_question(driver)
    
@then('Verify Question with fillers should be available in case of Filler type question') 
def verify_fill_in_the_blanks_question(driver):
    testquestionscn.navigate_to_first_qn(driver)
    testquestionscn.verify_fill_in_the_blanks_question(driver)

@when('User is in objective test question screen')
@when('Verify that user is in objective test question screen')    
@then('Verify that user is in objective test question screen')
def verify_test_question_screen(driver):
    testquestionscn.verify_test_question_screen(driver)
    
@when('Bookmark a question')
def book_mark_a_question(driver):
    testquestionscn.book_mark_a_question(driver)
    

@when('Remove bookmark from question')
def remove_book_mark_in_qn_screen(driver):
    testquestionscn.remove_book_mark_in_qn_screen(driver)
    
@then('Verify dot should display above the Questions navigation bar')
def verify_bookmarked_dot_on_qn_number(driver):
    testquestionscn.verify_bookmarked_dot_on_qn_number(driver)
    

@then('Verify dot should be removed from the question navigation bar')
def verify_bookmarked_dot_removed(driver):
    testquestionscn.verify_bookmarked_dot_removed(driver)
    
@then('Verify current question should bookmarked with bookmark icon in subject theme color')
def verify_question_bookmarked(driver):
    testquestionscn.verify_bookmark_color()

@then('Verify current question bookmark should be removed')
def verify_bookmark_removed(driver):
    testquestionscn.verify_gray_color(driver)
    
@given(parsers.parse('Get "{Subject}" subject theme color'))
def get_subject_color(driver,Subject):
    testquestionscn.remove_bookmark_in_book_mark_screen(driver)
    testquestionscn.get_subject_color(driver,Subject)

@then('Verify Question number along with question number tab should be shown')
def verify_question_number_tab(driver):
    testquestionscn.verify_question_number_tab(driver)

@when('Navigate back to previous fill in the blanks Question')  
@when('Tap on "Next" button')
def tap_on_next_button(driver):
    testquestionscn.tap_on_next_button(driver)

@when('Navigate back to previous Multi select Question') 
@when('Navigate back to previous Multiple choice Question')
@when('Navigate back to previous Question')
@when('Tap on "Previous" button')
def tap_on_previous_button(driver):
    testquestionscn.tap_on_previous_button(driver)
    
@then('Verify previous question should be shown')    
@then('Verify next question should be shown')
def user_in_different_qn_scn(driver):
    testquestionscn.user_in_different_qn_scn(driver)
    
@when('Tap on particular question number')
def navigate_to_particular_qn_screen(driver):
    testquestionscn.navigate_to_particular_qn_screen(driver)
    
@then('Verify that user should navigate to particular question screen')
def verify_particular_qn_scn(driver):
    testquestionscn.verify_particular_qn_scn(driver)
    
@when('User is in first question')
def user_is_in_first_question_scn(driver):
    testquestionscn.user_is_in_first_question_scn(driver)
    
@when('Navigate to last question')
def navigate_to_last_question(driver):
    testquestionscn.navigate_to_last_question(driver)
    
@then('Verify that "Next" button should not be shown')
def next_button_not_shown(driver):
    testquestionscn.next_button_not_shown(driver)
    
@then('Verify that "Previous" button should not be shown')
def previous_button_not_shown(driver):
    testquestionscn.previous_button_not_shown(driver)
    
@then("Verify keypad should appear on the user device")
def is_keyboadrd_shown(driver):
    testquestionscn.is_keypad_enabled(driver)
    
@when('Tap on the blank space')
def tap_on_edit_text(driver):
    testquestionscn.tap_on_edit_text(driver)

@when('Navigate to fill in the blanks question screen')
def navigate_to_fill_in_the_blanks_screen(driver):
    testquestionscn.navigate_to_objective_test_question_scn(driver)
    testquestionscn.verify_test_question_screen(driver)
    testquestionscn.verify_fill_in_the_blanks_question(driver)
    
@then('Verify Question on the screen')
def get_question(driver):
    testquestionscn.get_question(driver)
    
@then('Verify Edit text blank should be shown on the screen')
def verify_edit_text_field_on_scn(driver):
    testquestionscn.verify_edit_text_field_on_scn(driver)

@then(parsers.parse('Verify the instruction text "{text}"'))
@then(parsers.parse('Verify the text "{text}"'))
def verify_the_content_desc_text(driver,text):
    testquestionscn.verify_the_content_desc_text(driver,text)
    
@when('Enter the <Answer>')
def enter_answer(driver,Answer):
    testquestionscn.enter_answer(driver,Answer)
    
@then('Verify that user should able to enter <Answer> on fill in the blanks question screen')
def verify_entered_answer(driver,Answer):
    testquestionscn.verify_entered_answer(driver,Answer)
    
@when('Navigate to Multiple choice question screen')
def navigate_to_multiple_choice_question(driver):
    testquestionscn.verify_multiple_choice_question(driver)

@when('Navigate to Multi select question screen')
def navigate_to_multi_select_question(driver):
    testquestionscn.navigate_to_objective_test_question_scn(driver)
    testquestionscn.verify_test_question_screen(driver)
    testquestionscn.verify_multi_select_question(driver)
    
@then('Verify Multiple choice options on the screen')
@then('Verify Multi select options on the screen')
def verify_options_shown(driver):
    testquestionscn.verify_options_shown(driver)
    
@then('Verify that radio button on the screen')
def verify_radio_buttons_on_question_Scn(driver):
    testquestionscn.verify_options_shown(driver)
    
@when('Select an option to answer')
def select_multiple_choice_option(driver):
    testquestionscn.select_multiple_choice_option(driver)

@then('Verify that selected option is highlighted for answer')
def image_compare(driver):
    testquestionscn.image_compare(driver)
    
@when('Select options to answer the question')
def select_multi_select_options(driver):
    testquestionscn.select_multi_select_options(driver)
    
@then('Verify that selected options are highlighted for answer')
def image_compare_multiselect(driver):
    testquestionscn.image_compare_multiselect(driver)
    
@then('Verify that previously saved multiple choice answer is shown')
def compare_multiple_choice_option(driver):
    testquestionscn.compare_multiple_choice_option(driver)

@then('Verify that previously saved fill in the blanks answer is shown')
@then('Verify that previously saved multi select answer is shown')
def compare_question_screen(driver):
    testquestionscn.compare_question_screen(driver)
    
@when('Navigate to Image type question screen')
def navigate_to_image_type_qn(driver):
    testquestionscn.navigate_to_objective_test_question_scn(driver)
    testquestionscn.verify_test_question_screen(driver)
    sleep(2)
    testquestionscn.navigate_to_image_type_qn(driver)
    
@when('Tap on Image')
def tap_on_image(driver):
    testquestionscn.tap_on_image(driver)

@then('Verify that image should be shown in Image view screen')
def verify_image_view_screen(driver):
    testquestionscn.verify_image_view_screen(driver)
    
@then('Verify that "Close" button should be shown on Image view screen')
def verify_image_view_cls_btn(driver):
    testquestionscn.verify_image_view_cls_btn(driver)
    
@when('Tap on device back button')
def tap_device_backbtn(driver):
    sleep(2)
    testquestionscn.tap_device_backbtn(driver)
    
@when('Tap on "Close" button Image view screen')
def tap_on_close_btn(driver):
    testquestionscn.tap_on_close_btn(driver)

@then('Verify that "Image view screen" should be dismissed')
def verify_image_view_dismissed(driver):
    testquestionscn.verify_image_view_dismissed(driver)

@then('Double tap on image views screen')   
@when('Double tap on image views screen')
def double_tap_on_image(driver):
    testquestionscn.double_tap_on_image(driver)

@when(parsers.parse('Verify that "{text}" bottom sheet dialog is shown'))    
@then(parsers.parse('Verify that "{text}" bottom sheet dialog is shown'))
def verify_bottomsheet_dialog_shown(driver,text):
    testquestionscn.verify_bottomsheet_dialog_shown(driver,text)
    
@when('Tap "Submit" button')
def tap_on_submit_button(driver):
    testquestionscn.tap_on_submit_button(driver)

@then('Verify "Report an Issue Test" icon')
@then('Verify Test paused Test icon')
@then('Verify Submit Test icon')    
@then('Verify Abort Test icon')
def verify_test_icon(driver):
    testquestionscn.verify_test_icon(driver)
    
@then(parsers.parse('Verify "{text}" title'))
def verify_bottom_sheet_dialog_title(driver,text):
    testquestionscn.verify_bottom_sheet_dialog_title(driver,text)
    
@then(parsers.parse('Verify "{text}" message'))
def verify_bottom_sheet_dialog_message(driver,text):
    testquestionscn.verify_bottom_sheet_dialog_message(driver,text)
    
@then(parsers.parse('Verify "{text}" primary action button'))
def verify_primary_button(driver,text):
    testquestionscn.verify_primary_button(driver,text)
    
@then(parsers.parse('Verify "{text}" secondary action button'))
def verify_secondary_button(driver,text):
    testquestionscn.verify_secondary_button(driver,text)

@when('Tap on the "Cancel" button on "Submit Test?" bottom sheet dialog')    
@when('Tap on "Abort" button on "Abort" bottom sheet dialog')
def tap_on_secondary_action_button(driver):
    testquestionscn.tap_on_secondary_action_button(driver)

@when('Tap on "Got It" button on "Help" bottom sheet dialog')
@when('Tap on "Submit" button on "Submit Test?" bottom sheet dialog')    
@when('Tap on "Cancel" button on "Abort" bottom sheet dialog')
def tap_on_primary_action_button(driver):
    testquestionscn.tap_on_primary_action_button(driver)
    
@then('Verify that user lands on the "Test List" screen')
def verify_test_list_screen(driver):
    testquestionscn.verify_test_list_screen(driver)
    
@then('Verify that user should be redirected to "Highlights" screen')
def verify_highlights_screen(driver):
    testquestionscn.verify_highlights_screen(driver)

@then('Verify that "Report an Issue" bottom sheet dialog is dismissed')
@then('Verify that "Test paused" bottom sheet dialog is dismissed')
@then('Verify that "Help" bottom sheet dialog is dismissed') 
@then('Verify that "Submit Test?" bottom sheet dialog is dismissed')    
@then('Verify that "Abort" bottom sheet dialog is dismissed')
def bottomsheet_dailog_dismissed(driver):
    testquestionscn.bottomsheet_dailog_dismissed(driver)
    
@then(parsers.parse('Verify "{text}" message on "Submit Test?" bottom sheet dialog'))
def verify_submit_test_message(driver,text):
    testquestionscn.verify_submit_test_message(driver,text)

@then('Verify that image is zoomed')
def image_zoom_in(driver):
    testquestionscn.image_zoom_in(driver)
    
@then('Verify that image is zoom out')
def image_zoom_out(driver):
    testquestionscn.image_zoom_out(driver)
    
@when('Tap on Pause button')
def tap_on_pause_button(driver):
    testquestionscn.tap_on_pause_button(driver)
    
@when(parsers.parse('Tap on "{text}" option'))
def tap_on_option(driver,text):
    testquestionscn.tap_on_option(driver,text)
    
@then(parsers.parse('Verify instruction "{text}" text should be shown below the help label'))
def verify_objective_test_instruction1(driver,text):
    testquestionscn.verify_objective_test_instruction1(driver,text)
    
@then('Verify instruction icons')
def verify_instruction_icons(driver):
    testquestionscn.verify_instruction_icons(driver)
    
@then(parsers.parse('Verify "{text}" option along with icon and right arrow'))
def verify_option_icon_rightarrow(driver,text):
    testquestionscn.verify_option_icon_rightarrow(driver,text)
    
@then('Verify that timer countdown should start')
def verify_countdown_timer_time(driver):
    testquestionscn.verify_countdown_timer_time(driver)
    
@then('Verify that Timer should count up from 00:00')
def get_qn_start_time(driver):
    testquestionscn.get_qn_start_time(driver)

@then('Verify that Timer should count up from previous recorded time')
@then('Verify that timer should count up for particular question')
def verify_countup_for_qn(driver):
    testquestionscn.verify_countup_for_qn(driver)
    
@when('Note down particular question timer count')
def get_qn_time(driver):
    testquestionscn.get_qn_time(driver)
    
@when('Tap on "Report an Issue" icon')
def tap_on_report_an_issue_icon(driver):
    testquestionscn.tap_on_report_an_issue_icon(driver)
    
@then(parsers.parse('Verify "{text}" option along with right arrow'))
def verify_option_rightarrow(driver,text):
    testquestionscn.verify_option_rightarrow(driver,text)
    


    
     
    
