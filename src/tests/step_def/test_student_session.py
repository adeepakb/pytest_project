from pytest_bdd import scenarios, given, then, when, parsers
from pytest import fixture
from POM_Pages.application_login import Login
from POM_Pages.student_session import StudentSession
from POM_Pages.session_popup import SessionAlert
from POM_Pages.mentor_session import MentorSession
from POM_Pages.staging_tlms import Stagingtlms
from POM_Pages.homepage import HomePage, Login_Credentials, getdata

scenarios('../features/Join Session  and  Chat.feature')


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


@then(parsers.parse('verify student is able to send the typed text "{text}" to tutor'))
def verify_user_sent_text(student_session, text):
    student_session.verify_student_sent_text(text)


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
    student_session.verify_student_sent_text(text)


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
def switch_off_data(login_in, student_session, text):
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


@given("ensure that tutor has joined the session and has enabled audio and video of student")
def start_tutor_session_and_enable_tutor_video_and_audio(mentor_session):
    mentor_session.start_tutor_session()
    mentor_session.enable_student_audio_and_video_by_global_controls()


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


@given("ensure that tutor has joined the session and has disabled tutor video")
def start_tutor_session_and_disable_tutor_video(mentor_session):
    mentor_session.start_tutor_session()
    mentor_session.disable_tutor_video()


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


@given(parsers.parse('ensure that tutor has joined the session and send message "{text}" in chat to students'))
def start_tutor_session_and_tutor_send_message_in_chat(mentor_session, text):
    mentor_session.start_tutor_session()
    mentor_session.send_message_in_chat(text)


@then("send around 8 messages")
def student_send_multiple_messages(student_session):
    global text_list
    text_list = ["1!Maths", "2@Chemistry", "3#Physics", "4$Biology", "5%Computer_Science", "6^English", "7&Hindi",
                 "8*(Economics)"]
    for i in range(len(text_list)):
        student_session.tap_on_chat_textbox()
        student_session.tap_on_chat_dialog()
        student_session.enter_text_in_chat(text_list[i])
        student_session.tap_on_chat_send()


@then("scroll the live chat")
def scroll_live_chat(student_session):
    student_session.scroll_chat_container()


@then("verify student scrolled the chat window and last message is visible")
def is_message_visible(student_session):
    flag = student_session.is_student_sent_text_visible(text_list[7])
    assert flag, "Student scrolled the chat window and " \
                 "last message is visible verification failed"


@then('tutor ends session')
def tutor_taps_on_end_session(mentor_session):
    mentor_session.tutor_end_session()


@then(parsers.parse('verify "{text}" bottom sheet dialog is not shown'))
def bottom_dialog_not_shown(login_in, text):
    assert (not login_in.text_match(text)), "%s text is displayed" % text


@then("close tutor session browser tab")
def close_mentor_session_tab(mentor_session):
    mentor_session.close_mentor_session_tab()


@given("reset student session")
def reset_session(driver):
    Stagingtlms(driver).reset_session()


@then("verify that videoplayer should not have any controls like seek bar,pause,play icons on the screen")
def is_video_play_pause_progress_bar_present(student_session):
    assert (not student_session.is_video_play_present()
            and not student_session.is_video_pause_progress_bar_present()
            and not student_session.is_video_progress_bar_present()),"seek bar,pause,play icons are present on the screen"
