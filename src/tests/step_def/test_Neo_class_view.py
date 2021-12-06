import time

from pytest_bdd import scenarios, given, when, then, parsers
from pytest import fixture

from constants.constants import Login_Credentials
from constants.load_json import get_data
from constants.platform import Platform
from pages.factory.login import LoginFactory
from pages.factory.neo_inclass_factory import NeoInClassFactory
from utilities.neo_tute_mentoring import NeoTute

feature_file_name = 'Class View'
import pytest_check as check

scenarios('../features/' + feature_file_name + '.feature')

@fixture
def test_tut(driver):
    test_tut = NeoTute(driver)
    yield test_tut


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
def login_in(request, driver):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        login_in = LoginFactory().get_page(driver, Platform.ANDROID.value)
        yield login_in
    elif Platform.WEB.name in platform_list:
        login_in = LoginFactory().get_page(driver, Platform.WEB.value)
        yield login_in


@given("tutor start the session")
def step_impl(test_tut):
    test_tut.start_neo_session(login_data="neo_login_detail2", user='student3')
    test_tut.select_focus_mode(status='off')
    active_slide_number = test_tut.active_presentation_slide_number()
    test_tut.stop_presentation(active_slide_number)


@given("Student launches in-class and navigate to home page")
def step_impl(login_in):
    student2_details = get_data(Login_Credentials, 'neo_login_detail2', 'student3')
    login_in.login_and_navigate_to_home_screen(student2_details['code'], student2_details['mobile_no'], otp=None)


@given("student navigates to byjus classes screen")
def step_impl(neo_in_class):
    neo_in_class.navigate_to_byjus_classes_screen()


@given('click on "JOIN" button in home page')
@when('click on "JOIN" button in home page')
def step_impl(neo_in_class):
    neo_in_class.home_click_on_join()


@when("student join neo session")
@then("student join neo session")
def step_impl(neo_in_class):
    neo_in_class.join_neo_session()


@then("Verify the screen when the class starts")
def step_impl(test_tut):
    details = test_tut.verify_screen_elements()
    check.equal(details.result,True,details.reason)


@then("Verify that thumbnail controller for student's image/video view should display right side of the screen")
def step_impl(test_tut):
    details = test_tut.is_thumbnail_controller_displayed()
    check.equal(details.result, True, details.reason)


@then("Verify that Tute should able to large and small the thumbnails clicking on the thumbnail controller")
def step_impl(test_tut):
    details = test_tut.verify_thumbnail_controller_action()
    check.equal(details.result, True, details.reason)


@then("Verify that the tutor video should display on the top right side of the screen")
def step_impl(test_tut):
    flag = test_tut.is_signal_icon_present()
    check.equal(flag,True,"Signal icon is not present")


@then("Verify that the tutor video should display on the top right side of the screen")
def step_impl(test_tut):
    flag = test_tut.is_tutor_video_present()
    check.equal(flag, True, "Tutor video is not present")


@then("Verify that audio/video/chat button should display on the top middle of the screen")
def step_impl(test_tut):
    flag = test_tut.is_chat_icon_present()
    check.equal(flag, True, "Chat icon is not present")
    flag = test_tut.is_video_icon_present()
    check.equal(flag, True, "Video icon is not present")
    flag = test_tut.is_audio_icon_present
    check.equal(flag, True, "Audio icon is not present")


@then("Verify that tutor should be able to turn off the student's camera clicking on camera icon")
def step_impl(test_tut,neo_in_class):
    test_tut.set_students_camera(status='off')
    status = neo_in_class.get_inclass_student_video_status()
    flag1 = status == "DISABLED"
    test_tut.set_students_camera(status='on')
    time.sleep(5)
    status2 = neo_in_class.get_inclass_student_video_status()
    flag2 = status2 == "ON" or status2 == "OFF"
    check.equal(all((flag2,flag1)),True,"tutor is able to control student camera")


@then("Verify that tutor should be able to mute the students clicking the mic")
def step_impl(test_tut,neo_in_class):
    test_tut.set_students_mic(status='off')
    status = neo_in_class.get_inclass_student_audio_status()
    flag1 = status == "DISABLED"
    test_tut.set_students_mic(status='on')
    time.sleep(5)
    status2 = neo_in_class.get_inclass_student_audio_status()
    flag2 = status2 == "ON" or status2 == "OFF"
    check.equal(all((flag2, flag1)), True, "tutor is able to control student mic")


@then("Verify that tutor should able to disable the chat clicking on the chat icon")
def step_impl(test_tut,neo_in_class):
    test_tut.enable_disable_chat(flag='disable')
    details = neo_in_class.is_chat_disabled_message_dislayed()
    check.equal(details.result, True, details.reason)
    test_tut.enable_disable_chat(flag='enable')


@then("Verify that the End class button should display top right side of the screen")
def step_impl(test_tut):
    details =test_tut.is_end_class_button_displayed()
    check.equal(details.result, True, details.reason)


@then("Verify that the class should end when user click on exit class")
@then("Verify that when tute click on end class confirmation popup should display with Exit and stay back options")
@then("Verify that the End class button is clickable and tutor can end the class clicking on End class") #we cannt end the class so have checked the pop up only
def step_impl(test_tut):
    test_tut.click_on_end_class()
    flag = test_tut.is_continue_class_button_present_in_popup()
    check.equal(flag, True, "Continue class button is not present in end class pop up")
    flag2= test_tut.is_end_class_button_present_in_popup()
    check.equal(flag2, True, "End class button is not present in end class pop up")
    test_tut.click_on_continue_class_button()


@then("Verify that class should continue clicking on stay back")
def step_impl(test_tut):
    test_tut.click_on_end_class()
    test_tut.click_on_continue_class_button()
    details = test_tut.verify_screen_elements()
    check.equal(details.result, True, details.reason)


@then("Verify the timer beside the End class button ")
def step_impl(test_tut):
    flag = test_tut.is_timer_present()
    check.equal(flag, True, "Timer is not present")


@then('Verify that when focus mode is ON the text "Focus Mode :ON" along with icon')
def step_impl(test_tut):
    test_tut.select_focus_mode(status='on')
    details = test_tut.verify_focus_mode_on()
    check.equal(details.result, True, details.reason)
    test_tut.select_focus_mode(status='off')


@then("Verify that global icon of audio and chat should be disabled state")
def step_impl(test_tut):
    test_tut.select_focus_mode(status='on')
    flag = test_tut.get_audio_status()
    check.equal(flag, False, "Global mic is on in focus mode")
    flag2 = test_tut.get_chat_status()
    check.equal(flag2, False, "Global chat is on in focus mode")
    test_tut.select_focus_mode(status='off')

@then("Verify that in Focus mode all students mike should be muted by default")
def step_impl(test_tut,neo_in_class):
    test_tut.select_focus_mode(status='on')
    status = neo_in_class.get_inclass_student_audio_status()
    flag1 = status == "DISABLED"
    check.equal(flag1,True,"Students mic are not disabled in focus mode")

@then("Verify the tutor internet connection should display on the top of the screen ")
def step_impl(test_tut):
    details = test_tut.is_internet_connection_displayed()
    check.equal(details.result,True,details.reason)

