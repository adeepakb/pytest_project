from pytest_bdd import scenarios, given, then, when, parsers
from pytest import fixture
from constants.platform import Platform
from pom_pages.android_pages.homepage import HomePage
from utilities.mentor_session import MentorSession
from pom_pages.android_pages.session_popup import SessionAlert
from utilities.staging_tlms import Stagingtlms
from pom_pages.factory.login import LoginFactory
from pom_pages.factory.ps_home_screen import PSHomescreenFactory
from pom_pages.factory.rate_session import RateSession

scenarios('../features/Rate Session screen - Post session end.feature')


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
def dashboard(request, driver):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        dashboard = RateSession().get_page(driver, Platform.ANDROID.value)
        yield dashboard
    elif Platform.WEB.name in platform_list:
        dashboard = RateSession().get_page(driver, Platform.WEB.value)
        yield dashboard


@fixture()
def home_screen(request, driver):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        home_screen = PSHomescreenFactory().get_page(driver, Platform.ANDROID.value)
        yield home_screen
    elif Platform.WEB.name in platform_list:
        home_screen = PSHomescreenFactory().get_page(driver, Platform.WEB.value)
        yield home_screen

@fixture
def mentor_session(driver):
    mentor_session = MentorSession(driver)
    yield mentor_session


@given(parsers.parse('tap on "{text}"'))
def navigate_to_live_classes(dashboard, text):
    dashboard.click_link(text)


@given("launch the app online and navigate to home screen")
def navigate_to_one_to_many_and_mega_user(driver):
    HomePage(driver).navigate_to_one_to_many_and_mega_user(driver)


@when("tap on premium school card")
def tap_on_premium_card(login_in):
    login_in.click_on_premium_school()


@when("navigate to one to mega homescreen")
def navigate_to_one_to_mega_homescreen(login_in):
    login_in.select_premium_school()


@then(parsers.parse('tap on "{text}" tab'))
def select_tab(dashboard, text):
    dashboard.tap_on_tab(text)


@when("Verify user has completed atleast a session")
def verify_session_completed(dashboard):
    global index
    index = dashboard.find_completed_notrated_session()


@then(parsers.parse('verify "{text}" hyperlink shown on the completed session cards'))
def verify_rate_session(dashboard, text):
    dashboard.verify_rate_session_link_is_present(text)


@then(parsers.parse('tap on "{text}" button'))
def tap_button(login_in, text):
    button_status = login_in.button_click(text)
    assert button_status is True, "Unable to find {text} button"


@then('tap on Okay button')
def tap_on_okay_button(dashboard):
    dashboard.tap_on_okay_button()


@then(parsers.parse('verify "{text}" button is displayed'))
def verify_button(dashboard, text):
    assert dashboard.verify_button(text),"button is not displayed"


# @then('tap on "Join Now" button')
# def tap_on_join_now(dashboard):
#     dashboard.tap_on_join_now()


@then(parsers.parse('verify "{text}" text is displayed'))
def verify_button_a(dashboard, text):
    verify_button(dashboard, text)


@then(parsers.parse('tap of rating option "{index}"'))
def tap_session_star(dashboard, index):
    dashboard.tap_on_star(int(index))


@then("tap on each star and verify user is able to select the stars")
def tap_session_star(dashboard):
    dashboard.tap_on_each_star_and_verify()


@then("deselect the selected stars and verify user is able to deselect the selected stars")
def verify_stars(dashboard):
    dashboard.deselect_selected_stars_and_verify()


@then("verify session details card is shown")
def verify_session_details(driver):
    session_pop = SessionAlert(driver)
    global details_dict
    details_dict = session_pop.verify_session_card_details_loaded()


@then(parsers.parse('verify text "{text}" is present'))
@then(parsers.parse('verify text "{text}" on Rate Session card'))
def verify_text(dashboard, text):
    is_present = dashboard.text_match(text)
    assert is_present is True, "%s is not present" %text


@then(parsers.parse('verify feedback option "{index}"- "{text}" with a checkbox is present'))
def verify_text(dashboard, text, index):
    dashboard.verify_feedback_and_checkbox_present(text, index)


@then(parsers.parse('verify the badge text "{text}" should be shown'))
def verify_badge_text(dashboard, text):
    verify_button(dashboard, text)


@given(parsers.parse('post-requisite "{assessment_name}" should be tagged for the particular classroom session'))
def attach_post_requisite(home_screen,driver, assessment_name):
    home_screen.attach_post_requisite_with_assessement(driver,assessment_name)


@given('detach post requisite for latest session')
def detach_requisite(home_screen,driver):
    home_screen.detach_post_requisite(driver)


@then(parsers.parse('verify the  text completed should be in green colour RGB value "{color_code}"'))
def verify_text_color(dashboard, color_code):
    dashboard.verify_color_of_completed_status(color_code)


@then("tap on Rate Session button")
def tap_rate_session_button(dashboard):
    dashboard.tap_rate_session_button()


@then(parsers.parse('verify text "{text}" at the top'))
def verify_button_a(dashboard, text):
    verify_button(dashboard, text)


@then("verify all Rate your session card details are displayed")
def verify_rate_session_card(dashboard):
    dashboard.verify_rate_session_details(details_dict)


@then("Verify Cancel button")
def verify_rate_session_cancel_button(dashboard):
    assert dashboard.verify_rate_session_close_button(),"Cancel button is not present"


@then("tap on close button")
def tap_rate_session_close_button(dashboard):
    dashboard.tap_rate_session_close_button()


@then("tap on device back button")
def tap_device_back(dashboard):
    dashboard.click_back()


@then("tap on back navigation icon")
def tap_device_back(dashboard):
    dashboard.back_navigation()


@then(parsers.parse('verify "{text}" button should be disabled state before selecting any stars'))
def verify_submit_button_disabled(dashboard, text):
    dashboard.verify_submit_button_enabled_or_not(text, False)


@then("tap on a star")
def tap_on_star(dashboard):
    dashboard.tap_on_star(1)


@then(parsers.parse('verify "{text}" button is enabled'))
def verify_submit_button_enabled(dashboard, text):
    dashboard.verify_submit_button_enabled_or_not(text, True)


@then("tap on Submit button")
def tap_on_submit_button(dashboard):
    dashboard.tap_on_submit_button()


@then(parsers.parse('switch "{text}" the device data'))
@when(parsers.parse('switch "{text}" the device data'))
def switch_off_data(login_in, text):
    login_in.toggle_wifi_connection(text)


@then(parsers.parse('verify offline message "{text}" text is shown'))
def verify_button_a(dashboard, text):
    verify_button(dashboard, text)


@then("tap on any previous session card")
def tap_on_any_session_card(login_in):
    login_in.click_on_session_card(1)


@then(parsers.parse('verify text "{text}" with icon'))
def verify_text_and_icon(dashboard, text):
    dashboard.text_match(text)
    assert dashboard.is_data_off_icon_displayed() is True, "Icon is not present"


@then('tap on session card')
def tap_on_first_session_card(dashboard):
    dashboard.tap_on_first_session_card()


@then(parsers.parse('verify user rating "{rating}" is reflected on Session details screen'))
def verify_rating_on_session_details_screen(dashboard, rating):
    dashboard.verify_rating_on_session_details_screen(rating)


@then(parsers.parse('verify in For you tab rated count "{rating}" is displayed'))
def verify_rating_on_session_card(dashboard, rating):
    dashboard.verify_rating_on_session_card(0, rating)


@then(parsers.parse('verify Rate Session hyperlink  text should not be shown on the  rated  session card'))
def verify_rate_session_link_is_not_present(dashboard):
    dashboard.verify_rate_session_link_is_not_present(index)


@then("tap on back navigation icon")
def tap_back_navigation(dashboard):
    dashboard.back_navigation()


@then("verify user is in premium school-home screen")
def verify_dashboard(dashboard):
    dashboard.text_match("Premium School")
    dashboard.text_match("For you")
    dashboard.text_match("Completed sessions")


@then(parsers.parse('tap on "{text}" button'))
def tap_button(login_in, text):
    button_status = login_in.button_click(text)
    assert button_status is True, f"Unable to find {text} button"


@then(
    "tap on each star and verify feedback options will come up and verify able to select/deselect the feedback options")
def verify_feedback_options(dashboard):
    dashboard.tap_on_each_star_and_verify_feedback()


@then("select a feedback")
def select_feedback(dashboard):
    dashboard.select_any_feedback()


@given("reset student session and start session")
def reset_session(driver, mentor_session):
    Stagingtlms(driver).reset_session('secondary')
    mentor_session.start_tutor_session('secondary')


@then('tutor should end the session')
def tutor_taps_on_end_session(mentor_session):
    mentor_session.wait_for_reset_buffer_time_to_complete()
    mentor_session.tutor_end_session()
