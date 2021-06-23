from pytest_bdd import scenarios, given, when, then, parsers
from constants.platform import Platform
from pages.factory.ps_home_screen import PSHomescreenFactory
from utilities.staging_tllms import Stagingtllms
from pages.factory.monthly_test import MonthlyTestFactory
from pytest import fixture
import pytest_check as check
import time

from utilities.staging_tutor_plus import StagingTutorPlus
from datetime import datetime as dt, timedelta

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


@fixture
def tllms(driver):
    staging_tllms = Stagingtllms(driver)
    yield staging_tllms


@fixture()
def home_screen(request, driver):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        home_screen = PSHomescreenFactory().get_page(driver, Platform.ANDROID.value)
        yield home_screen
    elif Platform.WEB.name in platform_list:
        home_screen = PSHomescreenFactory().get_page(driver, Platform.WEB.value)
        yield home_screen


@given("The session should be converted to a monthly test")
def step_impl(m_test, staging_tutor_plus, db):
    staging_tutor_plus.set_user().convert_video_session(db=db, subject_topic_name=("", ""))


@given("login as user with not completed assessment")
def step_impl(login):
    login.toggle_wifi_connection('on')
    login.set_user_profile(user_profile='user_1', sub_profile='profile_1').verify_user_profile()


@given("The session should be converted to a unit test")
def step_impl(m_test, staging_tutor_plus, login, db):
    login.toggle_wifi_connection('on')
    db.login_profile = "login_details_3"
    db.user_profile = "user_1"
    db.sub_profile = "profile_1"
    login.set_user_profile(
        login_profile=db.login_profile, user_profile=db.user_profile, sub_profile=db.sub_profile).verify_user_profile()
    login.click_on_premium_school()
    tp_name = m_test.get_up_test_topic_name()
    staging_tutor_plus.set_user().convert_video_session(subject_topic_name=tp_name)


@given("login as user with unit test scheduled")
def step_impl(m_test):
    m_test.driver.launch_app()


@given("The masterclass session should be converted to a monthly test for 3+1 user")
def step_impl(db, login, m_test, staging_tutor_plus):
    login_profile = "login_details_3"
    user_profile = "user_2"
    sub_profile = "profile_5"
    login.set_user_profile(
        login_profile=login_profile, user_profile=user_profile, sub_profile=sub_profile
    ).verify_user_profile()
    login.set_user_profile(user_profile='user_1', sub_profile='profile_1').verify_user_profile()


@given("The session should be converted to a unit test")
def step_impl(m_test, staging_tutor_plus, login, db):
    login.toggle_wifi_connection('on')
    db.login_profile = "login_details_3"
    db.user_profile = "user_1"
    db.sub_profile = "profile_1"
    # login.set_user_profile(
    #     login_profile=db.login_profile, user_profile=db.user_profile, sub_profile=db.sub_profile).verify_user_profile()
    login.click_on_premium_school()
    tp_name = m_test.get_up_test_topic_name()
    staging_tutor_plus.set_user().convert_video_session(subject_topic_name=tp_name, db=db)


@given("login as user with unit test scheduled")
def step_impl(m_test):
    m_test.driver.launch_app()


@given("The masterclass session should be converted to a monthly test for 3+1 user")
def step_impl(db, login, m_test, staging_tutor_plus):
    login_profile = "login_details_3"
    user_profile = "user_2"
    sub_profile = "profile_5"
    login.set_user_profile(
        login_profile=login_profile, user_profile=user_profile, sub_profile=sub_profile
    ).verify_user_profile()
    login.click_on_premium_school()
    m_test.book_master_class(db=db)
    tp_name = m_test.get_up_test_topic_name(session_type="masterclass")
    staging_tutor_plus.set_user(login_profile, user_profile, sub_profile).convert_video_session(
        subject_topic_name=tp_name, assessment_type="monthly test")
    m_test.driver.launch_app()


@given("The session should be converted to a monthly test for ps user 1")
def step_impl(db, login, m_test, staging_tutor_plus):
    login_profile = "login_details_3"
    user_profile = "user_2"
    sub_profile = "profile_1"
    login.set_user_profile(
        login_profile=login_profile, user_profile=user_profile, sub_profile=sub_profile
    ).verify_user_profile()
    login.click_on_premium_school()
    m_test.book_master_class(db=db)
    tp_name = m_test.get_up_test_topic_name(session_type="masterclass")
    staging_tutor_plus.set_user(login_profile, user_profile, sub_profile).convert_video_session(
        subject_topic_name=tp_name, assessment_type="monthly test")
    m_test.driver.launch_app()


@given("The session should be converted to a monthly test with no post requisite for ps user 1")
def step_impl(db, login, m_test, staging_tutor_plus):
    login_profile = "login_details_3"
    user_profile = "user_2"
    sub_profile = "profile_1"
    login.set_user_profile(
        login_profile=login_profile, user_profile=user_profile, sub_profile=sub_profile
    ).verify_user_profile()
    login.click_on_premium_school()
    m_test.book_master_class(db=db)
    tp_name = m_test.get_up_test_topic_name(session_type="masterclass")
    staging_tutor_plus.set_user(login_profile, user_profile, sub_profile).convert_video_session(
        subject_topic_name=tp_name, assessment_type="monthly test")
    m_test.driver.launch_app()


@given("The session should be converted to a monthly test for ps user 1")
def step_impl(db, login, m_test, staging_tutor_plus):
    login_profile = "login_details_3"
    user_profile = "user_2"
    sub_profile = "profile_1"
    login.set_user_profile(
        login_profile=login_profile, user_profile=user_profile, sub_profile=sub_profile
    ).verify_user_profile()
    login.click_on_premium_school()
    m_test.book_master_class(db=db)
    tp_name = m_test.get_up_test_topic_name(session_type="masterclass")
    staging_tutor_plus.set_user(login_profile, user_profile, sub_profile).convert_video_session(
        subject_topic_name=tp_name, assessment_type="monthly test")
    m_test.driver.launch_app()


@given("The session should be converted to a monthly test with no post requisite for ps user 1")
def step_impl(db, login, m_test, staging_tutor_plus):
    login_profile = "login_details_3"
    user_profile = "user_2"
    sub_profile = "profile_1"
    login.set_user_profile(
        login_profile=login_profile, user_profile=user_profile, sub_profile=sub_profile
    ).verify_user_profile()
    login.click_on_premium_school()
    m_test.book_master_class(db=db)
    tp_name = m_test.get_up_test_topic_name(session_type="masterclass")
    staging_tutor_plus.set_user(login_profile, user_profile, sub_profile).convert_video_session(
        subject_topic_name=tp_name, assessment_type="monthly test pre")
    m_test.driver.launch_app()


@given("login as ps user 1 with monthly test scheduled")
def login_ps_user_1(login, m_test):
    login_profile = "login_details_3"
    user_profile = "user_2"
    sub_profile = "profile_1"
    login.set_user_profile(
        login_profile=login_profile, user_profile=user_profile, sub_profile=sub_profile
    ).verify_user_profile()
    # login.click_on_premium_school()
    m_test.driver.launch_app()


# @given("The session should be converted to a monthly test for ps user 2")
# def step_impl(db, login, m_test, staging_tutor_plus):
#     login_profile = "login_details_3"
#     user_profile = "user_2"
#     sub_profile = "profile_4"
#     login.set_user_profile(
#         login_profile=login_profile, user_profile=user_profile, sub_profile=sub_profile
#     ).verify_user_profile()
#     login.click_on_premium_school()
#     m_test.book_master_class(db=db)
#     tp_name = m_test.get_up_test_topic_name(session_type="masterclass")
#     staging_tutor_plus.set_user(login_profile, user_profile, sub_profile).convert_video_session(
#         subject_topic_name=tp_name, assessment_type="monthly test")
#     m_test.driver.launch_app()


@given('Precondition : "send_results_at" is set to the past date')
def step_impl(staging_tutor_plus):
    staging_tutor_plus.modify_test_requisite_assessment(
        channel_id=None, field="result_time", day="yesterday", status="expire",
        grade="8")


@given("login post the \"available_starting\" time")
def step_impl(login, m_test, staging_tutor_plus):
    details = staging_tutor_plus.is_session_started()
    check.equal(details.result, True, details.reason)
    login_ps_user_1(login, m_test)
    m_test.book_master_class(db=db)
    tp_name = m_test.get_up_test_topic_name(session_type="masterclass")
    staging_tutor_plus.set_user(login_profile, user_profile, sub_profile).convert_video_session(
        subject_topic_name=tp_name, assessment_type="monthly test pre")
    m_test.driver.launch_app()


@given("login as ps user 1 with monthly test scheduled")
def login_ps_user_1(login, m_test):
    login_profile = "login_details_3"
    user_profile = "user_2"
    sub_profile = "profile_1"
    login.set_user_profile(
        login_profile=login_profile, user_profile=user_profile, sub_profile=sub_profile
    ).verify_user_profile()
    # login.click_on_premium_school()
    m_test.driver.launch_app()


# @given("The session should be converted to a monthly test for ps user 2")
# def step_impl(db, login, m_test, staging_tutor_plus):
#     login_profile = "login_details_3"
#     user_profile = "user_2"
#     sub_profile = "profile_4"
#     login.set_user_profile(
#         login_profile=login_profile, user_profile=user_profile, sub_profile=sub_profile
#     ).verify_user_profile()
#     login.click_on_premium_school()
#     m_test.book_master_class(db=db)
#     tp_name = m_test.get_up_test_topic_name(session_type="masterclass")
#     staging_tutor_plus.set_user(login_profile, user_profile, sub_profile).convert_video_session(
#         subject_topic_name=tp_name, assessment_type="monthly test")
#     m_test.driver.launch_app()


@given('Precondition : "send_results_at" is set to the past date')
def step_impl(staging_tutor_plus):
    staging_tutor_plus.modify_test_requisite_assessment(
        channel_id=None, field="result_time", day="yesterday", status="expire",
        grade="8")


@given("login post the \"available_starting\" time")
def step_impl(login, m_test, staging_tutor_plus):
    details = staging_tutor_plus.is_session_started()
    check.equal(details.result, True, details.reason)
    login_ps_user_1(login, m_test)


@then("Verify that the title of the test(unit test/monthly test) should be present")
def step_impl(m_test):
    check.equal(m_test.verify_session_details(detail="subject title"), True,
                "The title of the test is not as expected.")


@then("verify the date and time format")
def step_impl(m_test):
    check.equal(m_test.verify_session_details(detail="session"), True,
                "The date and time format of the test is not as expected.")


@when("Verify that the test session card should be present")
def step_impl(m_test):
    details = m_test.is_test_card_displayed()
    check.equal(details.result, True, details.reason)


@then("verify that the session topic should be present")
def step_impl(m_test):
    check.equal(m_test.verify_session_details(detail="topic name"), True, "Session topic name might not be displayed.")


@then("verify that the test icon should be present")
def step_impl(m_test):
    check.equal(m_test.verify_session_details(detail="test icon"), True, "Session test icon might not be displayed.")


@then('verify that the text "Good luck for the test" should be present')
def step_impl(m_test):
    check.equal(m_test.verify_session_details(detail="wish text"), True, "Session wish message might not be displayed.")


@then('Verify that the text "Good luck for your test" should be displayed in details screen')
def step_impl(m_test):
    check.equal(m_test.verify_session_details(detail="wish text", screen="details screen"),
                True, "Session wish message might not be displayed.")


@then('verify that the "Start" button should be present')
def step_impl(m_test):
    check.equal(m_test.verify_session_details(detail="start test button"), True,
                "Session 'Start Test' button might not be displayed.")


@then("verify that the \"Start Test\" button should be present in details screen")
def step_impl(m_test):
    m_test.verify_session_details(detail="start test button", screen="details screen")


@when("the user is in For you Tab")
def step_impl(std_board):
    std_board.ps_home_page_tab(tab_name='For you')


@then("click on \"Start Test\" button and verify user landed on instruction screen")
def step_impl(m_test):
    m_test.start_test(screen="session details")
    m_test.verify_test_instruction_screen()


@then("verify \"Start\" button is displayed on instruction screen")
def step_impl(m_test):
    m_test.verify_test_instruction_screen(detail="start button")


@when("click on test session card")
def step_impl(m_test):
    details = m_test.click_on_test_card()
    check.equal(details.result, True, details.reason)


@when("click on \"Start Test\" button")
def step_impl(m_test):
    m_test.start_test()


@when("verify session details page is displayed")
def step_impl(m_test):
    details = m_test.is_session_details_page_displayed()
    check.equal(details.result, True, details.reason)


@when("user starts assessment and land on final question")
def step_impl(m_test, db):
    m_test.start_assessment_web(db=db)
    details = m_test.verify_last_question(db=db)
    check.equal(details.result, True, details.reason + " Unable to reach last question of assessment.")


@then("Verify the exit assessment button on the final screen")
def step_impl(m_test):
    details = m_test.is_end_finish_button_displayed()
    check.equal(details.result, True, details.reason)


@then("verify that the \"Results\" button should be displayed")
def step_impl(m_test):
    details = m_test.is_result_button_displayed()
    check.equal(details.result, True, details.reason)


@when("quit the assessment in between on app")
@when("press back and land on student dashboard screen")
@then("press back and land on student dashboard screen")
def step_impl(m_test):
    m_test.click_back()
    check.equal(m_test.wait_activity('OneToMegaHomeActivity'), True, "User is not in OneToMegaHomeActivity")


@then("verify that \"Resume\" button is displayed on the screen")
def step_impl(m_test):
    details = m_test.is_resume_button_displayed()
    check.equal(details.result, True, details.reason)


@then("verify elements in assessment screen")
def step_impl(m_test, db):
    details = m_test.verify_web_assessment_screen(db=db)
    check.equal(details.result, True, details.reason)


@when("take the assessment on the web")
def step_impl(m_test, db):
    db.login_profile = "login_details_3"
    db.user_profile = "user_1"
    db.sub_profile = "profile_1"
    m_test.resume_assessment_on_web(db=db)


@then("test status should be in Resume state")
def step_impl(db):
    check.equal(db.resume_btn_displayed, True, "Resume button might not be displayed.")


@then("tap on exit assessment and verify confirmation pop up")
def step_impl(m_test):
    details = m_test.assessment_confirmation_pop_up()
    check.equal(details.result, True, details.reason)


@then("Verify that when the internet is turned off while taking the test assessment")
def step_impl(m_test, db):
    details = m_test.offline_assessment(db=db)
    check.equal(details.result, True, details.reason + " offline assessment was not successful.")


@then("verify that status should be changed to resume")
def step_impl(m_test):
    details = m_test.is_resume_button_displayed()
    check.equal(details.result, True, details.reason + " offline assessment did not convert session to 'Resume' state.")


@when("submit the assessment in offline")
def step_impl(m_test, db):
    m_test.submit_assessment_offline(db=db)


@then("Verify that internet error message is displayed")
def step_impl(m_test):
    details = m_test.is_error_msg_displayed()
    check.equal(details.result, True, details.reason)


@when("expire the test session from the backend")
def step_impl(staging_tutor_plus):
    staging_tutor_plus.modify_test_requisite_assessment(field="end_time", day="today", status="expire", grade="8")


@when("user should not attend the test")
def step_impl(m_test):
    check.equal(m_test.verify_session_details(detail="start test button"), True,
                "Session 'Start Test' button might not be displayed.")


@when("test session should be ended")
def step_impl(m_test):
    check.equal(m_test.verify_session_details(detail="completed status"), True, "Session might not be completed yet.")


@then("verify text \"Test Expired. It was supposed to be taken during session time\" should be displayed")
def step_impl(m_test):
    check.equal(m_test.verify_session_details(detail="completed status"), False, "Session might not be expired.")


@when("verify that student has completed the session")
def step_impl(db, m_test):
    check.equal(m_test.complete_assessment_session(db=db), True, "unable to complete the assessment session.")


@when("verify that session has reached end time")
def step_impl(m_test):
    check.equal(m_test.is_session_end_time_reached(), True, "session might not be ended.")


@then("verify that the session card is moved to completed tab")
def step_impl(m_test):
    details = m_test.is_assessment_displayed_in_completed_tab()
    check.equal(details.result, True, details.reason + " completed session might not be moved to 'Completed' tab.")


@then("verify that \"Start Test\" button should not be enabled for the assessment")
def step_impl(m_test):
    check.equal(m_test.verify_session_details(detail="start test button"), False,
                "Session 'Start Test' button might be displayed.")


@when("Verify that the \"Start Test\" button should be enabled automatically in the session card")
def step_impl(m_test):
    details = m_test.is_start_test_btn_displayed_at_start_time()
    check.equal(details.result, True, details.reason)


@given('give a delay of “120” seconds')
def step_impl(m_test):
    time.sleep(120)


@given("login as user with unit test scheduled")
def step_impl(login):
    login.toggle_wifi_connection('on')
    login.set_user_profile(user_profile='user_1', sub_profile='profile_1').verify_user_profile()


@then('user should not see the assessment session joining pop up')
def step_impl(home_screen):
    assert home_screen.click_on_dissmiss() is False


@when('the user is in For you Tab')
def step_impl(m_test):
    m_test.click_on_for_you_tab()


@then(parsers.parse('Verify that the title of the test should be "{text}"'))
def step_impl(m_test, text):
    title, session_time, session_title = m_test.get_card_detail()
    assert title, text


@then('validate elements of monthly session card')
def step_impl(m_test, staging_tutor_plus):
    m_test.verify_session_details('subject title')
    m_test.verify_session_details('status')
    m_test.verify_session_details('heading')


@then('user should be able to view post requisites')
def step_impl(std_board):
    assert std_board.is_pre_post_requisite_displayed(post=True, session='completed')
    std_board.driver.back()


@then('user is able to do action on post requisites')
def step_impl(std_board):
    std_board.do_action_on_post_requisite()


@when('navigate to the completed tab')
def step_impl(m_test):
    m_test.click_on_completed_tab()


@then(parsers.parse('verify that student has card with "{resume}" assessment'))
def step_impl(std_board, resume):
    assert std_board.verify_rate_join_now(expected=resume.lower())


@when(parsers.parse('click on "{button}" button'))
def step_impl(m_test, button):
    m_test.button_click(button)


@given('login as user with “incompleted assessment”')
def step_impl(login):
    login.toggle_wifi_connection('on')
    login.set_user_profile(user_profile='user_1', sub_profile='profile_1').verify_user_profile()


@given('user has not started the test session')
def step_impl(m_test, **kwargs):
    assert m_test.is_button_displayed_with_text(button_name='Start Test'), " Start Test button not found"


@given(parsers.parse('verify that the text "{button}" button should be present on the card'))
def step_impl(m_test, button):
    m_test.is_button_displayed_with_text(button_name=button)


@given('verify that student can take test from completed tab')
def step_impl(m_test):
    assert m_test.is_status_displayed()


@when('user starts assessment and land on final question')
def step_impl(m_test):
    assert m_test.do_assignment(finish=False)


@when(
    'verify whether there is any interruption when the session has reached end time while student is still taking the assessment')
def step_impl(m_test):
    assert m_test.check_no_interruption_in_assignment() is True


@given("The session should be converted to a monthly test with test end time greater than session end time")
def step_impl(m_test, staging_tutor_plus, db):
    staging_tutor_plus.set_user().convert_video_session(db=db)


@given("The session should be converted to a monthly test with session end time lesser than test end time")
def step_impl(m_test, tllms, staging_tutor_plus, db):
    staging_tutor_plus.set_user().convert_video_session(db=db, assessment_type="monthly test",
                                                        subject_topic_name=("", ""))
    staging_tutor_plus.change_assessment_time(db, minutes_to_add=+2, current=False)


@given("login as user with expired assessment")
def step_impl(login):
    login.toggle_wifi_connection('on')
    login.set_user_profile(user_profile='user_1', sub_profile='profile_1').verify_user_profile()


@given('login as user with "ending assessment time"')
def step_impl(login):
    login.toggle_wifi_connection('on')
    login.set_user_profile(user_profile='user_1', sub_profile='profile_1').verify_user_profile()


@then(parsers.parse('verify that student has test card with "{text}" assessment'))
def step_impl(std_board, text):
    assert std_board.verify_test_status(expected=text.lower()), "expired text was not found on any card"


@given("The session should be converted to a monthly test with test time lesser than current time")
def step_impl(m_test, tllms, staging_tutor_plus, db):
    staging_tutor_plus.set_user().convert_video_session(db=db, assessment_type="monthly test",
                                                        subject_topic_name=("", ""))
    staging_tutor_plus.change_assessment_time(db, minutes_to_add=-2, current=True)


@given("The session should be converted to a monthly test with post requisite")
def step_impl(m_test, staging_tutor_plus, db):
    staging_tutor_plus.set_user().convert_video_session(db=db, subject_topic_name=("", ""), assessment_type="pre-post")


@given("The session should be converted to a monthly test with ending assessment time")
def step_impl(m_test, tllms, staging_tutor_plus, db):
    staging_tutor_plus.set_user().convert_video_session(db=db, assessment_type="monthly test",
                                                        subject_topic_name=("", ""))
    staging_tutor_plus.change_assessment_time(db, minutes_to_add=-2, current=True)
