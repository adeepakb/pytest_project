from pytest_bdd import scenarios, given, then, when, parsers
from pytest import fixture
from constants.platform import Platform
from pages.factory.login import LoginFactory
from pages.factory.neo_inclass_factory import NeoInClassFactory
import pytest_check as check
from utilities.neo_tute_mentoring import NeoTute
from constants.constants import Login_Credentials
from constants.load_json import get_data

scenarios('../features/Join session.feature')


@fixture()
def login_in(request, driver):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        login_in = LoginFactory().get_page(driver, Platform.ANDROID.value)
        yield login_in
    elif Platform.WEB.name in platform_list:
        login_in = LoginFactory().get_page(driver, Platform.WEB.value)
        yield login_in


@fixture()
def neo_in_class(request, driver):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        neo_in_class = NeoInClassFactory().get_page(driver, Platform.ANDROID.value)
        yield neo_in_class
    elif Platform.WEB.name in platform_list:
        neo_in_class = NeoInClassFactory().get_page(driver, Platform.WEB.value)
        yield neo_in_class


@fixture()
def neo_tute(driver):
    neo_tute = NeoTute(driver)
    yield neo_tute


@given("Launch the application online")
def step_impl(login_in):
    student1_details = get_data(Login_Credentials, 'neo_login_detail3', 'student1')
    login_in.login_and_navigate_to_home_screen(student1_details['code'], student1_details['mobile_no'], otp=None)


@given("tutor start the session")
def step_impl(neo_tute):
    neo_tute.start_neo_session(login_data="neo_login_detail3", user='student1')

@when('join neo session')
def step_impl(neo_in_class):
    neo_in_class.home_click_on_join()

@then('Verify that user is able to join neo class')
def step_impl(neo_in_class):
    neo_in_class.join_neo_session_student('mic-on', 'cam-on')
    details = neo_in_class.is_session_topic_inclass_present()
    check.equal(details.result, True, details.reason)

@then('Verify that the student is visible clearly or not when the camera is enabled.')
def step_impl(neo_in_class):
    details = neo_in_class.is_cam_in_join_class_present()
    check.equal(details.result, True, details.reason)

@then("Verify the student's audio when the mic is enabled")
def step_impl(neo_in_class):
    details = neo_in_class.is_mic_in_join_class_present()
    check.equal(details.result, True, details.reason)


@then('Verify the class joining screen before the class starts')
def step_impl(neo_in_class):
    details = neo_in_class.verify_join_class_screen()
    check.equal(details.result, True, details.reason)


@then('Verify the functionality of the Audio and video settings')
@then("Verify the functionality of the mic and the camera on the student's screen")
def step_impl(neo_in_class):
    neo_in_class.turn_on_off_join_class_student_mic('OFF')
    neo_in_class.turn_on_off_join_class_student_video('OFF')
    details = neo_in_class.verify_audio_video_functionality()
    check.equal(details.result, True, details.reason)


@then('Verify the student video and audio in poor network')
def step_impl(neo_in_class):
    neo_in_class.set_network_flaky()
    details = neo_in_class.is_network_failed_toast_msg_present()
    check.equal(details.result, True, details.reason)
    details = neo_in_class.is_mic_in_join_class_present()
    check.equal(details.result, True, details.reason)
    details = neo_in_class.is_cam_in_join_class_present()
    check.equal(details.result, True, details.reason)
    neo_in_class.set_network_on()


@then("session started X minute back message should be displayed when user joins after the session starts time.")
def step_impl(neo_in_class):
    details = neo_in_class.verify_class_started_message()
    check.equal(details.result, True, details.reason)


@then("Verify that the student should join and leave the class multiple times")
def step_impl(neo_in_class):
    neo_in_class.exit_session()
    neo_in_class.join_neo_session_from_classes_page_paid()
    neo_in_class.join_neo_session_student('mic-on', 'cam-on')
    neo_in_class.exit_session()
    neo_in_class.join_neo_session_from_classes_page_paid()


@then("Verify that confirmation popup should be displayed when user click on leave the session")
def step_impl(neo_in_class):
    neo_in_class.join_neo_session_student('mic-on', 'cam-on')
    neo_in_class.click_on_kebab_menu()
    neo_in_class.click_on_exit_class_in_student()
    flag =neo_in_class.verify_header_in_exit_class_popup()
    check.equal(flag,True, "Confirmation popup is not displayed")
    neo_in_class.click_on_stayback_in_exit_popup()


@then("verify that validation should be displayed when user try join the class with out internet connection")
def step_impl(neo_in_class):
    neo_in_class.exit_session()
    neo_in_class.set_wifi_connection_off()
    neo_in_class.join_neo_session_student('mic-on', 'cam-on')
    neo_in_class.verify_join_session_network_error_popup()
    neo_in_class.set_wifi_connection_on()
    neo_in_class.click_on_retry_button()
    details = neo_in_class.verify_class_started_message()
    check.equal(details.result, True, details.reason)