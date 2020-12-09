from pytest_bdd import scenarios, given, then, when, parsers
from pytest import fixture
from POM_Pages.application_login import Login
from POM_Pages.student_session import StudentSession
from POM_Pages.session_popup import SessionAlert
from POM_Pages.mentor_session import MentorSession
from POM_Pages.staging_tlms import Stagingtlms
from POM_Pages.homepage import HomePage, Login_Credentials, getdata

scenarios('../features/Session Flow.feature')


@fixture
def login_in(driver):
    login_in = Login(driver)
    yield login_in


@fixture
def student_session(driver):
    student_session = StudentSession(driver)
    yield student_session


@fixture
def mentor_session(driver):
    mentor_session = MentorSession(driver)
    yield mentor_session


@given('ensure tutor has started the session')
def start_tutor_session(mentor_session):
    mentor_session.start_tutor_session()


@given("launch the app and navigate to home screen")
def login_as_one_mega_user(driver):
    HomePage(driver).navigate_to_one_to_many_and_mega_user(driver)


@given("tap on Premium School card")
def tap_on_premium_card(login_in):
    login_in.click_on_premium_school()


@given("navigate to one to mega homescreen")
def navigate_to_one_to_mega_homescreen(login_in):
    login_in.click_on_link('Premium School')


@then(parsers.parse('verify "{text}" option is enabled for the current day session on your session has started card'))
@when(parsers.parse('verify "{text}" option is enabled for the current day session on your session has started card'))
@then("verify user is landed on one to mega dashboard homescreen")
def verify_join_now_is_enabled(driver, student_session, text):
    global details_dict
    session_pop = SessionAlert(driver)
    session_pop.verify_popup_present()
    details_dict = session_pop.content_card_loaded()
    student_session.verify_button(text)


@then('tap on "Join Now" button')
def tap_on_join_now(student_session):
    student_session.tap_on_join_now()


@when(parsers.parse('tap on "{text}" button'))
@then(parsers.parse('tap on "{text}" button'))
def tap_button(login_in, student_session, text):
    button_status = login_in.button_click(text)
    assert button_status is True, "Unable to find {text} button"
    student_session.speed_test()


@then(parsers.parse('verify "{text}" bottom sheet dialog should be shown'))
@then(parsers.parse('verify text "{text}" on welcome screen'))
def verify_text(login_in, text):
    profile_name = getdata(Login_Credentials, 'login_detail3', 'profile_one_to_many_and_mega')
    text = text.format(username=profile_name).encode('utf-8').decode('unicode_escape')
    assert login_in.text_match(text), "%s text is not displayed" % text


@then("verify loader 3 dots icon")
def verify_dots_icon(student_session):
    assert student_session.is_dots_icon_displayed() is True, "3 dots icon is not present"


@then("verify byju's tutor icon")
def verify_tutor_icon(student_session):
    assert student_session.is_tutor_icon_displayed() is True, "Tutor Icon is not present"


@then("verify subject name")
def verify_subject_name(student_session):
    student_session.verify_subject_name(details_dict["Subject"])


@then("verify chapter name")
def verify_chapter_name(student_session):
    student_session.verify_chapter_name(details_dict["Topic"])


@then("Verify user lands on white board screen")
def verify_white_board(student_session):
    is_present = student_session.is_white_board_present()
    assert is_present is True, "White board is not present in student screen"


@then("verify video icon should be disabled")
def verify_video_option_disabled(student_session):
    is_enabled = student_session.is_student_video_icon_enabled()
    assert is_enabled == 'false', "Video icon is not disabled"


@then("verify mic option should be disabled")
def verify_mic_option_disabled(student_session):
    is_enabled = student_session.is_student_mic_option_enabled()
    assert is_enabled == 'false', "Mic icon is not disabled"


@then("verify student video screen should be disabled")
def verify_video_screen_disabled(student_session):
    assert student_session.is_student_video_screen_present() is False, "Video screen is not disabled"


@then("verify chat icon is displayed")
def tap_on_chat_icon(student_session):
    assert student_session.is_chat_icon_displayed(), "chat icon is not displayed"


@then("tap on chat icon")
def tap_on_chat_icon(student_session):
    student_session.tap_on_chat_icon()


@then("verify Live chat is enabled")
def verify_live_chat_enabled(student_session):
    is_enabled = student_session.is_student_chat_enabled()
    assert is_enabled is True, "Live chat is disabled"


@then('verify that live chat is launched')
@then("verify the text Live chat as header")
def verify_live_chat_enabled(student_session):
    is_present = student_session.is_live_chat_displayed()
    assert is_present is True, "Live chat header is not displayed"


@then("verify chat close button")
def verify_chat_close_icon(student_session):
    assert student_session.is_chat_close_icon_displayed(), "chat close icon is not displayed"


@then("tap on chat close icon")
def close_chat(student_session):
    student_session.close_chat()


@then("tap outside chat layout")
def close_chat(student_session):
    student_session.tap_outside_dialog_layout()


@then("verify that chat window should be closed")
def verify_live_chat_disabled(student_session):
    is_enabled = student_session.is_student_chat_enabled()
    assert is_enabled is False, "chat is not closed"


@then("verify user is landed on tutor videoplayer screen")
@then("verify video elements are present")
def verify_live_chat_disabled(student_session):
    is_enabled = student_session.video_elements_present()
    assert is_enabled is True, "user is not on tutor videoplayer screen"


@then("tap on live chat is disabled text box")
def tap_on_disabled_chat(student_session):
    student_session.tap_on_disabled_chat()


@then('tap on "Type something" text box')
def tap_on_chat_textbox(student_session):
    student_session.tap_on_chat_textbox()


@then("verify chat dialog should be displayed")
def verify_student_chat_dialog(student_session):
    assert student_session.verify_student_chat_dialog(), "Chat dialog is not present"


@then("tap on chat dialog")
def tap_on_chat_dialog(student_session):
    student_session.tap_on_chat_dialog()


@then("verify that cursor should point to the first place of the text field")
def is_cursor_present(student_session):
    assert student_session.is_cursor_present(), "Cursor is not present and hence text field is not focused"


@then("verify smileys are disabled")
def is_emoji_class_present(student_session):
    assert not student_session.is_emoji_present(), "Emoji is present in chat box"


@then("verify device keypad should be enabled")
def verify_device_keypad_shown(student_session):
    student_session.is_keyboard_shown()


@then(parsers.parse('Enter text "{text}" in chat dialog'))
def enter_text(student_session, text):
    student_session.enter_text_in_chat(text)


@then(parsers.parse('verify user is able to enter the chat text "{text}"'))
def verify_user_able_to_enter_text(student_session, text):
    student_session.verify_entered_chat(text)


@then("tap on send button in the chat box")
def tap_on_send_button(student_session):
    student_session.tap_on_chat_send()


@then("tap on device back button")
def tap_device_back(student_session):
    student_session.click_back()


@then(parsers.parse('verify student able to view teacher message "{text}"'))
@then(parsers.parse('verify student is able to send the typed text "{text}" to tutor'))
def verify_user_sent_text(student_session, text):
    assert student_session.verify_message_at_student_side(text), "%s message is not present" % text


@then(parsers.parse('Paste the copied text "{text}" in the chat field'))
def enter_chat_text(student_session, text):
    student_session.enter_text_in_chat(text)


@then(parsers.parse('verify user is able to paste the text "{text}"'))
def paste_chat_text(student_session, text):
    student_session.verify_entered_chat(text)


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
    button_displayed = login_in.is_button_displayed(text)
    assert button_displayed is True, f"Button {text} is not displayed"


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
    login_in.is_offline_validation_layout_displayed()


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
    is_enabled = student_session.is_student_chat_enabled()
    assert is_enabled is False, "Live chat is not disabled"


@then("verify chat dialog should not be displayed")
def verify_student_chat_dialog_not_present(student_session):
    assert (not student_session.verify_student_chat_dialog()), "Chat dialog is present"


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
    assert (not login_in.text_match(text)), "%s text is displayed" % text


@then("close tutor session browser tab")
def close_mentor_session_tab(mentor_session):
    mentor_session.close_mentor_session_tab()


@given("reset student session if the session is incase completed")
def reset_session(driver):
    Stagingtlms(driver).reset_session()


@then("verify that videoplayer should not have any controls like seek bar,pause,play icons on the screen")
def is_video_play_pause_progress_bar_present(student_session):
    assert (not student_session.is_video_play_present()
            and not student_session.is_video_pause_progress_bar_present()
            and not student_session.is_video_progress_bar_present()), "seek bar,pause,play icons are present on the screen"


@when("verify elements in Tutor's chat window")
def verify_tutor_chat_window(mentor_session):
    mentor_session.verify_tutor_chat_window()


@then("Verify when student sends message student name is shown")
def verify_student_name(mentor_session):
    mentor_session.verify_student_name_present()


@then("Verify that Ban button , Approve button and Reject button is shown")
def verify_ban_approve_reject(mentor_session):
    mentor_session.verify_ban_approve_reject_present()


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
    mentor_session.verify_ban_options_and_buttons()


@then('Verify that Inappropriate Content should be selected by default')
def verify_default_ban_option(mentor_session):
    mentor_session.verify_default_ban_option()


@then('Verify that while clicking on Cancel button the pop-up should go off')
def verify_ban_cancel(mentor_session):
    mentor_session.verify_ban_cancel()


@then("Verify the while clicking outside of the pop-up it should go off")
def step_impl(mentor_session):
    mentor_session.verify_click_outside_ban_popup()


@then("Verify on clicking on Ban button user should be banned and banned student messages should not be shown")
def verify_ban_student(mentor_session):
    mentor_session.verify_ban_student()


@then("tap on the tick mark (approve button) in the message")
def tap_on_approve_message(mentor_session):
    mentor_session.tap_on_approve_message()


@then(parsers.parse('verify tutor received "{text}" message from student'))
@then(parsers.parse('Verify that the tutor is able to approve the message "{text}"'))
def tap_on_approve_message(mentor_session, text):
    assert mentor_session.is_message_present_for_tutor(text), "Student's message not present at tutor side"


@then(parsers.parse('Verify that the tutor is able to reject the message "{text}"'))
def tap_on_approve_message(mentor_session, text):
    assert not mentor_session.is_message_present_for_tutor(text), "student's message still present at tutor side"


@then('tap on "x" button(reject button) shown in the message')
def tap_on_reject_message(mentor_session):
    mentor_session.tap_on_reject_message()


@then(parsers.parse('verify that approved message "{text}" is shown in the other student chat window'))
def login_as_student2_and_verify_approved_msg(student_session, text):
    user_name = getdata(Login_Credentials, 'login_detail3', 'profile_one_to_many_and_mega')
    expected_text = user_name + " " + text
    assert student_session.verify_message_at_student_side(expected_text), "approved message is not present"


@then('login as another student who attends same session')
def login_as_student2(driver, login_in):
    HomePage(driver).login_as_another_one_mega_user(driver)
    login_in.click_on_premium_school()
    login_in.click_on_link('Premium School')


@then(parsers.parse('verify that rejected message "{text}" is not shown in the other student chat window'))
def verify_rejected_msg(student_session, text):
    user_name = getdata(Login_Credentials, 'login_detail3', 'profile_one_to_many_and_mega')
    expected_text = user_name + " " + text
    assert not student_session.verify_message_at_student_side(expected_text), "rejected message is  present"


@given('verify reset buffer time is completed')
def wait_for_reset_buffer_time_to_complete(mentor_session):
    mentor_session.wait_for_reset_buffer_time_to_complete()
