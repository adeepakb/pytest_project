from pytest_bdd import scenarios, given, then, when, parsers
from pytest import fixture
from constants.platform import Platform
from pages.factory.login import LoginFactory
from pages.factory.neo_inclass_factory import NeoInClassFactory
import pytest_check as check



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
    login_in.login_for_neo_class()
# def login_as_one_mega_user(login_in):
#     login_profile = "login_detail5"
#     user_profile = "user_1"
#     sub_profile = "profile_1"
#     login_in.navigate_to_home_screen(login_profile, user_profile, sub_profile)

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
@then('join neo session')
def join_a_neo_class(neo_in_class):
    neo_in_class.home_click_on_join()

@when('click on start class')
@then('click on start class')
def join_a_neo_session(neo_in_class):
    neo_in_class.join_neo_session()

@when('Exit the class')
@then('Exit the class')
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

@then('verify the rating popup')
def step_impl(neo_in_class):
    details = neo_in_class.verify_header_in_rating_popup()
    check.equal(details.result, True, details.reason)


@then('choose any rating option')
def step_impl(neo_in_class):
    neo_in_class.select_any_option_in_rating("Terrible")

@then('choose any feedback option')
@then('choose the feedback option for rating')
def step_impl(neo_in_class):
    neo_in_class.select_any_feedback_option("Teaching Technique")

@then('verify the tutor rating')
def step_impl(neo_in_class):
    check.equal(neo_in_class.verify_the_feedback_text(),True,"popup is present")

@then("verify 'How was your class text' in rating popup")
def step_impl(neo_in_class):
    details = neo_in_class.verify_the_text_in_rating_popup()
    check.equal(details.result, True, details.reason)

@then('verify the smileys with options in rating popup')
def step_impl(neo_in_class):
    details = neo_in_class.is_star_options_present_in_rating_popup()
    check.equal(details.result, True, details.reason)

@then('verify the close icon in rating popup')
def step_impl(neo_in_class):
    check.equal(neo_in_class.is_close_icon_in_rating_popup_present(), True, "close icon is present")

@then('choose tutor rating option')
def step_impl(neo_in_class):
    neo_in_class.select_any_option_in_rating("Good")

@then('verify continue button enabled')
def step_impl(neo_in_class):
    details = neo_in_class.is_continue_btn_enabled()
    check.equal(details.result, True, details.reason)

@then('verify the selected rating option')
def step_impl(neo_in_class):
    details = neo_in_class.is_selected_rating_option_present()
    check.equal(details.result, True, details.reason)

@then('click on continue button')
def step_impl(neo_in_class):
    neo_in_class.click_on_continue_btn_in_rating_popup()

@then('verify submit button enabled')
def step_impl(neo_in_class):
    details = neo_in_class.is_submit_btn_enabled()
    check.equal(details.result, True, details.reason)

@then('click on submit button')
def step_impl(neo_in_class):
    neo_in_class.click_on_submit_button_in_feedback()

@then('close the feedback popup')
def step_impl(neo_in_class):
    neo_in_class.click_on_close_icon_in_rating()

@then('choose any rating option good or great')
def step_impl(neo_in_class):
    neo_in_class.select_any_option_in_rating("Good")

@then('verify the what did you like the most text')
def step_impl(neo_in_class):
    details = neo_in_class.verify_the_what_did_you_like_text()
    check.equal(details.result, False, details.reason)

@then('verify Thank you popup')
def step_impl(neo_in_class):
    check.equal(neo_in_class.verify_text_in_Thank_you_popup(),True,"popup is present")

@then('select multiple rating options')
def step_impl(neo_in_class):
    neo_in_class.select_any_option_in_rating("Terrible")
    neo_in_class.select_any_option_in_rating("Bad")
    neo_in_class.select_any_option_in_rating("Okay")
    neo_in_class.select_any_option_in_rating("Good")
    neo_in_class.select_any_option_in_rating("Great")


@then('choose any rating option bad or okay or Terrible')
def step_impl(neo_in_class):
    neo_in_class.select_any_option_in_rating("Terrible")

@then('verify "What could be improved" text')
def step_impl(neo_in_class):
    details = neo_in_class.verify_the_what_could_be_improved_text()
    check.equal(details.result, True, details.reason)

@then('choose more than one feedback options')
def step_impl(neo_in_class):
    neo_in_class.select_any_feedback_option("Teaching Technique")
    neo_in_class.select_any_feedback_option("Solution Provided")

@then('choose others feedback option')
def step_impl(neo_in_class):
    neo_in_class.select_any_feedback_option("Other")

@then('verify the comments box')
def step_impl(neo_in_class):
    details = neo_in_class.is_add_your_comments_box_present()
    check.equal(details.result, False, details.reason)

@then('add comments in the feedback')
def step_impl(neo_in_class):
    neo_in_class.enter_comments_in_comments_box("other issue")

@then('verify the selected rating options')
def step_impl(neo_in_class):
    details = neo_in_class.is_rating_popup_present()
    check.equal(details.result, False, details.reason)

@then('close the rating popup and verify')
def step_impl(neo_in_class):
    neo_in_class.click_on_close_icon_in_rating()
    details = neo_in_class.is_rating_popup_present()
    check.equal(details.result, False, details.reason)

@then('verify tutor details in tutor rating popup')
def step_impl(neo_in_class):
    details = neo_in_class.is_tutor_details_present_in_popup()
    check.equal(details.result, True, details.reason)

@then('verify the menu in bottom container')
def step_impl(neo_in_class):
    details = neo_in_class.is_kebab_menu_present()
    check.equal(details.result, True, details.reason)

@then('verify color of emoji')
def step_impl(neo_in_class):
    details = neo_in_class.get_selected_emoji_color('rgba(51, 51, 51, 1)')
    check.equal(details.result, True, details.reason)

