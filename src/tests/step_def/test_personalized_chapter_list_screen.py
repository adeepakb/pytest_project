from pytest_bdd import scenarios, given, when, then, parsers

from pages.android.homepage import HomePage
from utilities.BasePage import BaseClass
from pages.android.personalizedChapterList import PersonalizedChapterList
from pages.android.Journeyloadingscreen import JourneyLoadingScreen
from pages.android.Journeymapscreen import JourneyMapScreen
from pages.android.Librarychapterlistscreen import LibraryChapterListsScreen

driver = fixture = 'driver'
baseClass = BaseClass()
home = HomePage(driver)
personalize = PersonalizedChapterList(driver)
journey_map=JourneyMapScreen(driver)
journey_loading=JourneyLoadingScreen(driver)
library=LibraryChapterListsScreen(driver)    

"""storing the feature file name"""
featureFileName = "Personalized chapter list screen"

# baseClass.setupLogs(featureFileName)

"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""
scenarios('../features/' + featureFileName + '.feature')


# scenario 1
@given('Launch the app online')
def launch_app(driver):
    # journey_loading.switch_to_wifi(driver)
    # code = getdata(Login_Credentials,'login_detail5_search', 'code')
    # countrycode = getdata(Login_Credentials,'login_detail5_search', 'country_code')
    # mobno = getdata(Login_Credentials,'login_detail5_search', 'mobile_no')
    # otp = getdata(Login_Credentials,'login_detail5_search','OTP')
    home.navigate_to_home_screen(driver)
    pass


@when('User is in Personalized chapter list screen')
def personalized_chapter_screen_two(driver):
    home.select_subject_mathematics(driver)


@then('Verify that trending journey card should be highlighted')
def trending_journey(driver):
    personalize.verify_trending_journey_card_highlighted(driver)

# scenario 2
@given('User is new user')
def new_user(driver):
    pass


@given('User is in Personalized chapter list screen')
def personalized_chapter_screen(driver):
    home.select_subject_mathematics(driver)
    personalize.verify_personalised_chapter_list_screen(driver)
    personalize.go_up_with_respect_to_highlight_journey(driver)
    

# # scenario 3
@given('Device is white listed for search experiment')
def search_experiment(driver):
    pass


@when('User is in personalized chapter list screen.')
def personalised_chapter_3_line(driver):
    home.select_subject_mathematics(driver)
    personalize.verify_personalised_chapter_list_screen(driver)


@when('Trending journey card is highlighted after third row of chapter')
def trending_journey_card_after_third_row(driver):
    personalize.varify_trending_journey_in_third_or_below_row(driver)


@then('Verify back arrow on top left corner of the screen')
def varify_back_arrow(driver):
    personalize.varify_back_arrow_button(driver)


@then('Subject name center aligned')
def check_subject_name(driver):
    personalize.verify_subject_name_centre_allign(driver)


@then('back Button on top right corner of the screen')
def check_top_right_button(driver):
    personalize.varify_back_arrow_button(driver)


@then('Search button on top right corner of the screen')
def check_search_button(driver):
    personalize.verify_search_button(driver)


@then('Sticky card with recently taken chapter name followed by forward arrow')
def sticky_card_arrow(driver):
    personalize.verify_min_sticky_card_with_forward_arrow(driver)


# scenario 4
@when('Trending journey card is highlighted in first two rows of chapter')
def trending_journey_card(driver):
    personalize.varify_trending_journey_in_first_and_second_row(driver)


@then('Library button along with the text library at the top right side of the screen')
def library_button(driver):
    personalize.scroll_up_with_highlight_journey(driver)
    personalize.verify_library_button_and_text(driver)


@then('Verify that App back button on top left side of the screen')
def app_back_button(driver):
    personalize.varify_back_arrow_button(driver)


@then('Subject name followed by number of Chapters and Journeys')
def subject_name(driver):
    personalize.verify_subject_name_with_chapters_and_journeys(driver)


@then('Hero image')
def hero_image(driver):
    pass


@then('Below that resume where you left card with the journey/video name followed by forward icon(->)')
def recomanded_learning(driver):
    personalize.verify_resume_card_with_forward_icon(driver)


@then('Below that all the topics with respective journey cards ,test cards and practice cards')
def below_journey_cards(driver):
    personalize.verify_test_practice_and_journey_cards(driver)


@then('Ensure that each chapters in the journey screen should be separated by thin line')
def thin_line(driver):
    pass

# scenario 5

# scenario 6
@when('User taps on library button')
def click_on_personalized(driver):
    personalize.click_on_library_button(driver)


@then('Verify that user should be switched to library chapter list screen')
def library_chapter_screen(driver):
    personalize.verify_library_screen(driver)


# Scenario 7
@when('User taps on back arrow in personalized chapter list screen')
def click_on_back_button(driver):
    personalize.click_on_back_arrow(driver)


@then('Verify that user should be navigate back to home screen')
def display_home_screen(driver):
    personalize.verify_home_screen(driver)

# scenario 8    
@when('User taps on search button')
def tap_on_search(driver):
    personalize.click_on_search_button(driver)

@then('Verify that user should be navigate to <SearchScreen>')
def search_screen(driver):
    personalize.verify_search_screen(driver)


# @Scenario 9 
@when('User taps on resume where you left card')
def resume(driver):
    personalize.click_on_sticky_card(driver)


@then('Verify that user should be navigate to particular journey')
def verify_journey(driver):
#     personalize.verify_journey_name_with_respect_to_sticky_card(driver)
    journey_loading.verify_journey_map_screen(driver)

# scenario 10
@when('User taps on resume the practice card')
def resume_practice(driver):
    personalize.click_on_practice_card(driver)
    personalize.quit_inbtween(driver)


@then('Verify that user should be navigate to particular practice')
def practice_screen(driver):
    personalize.verify_practice_screen(driver)


# scenario 11
@when('User taps on resume the test card')
def resume_test(driver):
    personalize.click_on_test_card(driver)


@then('Verify that user should be navigate to particular test')
def ttest_screen(driver):
    personalize.verify_test_screen(driver)


# scenario 12
@when('User is in personalized chapter list screen')
def personalised_list(driver):
    home.select_subject_mathematics(driver)
    personalize.verify_personalised_chapter_list_screen(driver)
    personalize.go_up_with_respect_to_highlight_journey(driver)

@then('Verify that journey card should have journey icon and journey name')
def journey_icon_and_journey_name(driver):
    personalize.verify_journey_card_icon_and_name(driver)
    


# scenario 13  
@then('Verify that number of journey cards under each topic on personalized chapter list screen should be based on back end')
def total_journey_cards(driver):
#     personalize.journey_cards_in_each_chapters(driver)
    personalize.get_allchapter_names(driver)
    
  
    
# scenario 14
# @when('User is in Personalized chapter list screen.')
# def personalized_chapter_screen_one(driver):
#     home.select_subject_mathematics(driver)
#     sleep(3)
#     personalize.scroll_up_with_highlight_journey(driver)
#     personalize.verify_personalised_chapter_list_screen(driver)
    
# @then('Verify that each chapter should consists of tests and practices and should be based on back end')
# def check_test_and_practice(driver):
#     personalize.verify_test_and_practice(driver)

# scenario 15
@then('Verify that user should be able to see only chapter name and test card and practice card')
def chapter_name_test_practice(driver):
    personalize.go_up_with_respect_to_highlight_journey(driver)
    personalize.verify_test_practice_and_journey_cards(driver)
    
    
# scenario 16
@then('Verify that scrolling upwards the top label should be minimized')
def min_top_label(driver):
    personalize.verify_minimise_top_label(driver)


# scenario 17 
@when('User taps on journey card')
def tap_journey(driver):
    personalize.scroll_up_with_highlight_journey(driver)
    journey_loading.click_on_journey_card(driver)


@then('Verify that user navigates to journey loading screen first and then journey map screen of particular topic')
def verify_journey_loading_and_map_screen(driver):
    journey_loading.verify_journey_loading_screen(driver)
    personalize.verify_journey_map_screen(driver)


# scenario 18  
@given('User is in Offline')
def offline(driver):
    journey_map.select_offline_mode(driver)

@when('User taps on a journey card')
def tap_on_a_journey(driver):
    personalize.scroll_up_with_highlight_journey(driver)
    journey_loading.click_on_new_journey_card(driver)
#     journey_map.click_on_trending_journey_card(driver)

@then(parsers.parse('Verify that "{text}" toast message should be shown'))
def toast_msg(driver,text):
    personalize.verify_toast_message(driver, text)


@then('user should be navigate back to chapter list screen')
def chapter(driver):
    library.verify_personalised_screen(driver)
    journey_loading.switch_to_wifi(driver)


#  scenario 19
@when('User taps on test card')
def tap_test(driver):
    personalize.click_on_test_card(driver)


@then('Verify that user should be navigates to <TestScreen> of particular topic')
def verify_test(driver):
    personalize.verify_test_screen(driver)


#  scenario 20
@when('User taps on practice card')
def tap_practice_card(driver):
    personalize.click_on_practice_card(driver)


@then('Verify that user should be navigate to <PracticeScreen> of particular topic')
def verify_practice_card(driver):
    personalize.verify_practice_screen(driver)
    