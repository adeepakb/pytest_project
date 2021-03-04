from pytest_bdd import scenarios, given, when, then, parsers

from time import sleep

from POM_Pages.Android_pages.homepage import HomePage
from POM_Pages.Android_pages.Librarychapterlistscreen import LibraryChapterListsScreen
from Utilities.BasePage import BaseClass
from POM_Pages.Android_pages.personalizedChapterList import PersonalizedChapterList

driver = fixture = 'driver'
baseClass = BaseClass()
home = HomePage(driver)
library = LibraryChapterListsScreen(driver)
personalize = PersonalizedChapterList(driver)

"""storing the feature file name"""
featureFileName = "Library chapter list screen"

#baseClass.setupLogs(featureFileName)

"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""
scenarios('../features/' + featureFileName + '.feature')


# scenario 1
@given('Launch the app online')
def launch_app(driver):
    # code = getdata(Login_Credentials,'login_detail5_search', 'code')
    # countrycode = getdata(Login_Credentials,'login_detail5_search', 'country_code')
    # mobno = getdata(Login_Credentials,'login_detail5_search', 'mobile_no')
    # otp = getdata(Login_Credentials,'login_detail5_search','OTP')
    home.navigate_to_home_screen(driver)
    pass


@given('User is in Personalized Chapter list screen')
def personalized_chapter_screen(driver):
    home.select_subject_mathematics(driver)

    
@when('User taps on app back button')
def tap_on_back_button(driver):
    personalize.click_on_back_arrow(driver)


@then('Verify that user should be navigate to home screen')
def navigate_to_home(driver):
    personalize.verify_home_screen(driver)


# scenario 2
@then('Verify the App back button on top left corner of the screen')
def app_back_btn(driver):
    library.verify_app_back_arrow(driver)


@then(parsers.parse('Personalized button along with the text "{text}" at the top right of the screen.'))
def personalised_btn(driver,text):
    library.verify_personalise_btn(driver, text)


@then('Search button should be shown next to personalized button.')
def search_btn(driver):
    personalize.verify_search_button(driver)


@then('Subject Name followed by number of Videos and Tests')
def sub_videos_tests(driver):
    library.verify_chapters_heading(driver)


@then('Below the top layout, a label Chapters and list of chapters(Library carousel) below it')
def chapters_chapters_list(driver):
    library.chapter_name_with_total_video_count(driver)

# scenario 3
@when('User is in Library Chapter list screen')
def library_chapter_screen(driver):
    home.select_subject_mathematics(driver)
    library.verify_library_cha_screen(driver)
    

@when('User taps on personalized button')
def tep_on_personalized_button(driver):
    library.click_on_personlised_button(driver)


@then('Verify that user switches to personalized mode chapter list screen')
def navigate_to_personalized_screen(driver):
    library.verify_personalised_screen(driver)


# scenario 4
@then('Verify that chapter name and total number of video count')
def chapter_name_with_video_count(driver):
    library.chapter_name_with_total_video_count(driver)


@then('Video card with video thumbnail and Video Progression below the video thumbnail')
def verify_video_card_and_video_thumbail(driver):
    library.verify_video_thumbnail_progression_bar(driver)
    


@then('Test Button and Practice Button')
def practice_and_test(driver):
    library.verify_test_and_practice_btns(driver)


# scenario 5
@then('Verify that Chapter name should be displayed')
def chapter_names(driver):
#     library.chapter_names_without_video(driver)
    pass


@then('Test button and Practice button')
def practice(driver):
    library.verify_test_and_practice_for_empty_chapter(driver)


# scenario 7
@then('Verify that each chapter in the subject should have video carousel in Library chapter list screen.')
def video_carousel(driver):
    library.verify_video_corousel(driver)


# scenario 8
@when('User taps on video card in Library chapter list screen of particular chapter')
def tap_on_video(driver):
    library.click_on_video_card(driver)


@then('Verify that user should be navigates to video list screen of particular topic')
def verify_video(driver):
    library.verify_video_screen_of_perticular_chapter(driver)


# scenario 9
@when('User taps on test button on library chapter list screen of particular chapter')
def click_on_test(driver):
    library.click_on_test_button(driver)


@then('Verify that user should be navigates to test list screen of particular topic')
def verify_test(driver):
    library.verify_test_screen(driver)


# scenario 10
@when('User taps on practice button on library chapter list screen of particular chapter')
def tap_on_practice(driver):
    library.click_on_practice_button(driver)
    sleep(2)


@then('Verify that user should be navigates to practice list screen of particular topic')
def verify_practice(driver):
    library.verify_practice_screen(driver)


# scenario 11
@when('User taps on back button on library chapter list screen')
def tep_on_back_button(driver):
    sleep(2)
    library.click_on_back_arrow(driver)


@then('Verify that user should be navigate to home screen')
def verify_home(driver):
    sleep(2)
    library.verify_home_screen(driver)


# scenario 12
@when('User taps on same subject card')
def tep_on_subject_card(driver):
    home.select_subject_mathematics(driver)


@then('Verify that user should be navigate to library chapter list screen')
def navigate_to_library_chapter_list_screen(driver):
    library.verify_library_screen(driver)
