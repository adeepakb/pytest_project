from time import sleep
from pytest_bdd import scenarios, given, when, then, parsers
from pages.android.engine_test_screen import EngineTestScreen
from utilities.base_page import BaseClass
driver = fixture = 'driver'


baseClass = BaseClass()
testlistscn = EngineTestScreen(driver)
featureFileName = 'Test List Screen'


# baseClass.setupLogs(featureFileName)


"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""

scenarios('../features/' + featureFileName + '.feature')

@given('Launch the app online and navigate to Home screen')
@given('Launch the app and navigate to Home screen')
def loginapp(driver):
    testlistscn.navigate_to_home_screen(driver)


@given(parsers.parse('Navigate to "{Subject}" library screen'))
def navigate_to_subject_library_scn(driver,Subject):
    testlistscn.navigate_to_library(driver, Subject)    
    
    
@when('Tap on the "Test" option')
def tap_on_test_link(driver):
    testlistscn.tap_on_test_link(driver)

@when('Verify that user lands on the "Test List" screen')    
@then('Verify that user lands on the "Test List" screen')
def verify_test_list_screen(driver):
    testlistscn.verify_test_list_screen(driver)


@then('Verify App back arrow icon should be shown')
def verify_app_back_button(driver):
    testlistscn.verify_app_back_button(driver)

@then('Verify Chapter Name should shown in the header of the screen')
def verify_chapter_name(driver):
    testlistscn.verify_chapter_name(driver)

@then('Verify Chapter icon should be shown top right side of the screen')
def verify_chapter_icon(driver):
    testlistscn.verify_header_icon(driver)
    
@then(parsers.parse('Verify "{text}" label'))
def verify_the_text(driver,text):
    testlistscn.verify_the_text(driver,text)

@then('Verify Test cards should be display below the Tests label')    
@then('Verify Objective test card should be display below the objective test label')
def verify_objective_test_list(driver):
    testlistscn.verify_objective_test_list(driver)
    
@then('Verify Subjective test card should be display below the Subjective Test label')
def verify_subjective_test_list(driver):
    testlistscn.verify_subjective_test_list(driver)

@then('Verify objective tests should be named "Objective Test 0x"')
def objective_test_card(driver):
    testlistscn.verify_objective_test_card(driver)

    
@then('Verify where x being numbers in ascending order of objective test')
def check_obective_test_order(driver):
    testlistscn.check_obective_test_order(driver)
    
@then('Verify "Start" button should shown in front of objective test')
def verify_start_button(driver):
    testlistscn.verify_start_button(driver)

@then('Verify subjective tests should be named "Subjective Test 0x" format')
def verify_subjective_test_card(driver):
    testlistscn.verify_subjective_test_card(driver)

    
@then('Verify where x being numbers in ascending order of subjective test')
def check_subjective_test_order(driver):
    testlistscn.check_subjective_test_order(driver)
    
@then('Verify "Revise" button should be appear front of Subjective test')
def verify_revise_button(driver):
    testlistscn.verify_revise_button(driver)

@given('Verify that user lands on the "Test List" screen')
def verify_test_list_screen1(driver):
    testlistscn.verify_test_list_screen(driver)

@given('Tap on the "Test" option')
def tap_on_test_link1(driver):
    testlistscn.tap_on_test_link(driver)
    
@when('Tap on the "Start" option')
def navigate_to_test_instruction_screen(driver):
    testlistscn.navigate_to_test_instruction_screen(driver)

@then('Tap on "Test" button in instruction screen')    
@when('Take a test')
def tap_on_test_button_on_instruction_scn(driver):
    testlistscn.tap_on_test_button_on_instruction_scn(driver)
    
@when('Submit the test')
def submit_test(driver):
    testlistscn.submit_test(driver)
    
@then('Verify "Start" button should be replaced with "Analyse" text')
def verify_analyse_option(driver):
    testlistscn.navigate_back_to_test_list_scn(driver)
    testlistscn.verify_analyse_option(driver)

@then('Verify retake test icon should be shown before Analyse text with chevron icon')
def verify_retake_test_icon(driver):
    testlistscn.verify_retake_test_icon(driver)

@then('Tap on retake test icon')    
@when('Tap on retake test icon')
def tap_on_retake_test_option(driver):
    testlistscn.tap_on_retake_test_option(driver)
    
@then('Verify user should redirect to Instruction screen')
def verify_test_instruction_screen(driver):
    testlistscn.verify_test_instruction_screen(driver)
    
@then('Verify user redirect to objective test Question screen')
def verify_test_question_screen(driver):
    testlistscn.verify_test_question_screen(driver)
    
@given(parsers.parse('Navigate to "{Subject}" learn screen'))
def navigate_to_learn_screen(driver,Subject):
    testlistscn.navigate_to_learn_screen(driver, Subject)  
    
@when('Tap on the test card which is present in learn screen')
def scroll_to_test_and_click(driver):
    testlistscn.scroll_to_test_and_click(driver)

@then('Tap on Analyse button')    
@when('Tap on Analyse button')
def tap_on_analyse_option(driver):
    testlistscn.tap_on_analyse_option(driver)
    
@then('Verify that user should redirect to the highlights screen')
def verify_highlights_screen(driver):
    testlistscn.verify_highlights_screen(driver)

@then('Tap on Start button')
@when('Tap on Start button')
def tap_on_start_button(driver):
    testlistscn.tap_on_start_button(driver)
    
@when('Tap on video card')
def tap_on_video_card(driver):
    testlistscn.tap_on_video_card(driver)
    
@when('Tap on Test list card on video list screen')
def tap_test_card_on_video_list(driver):
    testlistscn.tap_test_card_on_video_list(driver)
    
@when('Tap on app back button')
def tap_on_app_backbtn(driver):
    sleep(2)
    testlistscn.app_backbtn(driver)
    
@then('Verify that user is in Library chapter list screen')
def verify_library_screen(driver):
    testlistscn.verify_library_screen(driver)
    
@then('Verify that user is in Learn chapter list screen')
def verify_learn_screen(driver):
    testlistscn.verify_learn_screen(driver)
    
@given(parsers.parse('Switch the grade to "{grade}"'))
def switch_grade(driver,grade):
    testlistscn.switch_grade(driver,grade) 
    
@when('disconnect device wifi/mobile data')
def off_internet(driver):
    testlistscn.select_offline_mode(driver)
    sleep(2)

    
@then(parsers.parse('Verify text message "{text}" shown at the bottom of the test list screen'))
def verify_snackbar_msg(driver,text):
    testlistscn.verify_snackbar_msg(driver,text)


@then('connect device wifi/mobile data')
def connect_internet(driver):
    testlistscn.select_online_mode(driver)
    sleep(2)

@then('Tap on Revise button')    
@when('Tap on Revise button')
def tap_on_revise_button(driver):
    testlistscn.tap_on_revise_button(driver)
    
@then('Verify Ncert Exemplars test card should be display below the Ncert Exemplars label')
def verify_ncert_exemplars_test_list(driver):
    testlistscn.verify_ncert_exemplars_test_list(driver)
    
@then('Verify Ncert Exercises card should be display below the Ncert Exercises label')
def verify_ncert_exercises_test_list(driver):
    testlistscn.verify_ncert_exercises_test_list(driver)




