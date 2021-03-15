from pytest_bdd import scenarios, when, then
feature_file_name = "Completed Sessions"

scenarios('../features/' + feature_file_name + '.feature')


@then('verify that recently completed session should be shown first in order')
def step_impl(std_board):
    assert std_board.is_completed_sessions_sorted(), "Sessions are not properly sorted."


@when('tap on app back or device back button')
def tap_on_app_back(std_board):
    std_board.click_app_back_btn()


@then('verify that user navigates to premium school home page')
def step_impl(std_board):
    assert std_board.is_premium_school_homepage_displayed(), "home page may not be displayed."
