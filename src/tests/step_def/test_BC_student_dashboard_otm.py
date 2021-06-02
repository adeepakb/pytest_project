from pytest import fixture
from pytest_bdd import scenarios, when, then, parsers

from utilities.staging_tllms import Stagingtllms
import pytest_check as check

feature_file_name = 'Student Dashboard'

scenarios('../features/' + feature_file_name + '.feature')


@fixture
def tllms(driver):
    staging_tllms = Stagingtllms(driver)
    yield staging_tllms


@when('on home screen tap on premium school card')
def tap_on_premium_school(login):
    login.click_on_premium_school()


@when("verify future session cards are displayed under 'For you' tab")
def verify_future_card(std_board):
    session = std_board.get_session()
    check.equal(session, None, "future session cards are displayed under 'For you' tab")


@when('verify join now button is displayed on ongoing sessions')
def verify_join_now_button(std_board):
    details = std_board.is_join_now_btn_displayed()
    check.equal(details.result, True, details.reason)


@then('verify okay button is present on offline bottom sheet dialog')
def verify_button_bottom_sheet(std_board):
    details = std_board.bottom_sheet_okay_btn(verify=True)
    check.equal(details.result, True, details.reason)


@then(parsers.re('tap on (?P<button>(?i:okay|join|retry))(?:.*button.*|button.*)'))
def tap_on_button(std_board, button):
    std_board.login.implicit_wait_for(0)
    std_board.click_on_button(button)
    std_board.login.implicit_wait_for(15)


@then('verify offline bottom sheet dialog is dismissed')
def verify_bottom_sheet(std_board):
    details = std_board.is_bottom_sheet_displayed()
    check.equal(details.result, False, details.reason)


@then('verify session related details should be loaded on the screen')
def verify_session_details(std_board):
    details = std_board.is_session_details_displayed()
    check.equal(details.result, True, details.reason)


@then('verify and complete the assessment')
def step_impl(std_board):
    details = std_board.complete_assessment()
    check.equal(details.result, True, details.reason)


@then('verify a test card is shown in the session detail screen')
def step_impl(std_board):
    details =  std_board.verify_and_start_assessment()
    check.equal(details.result, True, details.reason)
