from pytest_bdd import scenarios, given, then, when, parsers
from pytest import fixture
from constants.platform import Platform
from pages.factory.login import LoginFactory
from pages.factory.neo_inclass_factory import NeoInClassFactory
from constants.constants import Login_Credentials
from constants.load_json import get_data
import pytest_check as check
from utilities.neo_tute_mentoring import NeoTute

scenarios('../features/In class-Notifications.feature')

@fixture()
def student1_login(request, driver):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        student1_login = LoginFactory().get_page(driver, Platform.ANDROID.value)
        yield student1_login
    elif Platform.WEB.name in platform_list:
        student1_login = LoginFactory().get_page(driver, Platform.WEB.value)
        yield student1_login


@fixture()
def student1_neo(request, student1_login):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        student1_neo = NeoInClassFactory().get_page(student1_login.driver, Platform.ANDROID.value)
        yield student1_neo
    elif Platform.WEB.name in platform_list:
        student1_neo = NeoInClassFactory().get_page(student1_login.driver, Platform.WEB.value)
        yield student1_neo


@fixture()
def neo_tute(driver):
    neo_tute = NeoTute(driver)
    yield neo_tute


@fixture()
def student2(request):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        student2 = LoginFactory().get_page(None, Platform.ANDROID.value)
        yield student2
    elif Platform.WEB.name in platform_list:
        student2 = LoginFactory().get_page(None, Platform.WEB.value)
        yield student2


@fixture()
def student2_neo(request, student2):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        student2_neo = NeoInClassFactory().get_page(student2.driver, Platform.ANDROID.value)
        yield student2_neo
    elif Platform.WEB.name in platform_list:
        student2_neo = NeoInClassFactory().get_page(student2.driver, Platform.WEB.value)
        yield student2_neo


@given("Launch the application online")
def login_as_neo_user(student1_login):
    student1_details = get_data(Login_Credentials, 'neo_login_detail3', 'student2')
    student1_login.login_and_navigate_to_home_screen(student1_details['code'], student1_details['mobile_no'], otp=None)


@given("tutor start the session")
def step_impl(neo_tute):
    neo_tute.start_neo_session(login_data="neo_login_detail3", user='student1')

@when('join neo session')
def step_impl(student1_neo):
    student1_neo.home_click_on_join()

@when('click on start class')
def step_impl(student1_neo):
    student1_neo.join_neo_session_student('mic-on', 'cam-on')

@then('Verify that when mic and chat is disabled by tutor, hovering over mic icon should show a toast message that mic and text options is disabled by tutor')
def step_impl(neo_tute, student1_neo):
    neo_tute.select_focus_mode('on')
    details = student1_neo.is_chat_disabled_message_dislayed(message = 'Live Chat is disabled')
    check.equal(details.result, True, details.reason)
    student1_neo.hover_on_inclass_audio_icon()
    details = student1_neo.is_mic_disabled_tooltip_present()
    check.equal(details.result, True, details.reason)

@then('Verify that the toast message is dismissed when hover is moved away from mic icon; verify that there is no distortion on the toast message when same appears and disappears')
def step_impl(neo_tute, student1_neo):
    neo_tute.select_focus_mode('on')
    student1_neo.hover_on_inclass_video_icon()
    details = student1_neo.is_mic_disabled_tooltip_present()
    check.equal(details.result, True, details.reason)


@then('Verify that the in-class notifications do not cover the video/content when full screen is not active')
def step_impl(neo_tute, student1_neo):
    neo_tute.find_video_slide()
    # student1_neo.hover_on_inclass_audio_icon()
    # details = student1_neo.is_mic_disabled_tooltip_present()
    # check.equal(details.result, True, details.reason)
    details = student1_neo.is_video_being_presented()
    check.equal(details.result, True, details.reason)


@then('Verify that when the student lowers hand a toast message is displayed prompting that student has lowered hand')
def step_impl(student1_neo):
    student1_neo.click_on_hand_raise()
    details = student1_neo.verify_text_in_lower_hand_tooltip()
    check.equal(details.result, True, details.reason)

@then('Verify that when focus mode is about to start the student is notified for same as in-class notification toast message, also verify the content of the message')
def step_impl(neo_tute,student1_neo):
    neo_tute.find_video_slide()
    details = student1_neo.is_focus_mode_toast_msg_present()
    check.equal(details.result, True, details.reason)
    details = student1_neo.verify_text_in_focus_mode_toast_msg()
    check.equal(details.result, True, details.reason)

@then('Verify that in-class notification toast message for focus mode should not have close icon and same should get dismissed automatically after xx seconds')
def step_impl(student1_neo):
    details = student1_neo.verify_close_icon_in_toast_message()
    check.equal(details.result, False, details.reason)


@then('Verify that the in-class notifications stay on the screen for xx seconds before disappearing from the screen')
def step_impl(student1_neo):
    student1_neo.hard_wait()
    details = student1_neo.is_focus_mode_toast_msg_present()
    check.equal(details.result, False, details.reason)

@then('Verify that there is a close button on the in-class notifications toast message which should allow students to close/dismiss the message')
def step_impl(student1_neo):
    details = student1_neo.verify_close_icon_in_toast_message()
    check.equal(details.result, True, details.reason)
    student1_neo.click_on_close_icon_in_toast_msg()
    details = student1_neo.is_network_failed_toast_msg_present()
    check.equal(details.result, False, details.reason)
    student1_neo.set_network_on()


@then('Verify that there is no distortion on the in-class notifications toast message or the session content when they appear or disappear from the screen')
def step_impl(neo_tute,student1_neo):
    neo_tute.find_video_slide()
    student1_neo.click_on_hand_raise()
    student1_neo.click_on_hand_raise()
    details = student1_neo.verify_text_in_lower_hand_tooltip()
    check.equal(details.result, True, details.reason)

@then("Verify that the in-class notifications toast message should have tutor's image and indication that the message is from tutor")
def step_impl(neo_tute, student1_neo):
    student1_details = get_data(Login_Credentials, 'neo_login_detail3', 'student2')
    student1_neo.click_on_hand_raise()
    neo_tute.click_on_menu_option(expected_student_name=student1_details['stud_name'], menu_item='Hands Down')
    details = student1_neo.verify_message_from_tutor_text("Message from Tutor")
    check.equal(details.result, True, details.reason)
    details = student1_neo.verify_pens_down_tooltip()
    check.equal(details.result, True, details.reason)
    student1_neo.click_on_close_icon_in_toast_msg()


@then('Verify that if network error happens, same is displayed as in-class notification toast message with "Retry" button')
def step_impl(student1_neo):
    student1_neo.set_network_flaky()
    details = student1_neo.is_network_failed_toast_msg_present()
    check.equal(details.result, True, details.reason)

