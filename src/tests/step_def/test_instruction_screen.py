from time import sleep
from pytest_bdd import scenarios, given, when, then, parsers
from pages.android.engine_test_screen import EngineTestScreen
from utilities.base_page import BaseClass
driver = fixture = 'driver'


baseClass = BaseClass()
testinstructionscn = EngineTestScreen(driver)
featureFileName = 'Instruction Screen'


# baseClass.setupLogs(featureFileName)


"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""

scenarios('../features/' + featureFileName + '.feature')

@given('Launch the app online and navigate to Home screen')
@given('Launch the app and navigate to Home screen')
def loginapp(driver):
    testinstructionscn.navigate_to_home_screen(driver)
    
@given(parsers.parse('Navigate to "{Subject}" chapter list screen'))
def navigate_to_subject_library_scn(driver,Subject):
    testinstructionscn.navigate_to_library(driver, Subject) 
    
@then('Verify App back arrow icon should be shown')
def verify_app_back_button(driver):
    testinstructionscn.verify_app_back_button(driver) 

@when('Tap on "Continue" button in instruction screen')    
@when('Tap on "Test" button in instruction screen')    
def tap_on_test_button_on_instruction_scn(driver):
    testinstructionscn.tap_on_test_button_on_instruction_scn(driver)  
    
@when('Tap on app back button')
def tap_on_app_backbtn(driver):
    sleep(2)
    testinstructionscn.app_backbtn(driver)
    
@then('Verify that user lands on the "Test List" screen')
def verify_test_list_screen1(driver):
    testinstructionscn.verify_test_list_screen(driver)
    
@when('Navigate to Objective test instruction screen')
def navigate_to_test_instruction_screen(driver):
    testinstructionscn.tap_on_test_link(driver)
    testinstructionscn.navigate_to_test_instruction_screen(driver)
    testinstructionscn.verify_test_instruction_screen(driver)
    testinstructionscn.verify_the_button(driver,'Take Test')
    
@given('Navigate to Objective test instruction screen')
def navigate_to_test_instruction_screen1(driver):
    testinstructionscn.tap_on_test_link(driver)
    testinstructionscn.navigate_to_test_instruction_screen(driver)
    testinstructionscn.verify_test_instruction_screen(driver)
    testinstructionscn.verify_the_button(driver,'Take Test')
    
@when('Tap on device back button')
def tap_device_backbtn(driver):
    sleep(2)
    testinstructionscn.tap_device_backbtn(driver)
    
@then('connect device wifi/mobile data')
def connect_internet(driver):
    testinstructionscn.select_online_mode(driver)
    sleep(2)
    
@when('disconnect device wifi/mobile data')
def off_internet(driver):
    testinstructionscn.select_offline_mode(driver)
    sleep(2)
    
@then('Verify Test icon should be shown top right side of the screen')
def verify_chapter_icon(driver):
    testinstructionscn.verify_header_icon(driver)
    
@then(parsers.parse('Verify "{text}" label'))
def verify_the_text(driver,text):
    testinstructionscn.verify_the_text(driver,text)
    
@then(parsers.parse('Verify the "{text}" button'))
def verify_the_button(driver,text):
    testinstructionscn.verify_the_button(driver,text)
    
@then('Verify number of Questions with icon should shown along with "Questions" text')
def verify_questions_and_icon(driver):
    testinstructionscn.verify_questions_and_icon(driver)
    
@then('Verify Minutes with icon should shown along with "Minutes" text')
def verify_time_and_icon(driver):
    testinstructionscn.verify_time_and_icon(driver)
    
@then(parsers.parse('Verify instruction text "{text}"'))
def verify_the_content_desc_text(driver,text):
    testinstructionscn.verify_the_content_desc_text(driver,text)
    
@then(parsers.parse('Verify instruction "{text}" text should shown below the instruction label'))
def verify_objective_test_instruction1(driver,text):
    testinstructionscn.verify_objective_test_instruction1(driver,text)
    
@then('Verify instruction icons')
def verify_instruction_icons(driver):
    testinstructionscn.verify_instruction_icons(driver)
    
@then('Verify user should land on Objective test question screen')
def verify_test_question_screen(driver):
    testinstructionscn.verify_test_question_screen(driver)
    
@when('Navigate to Subjective test instruction screen')
def navigate_to_test_Subjective_instruction_screen(driver):
    testinstructionscn.tap_on_test_link(driver)
    testinstructionscn.navigate_to_subjective_test_instruction_scn(driver)    
    
@given('Navigate to Subjective test instruction screen')
def navigate_to_test_Subjective_instruction_screen1(driver):
    testinstructionscn.tap_on_test_link(driver)
    testinstructionscn.navigate_to_subjective_test_instruction_scn(driver)

@then('Verify user should land on Ncert Exercises test question screen')
@then('Verify user should land on Ncert Exemplars test question screen')    
@then('Verify user should land on Subjective test question screen')
def verify_finish_btn_on_test_question_screen(driver):
    testinstructionscn.verify_finish_btn_on_test_question_screen(driver)
    
@given('Navigate to Ncert Exercises test instruction screen')
def navigate_to_ncert_exercises_test_instruction_scn(driver):
    testinstructionscn.tap_on_test_link(driver)
    testinstructionscn.navigate_to_ncert_exercises_test_instruction_scn(driver)
    
@given('Navigate to Ncert Exemplars test instruction screen')
def navigate_to_ncert_examplar_test_instruction_scn(driver):
    testinstructionscn.tap_on_test_link(driver)
    testinstructionscn.navigate_to_ncert_examplar_test_instruction_scn(driver)
    
@then('Verify Chapter Name and test name should be shown on the screen') 
def verify_test_name_on_instruction_screen(driver):
    testinstructionscn.verify_test_name_on_instruction_screen(driver)
    
@when('Navigate to Ncert Exercises test instruction screen')
def navigate_to_ncert_exercises_test_instruction_scn1(driver):
    testinstructionscn.tap_on_test_link(driver)
    testinstructionscn.navigate_to_ncert_exercises_test_instruction_scn(driver)
    
@when('Navigate to Ncert Exemplars test instruction screen')
def navigate_to_ncert_examplar_test_instruction_scn1(driver):
    testinstructionscn.tap_on_test_link(driver)
    testinstructionscn.navigate_to_ncert_examplar_test_instruction_scn(driver)


    
    