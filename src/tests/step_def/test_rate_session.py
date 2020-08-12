from pytest_bdd import scenarios, given, then, when, parsers
from pytest import fixture
from src.POM_Pages.application_login import Login
from src.POM_Pages.choose_topic import ChooseTopic
from src.POM_Pages.ratesession import Dashboard
from src.POM_Pages.session_popup import SessionAlert
from src.POM_Pages.student_session import StudentSession

scenarios('../features/rate_session.feature')


@fixture
def login_in(browser):
    login_in = Login(browser)
    yield login_in


@fixture
def dashboard(browser):
    dashboard = Dashboard(browser)
    yield dashboard


@given('Launch the tutor application online')
def launch_app_online():
    pass


@given(parsers.parse('tap on "{text}"'))
def navigate_to_live_classes(dashboard, text):
    dashboard.click_link(text)


@given("navigate to home page and verify student profile")
def verify_student_session(login_in, browser):
    login_in.click_on_premium_school()
    # pop_up_displayed = SessionAlert(browser)
    # pop_up_displayed.cancel_join_session()


@given('Navigate Tutor Home screen')
def navigate_to_home_screen(browser):
    instance = Login(browser)
    instance.allow_deny_permission(['allow', 'allow', 'allow'])
    instance.enter_phone('1111333300')
    instance.button_click('Next')
    instance.enter_password('112233')
    instance.button_click('Next')


@given('navigate to one to many student dashboard screen')
def click_on_session_card_enter():
    pass


@when("Verify user has completed atleast a session")
def verify_session_completed(dashboard):
    global index
    index = dashboard.find_completed_notrated_session()


@then(parsers.parse('verify "{text}" hyperlink shown on the completed session cards'))
def verify_rate_session(dashboard, text):
    dashboard.verify_rate_session_link_is_present(text)


@then(parsers.parse('tap on "{text}" hyperlink'))
@when(parsers.parse('tap on "{text}" hyperlink'))
def tap_rate_session(dashboard, text):
    dashboard.tap_rate_session_link(index)


@then(parsers.parse('verify "{text}" button is displayed'))
def verify_button(dashboard, text):
    dashboard.verify_button(text)


@then(parsers.parse('verify text "{text}"'))
def verify_button_a(dashboard, text):
    verify_button(dashboard, text)


@then("verify session details card is shown")
def verify_session_details(browser):
    session_pop = SessionAlert(browser)
    global details_dict
    details_dict = session_pop.verify_session_card_details_loaded()


@then(parsers.parse('verify text "{text}" on Rate Session card'))
def verify_text(dashboard, text):
    dashboard.text_match(text)


@then(parsers.parse('verify the badge text "{text}" should be shown'))
def verify_badge_text(dashboard, text):
    verify_button(dashboard, text)


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
    dashboard.verify_rate_session_close_button()


@then("tap on close button")
def tap_rate_session_close_button(dashboard):
    dashboard.tap_rate_session_close_button()


@then("tap on device back button")
def tap_device_back(dashboard):
    dashboard.click_back()


@then("tap on back navigation icon")
def tap_device_back(dashboard):
    dashboard.back_navigation()


@then("tap on each star and verify user is able to select the stars")
def tap_session_star(dashboard):
    dashboard.tap_on_each_star_and_verify()


@then("deselect the selected stars and verify user is able to deselect the selected stars")
def verify_stars(dashboard):
    dashboard.deselect_selected_stars_and_verify()


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
def switch_off_data(browser, text):
    instance = Login(browser)
    instance.toggle_wifi_connection(text)


@then(parsers.parse('verify offline message "{text}" text is shown'))
def verify_button_a(dashboard, text):
    verify_button(dashboard, text)


@then("tap on any previous session card")
def tap_on_any_session_card(browser):
    instance = Login(browser)
    instance.click_on_session_card(1)


@then(parsers.parse('verify text "{text}" with icon'))
def verify_text_and_icon(dashboard, text):
    dashboard.text_match(text)
    assert dashboard.is_data_off_icon_displayed() is True, "Icon is not present"


@then(parsers.parse('verify user rating "{rating}" is reflected on Session details screen'))
def verify_rating_on_session_details_screen(dashboard, rating):
    dashboard.verify_rating_on_session_details_screen(rating)


@then(parsers.parse('verify user given rating "{rating}" should be reflecting on the session card'))
def verify_rating_on_session_card(dashboard, rating):
    dashboard.verify_rating_on_session_card(index, rating)


@then(parsers.parse('verify Rate Session hyperlink  text should not be shown on the  rated  session card'))
def verify_rate_session_link_is_not_present(dashboard):
    dashboard.verify_rate_session_link_is_not_present(index)


@then("tap on back navigation icon")
def tap_back_navigation(dashboard):
    dashboard.back_navigation()


@then("Verify user is in dashboard")
def verify_dashboard(dashboard):
    dashboard.text_match("Classroom")


@then(parsers.parse('tap on "{text}" button'))
def tap_button(login_in, text):
    button_status = login_in.button_click(text)
    assert button_status is True, f"Unable to find {text} button"


@then("tap on each star and verify feedback options will come up and verify able to select/deselect the feedback options")
def verify_feedback_options(dashboard):
    dashboard.tap_on_each_star_and_verify_feedback()


@then("select a feedback")
def select_feedback(dashboard):
    dashboard.select_any_feedback()
