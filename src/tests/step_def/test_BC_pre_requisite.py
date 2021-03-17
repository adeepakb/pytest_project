from pytest import fixture
from pytest_bdd import scenarios, then

from utilities.staging_tllms import Stagingtllms

feature_file_name = 'Pre requisites and its resource type'

scenarios('../features/' + feature_file_name + '.feature')


@fixture
def tllms(driver):
    staging = Stagingtllms(driver)
    yield staging


@then('verify the completed session card with all details')
def step_impl(ssn_req):
    assert ssn_req.verify_session_card_details()


@then('verify the up next session card with all details')
def step_impl(ssn_req):
    ssn_req.click_app_back_btn()
    assert ssn_req.verify_session_card_details()


@then('verify the future session card with all details')
def step_impl(ssn_req, std_board):
    std_board.refresh()
    ssn_req.future_card()
    assert ssn_req.verify_session_card_details(session='future')


@then('verify pre requisite card details')
def step_impl(ssn_req):
    assert ssn_req.verify_pre_requisite_details()


@then('verify app home is displayed')
def step_impl(ssn_req):
    assert ssn_req.verify_app_home_screen()


@then('click on get help button and verify that user navigates to get help screen')
def step_impl(std_board):
    assert std_board.is_live_chat_loaded()
