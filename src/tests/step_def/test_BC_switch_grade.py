from pytest_bdd import scenarios, given, then, when
from pytest import fixture
from pages.android.trialclass_android import TrailClassAndroid, TrailClassFuturePaid
from pages.android.masterclass import MasterClassFuturePaid

feature_file_name = 'Parity user support'

scenarios('../features/' + feature_file_name + '.feature')


@fixture
def trial_class_future(driver):
    trial_class_future = TrailClassFuturePaid(driver)
    yield trial_class_future


@fixture
def trial_class(driver):
    trial_class = TrailClassAndroid(driver)
    yield trial_class


@fixture
def m_class_future(driver):
    m_class_future = MasterClassFuturePaid(driver)
    yield m_class_future


@given("verify Byju's Classes subscribed user is logged in")
def step_impl(login):
    login.set_user_profile(user_profile='user_1', sub_profile='profile_2').verify_home_screen()


@given("verify Byju's Classes expired user is logged in")
def step_impl(login):
    login.set_user_profile(user_profile='user_1', sub_profile='profile_2').verify_home_screen()
    login.switch_grade(grade=8)
    assert login.subscription_expired()


@given("Verify that user selects the future subscribed grade")
@when("Verify that user selects the future subscribed grade")
def step_impl(login):
    login.switch_grade(grade=10)


@then("Verify that Free trail and master classes should be displayed in recommended section")
@then("Parity user with Expired PS can access Free trail and masterclass in future paid cohort")
def step_impl(m_class_future, trial_class_future):
    assert m_class_future.is_master_class_available()
    assert trial_class_future.is_trial_class_available()


@then("verify that user should be able to book free trail and masterclasses")
def step_impl(m_class, m_class_future, trial_class_future, trial_class):
    trial_class_future.book_trial_class()
    m_class.book_special_master_class()
    assert trial_class.is_trial_class_booked()
    assert m_class_future.is_master_class_booked()

