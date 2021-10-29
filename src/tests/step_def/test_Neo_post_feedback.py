from pytest_bdd import scenarios, given, then, when, parsers
from pytest import fixture
from constants.platform import Platform
from pages.factory.login import LoginFactory
from pages.factory.neo_inclass_factory import NeoInClassFactory
import pytest_check as check
from utilities.neo_tute_mentoring import NeoTute



scenarios('../features/Post-Class Feedback flow.feature')

@fixture()
def student1_login(request, driver):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        student1_login = LoginFactory().get_page(driver, Platform.ANDROID.value)
        yield student1_login
    elif Platform.WEB.name in platform_list:
        student1_login = LoginFactory().get_page(driver, Platform.WEB.value)
        yield student1_login


@fixture()
def student1_neo(request, student1_login):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        student1_neo = NeoInClassFactory().get_page(student1_login.driver, Platform.ANDROID.value)
        yield student1_neo
    elif Platform.WEB.name in platform_list:
        student1_neo = NeoInClassFactory().get_page(student1_login.driver, Platform.WEB.value)
        yield student1_neo


@fixture()
def neo_tute(driver):
    neo_tute = NeoTute(driver)
    yield neo_tute


@given("Launch the application online")
def login_as_neo_user(student1_login):
    student1_login.login_and_navigate_to_home_screen('+91-', '2011313229', otp=None)

@given("tutor start the session")
def step_impl(neo_tute):
    neo_tute.start_neo_session()

@when("tap on premium school card")
@then("tap on premium school card")
def tap_on_premium_card(student1_login):
    student1_login.click_on_premium_school()

@when("click on the hamburger menu")
def click_on_hamburger_menu(student1_login):
    student1_login.click_on_hamburger()

@when('tap on byjus classes card')
@when("navigate to one to mega homescreen")
def navigate_to_one_to_mega_homescreen(student1_login):
    student1_login.click_on_byjus_classes()

@when('join neo session')
def join_a_neo_class(student1_neo):
    student1_neo.home_click_on_join()

@when('click on start class')
def join_a_neo_session(student1_neo):
    student1_neo.join_neo_session_student('mic-on', 'cam-on')

@when('Exit the class')
def step_impl(student1_neo):
    student1_neo.click_on_kebab_menu()
    student1_neo.click_on_exit_class_in_student()

@when('verify exit class popup')
def step_impl(student1_neo):
    check.equal(student1_neo.verify_header_in_exit_class_popup(),True,"popup is present")

@then('click on exit class button in exit popup')
@when('click on exit class button in exit popup')
def step_impl(student1_neo):
    student1_neo.click_on_exit_class_in_exit_popup()


@then('Verify the post the session Feedback popup should display on top of the video screen')
def step_impl(student1_neo):
    details = student1_neo.verify_header_in_rating_popup()
    check.equal(details.result, True, details.reason)

@then("Verify that the Feedback3 screen should be displayed with 'How was your experience with our tutor'( with five smileys)")
@then('Verify that the rating should include the class rating and tutor rating')
def step_impl(student1_neo):
    student1_neo.select_any_option_in_rating("Terrible")
    student1_neo.select_any_feedback_option("Teaching Technique")
    student1_neo.click_on_continue_btn_in_rating_popup()
    details1 = student1_neo.verify_the_feedback_text()
    check.equal(details1.result, True, details1.reason)

@then("Verify the class rating feedback screen should display with 'How was your class' (with 5 smiley options)")
def step_impl(student1_neo):
    student1_neo.navigate_to_home_click_on_join()
    student1_neo.join_neo_session_student('mic-on', 'cam-on')
    student1_neo.click_on_kebab_menu()
    student1_neo.click_on_exit_class_in_student()
    student1_neo.click_on_exit_class_in_exit_popup()
    details = student1_neo.verify_the_text_in_rating_popup()
    check.equal(details.result, True, details.reason)
    details1 = student1_neo.is_star_options_present_in_rating_popup()
    check.equal(details1.result, True, details1.reason)


@then('Verify that close icon should present on the feedback popup and it is clickable')
def step_impl(student1_neo):
    check.equal(student1_neo.is_close_icon_in_rating_popup_present(), True, "close icon is present")

@then("Verify that the students can skip the ratings at any point")
@then('Verify that feed-back popup should close when user clicks on the close icon')
def step_impl(student1_neo):
    student1_neo.click_on_close_icon_in_rating()
    details = student1_neo.is_session_topic_inclass_present()
    check.equal(details.result, False, details.reason)


@then('Verify that continue button should be enabled when user selects any emoji')
def step_impl(student1_neo):
    student1_neo.select_any_option_in_rating("Terrible")
    student1_neo.select_any_feedback_option("Teaching Technique")
    details = student1_neo.is_continue_btn_enabled()
    check.equal(details.result, True, details.reason)


@then("Verify that the next screen should be display the selected emoji with other emojis and 'What did you like the most'")
def step_impl(student1_neo):
    student1_neo.select_any_option_in_rating("Good")
    details = student1_neo.verify_the_what_did_you_like_text()
    check.equal(details.result, True, details.reason)


@then('Verify that the emoji which is selected in the previous screen should be highlighted in the next screen')
def step_impl(student1_neo):
    student1_neo.select_any_option_in_rating("Terrible")
    details = student1_neo.is_selected_rating_option_present()
    check.equal(details.result, True, details.reason)


@then('Verify that submitted button should be enabled when user selects any option from what did you like the most? and clicking on the submit button feedback3 should display')
def step_impl(student1_neo):
    # student1_neo.select_any_option_in_rating("Terrible")
    # student1_neo.select_any_feedback_option("Teaching Technique")
    student1_neo.click_on_continue_btn_in_rating_popup()
    student1_neo.select_any_option_in_rating("Good")
    student1_neo.select_any_feedback_option("Teaching Technique")
    details = student1_neo.is_submit_btn_enabled()
    check.equal(details.result, True, details.reason)


@then("Verify that tutor's name, profile picture and number of sessions assisted should be displayed in Feedback3 screen")
def step_impl(student1_neo):
    student1_neo.select_any_option_in_rating("Terrible")
    student1_neo.select_any_feedback_option("Teaching Technique")
    student1_neo.click_on_continue_btn_in_rating_popup()
    details = student1_neo.is_tutor_details_present_in_popup()
    check.equal(details.result, True, details.reason)


@then("Verify that user can't select multiple emojis")
def step_impl(student1_neo):
    student1_neo.select_any_option_in_rating("Terrible")
    student1_neo.select_any_option_in_rating("Bad")
    student1_neo.select_any_option_in_rating("Okay")
    student1_neo.select_any_option_in_rating("Good")
    student1_neo.select_any_option_in_rating("Great")
    details = student1_neo.verify_multiple_selected_rating_options()
    check.equal(details.result, False, details.reason)

@then("verify that the details of feedback4 should be displayed with 'what can be improved?' with different options in feedback5 popup.")
def step_impl(student1_neo):
    student1_neo.select_any_option_in_rating("Terrible")
    details = student1_neo.verify_the_what_could_be_improved_text()
    check.equal(details.result, True, details.reason)

@then("Verify that the user should able to select multiple options from 'What can be improved?'")
def step_impl(student1_neo):
    student1_neo.select_any_option_in_rating("Terrible")
    details = student1_neo.verify_the_what_could_be_improved_text()
    check.equal(details.result, True, details.reason)
    student1_neo.select_any_feedback_option("Teaching Technique")
    student1_neo.select_any_feedback_option("Solution Provided")


@then("Verify that when user selects others option from 'What can be improved?' , an additional comments textbox should display with the text' Add your comment here")
def step_impl(student1_neo):
    student1_neo.select_any_option_in_rating("Terrible")
    student1_neo.select_any_feedback_option("Other")
    details = student1_neo.is_add_your_comments_box_present()
    check.equal(details.result, True, details.reason)

@then('Verify submit button after adding comments in the feedback section')
def step_impl(student1_neo):
    student1_neo.select_any_option_in_rating("Terrible")
    student1_neo.select_any_feedback_option("Other")
    student1_neo.enter_comments_in_comments_box("other issue")
    details = student1_neo.is_submit_btn_enabled()
    check.equal(details.result, True, details.reason)

@then("Verify that when user submit the ratings 'thank you' popup should be displayed")
def step_impl(student1_neo):
    student1_neo.navigate_to_home_click_on_join()
    student1_neo.join_neo_session_student('mic-on', 'cam-on')
    student1_neo.click_on_kebab_menu()
    student1_neo.click_on_exit_class_in_student()
    student1_neo.click_on_exit_class_in_exit_popup()
    student1_neo.select_any_option_in_rating("Terrible")
    student1_neo.select_any_feedback_option("Teaching Technique")
    student1_neo.click_on_continue_btn_in_rating_popup()
    details1 = student1_neo.verify_the_feedback_text()
    check.equal(details1.result, True, details1.reason)
    student1_neo.select_any_option_in_rating("Good")
    student1_neo.select_any_feedback_option("Teaching Technique")
    student1_neo.click_on_submit_button_in_feedback()
    details = student1_neo.verify_text_in_Thank_you_popup()
    check.equal(details.result, True, details.reason)


@then('Verify that the rating popup should display whether the student leaves the session or the session ends')
def step_impl(student1_neo):
    details = student1_neo.verify_header_in_rating_popup()
    check.equal(details.result, True, details.reason)

@then("Verify that student should able to rejoin the class after submitting the ratings")
@then('Verify that feedback popup should display when user rejoins the class who has already submitted the feedback')
def step_impl(student1_neo):
    student1_neo.select_any_option_in_rating("Terrible")
    student1_neo.select_any_feedback_option("Teaching Technique")
    student1_neo.click_on_continue_btn_in_rating_popup()
    details1 = student1_neo.verify_the_feedback_text()
    check.equal(details1.result, True, details1.reason)
    student1_neo.select_any_option_in_rating("Great")
    student1_neo.select_any_feedback_option("Audio Quality")
    student1_neo.click_on_submit_button_in_feedback()
    student1_neo.refresh_and_join_the_session('mic-on', 'cam-on')
    student1_neo.click_on_kebab_menu()
    student1_neo.click_on_exit_class_in_student()
    student1_neo.click_on_exit_class_in_exit_popup()
    details = student1_neo.verify_header_in_rating_popup()
    check.equal(details.result, True, details.reason)


@then('Verify that rating popup should display when user close the ratings and rejoins the session again')
def step_impl(student1_neo):
    student1_neo.refresh_and_join_the_session('mic-on', 'cam-on')
    student1_neo.click_on_kebab_menu()
    student1_neo.click_on_exit_class_in_student()
    student1_neo.click_on_exit_class_in_exit_popup()
    student1_neo.select_any_option_in_rating("Good")
    student1_neo.select_any_feedback_option("Teaching Technique")
    student1_neo.click_on_close_icon_in_rating()
    student1_neo.navigate_to_home_click_on_join()
    student1_neo.join_neo_session_student('mic-on', 'cam-on')
    student1_neo.click_on_kebab_menu()
    student1_neo.click_on_exit_class_in_student()
    student1_neo.click_on_exit_class_in_exit_popup()
    details = student1_neo.verify_header_in_rating_popup()
    check.equal(details.result, True, details.reason)

@then("Verify the colour's of the emojis")
def step_impl(student1_neo):
    student1_neo.select_any_option_in_rating("Great")
    details = student1_neo.get_selected_emoji_color('rgba(51, 51, 51, 1)')
    check.equal(details.result, True, details.reason)