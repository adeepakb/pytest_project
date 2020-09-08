from pytest_bdd import scenarios, given, then, when, parsers
from pytest import fixture
from POM_Pages.application_login import Login
from POM_Pages.student_session import StudentSession
from POM_Pages.homepage import HomePage

scenarios('../features/Home Screen.feature')


@fixture
def login_in(browser):
    login_in = Login(browser)
    yield login_in


@given("user logged in and is having one to many and one to mega subscription")
def navigate_to_one_to_many_and_mega_user(browser):
    HomePage(browser).navigate_to_one_to_many_and_mega_user(browser)


@given("user logged in and is having only one subscription")
@given("user logged in and is having only one to many subscription")
def navigate_to_one_to_many_user(browser):
    HomePage(browser).navigate_to_one_to_many_user(browser)


@given("user logged in and is having only one to mega subscription")
def login_as_one_mega_user_only(browser):
    HomePage(browser).login_as_one_mega_user_only(browser)


@when("Tap on premium card")
def tap_on_premium_card(login_in, browser):
    login_in.click_on_premium_school()
    StudentSession(browser).download_materials_for_session()
    StudentSession(browser).cancel_join_session_dialog()


@then(parsers.parse('Verify that user land on the "{text}" screen'))
@then(parsers.parse('Verify that the user is navigated to "{text}" session screen'))
@then(parsers.parse('verify that the "{text}" card is present in the home screen'))
def verify_text(login_in, text):
    assert login_in.text_match(text), "%s text is not displayed " % text


@then(parsers.parse('verify "{text}" card is present'))
def verify_text(login_in, text):
    assert login_in.text_match(text), "%s text is not displayed " % text
