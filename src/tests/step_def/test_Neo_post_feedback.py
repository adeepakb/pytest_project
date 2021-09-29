from pytest_bdd import scenarios, given, then, when, parsers
from pytest import fixture
from constants.platform import Platform
from pages.factory.login import LoginFactory
from pages.factory.neo_inclass_factory import NeoInClassFactory
import pytest_check as check
from utilities.neo_tute_mentoring import NeoTute



scenarios('../features/Post-Class Feedback flow.feature')


@fixture()
def login_in(request, driver):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        login_in = LoginFactory().get_page(driver, Platform.ANDROID.value)
        yield login_in
    elif Platform.WEB.name in platform_list:
        login_in = LoginFactory().get_page(driver, Platform.WEB.value)
        yield login_in

@fixture()
def neo_in_class(request, driver):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        neo_in_class = NeoInClassFactory().get_page(driver, Platform.ANDROID.value)
        yield neo_in_class
    elif Platform.WEB.name in platform_list:
        neo_in_class = NeoInClassFactory().get_page(driver, Platform.WEB.value)
        yield neo_in_class

@given("Launch the application online")
def login_as_neo_user(login_in):
    login_in.login_and_navigate_to_home_screen('+91-', '2011313229', otp=None)

@given("tutor start the session")
def step_impl(driver):
    NeoTute(driver).start_neo_session()

@when("tap on premium school card")
@then("tap on premium school card")
def tap_on_premium_card(login_in):
    login_in.click_on_premium_school()

@when("click on the hamburger menu")
def click_on_hamburger_menu(login_in):
    login_in.click_on_hamburger()

@when('tap on byjus classes card')
@when("navigate to one to mega homescreen")
def navigate_to_one_to_mega_homescreen(login_in):
    login_in.click_on_byjus_classes()

@when('join neo session')
def join_a_neo_class(neo_in_class):
    neo_in_class.home_click_on_join()

@when('click on start class')
def join_a_neo_session(neo_in_class):
    neo_in_class.join_neo_session_student('mic-on', 'cam-on')

@when('Exit the class')
def step_impl(neo_in_class):
    neo_in_class.click_on_kebab_menu()
    neo_in_class.click_on_exit_class_in_student()

@when('verify exit class popup')
def step_impl(neo_in_class):
    check.equal(neo_in_class.verify_header_in_exit_class_popup(),True,"popup is present")

@then('click on exit class button in exit popup')
@when('click on exit class button in exit popup')
def step_impl(neo_in_class):
    neo_in_class.click_on_exit_class_in_exit_popup()


@then('Verify the post the session Feedback popup should display on top of the video screen')
def step_impl(neo_in_class):
    details = neo_in_class.verify_header_in_rating_popup()
    check.equal(details.result, True, details.reason)

@then("Verify that the Feedback3 screen should be displayed with 'How was your experience with our tutor'( with five smileys)")
@then('Verify that the rating should include the class rating and tutor rating')
def step_impl(neo_in_class):
    neo_in_class.select_any_option_in_rating("Terrible")
    neo_in_class.select_any_feedback_option("Teaching Technique")
    neo_in_class.click_on_continue_btn_in_rating_popup()
    check.equal(neo_in_class.verify_the_feedback_text(),True,"popup is present")

@then("Verify the class rating feedback screen should display with 'How was your class' (with 5 smiley options)")
def step_impl(neo_in_class):
    details = neo_in_class.verify_the_text_in_rating_popup()
    check.equal(details.result, True, details.reason)
    details1 = neo_in_class.is_star_options_present_in_rating_popup()
    check.equal(details1.result, True, details1.reason)

@then("Verify that the students can skip the ratings at any point")
@then('Verify that close icon should present on the feedback popup and it is clickable')
def step_impl(neo_in_class):
    check.equal(neo_in_class.is_close_icon_in_rating_popup_present(), True, "close icon is present")


@then('Verify that feed-back popup should close when user clicks on the close icon')
def step_impl(neo_in_class):
    neo_in_class.click_on_close_icon_in_rating()
    details = neo_in_class.is_rating_popup_present()
    check.equal(details.result, False, details.reason)


@then('Verify that continue button should be enabled when user selects any emoji')
def step_impl(neo_in_class):
    neo_in_class.select_any_option_in_rating("Terrible")
    neo_in_class.select_any_feedback_option("Teaching Technique")
    details = neo_in_class.is_continue_btn_enabled()
    check.equal(details.result, True, details.reason)


@then("Verify that the next screen should be display the selected emoji with other emojis and 'What did you like the most'")
def step_impl(neo_in_class):
    neo_in_class.select_any_option_in_rating("Good")
    details = neo_in_class.verify_the_what_did_you_like_text()
    check.equal(details.result, False, details.reason)


@then('Verify that the emoji which is selected in the previous screen should be highlighted in the next screen')
def step_impl(neo_in_class):
    neo_in_class.select_any_option_in_rating("Terrible")
    details = neo_in_class.is_selected_rating_option_present()
    check.equal(details.result, True, details.reason)


@then('Verify that submitted button should be enabled when user selects any option from what did you like the most? and clicking on the submit button feedback3 should display')
def step_impl(neo_in_class):
    neo_in_class.select_any_option_in_rating("Terrible")
    neo_in_class.select_any_feedback_option("Teaching Technique")
    neo_in_class.click_on_continue_btn_in_rating_popup()
    neo_in_class.select_any_option_in_rating("Good")
    neo_in_class.select_any_feedback_option("Teaching Technique")
    details = neo_in_class.is_submit_btn_enabled()
    check.equal(details.result, True, details.reason)


@then("Verify that tutor's name, profile picture and number of sessions assisted should be displayed in Feedback3 screen")
def step_impl(neo_in_class):
    neo_in_class.select_any_option_in_rating("Terrible")
    neo_in_class.select_any_feedback_option("Teaching Technique")
    neo_in_class.click_on_continue_btn_in_rating_popup()
    details = neo_in_class.is_tutor_details_present_in_popup()
    check.equal(details.result, True, details.reason)


@then("Verify that user can't select multiple emojis")
def step_impl(neo_in_class):
    neo_in_class.select_any_option_in_rating("Terrible")
    neo_in_class.select_any_option_in_rating("Bad")
    neo_in_class.select_any_option_in_rating("Okay")
    neo_in_class.select_any_option_in_rating("Good")
    neo_in_class.select_any_option_in_rating("Great")
    details = neo_in_class.verify_multiple_selected_rating_options()
    check.equal(details.result, False, details.reason)

@then("verify that the details of feedback4 should be displayed with 'what can be improved?' with different options in feedback5 popup.")
def step_impl(neo_in_class):
    neo_in_class.select_any_option_in_rating("Terrible")
    details = neo_in_class.verify_the_what_could_be_improved_text()
    check.equal(details.result, True, details.reason)

@then("Verify that the user should able to select multiple options from 'What can be improved?'")
def step_impl(neo_in_class):
    neo_in_class.select_any_option_in_rating("Terrible")
    details = neo_in_class.verify_the_what_could_be_improved_text()
    check.equal(details.result, True, details.reason)
    neo_in_class.select_any_feedback_option("Teaching Technique")
    neo_in_class.select_any_feedback_option("Solution Provided")


@then("Verify that when user selects others option from 'What can be improved?' , an additional comments textbox should display with the text' Add your comment here")
def step_impl(neo_in_class):
    neo_in_class.select_any_option_in_rating("Terrible")
    neo_in_class.select_any_feedback_option("Other")
    details = neo_in_class.is_add_your_comments_box_present()
    check.equal(details.result, True, details.reason)

@then('Verify submit button after adding comments in the feedback section')
def step_impl(neo_in_class):
    neo_in_class.select_any_option_in_rating("Terrible")
    neo_in_class.select_any_feedback_option("Other")
    neo_in_class.enter_comments_in_comments_box("other issue")
    details = neo_in_class.is_submit_btn_enabled()
    check.equal(details.result, True, details.reason)

@then("Verify that when user submit the ratings 'thank you' popup should be displayed")
def step_impl(neo_in_class):
    neo_in_class.select_any_option_in_rating("Terrible")
    neo_in_class.select_any_feedback_option("Teaching Technique")
    neo_in_class.click_on_continue_btn_in_rating_popup()
    neo_in_class.select_any_option_in_rating("Good")
    neo_in_class.select_any_feedback_option("Teaching Technique")
    neo_in_class.click_on_submit_button_in_feedback()
    details = neo_in_class.verify_text_in_Thank_you_popup()
    check.equal(details.result, True, details.reason)


@then('Verify that the rating popup should display whether the student leaves the session or the session ends')
def step_impl(neo_in_class):
    details = neo_in_class.verify_header_in_rating_popup()
    check.equal(details.result, True, details.reason)

@then("Verify that student should able to rejoin the class after submitting the ratings")
@then('Verify that feedback popup should display when user rejoins the class who has already submitted the feedback')
def step_impl(neo_in_class):
    neo_in_class.select_any_option_in_rating("Terrible")
    neo_in_class.select_any_feedback_option("Teaching Technique")
    neo_in_class.click_on_continue_btn_in_rating_popup()
    neo_in_class.select_any_option_in_rating("Good")
    neo_in_class.select_any_feedback_option("Teaching Technique")
    neo_in_class.click_on_submit_button_in_feedback()
    neo_in_class.home_click_on_join()
    neo_in_class.join_neo_session_student('mic-on', 'cam-on')
    neo_in_class.click_on_kebab_menu()
    neo_in_class.click_on_exit_class_in_student()
    neo_in_class.click_on_exit_class_in_exit_popup()
    details = neo_in_class.verify_header_in_rating_popup()
    check.equal(details.result, True, details.reason)


@then('Verify that rating popup should display when user close the ratings and rejoins the session again')
def step_impl(neo_in_class):
    neo_in_class.select_any_option_in_rating("Good")
    neo_in_class.select_any_feedback_option("Teaching Technique")
    neo_in_class.click_on_close_icon_in_rating()
    neo_in_class.home_click_on_join()
    neo_in_class.join_neo_session_student('mic-on', 'cam-on')
    neo_in_class.click_on_kebab_menu()
    neo_in_class.click_on_exit_class_in_student()
    neo_in_class.click_on_exit_class_in_exit_popup()
    details = neo_in_class.verify_header_in_rating_popup()
    check.equal(details.result, True, details.reason)

@then("Verify the colour's of the emojis")
def step_impl(neo_in_class):
    neo_in_class.select_any_option_in_rating("Great")
    details = neo_in_class.get_selected_emoji_color('rgba(51, 51, 51, 1)')
    check.equal(details.result, True, details.reason)