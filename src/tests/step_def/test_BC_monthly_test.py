from pytest_bdd import scenarios, given, when, then
from constants.platform import Platform
from utilities.staging_tllms import Stagingtllms
from pages.factory.monthly_test import MonthlyTestFactory
from pytest import fixture

from utilities.staging_tutor_plus import StagingTutorPlus

feature_file_name = 'Monthly Test'

scenarios('../features/' + feature_file_name + '.feature')


@fixture
def m_test(request, driver):
    platform_list = request.config.getoption("platform")
    if Platform.ANDROID.name.lower() == platform_list[-1].lower():
        std_board = MonthlyTestFactory().get_page(driver, Platform.ANDROID.value)
        yield std_board
    else:
        raise NotImplementedError()


@fixture
def staging_tutor_plus(driver):
    stp = StagingTutorPlus(driver)
    yield stp


@given("The session should be converted to a monthly test")
def step_impl(m_test, staging_tutor_plus):
    staging_tutor_plus.set_user().convert_video_session()


@given("login as user with monthly test scheduled")
def step_impl(login):
    login.toggle_wifi_connection('on')
    login.set_user_profile(user_profile='user_1', sub_profile='profile_1').verify_user_profile()
    login.click_on_premium_school()


@then("Verify that the title of the test(unit test/monthly test) should be present")
def step_impl(m_test):
    assert m_test.verify_session_card_details(detail="subject title"), "The title of the test is not as expected."


@then("verify the date and time format")
def step_impl(m_test):
    assert m_test.verify_session_card_details(detail="session time"), "The date and time format is not as expected."


@when("Verify that the test session card should be present")
def step_impl(m_test):
    assert m_test.is_test_card_displayed(), "Test card might not be displayed."


@then("verify that the session topic should be present")
def step_impl(m_test):
    assert m_test.verify_session_card_details(detail="topic name"), "Session topic name might not be displayed."


@then("verify that the test icon should be present")
def step_impl(m_test):
    assert m_test.verify_session_card_details(detail="test icon"), "Session test icon might not be displayed."


@then('verify that the text "Good luck for the test" should be present')
def step_impl(m_test):
    assert m_test.verify_session_card_details(detail="wish text"), "Session wish message might not be displayed."


@then('verify that the "Start" button should be present')
def step_impl(m_test):
    assert m_test.verify_session_card_details(detail="start test button"), \
        "Session 'Start Test' button might not be displayed."


@given('The session should be converted to a unit test')
def step_impl(m_test):
    print('deepak')