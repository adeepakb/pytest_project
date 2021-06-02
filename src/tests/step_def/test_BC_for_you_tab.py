from pytest import fixture
from pytest_bdd import scenarios, given, when, then
from utilities.staging_tllms import Stagingtllms
import pytest_check as check

feature_file_name = 'For you Tab - Upcoming sessions'

scenarios('../features/' + feature_file_name + '.feature')


@fixture
def tllms(driver):
    staging_tllms = Stagingtllms(driver)
    yield staging_tllms


@given('delete requisite attachment')
def detach_requisite_attachment(std_board, tllms, db):
    tllms.detach_requisite_attachment(user_profile=db.user_profile)


@given('verify that in "For you" tab last completed session should not be displayed')
def step_impl(std_board):
    detail = std_board.is_completed_session_displayed()
    check.equal(detail.result, False, detail.reason)


@then('verify that the "For You" tab will contain the next 6 (14 for 11-12th) upcoming sessions for the user')
def is_all_sessions_displayed(std_board):
    detail = std_board.is_all_sessions_displayed()
    check.equal(detail.result, True, detail.reason)


@then('verify that rate now the card is displayed')
def is_rate_now_card_displayed(std_board):
    detail = std_board.is_rate_now_card_displayed()
    check.equal(detail.result, True, detail.reason)


@then('verify for completed session rated count is displayed')
def is_rated_count_displayed(std_board):
    detail = std_board.is_rated_count_displayed()
    check.equal(detail.result, True, detail.reason)


@then('verify date, subject name and completed text should be displayed')
@when('verify date, subject name and completed text should be displayed')
def is_pr_details_displayed(std_board):
    detail = std_board.is_pr_details_displayed()
    check.equal(detail.result, True, detail.reason)


@then('verify that the last completed session should be displayed in the "Completed session" tab')
def step_impl(std_board):
    detail = std_board.is_completed_session_displayed()
    check.equal(detail.result, True, detail.reason)
