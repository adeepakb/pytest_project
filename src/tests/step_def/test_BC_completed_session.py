from pytest import fixture
from pytest_bdd import scenarios, when, then
import pytest_check as check

from utilities.staging_tllms import Stagingtllms

feature_file_name = "Completed Sessions"

scenarios('../features/' + feature_file_name + '.feature')


@fixture
def tllms(driver):
    staging = Stagingtllms(driver)
    yield staging


@then('verify that recently completed session should be shown first in order')
def step_impl(std_board):
    detail = std_board.is_completed_sessions_sorted()
    check.equal(detail.result, True, detail.reason)


@when('tap on app back or device back button')
def tap_on_app_back(std_board):
    std_board.click_app_back_btn()


@then('verify that user navigates to premium school home page')
def step_impl(std_board):
    detail = std_board.is_premium_school_homepage_displayed()
    check.equal(detail.result, True, detail.reason)
