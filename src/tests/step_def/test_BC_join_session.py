from pytest_bdd import scenarios, given, then, when, parsers
from pytest import fixture
from constants.load_json import get_data
from constants.constants import Login_Credentials
from pages.android.session_popup import SessionAlert
from utilities.mentor_session import MentorSession
from utilities.staging_tlms import Stagingtlms
from pages.android.homepage import HomePage
from pages.factory.login import LoginFactory
from pages.factory.student_session import StudentSessionFactory
from constants.platform import Platform
import pytest_check as check

scenarios('../features/Session Flow.feature')


@fixture()
def login_in(request, driver):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        login_in = LoginFactory().get_page(driver, Platform.ANDROID.value)
        yield login_in
    elif Platform.WEB.name in platform_list:
        login_in = LoginFactory().get_page(driver, Platform.WEB.value)
        yield login_in


@fixture
def student_session(request, driver):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        student_session = StudentSessionFactory().get_page(driver, Platform.ANDROID.value)
        yield student_session
    elif Platform.WEB.name in platform_list:
        student_session = StudentSessionFactory().get_page(driver, Platform.WEB.value)
        yield student_session


@fixture
def mentor_session(driver):
    mentor_session = MentorSession(driver)
    yield mentor_session


@given('ensure tutor has started the session')
def start_tutor_session(mentor_session):
    mentor_session.start_tutor_session()


@given("launch the application and navigate to home screen")
def login_as_one_mega_user(driver):
    HomePage(driver).navigate_to_one_to_many_and_mega_user(driver)


@given("tap on Premium School card")
def tap_on_premium_card(login_in):
    login_in.click_on_premium_school()


@given("navigate to one to mega homescreen")
def navigate_to_one_to_mega_homescreen(login_in):
    login_in.click_on_link("Byju's classes")


@then(parsers.parse('verify "{text}" option is enabled for the current day session on your session has started card'))
@when(parsers.parse('verify "{text}" option is enabled for the current day session on your session has started card'))
def verify_join_now_is_enabled(driver, student_session, text, login_in):
    global details_dict
    student_session.tap_on_completed_tab()
    login_in.click_on_completed_card(0)
    session_pop = SessionAlert(driver)
    details_dict = session_pop.verify_session_card_details_loaded()
    student_session.verify_button(text)


@then("verify user is landed on one to mega dashboard homescreen")
def is_user_in_ps_page(student_session):
    details = student_session.is_user_in_ps_page()
    check.equal(details.result, True, details.reason)


@then('tap on "Join Now" button')
def tap_on_join_now(student_session):
    student_session.tap_on_join_now()


@when(parsers.parse('tap on "{text}" button'))
@then(parsers.parse('tap on "{text}" button'))
def tap_button(login_in, student_session, text):
    button_status = login_in.button_click(text)
    check.equal(button_status.result, True, button_status.reason)
    student_session.speed_test()


@then(parsers.parse('verify "{text}" bottom sheet dialog should be shown'))
@then(parsers.parse('verify text "{text}" on welcome screen'))
def verify_text(login_in, text):
    profile_name = get_data(Login_Credentials, 'login_detail3', 'profile_one_to_many_and_mega')
    text = text.format(username=profile_name).encode('utf-8').decode('unicode_escape')
    details = login_in.text_match(text)
    check.equal(details.result,True, details.reason)


@then("verify loader 3 dots icon")
def verify_dots_icon(student_session):
    details = student_session.is_dots_icon_displayed()
    check.equal(details.result ,True,details.reason)


@then("verify byju's tutor icon")
def verify_tutor_icon(student_session):
    details = student_session.is_tutor_icon_displayed()
    check.equal(details.result,True,details.reason)


@then("verify subject name")
def verify_subject_name(student_session):
    details = student_session.verify_subject_name(details_dict["Subject"])
    check.equal(details.result,True,details.reason)


@then("verify chapter name")
def verify_chapter_name(student_session):
    details = student_session.verify_chapter_name(details_dict["Topic"])
    check.equal(details.result, True,details.reason)


@then("verify chat icon is displayed")
def tap_on_chat_icon(student_session):
    details = student_session.is_chat_icon_displayed()
    check.equal(details.result,True, details.reason)


@then("tap on chat icon")
def tap_on_chat_icon(student_session):
    student_session.tap_on_chat_icon()


@then("verify Live chat is enabled")
def verify_live_chat_enabled(student_session):
    details = student_session.is_student_chat_enabled()
    check.equal(details.result,True, details.reason)


@then('verify that live chat is launched')
@then("verify the text Live chat as header")
def verify_live_chat_enabled(student_session):
    details = student_session.is_live_chat_displayed()
    check.equal(details.result,True, details.reason)


@then("verify chat close button")
def verify_chat_close_icon(student_session):
    details = student_session.is_chat_close_icon_displayed()
    check.equal(details.result, True,details.reason)


@then("tap on chat close icon")
def close_chat(student_session):
    student_session.close_chat()


@then("tap outside chat layout")
def close_chat(student_session):
    student_session.tap_outside_dialog_layout()


@then("verify that chat window should be closed")
def verify_live_chat_disabled(student_session):
    details = student_session.is_student_chat_enabled()
    check.equal(details.result,False,details.reason)


@then("verify user is landed on tutor videoplayer screen")
@then("verify video elements are present")
def verify_live_chat_disabled(student_session):
    details = student_session.video_elements_present()
    check.equal(details.result,True,details.reason)


@then("tap on live chat is disabled text box")
def tap_on_disabled_chat(student_session):
    student_session.tap_on_disabled_chat()


@then('tap on "Type something" text box')
def tap_on_chat_textbox(student_session):
    student_session.tap_on_chat_textbox()


@then("verify chat dialog should be displayed")
def verify_student_chat_dialog(student_session):
    details = student_session.verify_student_chat_dialog()
    check.equal(details.result,True,details.reason)


@then("tap on chat dialog")
def tap_on_chat_dialog(student_session):
    student_session.tap_on_chat_dialog()


@then("verify that cursor should point to the first place of the text field")
def is_cursor_present(student_session):
    details = student_session.is_cursor_present()
    check.equal(details.result, True,details.reason)


@then("verify smileys are disabled")
def is_emoji_class_present(student_session):
    details = student_session.is_emoji_present()
    check.equal(details.result,False, details.reason)


@then("verify device keypad should be enabled")
def verify_device_keypad_shown(student_session):
    details = student_session.is_keyboard_shown()
    check.equal(details.is_keyboard_shown().result,True,details.reason)


@then(parsers.parse('Enter text "{text}" in chat dialog'))
def enter_text(student_session, text):
    student_session.enter_text_in_chat(text)


@then(parsers.parse('verify user is able to enter the chat text "{text}"'))
def verify_user_able_to_enter_text(student_session, text):
    details = student_session.verify_entered_chat(text)
    check.equal(details.result, True,details.reason)


@then("tap on send button in the chat box")
def tap_on_send_button(student_session):
    student_session.tap_on_chat_send()


@then("tap on device back button")
def tap_device_back(student_session):
    student_session.click_back()


@then(parsers.parse('verify student able to view teacher message "{text}"'))
@then(parsers.parse('verify student is able to send the typed text "{text}" to tutor'))
def verify_user_sent_text(student_session, text):
    details = student_session.verify_message_at_student_side(text)
    check.equal(details.result,True,details.reason)


@then(parsers.parse('Paste the copied text "{text}" in the chat field'))
def enter_chat_text(student_session, text):
    student_session.enter_text_in_chat(text)


@then(parsers.parse('verify user is able to paste the text "{text}"'))
def paste_chat_text(student_session, text):
    details = student_session.verify_entered_chat(text)
    check.equal(details.result, True,details.reason)


@then(parsers.parse('tap on "{text}" button present in the ongoing session bottom sheet dialog'))
def click_on_button(login_in, text):
    login_in.button_click(text)


@then(parsers.parse('verify student is able to view the tutor message "{text}"'))
@then(parsers.parse('verify old chat thread message "{text}" should be displayed in chat window'))
def verify_old_chat(student_session, text):
    student_session.verify_message_at_student_side(text)


@given("navigate to home page and verify student profile")
def verify_student_session(student_session):
    global profile_name
    profile_name = student_session.verify_student_profile()


@then(parsers.parse('verify "{text}" button should be displayed'))
def button_verify(login_in, text):
    details = login_in.is_button_displayed(text)
    check.equal(details.result,True,details.reason)


@then(parsers.parse('verify "{text}" should be displayed'))
def verify_text_is_present(login_in, text):
    verify_text(login_in, text)


@then("verify ongoing session bottom sheet dialog should disappear")
@then("verify offline related bottom sheet dialog should disappear")
def verify_offline_dialog_sheet_disappeared(student_session):
    student_session.verify_offline_dialog_disappeared()


@then(parsers.parse('switch "{text}" the device data'))
def switch_off_data(login_in, text):
    login_in.toggle_wifi_connection(text)


@then("verify offline related bottom sheet dialog should be displayed")
def verify_offline_validation_layout(login_in):
    details = login_in.is_offline_validation_layout_displayed()
    check.equal(details.result, True, details.reason)


@then('tap on "Cancel" text')
def tap_on_cancel(student_session):
    student_session.tap_on_cancel()


@then("verify uploaded pdf should be displayed on the student white screen")
def is_teaching_material_present(student_session):
    student_session.is_teaching_material_present()


@then("verify video icon should be enabled")
def verify_video_option_enabled(student_session):
    is_enabled = student_session.is_student_video_icon_enabled()
    assert is_enabled == 'true', "Video icon is not disabled"


@then("verify mic option should be enabled")
def verify_mic_option_disabled(student_session):
    is_enabled = student_session.is_student_mic_option_enabled()
    assert is_enabled == 'true', "Mic icon is not disabled"


@then("verify student video screen should be enabled")
def verify_video_screen_disabled(student_session):
    assert student_session.is_student_video_screen_present() is True, "Video screen is disabled"


@then("tap on video icon")
def tap_on_video_icon(student_session):
    student_session.tap_on_video_icon()


@then("tap on audio mic icon")
def tap_on_audio_mic_icon(student_session):
    student_session.tap_on_audio_mic_icon()


@then(parsers.parse(
    'verify tutor video should be disabled and verify black colour RGB value "{color_code}" screen is displayed'))
def is_tutor_video_muted_and_black_screen_displayed(student_session, color_code):
    student_session.is_tutor_video_muted_and_black_screen_displayed(color_code)


@then(parsers.parse('switch "{text}" the tutor chat toggle button'))
def toggle_chat(mentor_session, text):
    mentor_session.toggle_chat(text)


@then("verify Live chat is disabled")
def verify_live_chat_enabled(student_session):
    details = student_session.is_student_chat_enabled()
    check.equal(details.result,False,details.reason)


@then("verify chat dialog should not be displayed")
def verify_student_chat_dialog_not_present(student_session):
    details = student_session.verify_student_chat_dialog()
    check.equal(details.result,False,details.reason)


@then(parsers.parse('teacher send message "{text}" in chat to students'))
def teacher_send_message_in_chat(mentor_session, text):
    mentor_session.send_message_in_chat(text)


@then(parsers.parse('send "{text}" message'))
def student_send_multiple_messages(student_session, text):
    student_session.tap_on_chat_textbox()
    student_session.enter_text_in_chat(text)
    student_session.tap_on_chat_send()


@then("scroll the live chat")
def scroll_live_chat(student_session):
    student_session.scroll_chat_container()


@then('tutor ends session')
def tutor_taps_on_end_session(mentor_session):
    mentor_session.tutor_end_session()


@then(parsers.parse('verify "{text}" bottom sheet dialog is not shown'))
def bottom_dialog_not_shown(login_in, text):
    details = login_in.text_match(text)
    check.equal(details.result, False,details.reason)


@then("close tutor session browser tab")
def close_mentor_session_tab(mentor_session):
    mentor_session.close_mentor_session_tab()


@given("reset student session if the session is incase completed")
def reset_session(driver):
    Stagingtlms(driver).reset_session()


@then("verify that videoplayer should not have any controls like seek bar,pause,play icons on the screen")
def is_video_play_pause_progress_bar_present(student_session):
    details = student_session.is_video_play_pause_progress_bar_present()
    check.equal(details.result, False, details.reason)


@when("verify elements in Tutor's chat window")
def verify_tutor_chat_window(mentor_session):
    details = mentor_session.verify_tutor_chat_window()
    check.equal(details.result, True, details.reason)


@then("Verify when student sends message student name is shown")
def verify_student_name(mentor_session):
    details = mentor_session.verify_student_name_present()
    check.equal(details.result,True, details.reason)


@then("Verify that Ban button , Approve button and Reject button is shown")
def verify_ban_approve_reject(mentor_session):
    details = mentor_session.verify_ban_approve_reject_present()
    check.equal(details.result,True, details.reason)


@then('tap on tutor chat icon')
@when('tap on tutor chat icon')
def tap_chat_icon(mentor_session):
    mentor_session.tap_chat_icon()


@then('tap on Ban button')
def tap_ban_icon(mentor_session):
    mentor_session.tap_ban_icon()


@then('Verify that "Ban the student" pop-up should be shown with the options as "Inappropriate Content",'
      '"Abusive Language","Content Sharing" and "Others" along with radio button and "Cancel" and "Ban" buttons')
def verify_ban_options_and_buttons(mentor_session):
    details = mentor_session.verify_ban_options_and_buttons()
    check.equal(details.result,True,details.reason)


@then('Verify that Inappropriate Content should be selected by default')
def verify_default_ban_option(mentor_session):
    details = mentor_session.verify_default_ban_option()
    check.equal(details.result,True,details.reason)


@then('Verify that while clicking on Cancel button the pop-up should go off')
def verify_ban_cancel(mentor_session):
    details = mentor_session.verify_ban_cancel()
    check.equal(details.result,True, details.reason)


@then("Verify the while clicking outside of the pop-up it should go off")
def step_impl(mentor_session):
    details =mentor_session.verify_click_outside_ban_popup()
    check.equal(details.result,True,details.reason)


@then("Verify on clicking on Ban button user should be banned and banned student messages should not be shown")
def verify_ban_student(mentor_session):
    details = mentor_session.verify_ban_student()
    check.equal(details.result,True, details.reason)


@then("tap on the tick mark (approve button) in the message")
def tap_on_approve_message(mentor_session):
    mentor_session.tap_on_approve_message()


@then(parsers.parse('verify tutor received "{text}" message from student'))
@then(parsers.parse('Verify that the tutor is able to approve the message "{text}"'))
def tap_on_approve_message(mentor_session, text):
    details = mentor_session.is_message_present_for_tutor(text)
    check.equal(details.result,True, details.reason)


@then(parsers.parse('Verify that the tutor is able to reject the message "{text}"'))
def tap_on_approve_message(mentor_session, text):
    details = mentor_session.is_message_present_for_tutor(text)
    check.equal(details.result, False,details.reason)


@then('tap on "x" button(reject button) shown in the message')
def tap_on_reject_message(mentor_session):
    mentor_session.tap_on_reject_message()


@then(parsers.parse('verify that approved message "{text}" is shown in the other student chat window'))
def login_as_student2_and_verify_approved_msg(student_session, text):
    user_name = get_data(Login_Credentials, 'login_detail3', 'profile_one_to_many_and_mega')
    expected_text = user_name + " " + text
    details =  student_session.verify_message_at_student_side(expected_text)
    check.equal(details.result, True, details.reason)


@then('login as another student who attends same session')
def login_as_student2(driver, login_in):
    HomePage(driver).login_as_another_one_mega_user(driver,'login_detail1')
    login_in.click_on_premium_school()


@then(parsers.parse('verify that rejected message "{text}" is not shown in the other student chat window'))
def verify_rejected_msg(student_session, text):
    user_name = get_data(Login_Credentials, 'login_detail3', 'profile_one_to_many_and_mega')
    expected_text = user_name + " " + text
    details = student_session.verify_message_at_student_side(expected_text)
    check.equal(details.result,False,details.reason)


@given('verify reset buffer time is completed')
def wait_for_reset_buffer_time_to_complete(mentor_session):
    mentor_session.wait_for_reset_buffer_time_to_complete()
