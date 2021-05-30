import pytest
from pytest_bdd import scenarios, given, then, when
from pytest import fixture
from pages.android.trialclass_android import TrailClassFuturePaid, TrailClassAndroid
from pages.android.masterclass import MasterClass, MasterClassFuturePaid
from utilities.staging_tllms import Stagingtllms
from constants.load_json import get_data

feature_file_name = 'Home Screen'

scenarios('../features/' + feature_file_name + '.feature')


@fixture
def tllms(driver):
    tllms = Stagingtllms(driver)
    yield tllms


@fixture
def trail_class_fp(driver):
    tc = TrailClassFuturePaid(driver)
    yield tc


@fixture
def trial_class(driver):
    trial_class = TrailClassAndroid(driver)
    yield trial_class


@fixture
def m_class_fp(driver):
    mc = MasterClassFuturePaid(driver)
    yield mc


@fixture
def m_class(driver):
    mc = MasterClass(driver)
    yield mc


@given("login as a free user")
def step_impl(login):
    login.set_user_profile(user_profile='user_2', sub_profile='profile_6').verify_home_screen()
    login.switch_grade(grade=8)
    login.click_on_premium_school()


@given("free trial classes should not be expired")
def step_impl(login, trial_class):
    if trial_class.is_free_trail_expired():
        pid = get_data("../../config/login_data.json", "login_details_3", "user_1")["profile_3"]["premium_id"]
        status = trial_class.delete_completed_sessions_api(premium_id=pid)
        assert status == 200, "delete completed free trail class was not successful."
        login.clear_app_from_recents()
    pass


@given("verify Byju's Classes subscribed user is logged in")
def step_impl(login):
    login.set_user_profile(user_profile='user_2', sub_profile='profile_4').verify_home_screen()
    login.switch_grade(grade=8)


@given("verify parity user is logged in")
def step_impl(login):
    login.set_user_profile(user_profile='user_1', sub_profile='profile_3').verify_home_screen()
    login.switch_grade(grade=8)


@given("reset app and login as parity user")
def step_impl(login):
    login.execute_command('adb shell pm clear %s' % login.package_name)
    login.execute_command('adb shell monkey -p %s -c android.intent.category.LAUNCHER 1' % login.package_name)
    login.set_user_profile(user_profile='user_2', sub_profile='profile_6').login_with_otp(bottom_sheet_dismiss=False)
    login.on_boarding_activity()


@given("verify and add slot for masterclass booking")
def step_impl(tllms, std_board):
    tllms.session_relaunch()
    tllms.verify_and_add_slot(cohort="14", course_tag="masterclass", minutes=4)
    std_board.refresh()


@given("verify and add slot for free trial booking")
def step_impl(tllms, std_board):
    tllms.verify_and_add_slot(cohort="14", course_tag="free_trial")
    std_board.refresh()


@when("verify master class are scheduled")
def step_impl(m_class):
    assert m_class.is_rc_session_card_displayed(), "'Master Class' sessions might not be loaded or scheduled."


@when("click on book button and select random date and click on cancel button")
def step_impl(m_class):
    m_class.select_random_masterclass_date()


@then("verify masterclass is not booked and user is landed on dashboard screen")
def step_impl(m_class):
    with pytest.raises(AssertionError):
        m_class.verify_booking_screen(booking_success_activity="BookingSuccessActivity")
    assert m_class.wait_activity("OneToMegaHomeActivity")


@when("click on book button and select random date and click book and confirm button")
def step_impl(m_class):
    m_class.select_random_masterclass_date(action="book")


@then("verify successfully booked screen should be displayed")
def step_impl(m_class):
    m_class.verify_booking_screen(booking_success_activity="BookingSuccessActivity")


@then("verify details of class started bottom sheet")
def step_impl(login):
    assert login.verify_bottom_sheet_details(), "class started bottom sheet might not be displayed."


@when("verify that user should be able to book free trail class")
def step_impl(trail_class_fp, trial_class):
    trail_class_fp.book_trial_class()
    assert trial_class.is_trial_class_booked()


@when("verify that user should be able to book masterclasses")
def step_impl(m_class, m_class_fp):
    m_class.book_special_master_class()
    assert m_class_fp.is_master_class_booked()


@then("join the free trial class from the home screen")
def step_impl(login):
    login.join_the_class_bottom_sheet()
