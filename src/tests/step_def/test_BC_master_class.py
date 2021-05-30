import pytest
from pytest_bdd import scenarios, given, when, then
from constants.platform import Platform
from utilities.staging_tllms import Stagingtllms
from pytest import fixture
feature_file_name = 'MasterClass'

scenarios('../features/' + feature_file_name + '.feature')


@fixture
def tllms(driver):
    staging = Stagingtllms(driver)
    yield staging


@given('verify profile for masterclass booking')
def step_impl(login):
    login.toggle_wifi_connection('on')
    login.driver.close_app()
    login.driver.activate_app(login.driver.desired_capabilities.get("appPackage"))
    login.set_user_profile(user_profile='user_2').verify_user_profile()
    login.click_on_premium_school()
    login.implicit_wait_for(30)


@given('verify profile for unscheduled masterclass')
def step_impl(login):
    login.toggle_wifi_connection('on')
    login.set_user_profile(user_profile='user_2', sub_profile='profile_3').verify_user_profile()
    login.click_on_premium_school()
    login.implicit_wait_for(15)


@given('verify profile for booking masterclass and validation')
def step_impl(login):
    login.toggle_wifi_connection('on')
    login.set_user_profile(user_profile='user_2', sub_profile='profile_3').verify_home_screen()
    login.click_on_premium_school()
    login.implicit_wait_for(15)


@given('verify master class is booked for the current day and is not completed')
def step_impl(m_class):
    assert m_class.is_master_class_available()


@when('verify master class are scheduled')
def step_impl(m_class):
    assert m_class.is_rc_session_card_displayed(), "'Master Class' sessions might not be loaded or scheduled."


@then('verify the display of master class in "Recommended Classes" section')
def step_impl(m_class):
    assert m_class.is_sessions_under_rc_displayed()


@then('verify details of master class session card')
def step_impl(m_class):
    assert m_class.verify_rc_session_card_details()


@then('verify that "Recommended Classes" section should display below three cards with see all CTA')
def step_impl(m_class):
    sessions_displayed = m_class.is_all_rc_sessions_displayed()
    see_more_less_option_displayed = m_class.is_see_all_link_displayed()
    assert sessions_displayed and see_more_less_option_displayed


@when('verify the display of regular class in "Up Next" section')
@then('verify the display of regular class in "Up Next" section')
def step_impl(m_class):
    assert m_class.is_regular_session_displayed()


@when('verify that master classes are not booked')
def step_impl(m_class):
    assert m_class.is_master_class_booked() is False


@when('verify more than one master classes are available')
def step_impl(m_class):
    assert m_class.is_all_rc_sessions_displayed()


@when('verify one masterclass is booked')
def step_impl(m_class, db):
    m_class.book_master_class(db=db)


@then('verify "See all" or "See less" option is displayed')
def step_impl(m_class):
    assert m_class.is_see_all_link_displayed()


@then('verify workshop tag is displayed on the available masterclasses')
def step_impl(m_class):
    assert m_class.is_all_workshop_tag_displayed()


@when('user taps on see all option')
def step_impl(m_class):
    m_class.click_option_see_more()


@when('user taps on see less option')
def step_impl(m_class):
    m_class.click_option_see_more(text='see less')


@then('verify user is able to scroll')
def step_impl(m_class):
    assert m_class.reset_view()


@then("verify the display of topic name")
def step_impl(m_class):
    assert m_class.verify_session_details('topic_name')


@then("verify display of slots")
def step_impl(m_class):
    assert m_class.verify_session_details('slots')


@then("verify the display Book button")
def step_impl(m_class):
    assert m_class.verify_session_details('book_button')


@when('tap on master class session card')
@then('tap on master class session card')
def step_impl(m_class):
    m_class.tap_on_master_card()


@then('try to book a master class session')
def step_impl(m_class, db):
    db.msg_status = m_class.book_offline(db=db)


@then('verify the error toast message is displayed')
def step_impl(db):
    assert db.msg_status, "error message is not displayed or its content might be changed."


@when('verify hidden upcoming sessions are displayed')
def step_impl(m_class):
    assert m_class.is_upcoming_regular_cards_displayed()


@then('verify that session list should collapse and shows fewer session')
def step_impl(m_class):
    assert m_class.is_upcoming_regular_cards_displayed(view='collapse')


@then('verify user should be able scroll to view all upcoming sessions')
def step_impl(m_class):
    assert m_class.is_regular_classes_scrollable()


@when('verify and add slot for master class booking')
def step_impl(tllms, std_board):
    tllms.verify_and_add_slot(cohort="29", course_tag="masterclass")
    std_board.refresh()


@when('add slot for master class booking post booking time')
def step_impl(tllms, std_board):
    tllms.verify_and_add_slot(cohort="29", course_tag="masterclass", minutes=2)
    std_board.refresh()


@then('book master class and verify details in booking and booked successful screen')
def step_impl(m_class, db):
    session_booked = m_class.book_master_class(validate=True, db=db)
    if session_booked is None:
        pytest.skip("Session is already booked!")
    assert session_booked is True


@then('verify masterclass it is listed in session list as per schedule date and time')
def step_impl(m_class, db):
    assert m_class.is_master_class_sorted(db)


@then('verify filling fast label is displayed')
def step_impl(m_class):
    assert m_class.verify_filling_fast_label()


@when('"Join Now" button is enabled before 30 minutes of the session')
def step_impl(m_class):
    btn = m_class.get_master_class_join_now_button()
    assert btn is not None and btn.is_displayed()


@then('verify that user is able to join the session')
def step_impl(m_class):
    m_class.join_master_class_session()


@then('verify that user is able to join the session from session details screen')
def step_impl(m_class):
    m_class.join_master_class_session('details_screen')


@when('verify that the session has crossed the booking time')
def step_impl(m_class):
    assert m_class.skip_the_session_booking_time()


@then('verify error message is displayed when user tries to book a session')
def step_impl(m_class, db):
    message = m_class.book_master_class(new_session=True, db=db)
    assert "All slots are booked for this session. Please try booking another" in message


@when('verify last master class session is ended but not rated')
def step_impl(m_class):
    m_class.end_master_class_session()


@then('verify completed master class should be displayed in "Completed" tab')
def step_impl(m_class):
    m_class.is_completed_mc_session_displayed('completed')


@when('all requisites are attached to booked masterclass session')
def step_impl(m_class):
    m_class.attach_requisite()


@then('verify completed masterclass session is displayed under both "For you" and "Completed" tab')
def step_impl(m_class):
    m_class.is_completed_mc_session_displayed('for you')
    m_class.is_completed_mc_session_displayed('completed')


@then('verify filling fast label should not be displayed on the booked masterclass session')
def step_impl(m_class):
    assert m_class.verify_filling_fast_label(section='regular') is False
