from pytest_bdd import scenarios, given, when, then

feature_file_name = 'For you Tab - Upcoming sessions'

scenarios('../features/' + feature_file_name + '.feature')


@given('delete requisite attachment')
def step_impl(tllms):
    tllms.detach_requisite_attachment()


@then('verify that the "For You" tab will contain the next 6 (14 for 11-12th) upcoming sessions for the user')
def step_impl(std_board):
    assert std_board.is_all_sessions_displayed()


@then('verify that rate now the card is displayed')
def step_impl(std_board):
    assert std_board.is_rate_now_card_displayed()


@then('verify for completed session rated count is displayed')
def step_impl(std_board):
    assert std_board.is_rated_count_displayed()


@when('verify date, subject name and completed text should be displayed')
def step_impl(std_board):
    assert std_board.is_pr_details_displayed()


@then('verify date, subject name and completed text should be displayed')
def step_impl(std_board):
    assert std_board.is_pr_details_displayed()
