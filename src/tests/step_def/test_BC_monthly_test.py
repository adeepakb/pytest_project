from pytest_bdd import scenarios, given, when, then, parsers
from constants.platform import Platform
from pages.factory.ps_home_screen import PSHomescreenFactory
from utilities.staging_tllms import Stagingtllms
from pages.factory.monthly_test import MonthlyTestFactory
from pytest import fixture
import time
from utilities.staging_tutor_plus import *
from datetime import datetime as dt, timedelta


feature_file_name = 'Monthly Test'

scenarios('../features/' + feature_file_name + '.feature')


@fixture
def tllms(driver):
    staging = Stagingtllms(driver)
    yield staging



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
    staging_tutor_plus.set_user().convert_video_session(db=db,subject_topic_name=("",""))


@given("login as user with not completed assessment")
def step_impl(login):
    login.toggle_wifi_connection('on')
    login.set_user_profile(user_profile='user_1', sub_profile='profile_1').verify_user_profile()


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
def step_impl(m_test,staging_tutor_plus, db):
    staging_tutor_plus.set_user().convert_video_session(test_type = 'unit test',db=db,subject_topic_name=("",""))


@given('give a delay of “120” seconds')
def step_impl(m_test):
    time.sleep(0)



@given("login as user with unit test scheduled")
def step_impl(login):
    login.toggle_wifi_connection('on')
    login.set_user_profile(user_profile='user_1', sub_profile='profile_1').verify_user_profile()


@then('user should not see the assessment session joining pop up')
def step_impl(home_screen):
    assert  home_screen.click_on_dissmiss() == False


@when('the user is in For you Tab')
def step_impl(m_test):
    m_test.click_on_for_you_tab()


@then(parsers.parse('Verify that the title of the test should be "{text}"'))
def step_impl(m_test, text):
    title, session_time,session_title = m_test.get_card_detail()
    assert title , text


@then('validate elements of monthly session card')
def step_impl(m_test,staging_tutor_plus):
    m_test.verify_session_details('subject title')
    #m_test.verify_session_details('topic_name_for_pre_post')
    m_test.verify_session_details('status')
    m_test.verify_session_details('heading')



@given('The session should be converted to a monthly test1')
def step_impl(m_test):
    print('deepak')


@then('user should be able to view post requisites')
def step_impl(std_board):
    assert std_board.is_pre_post_requisite_displayed(post= True,session='completed')
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
def step_impl(m_test,button):
    m_test.click_on_button(button)


@given('login as user with “incomplested assessment”')
def step_impl(login):
    login.toggle_wifi_connection('on')
    login.set_user_profile(user_profile='user_1', sub_profile='profile_1').verify_user_profile()


@given('user has not started the test session')
def step_impl(login, **kwargs):
    login.toggle_wifi_connection('on')
    login.set_user_profile(user_profile='user_1', sub_profile='profile_1').verify_user_profile()


@given(parsers.parse('verify that the text "{button}" button should be present on the card'))
def step_impl(m_test,button):
    m_test.is_button_displayed(button_name=button)


@given('verify that student can take test from completed tab')
def step_impl(m_test):
    assert m_test.is_status_displayed()


@when('user starts assessment and land on final question')
def step_impl(m_test):
    assert m_test.do_assignment(finish=False)


@when('verify whether there is any interruption when the session has reached end time while student is still taking the assessment')
def step_impl(m_test):
    assert m_test.check_no_interruption_in_assignment()==True


@given("The session should be converted to a monthly test with test end time greater than session end time")
def step_impl(m_test, staging_tutor_plus, db):
    staging_tutor_plus.set_user().convert_video_session(db=db)


@given("The session should be converted to a monthly test with session end time lesser than test end time")
def step_impl(m_test, tllms,staging_tutor_plus, db):
    staging_tutor_plus.set_user().convert_video_session(db=db,assessment_type="monthly test", subject_topic_name=("",""))
    sd = db.sd
    time_of_interest=sd[0]['time']
    time_of_interest = time_of_interest.split("\n")[1].split("-")[1]
    time_list = sd[0]['time'].replace("\n", " ").split(" - ")
    date = time_list[0].split(" ")[0]
    new_timelist = []
    new_timelist.append(date)
    new_timelist.append(" " + time_list[1])
    new_time = "".join(new_timelist)
    time_required = dt.strptime(new_time, '%d-%b-%Y %H:%M')
    import datetime
    two_minute = datetime.timedelta(minutes=2)
    time_required_new = time_required + two_minute
    tllms.modify_test_requisite_assessment(sd[0]['channel'],field="end_time",day = 'today',status='expire',time=time_required_new)


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




