from pytest import fixture
from pytest_bdd import scenarios, then
import pytest_check as check

from utilities.staging_tllms import Stagingtllms

feature_file_name = 'Pre requisites and its resource type'

scenarios('../features/' + feature_file_name + '.feature')


@fixture
def tllms(driver):
    staging = Stagingtllms(driver)
    yield staging


@then('verify the completed session card with all details')
def step_impl(ssn_req):
    details = ssn_req.verify_session_card_details()
    check.equal(details.result, True, details.reason)


@then('verify the up next session card with all details')
def step_impl(ssn_req):
    ssn_req.click_app_back_btn()
    details = ssn_req.verify_session_card_details()
    check.equal(details.result, True, details.reason)


@then('verify the future session card with all details')
def step_impl(ssn_req, std_board):
    std_board.refresh()
    ssn_req.future_card()
    details = ssn_req.verify_session_card_details(session='future')
    check.equal(details.result, True, details.reason)


@then('verify pre requisite card details')
def step_impl(ssn_req):
    details = ssn_req.verify_pre_requisite_details()
    check.equal(details.result, True, details.reason)


@then('verify app home is displayed')
def step_impl(ssn_req):
    details = ssn_req.verify_app_home_screen()
    check.equal(details.result, True, details.reason)


@then('click on get help button and verify that user navigates to get help screen')
def step_impl(std_board):
    details = std_board.is_live_chat_loaded()
    check.equal(details.result, True, details.reason)
