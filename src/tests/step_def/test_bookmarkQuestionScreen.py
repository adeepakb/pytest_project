from time import sleep
import subprocess
from selenium.webdriver.common import keys
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from pytest_bdd import scenarios, given, when, then, parsers,scenario
from POM_Pages.bookmarkQuestionScreen import BookMarkQuestionScreen
import pytest
import logging
import datetime
from Utilities.BasePage import BaseClass
browser = fixture = 'browser'


baseClass = BaseClass()
bookmarkQnScn=BookMarkQuestionScreen(browser)
featureFileName = 'Bookmark questions'


# baseClass.setupLogs(featureFileName)

"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""

scenarios('../features/' + featureFileName + '.feature')


@given('Launch the app online and navigate to Home screen')
def loginapp(browser):
    bookmarkQnScn.navigate_to_home_screen(browser)

@given('Navigate to Highlights screen')    
@given('Bookmark a question')
def bookmark_a_question(browser):
    bookmarkQnScn.bookmark_qn_from_test(browser)


@when('Navigate to bookmark home screen')
def navigate_to_book_mark_screen(browser):
    bookmarkQnScn.navigate_back_home_screen(browser)
    bookmarkQnScn.navigate_to_book_mark_screen(browser)


@then('Verify that bookmarked question should be present in Bookmark home screen under All tab')
def verify_question(browser):
    bookmarkQnScn.verify_question(browser)


@then(parsers.parse('Verify below that chapter name and "{subject}" subject name on bookmark subject screen'))    
@then(parsers.parse('Verify below that chapter name and "{subject}" subject name'))
def verify_subject_and_concept_name1(browser,subject):
    bookmarkQnScn.verify_subject_and_chapter_name(browser,subject)


@then('Verify the bookmark icon on bookmark subject screen')
@then('Verify the bookmark icon on bookmark home screen')
def is_bookmark_icon_shown1(browser):
    bookmarkQnScn.is_bookmark_icon_shown(browser)


@then(parsers.parse('Verify that bookmarked question should be present under "{subject}" tab'))
def verify_qn_under_sub_tab1(browser,subject):
    bookmarkQnScn.scroll_horizontal(browser,subject)
    sleep(2)
    bookmarkQnScn.verify_question(browser)

    
@when('Navigate to test instruction screen')
def navigate_to_test_instscreen(browser):
    bookmarkQnScn.navigate_to_test(browser)


@then(parsers.parse('Verify that in the test instruction screen "{text}" message should not be shown.'))
def istruction_notfound(browser,text):
    bookmarkQnScn.istruction_notfound(browser,text)      


@then(parsers.parse('Verify that in the test instruction screen "{text}" message should be shown.'))
def istruction_found(browser,text):
    bookmarkQnScn.istruction_found(browser,text)      


@when('Tap on Test button in Instruction screen')
def navigate_to_test_screen(browser):
    bookmarkQnScn.navigate_to_test_screen(browser)

 
@then('Verify that Bookmark icon should be present in the test screen')
def verify_bookmark_icon_ontestscreen(browser):
    bookmarkQnScn.verify_bookmark_icon_ontestscreen(browser)


@when('Bookmark a test question and once again tap on same bookmark icon')
def book_mark_a_question(browser):
    bookmarkQnScn.book_mark_a_question(browser)
    bookmarkQnScn.remove_book_mark_in_qn_screen(browser)


@then(parsers.parse('Verify that "{text}" toast message should be displayed at the bottom of the screen'))
def verify_toast_msg(browser,text):
    bookmarkQnScn.verify_toast_msg(browser,text)


@then('Verify unbookmarked question should not be displayed in the bookmark home screen under All tab')
def navigate_to_bookmark_screen_andverify(browser):
    bookmarkQnScn.quit_inbtween(browser)
    bookmarkQnScn.navigate_back_home_screen(browser)
    bookmarkQnScn.navigate_to_book_mark_screen(browser)
    sleep(2)
    bookmarkQnScn.question_not_found(browser)


@then(parsers.parse('Verify that question should be removed under "{subject}" tab'))
@then(parsers.parse('Verify unbookmarked question should not be displayed under "{subject}" tab'))
def navigate_to_subject_tab_verify(browser,subject):
    bookmarkQnScn.scroll_horizontal(browser,subject)
    sleep(2)
    bookmarkQnScn.question_not_found(browser)


@when('Tap on "View Solution" button')
def tap_on_view_solutions(browser):
    bookmarkQnScn.tap_on_view_solutions(browser)
    
      
@when('Tap on filter icon on top right corner')
def tap_on_filter_icon(browser):
    sleep(2)
    bookmarkQnScn.tap_on_filter_icon(browser)
    
      
@when('Tap on "Bookmarked" option from the filter list')
def tap_on_Bookmarked_option(browser):
    bookmarkQnScn.tap_on_Bookmarked_option(browser)
     

@then('Verify that bookmarked questions should be displayed on solution screen')   
def verify_qn_on_solutionscreen(browser):
    bookmarkQnScn.verify_qn_on_solutionscreen(browser)
    
    
@given('Navigate to practice question screen')
def navigate_to_practice_qn_scn(browser):
    bookmarkQnScn.navigate_to_practice_qn_scn(browser)
    
 
@given('Bookmark a practice question')
def bookmark_practice_qn(browser):
    bookmarkQnScn.bookmark_practice_qn(browser)
    bookmarkQnScn.quit_inbtween(browser)


@when('Tap on bookmarked question')
def tap_on_qn_in_bookmark_scn(browser):
    bookmarkQnScn.tap_on_qn_in_bookmark_scn(browser)    

    
@then('User should navigate to bookmark question screen')
def verify_bookmark_qn_screen(browser):
    bookmarkQnScn.verify_bookmark_qn_screen(browser)

    
@then('Verify that App back should be present at the button at the top left corner of the screen')
def verify_app_back_button(browser):
    bookmarkQnScn.verify_app_back_button(browser)


@then('Verify Share icon')
def verify_share_icon(browser):
    bookmarkQnScn.verify_share_icon(browser)


@then('Verify Bookmark icon')
def verify_Bookmark_icon(browser):
    bookmarkQnScn.verify_Bookmark_icon(browser)


@then('Verify label Concept followed by chapter name')
def verify_chapter_label(browser):
    bookmarkQnScn.verify_chapter_label(browser)


@then('Verify bookmarked question with solution')
def verify_qn_and_solution(browser):
    bookmarkQnScn.verify_qn_and_solution(browser)


@then('Verify that user should navigate to bookmark home screen')
def verify_bookmark_homescreen(browser):
    bookmarkQnScn.verify_bookmark_homescreen(browser)


@when('Tap on app back button')    
def app_backbtn(browser):
    sleep(2)
    bookmarkQnScn.app_backbtn(browser)


@when('Tap on device back button')
def tap_device_backbtn(browser):
    sleep(2)
    bookmarkQnScn.tap_device_backbtn(browser) 

    
@given('Navigate to bookmark question screen')
def navigate_to_book_mark_question_screen(browser):
    bookmarkQnScn.navigate_to_practice_qn_scn(browser)
    bookmarkQnScn.bookmark_practice_qn(browser)
    bookmarkQnScn.quit_inbtween(browser)
    bookmarkQnScn.navigate_back_home_screen(browser)
    bookmarkQnScn.navigate_to_book_mark_screen(browser)
    bookmarkQnScn.tap_on_qn_in_bookmark_scn(browser)

         
@when('Unbookmark the question in bookmark question screen')
def unbookmark_a_qn(browser):
    bookmarkQnScn.remove_bookmark_in_qnscn(browser)
    
    
@then('Verify that particular question should be removed from the bookmark home screen under All tab')
def verify_qn_removed_under_all_tab(browser):
    bookmarkQnScn.app_backbtn(browser)
    sleep(2)
    bookmarkQnScn.question_not_found(browser)


@when('Unbookmark the question in subject bookmark screen')
@when('Unbookmark the question in bookmark home screen')
def remove_bookmark_inbookmark_scn(browser):
    bookmarkQnScn.remove_bookmark_inbookmark_scn(browser)
    

@then(parsers.parse('Verify "{text}" option should be shown along with the snackbar message'))
def verify_snackbar_action_button(browser,text):
    bookmarkQnScn.verify_snackbar_action_button(browser,text)
    

@given('Navigate to bookmark home screen after bookmarking a question')
def navigate_to_book_mark_home_screen(browser):
    bookmarkQnScn.navigate_to_practice_qn_scn(browser)
    bookmarkQnScn.bookmark_practice_qn(browser)
    bookmarkQnScn.quit_inbtween(browser)
    bookmarkQnScn.navigate_back_home_screen(browser)
    bookmarkQnScn.navigate_to_book_mark_screen(browser)


@then(parsers.parse('Verify that "{text}" snackbar message should be displayed at the bottom of the screen'))
def verify_snackbar_msg(browser,text):
    bookmarkQnScn.verify_snackbar_msg(browser,text)


@given('Unbookmark the question in subject bookmark screen')
@given('Unbookmark the question in bookmark home screen')
def remove_bookmark_inbookmark_scn1(browser):
    bookmarkQnScn.remove_bookmark_inbookmark_scn(browser)


@then('Verify that removed question should reappear in the bookmark subject screen')    
@then('Verify that removed question should reappear in the bookmark home screen')
def verify_removed_question(browser):
    sleep(2)
    bookmarkQnScn.verify_question(browser)
    
    
@when('Tap on UNDO option')
def tap_on_undo_option(browser):
    bookmarkQnScn.tap_on_undo_option(browser)
    

@given(parsers.parse('Bookmark a question and navigate to bookmark "{subject}" screen'))
def navigate_to_subject_tab(browser,subject):
    bookmarkQnScn.bookmark_qn_from_test(browser)
    bookmarkQnScn.navigate_back_home_screen(browser)
    bookmarkQnScn.navigate_to_book_mark_screen(browser)
    bookmarkQnScn.scroll_horizontal(browser, subject)
    sleep(2)


@then('Verify that question should be present under All tab') 
def verify_qn_under_all_tab(browser):
    bookmarkQnScn.app_backbtn(browser)
    sleep(2)
    bookmarkQnScn.navigate_to_book_mark_screen(browser)
    bookmarkQnScn.verify_question(browser)


@when('Bookmark a practice question and once again tap on same bookmark icon')
def bookmark_qn_and_remove(browser):
    bookmarkQnScn.bookmark_practice_qn(browser)
    sleep(2)
    bookmarkQnScn.remove_book_mark_in_practiceqn_screen(browser)


@given(parsers.parse('Navigate to "{Subject}" library screen'))
def navigate_to_subject_library_scn(browser,Subject):
    bookmarkQnScn.navigate_to_library(browser, Subject)

    
@when('Tap on Bookmark icon in test question screen')
def bookmark_test_qn(browser):
    sleep(2)
    bookmarkQnScn.book_mark_a_question(browser)
 
    
@then('Verify that bookmark icon color should be same as subject theme color')
def verify_color_match(browser):
#     bookmarkQnScn.verify_bookmarkicon_with_subject_theme_color(browser)
    pass


@when('Tap on Bookmark icon in practice question screen')   
def bookmark_practice_qn1(browser):
    sleep(2)
    bookmarkQnScn.bookmark_practice_qn(browser)


        

