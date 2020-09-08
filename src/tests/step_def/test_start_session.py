from pytest_bdd import scenarios, given, then, when, parsers
from pytest import fixture
from POM_Pages.application_login import Login
from POM_Pages.student_session import StudentSession
from POM_Pages.session_popup import SessionAlert
from POM_Pages.homepage import HomePage
from POM_Pages.start_session import StartSession

scenarios('../features/Start Session.feature')


@fixture
def login_in(browser):
    login_in = Login(browser)
    yield login_in


@fixture
def start_session(browser):
    start_session = StartSession(browser)
    yield start_session


@given("navigate to home page and verify student profile")
def verify_student_session(browser):
    HomePage(browser).navigate_to_one_to_many_user(browser)


@when("tap on premium card")
def tap_on_premium_card(login_in):
    login_in.click_on_premium_school()


@then("user taps on upcoming session")
def tap_on_premium_card(start_session, browser):
    StudentSession(browser).download_materials_for_session()
    StudentSession(browser).cancel_join_session_dialog()
    start_session.find_up_next_session()


@then(parsers.parse('verify that current upcoming course has "{text}" button'))
def verify_text(login_in, text):
    login_in.is_button_displayed(text)


@then(parsers.parse('verify "{text}" text is displayed'))
def verify_text(login_in, text):
    login_in.text_match(text)


@then("verify that back arrow button on top left hand side of the screen")
def tap_on_premium_card(start_session):
    start_session.is_back_arrow_button_displayed()


@then("verify session details card is shown")
def verify_session_details(browser):
    global details_dict
    details_dict = SessionAlert(browser).verify_session_card_details_loaded()


@then("click on device back button")
def click_device_back(start_session):
    start_session.click_device_back()


@then("click on back arrow button")
def click_back_arrow_button(start_session):
    start_session.click_back_arrow_button()


@then("user should land on student dashboard screen")
def tap_on_premium_card(login_in):
    login_in.text_match("Classroom")
