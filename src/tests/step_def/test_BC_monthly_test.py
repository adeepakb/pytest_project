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


@fixture
def tllms(driver):
    staging_tllms = Stagingtllms(driver)
    yield staging_tllms


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
    # m_test.book_master_class(db=db)
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
    assert staging_tutor_plus.is_session_started(), "Session is not started or might be ended."
    login_ps_user_1(login, m_test)


@then("Verify that the title of the test(unit test/monthly test) should be present")
def step_impl(m_test):
    assert m_test.verify_session_details(detail="subject title"), "The title of the test is not as expected."


@then("verify the date and time format")
def step_impl(m_test):
    assert m_test.verify_session_details(detail="session time"), "The date and time format is not as expected."


@when("Verify that the test session card should be present")
def step_impl(m_test):
    assert m_test.is_test_card_displayed(), "Test card might not be displayed."


@then("verify that the session topic should be present")
def step_impl(m_test):
    assert m_test.verify_session_details(detail="topic name"), "Session topic name might not be displayed."


@then("verify that the test icon should be present")
def step_impl(m_test):
    assert m_test.verify_session_details(detail="test icon"), "Session test icon might not be displayed."


@then('verify that the text "Good luck for the test" should be present')
def step_impl(m_test):
    assert m_test.verify_session_details(detail="wish text"), "Session wish message might not be displayed."


@then('Verify that the text "Good luck for your test" should be displayed in details screen')
def step_impl(m_test):
    assert m_test.verify_session_details(detail="wish text", screen="details screen"), \
        "Session wish message might not be displayed."


@then('verify that the "Start" button should be present')
def step_impl(m_test):
    assert m_test.verify_session_details(detail="start test button"), \
        "Session 'Start Test' button might not be displayed."


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
    assert m_test.click_on_test_card(), "Unable to find the 'Test' session card"


@when("click on \"Start Test\" button")
def step_impl(m_test):
    m_test.start_test()


@when("verify session details page is displayed")
def step_impl(m_test):
    assert m_test.is_session_details_page_displayed()


@when("user starts assessment and land on final question")
def step_impl(m_test, db):
    m_test.start_assessment_web(db=db)
    assert m_test.verify_last_question(db=db), "Unable to reach last question of assessment."


@then("Verify the exit assessment button on the final screen")
def step_impl(m_test):
    assert m_test.is_end_finish_button_displayed(), \
        "'Exit Assessment' or 'Finish' button might be displayed on the final question screen"


@then("verify that the \"Results\" button should be displayed")
def step_impl(m_test):
    assert m_test.is_result_button_displayed(), "'Result' button might not be displayed."


@when("quit the assessment in between on app")
@when("press back and land on student dashboard screen")
@then("press back and land on student dashboard screen")
def step_impl(m_test):
    m_test.click_back()
    assert m_test.wait_activity('OneToMegaHomeActivity')


@then("verify that \"Resume\" button is displayed on the screen")
def step_impl(m_test):
    assert m_test.is_resume_button_displayed(), "\"Resume\" button might not be displayed."


@then("verify elements in assessment screen")
def step_impl(m_test, db):
    assert m_test.verify_web_assessment_screen(db=db), "Some elements in assessment screen might not be displayed."


@when("take the assessment on the web")
def step_impl(m_test, db):
    db.login_profile = "login_details_3"
    db.user_profile = "user_1"
    db.sub_profile = "profile_1"
    m_test.resume_assessment_on_web(db=db)


@then("test status should be in Resume state")
def step_impl(db):
    assert db.resume_btn_displayed, "Resume button might not be displayed."


@then("tap on exit assessment and verify confirmation pop up")
def step_impl(m_test):
    assert m_test.assessment_confirmation_pop_up(), \
        "pop up message might not be displayed or it's content might have been changed."


@then("Verify that when the internet is turned off while taking the test assessment")
def step_impl(m_test, db):
    assert m_test.offline_assessment(db=db), "offline assessment was not successful."


@then("verify that status should be changed to resume")
def step_impl(m_test):
    assert m_test.is_resume_button_displayed(), "offline assessment did not convert session to 'Resume' state."


@when("submit the assessment in offline")
def step_impl(m_test, db):
    m_test.submit_assessment_offline(db=db)


@then("Verify that internet error message is displayed")
def step_impl(m_test):
    assert m_test.is_error_msg_displayed(), "Unable to catch error message."


@when("expire the test session from the backend")
def step_impl(staging_tutor_plus):
    staging_tutor_plus.modify_test_requisite_assessment(field="end_time", day="today", status="expire", grade="8")


@when("user should not attend the test")
def step_impl(m_test):
    assert m_test.verify_session_details(detail="start test button"), \
        "Session 'Start Test' button might not be displayed."


@when("test session should be ended")
def step_impl(m_test):
    assert m_test.verify_session_details(detail="completed status"), "Session might not be completed yet."


@then("verify text \"Test Expired. It was supposed to be taken during session time\" should be displayed")
def step_impl(m_test):
    assert m_test.verify_session_details(detail="completed status") is False, "Session might not be expired."


@when("verify that student has completed the session")
def step_impl(db, m_test):
    assert m_test.complete_assessment_session(db=db), "unable to complete the assessment session."


@when("verify that session has reached end time")
def step_impl(m_test):
    assert m_test.is_session_end_time_reached(), "session might not be ended."


@then("verify that the session card is moved to completed tab")
def step_impl(m_test):
    assert m_test.is_assessment_displayed_in_completed_tab(), "completed session might not be moved to 'Completed' tab."


@then("verify that \"Start Test\" button should not be enabled for the assessment")
def step_impl(m_test):
    assert m_test.verify_session_details(detail="start test button") is False, \
        "Session 'Start Test' button might be displayed."


@when("Verify that the \"Start Test\" button should be enabled automatically in the session card")
def step_impl(m_test):
    assert m_test.is_start_test_btn_displayed_at_start_time(), "\"Start Test\" button might not be displayed."

