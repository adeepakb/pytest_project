from time import sleep
from pytest_bdd import scenarios, given, when, then, parsers
from POM_Pages.Android_pages.bookmarkQuestionScreen import BookMarkQuestionScreen
from Utilities.BasePage import BaseClass
driver = fixture = 'driver'


baseClass = BaseClass()
bookmarkQnScn=BookMarkQuestionScreen(driver)
featureFileName = 'Bookmark questions'


# baseClass.setupLogs(featureFileName)

"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""

scenarios('../features/' + featureFileName + '.feature')


@given('Launch the app online and navigate to Home screen')
def loginapp(driver):
    bookmarkQnScn.navigate_to_home_screen(driver)

@given('Navigate to Highlights screen')    
@given('Bookmark a question')
def bookmark_a_question(driver):
    bookmarkQnScn.bookmark_qn_from_test(driver)


@when('Navigate to bookmark home screen')
def navigate_to_book_mark_screen(driver):
    bookmarkQnScn.navigate_back_home_screen(driver)
    bookmarkQnScn.navigate_to_book_mark_screen(driver)


@then('Verify that bookmarked question should be present in Bookmark home screen under All tab')
def verify_question(driver):
    bookmarkQnScn.verify_question(driver)


@then(parsers.parse('Verify below that chapter name and "{subject}" subject name on bookmark subject screen'))    
@then(parsers.parse('Verify below that chapter name and "{subject}" subject name'))
def verify_subject_and_concept_name1(driver,subject):
    bookmarkQnScn.verify_subject_and_chapter_name(driver,subject)


@then('Verify the bookmark icon on bookmark subject screen')
@then('Verify the bookmark icon on bookmark home screen')
def is_bookmark_icon_shown1(driver):
    bookmarkQnScn.is_bookmark_icon_shown(driver)


@then(parsers.parse('Verify that bookmarked question should be present under "{subject}" tab'))
def verify_qn_under_sub_tab1(driver,subject):
    bookmarkQnScn.scroll_horizontal(driver,subject)
    sleep(2)
    bookmarkQnScn.verify_question(driver)

    
@when('Navigate to test instruction screen')
def navigate_to_test_instscreen(driver):
    bookmarkQnScn.navigate_to_test(driver)


@then(parsers.parse('Verify that in the test instruction screen "{text}" message should not be shown.'))
def istruction_notfound(driver,text):
    bookmarkQnScn.istruction_notfound(driver,text)      


@then(parsers.parse('Verify that in the test instruction screen "{text}" message should be shown.'))
def istruction_found(driver,text):
    bookmarkQnScn.istruction_found(driver,text)      


@when('Tap on Test button in Instruction screen')
def navigate_to_test_screen(driver):
    bookmarkQnScn.navigate_to_test_screen(driver)

 
@then('Verify that Bookmark icon should be present in the test screen')
def verify_bookmark_icon_ontestscreen(driver):
    bookmarkQnScn.verify_bookmark_icon_ontestscreen(driver)


@when('Bookmark a test question and once again tap on same bookmark icon')
def book_mark_a_question(driver):
    bookmarkQnScn.book_mark_a_question(driver)
    bookmarkQnScn.remove_book_mark_in_qn_screen(driver)


@then(parsers.parse('Verify that "{text}" toast message should be displayed at the bottom of the screen'))
def verify_toast_msg(driver,text):
    bookmarkQnScn.verify_toast_msg(driver,text)


@then('Verify unbookmarked question should not be displayed in the bookmark home screen under All tab')
def navigate_to_bookmark_screen_andverify(driver):
    bookmarkQnScn.quit_inbtween(driver)
    bookmarkQnScn.navigate_back_home_screen(driver)
    bookmarkQnScn.navigate_to_book_mark_screen(driver)
    sleep(2)
    bookmarkQnScn.question_not_found(driver)


@then(parsers.parse('Verify that question should be removed under "{subject}" tab'))
@then(parsers.parse('Verify unbookmarked question should not be displayed under "{subject}" tab'))
def navigate_to_subject_tab_verify(driver,subject):
    bookmarkQnScn.scroll_horizontal(driver,subject)
    sleep(2)
    bookmarkQnScn.question_not_found(driver)


@when('Tap on "View Solution" button')
def tap_on_view_solutions(driver):
    bookmarkQnScn.tap_on_view_solutions(driver)
    
      
@when('Tap on filter icon on top right corner')
def tap_on_filter_icon(driver):
    sleep(2)
    bookmarkQnScn.tap_on_filter_icon(driver)
    
      
@when('Tap on "Bookmarked" option from the filter list')
def tap_on_Bookmarked_option(driver):
    bookmarkQnScn.tap_on_Bookmarked_option(driver)
     

@then('Verify that bookmarked questions should be displayed on solution screen')   
def verify_qn_on_solutionscreen(driver):
    bookmarkQnScn.verify_qn_on_solutionscreen(driver)
    
    
@given('Navigate to practice question screen')
def navigate_to_practice_qn_scn(driver):
    bookmarkQnScn.navigate_to_practice_qn_scn(driver)
    
 
@given('Bookmark a practice question')
def bookmark_practice_qn(driver):
    bookmarkQnScn.bookmark_practice_qn(driver)
    bookmarkQnScn.quit_inbtween(driver)


@when('Tap on bookmarked question')
def tap_on_qn_in_bookmark_scn(driver):
    bookmarkQnScn.tap_on_qn_in_bookmark_scn(driver)    

    
@then('User should navigate to bookmark question screen')
def verify_bookmark_qn_screen(driver):
    bookmarkQnScn.verify_bookmark_qn_screen(driver)

    
@then('Verify that App back should be present at the button at the top left corner of the screen')
def verify_app_back_button(driver):
    bookmarkQnScn.verify_app_back_button(driver)


@then('Verify Share icon')
def verify_share_icon(driver):
    bookmarkQnScn.verify_share_icon(driver)


@then('Verify Bookmark icon')
def verify_Bookmark_icon(driver):
    bookmarkQnScn.verify_Bookmark_icon(driver)


@then('Verify label Concept followed by chapter name')
def verify_chapter_label(driver):
    bookmarkQnScn.verify_chapter_label(driver)


@then('Verify bookmarked question with solution')
def verify_qn_and_solution(driver):
    bookmarkQnScn.verify_qn_and_solution(driver)


@then('Verify that user should navigate to bookmark home screen')
def verify_bookmark_homescreen(driver):
    bookmarkQnScn.verify_bookmark_homescreen(driver)


@when('Tap on app back button')    
def app_backbtn(driver):
    sleep(2)
    bookmarkQnScn.app_backbtn(driver)


@when('Tap on device back button')
def tap_device_backbtn(driver):
    sleep(2)
    bookmarkQnScn.tap_device_backbtn(driver) 

    
@given('Navigate to bookmark question screen')
def navigate_to_book_mark_question_screen(driver):
    bookmarkQnScn.navigate_to_practice_qn_scn(driver)
    bookmarkQnScn.bookmark_practice_qn(driver)
    bookmarkQnScn.quit_inbtween(driver)
    bookmarkQnScn.navigate_back_home_screen(driver)
    bookmarkQnScn.navigate_to_book_mark_screen(driver)
    bookmarkQnScn.tap_on_qn_in_bookmark_scn(driver)

         
@when('Unbookmark the question in bookmark question screen')
def unbookmark_a_qn(driver):
    bookmarkQnScn.remove_bookmark_in_qnscn(driver)
    
    
@then('Verify that particular question should be removed from the bookmark home screen under All tab')
def verify_qn_removed_under_all_tab(driver):
    bookmarkQnScn.app_backbtn(driver)
    sleep(2)
    bookmarkQnScn.question_not_found(driver)


@when('Unbookmark the question in subject bookmark screen')
@when('Unbookmark the question in bookmark home screen')
def remove_bookmark_inbookmark_scn(driver):
    bookmarkQnScn.remove_bookmark_inbookmark_scn(driver)
    

@then(parsers.parse('Verify "{text}" option should be shown along with the snackbar message'))
def verify_snackbar_action_button(driver,text):
    bookmarkQnScn.verify_snackbar_action_button(driver,text)
    

@given('Navigate to bookmark home screen after bookmarking a question')
def navigate_to_book_mark_home_screen(driver):
    bookmarkQnScn.navigate_to_practice_qn_scn(driver)
    bookmarkQnScn.bookmark_practice_qn(driver)
    bookmarkQnScn.quit_inbtween(driver)
    bookmarkQnScn.navigate_back_home_screen(driver)
    bookmarkQnScn.navigate_to_book_mark_screen(driver)


@then(parsers.parse('Verify that "{text}" snackbar message should be displayed at the bottom of the screen'))
def verify_snackbar_msg(driver,text):
    bookmarkQnScn.verify_snackbar_msg(driver,text)


@given('Unbookmark the question in subject bookmark screen')
@given('Unbookmark the question in bookmark home screen')
def remove_bookmark_inbookmark_scn1(driver):
    bookmarkQnScn.remove_bookmark_inbookmark_scn(driver)


@then('Verify that removed question should reappear in the bookmark subject screen')    
@then('Verify that removed question should reappear in the bookmark home screen')
def verify_removed_question(driver):
    sleep(2)
    bookmarkQnScn.verify_question(driver)
    
    
@when('Tap on UNDO option')
def tap_on_undo_option(driver):
    bookmarkQnScn.tap_on_undo_option(driver)
    

@given(parsers.parse('Bookmark a question and navigate to bookmark "{subject}" screen'))
def navigate_to_subject_tab(driver,subject):
    bookmarkQnScn.bookmark_qn_from_test(driver)
    bookmarkQnScn.navigate_back_home_screen(driver)
    bookmarkQnScn.navigate_to_book_mark_screen(driver)
    bookmarkQnScn.scroll_horizontal(driver, subject)
    sleep(2)


@then('Verify that question should be present under All tab') 
def verify_qn_under_all_tab(driver):
    bookmarkQnScn.app_backbtn(driver)
    sleep(2)
    bookmarkQnScn.navigate_to_book_mark_screen(driver)
    bookmarkQnScn.verify_question(driver)


@when('Bookmark a practice question and once again tap on same bookmark icon')
def bookmark_qn_and_remove(driver):
    bookmarkQnScn.bookmark_practice_qn(driver)
    sleep(2)
    bookmarkQnScn.remove_book_mark_in_practiceqn_screen(driver)


@given(parsers.parse('Navigate to "{Subject}" library screen'))
def navigate_to_subject_library_scn(driver,Subject):
    bookmarkQnScn.navigate_to_library(driver, Subject)

    
@when('Tap on Bookmark icon in test question screen')
def bookmark_test_qn(driver):
    sleep(2)
    bookmarkQnScn.book_mark_a_question(driver)
 
    
@then('Verify that bookmark icon color should be same as subject theme color')
def verify_color_match(driver):
#     bookmarkQnScn.verify_bookmarkicon_with_subject_theme_color(driver)
    pass


@when('Tap on Bookmark icon in practice question screen')   
def bookmark_practice_qn1(driver):
    sleep(2)
    bookmarkQnScn.bookmark_practice_qn(driver)


        

