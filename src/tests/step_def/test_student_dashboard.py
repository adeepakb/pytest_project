from pytest import fixture
from pytest_bdd import scenarios, given, when, then, parsers
from selenium.common.exceptions import NoSuchElementException

from POM_Pages.application_login import Login
from POM_Pages.dropdown_month_select import DropDownSelect
from POM_Pages.session_popup import SessionAlert
from POM_Pages.student_dashboard import StudentDashboard
from Utilities.tutor_common_methods import TutorCommonMethods

feature_file_name = 'student_dashboard'

scenarios('../features/' + feature_file_name + '.feature')


@fixture
def std_board(browser):
    stud_b = StudentDashboard(browser)
    yield stud_b


@fixture
def login_in(browser):
    login_in = Login(browser)
    yield login_in


@given('Clean launch the tutor app online')
def clean_launch_app():
    TutorCommonMethods.execute_command('adb shell pm clear com.byjus.tutorplus')


@given('navigate to one to many student dashboard screen')
def given_navigate_dashboard_screen(login_in, browser):
    try:
        login_in.click_on_premium_school()
        pop_up_displayed = SessionAlert(browser)
        pop_up_displayed.cancel_join_session()
    except AssertionError:
        login_in.click_on_one_to_many()


@when('navigate to one to many student dashboard screen')
def navigate_dashboard_screen(login_in, browser):
    try:
        login_in.click_on_premium_school()
        pop_up_displayed = SessionAlert(browser)
        pop_up_displayed.cancel_join_session()
    except AssertionError:
        login_in.click_on_one_to_many()


@given('Launch the tutor app online')
def launch_app(login_in):
    login_in.implicit_wait_for(15)


@when('verify by default "UP NEXT" session card should be selected')
@then('verify by default "UP NEXT" session card should be selected')
def verify_up_next_selected(std_board):
    card_selected = std_board.is_up_next_card_selected()
    assert card_selected is True, "UP NEXT label may not be displayed or chapter name does not match"


@when('tap on any session card')
@then('tap on any session card')
def tap_on_random_card(std_board):
    std_board.random_card().click()


@then('tap on Retry button')
def tap_on_retry(std_board):
    std_board.tap_button_retry()


@then('verify respective session details are loaded')
def verify_session_details_card_all(std_board):
    details_match = std_board.verify_session_details()
    assert details_match is True, "Details dosen't not match."


@then('switch on the device data')
def switch_connectivity_on(std_board):
    std_board.toggle_wifi_connection('on')


@then('Launch the app again')
def app_re_launch(login_in):
    login_in.switch_back_to_app()


@given('Verify that user is landed on login screen')
def given_login_screen_displayed(login_in):
    login_screen = login_in.is_login_form_displayed()
    assert login_screen is True, "Login page is not displayed"


@when('Enter registered mobile number in mobile number field')
def enter_reg_number(login_in):
    login_in.enter_reg_mobile_number()


@when('Verify that user is landed on login screen')
@then('Verify that user is landed on login screen')
def login_screen_displayed(login_in):
    login_screen = login_in.is_login_form_displayed()
    assert login_screen is True, "Login page is not displayed"


@given(parsers.parse('"{text}" all the app permissions'))
def set_all_permissions(login_in, text):
    login_in.allow_deny_permission([text, text, text])


@then(parsers.parse('tap on "{text}" button'))
@when(parsers.parse('tap on "{text}" button'))
def tap_button(login_in, text):
    button_status = login_in.button_click(text)
    assert button_status is True, f"Unable to find {text} button"


@when('verify auto verify bottom sheet dialog is displayed')
@then('verify auto verify bottom sheet dialog is displayed')
def verify_otp_auto_verify_dialog_box(login_in):
    login_in.implicit_wait_for(0)
    try:
        login_in.click_on_link('Login with OTP')
    except NoSuchElementException:
        pass
    dialog_box_displayed = login_in.is_auto_otp_dialog_box_displayed()
    login_in.implicit_wait_for(15)
    assert dialog_box_displayed, "Auto Verification is not present"


@when('enter a valid otp in the otp field')
def enter_valid_otp(login_in):
    login_in.enter_otp()


@then('minimize the app by tapping on device back button')
def tap_on_device_back_btn(login_in):
    login_in.tap_bck_btn()


@when('verify user is landed on one to many student dashboard screen')
@then('verify user is landed on one to many student dashboard screen')
def verify_one_to_many_dashboard(login_in):
    screen_displayed = login_in.is_one_to_many_dashboard_displayed()
    assert screen_displayed is True, "Student one to many dashboard is not displayed"


@then('verify user is landed on one to many student dashboard')
def then_verify_one_to_many_dashboard(login_in, browser):
    verify_one_to_many_dashboard(login_in)


@then(parsers.parse('verify Byjus icon followed by "{text}" text'))
def verify_icon_and_text(std_board, text):
    std_board.image_text_verification()
    std_board.text_verify_classroom(text)


@then(parsers.parse('verify "{text}" Month \'YY text'))
def verify_session_text(std_board, text):
    std_board.check_month_header_format(text)


@then('verify by default current month should be selected')
def verify_current_month_selected(std_board):
    current_month_displayed = std_board.verify_current_month()
    assert current_month_displayed is True, "Current month does not match or might not be in the view."


@then('verify profile avatar')
def verify_profile_avatar(std_board):
    avatar_displayed = std_board.is_profile_avatar_displayed()
    assert avatar_displayed is True, "Logo is not displayed or may not be in view."


@then('verify previous sessions cards are displayed')
def verify_attended_cards_displayed(std_board):
    attend_card_displayed = std_board.is_attended_cards_displayed()
    assert attend_card_displayed is True, "Student has not completed any session."


@then('verify Future session cards are displayed')
def verify_unattnd_cards_displayed(std_board):
    not_attnd_cards = std_board.is_attended_cards_not_displayed()
    assert not_attnd_cards is True, "Either all sessions are taken or unattended cards might not properly displayed"


@then('verify SESSION DETAILS card is displayed')
def verify_session_details_displayed(std_board):
    session_dtls_card_displayed = std_board.is_session_details_card_displayed()
    assert session_dtls_card_displayed is True, "Details card is not displayed."


@then('verify subject icon in session card')
def verify_subject_icon(std_board):
    subjects_icon_displayed = std_board.is_cards_subjects_icon_displayed()
    assert subjects_icon_displayed is True, "One or more card(s) subject icon may not be displayed."


@then('verify subject name in the session card is displayed')
def verify_subject_name(std_board):
    subject_name_displayed = std_board.is_cards_subjects_name_displayed()
    assert subject_name_displayed is True, "One or more card(s) subject name may not be displayed."


@then('verify topic name in the session card is displayed')
def verify_topic_name(std_board):
    topic_name_displayed = std_board.is_cards_topic_name_displayed()
    assert topic_name_displayed is True, "One or more card(s) topic name may not be displayed."


@then('verify DD MMM, DAY,HH:MM AM/PM details are displayed')
def verify_schedule_details_displayed(std_board):
    s_details_displayed = std_board.is_cards_schedule_details_displayed()
    assert s_details_displayed is True, "Schedule details may not be in specified format."


@then('verify Rate Session option is displayed')
def verify_rate_session_displayed(std_board):
    rate_session_displayed = std_board.is_cards_rate_session_displayed()
    assert rate_session_displayed is True, "User may not took yet any session."


@then(parsers.parse('verify text "{text}"'))
def verify_text(std_board, text):
    text_displayed = std_board.verify_is_text_displayed(text)
    assert text_displayed is True, f"The text {text} is not displayed."


@then('verify subject name is displayed')
def verify_session_dtls_subj_name(std_board):
    subj_displayed = std_board.is_subject_name_displayed()
    assert subj_displayed is True, "The subject name is not displayed."


@then('verify topic name is displayed')
def verify_session_dtls_topic_name(std_board):
    topic_name = std_board.is_topic_name_displayed()
    assert topic_name is True, "The topic name is not displayed"


@then('verify calender icon followed by date format DD MMM,Day is displayed')
def verify_calendar_icon_and_details(std_board):
    calendar_details = std_board.is_calendar_details_displayed()
    assert calendar_details is True, "Calendar details is not displayed correctly."


@then('verify time icon followed by HH:MM AM/PM details are displayed')
def verify_time_icon_and_details(std_board):
    time_details = std_board.is_time_details_displayed()
    assert time_details is True, "Time details is not displayed correctly."


@then('verify topic description')
def verify_topic_desc_details(std_board):
    topic_desc_displayed = std_board.is_topic_desc_displayed()
    assert topic_desc_displayed, "Topic description not displayed."


@then('verify Change topic card is displayed if session starts in post 2 days')
def verify_card_detail_change_topic(std_board):
    change_topic_card_displayed = std_board.is_choose_topic_displayed()
    assert change_topic_card_displayed, "OPPS! 'Choose Topic' card not displayed."


@then('verify Your session starts in with day is displayed if session starts within 2 days')
def verify_session_starts_text_displayed(std_board):
    session_starts_text = std_board.is_sessions_starts_in_displayed()
    assert session_starts_text == 'Your session starts in', "Content 'Your session starts in' is not displayed."


@then('verify session starts timer is displayed if session starts within 24 hours')
def verify_timer_displayed(std_board):
    timer_displayed = std_board.is_timer_displayed()
    assert timer_displayed is True, "Timer is not displayed."


@when('switch off the device data')
def switch_connectivity_off(std_board):
    while True:
        msg = std_board.is_one_to_many_screen_displayed()
        if msg:
            break
    std_board.toggle_wifi_connection('off')


@then(parsers.parse('verify "{text}" text should be displayed on card'))
def check_session_details_card_text(std_board, text):
    msg_displayed = std_board.is_wifi_relevant_msg_displayed(text)
    assert msg_displayed is True, "Message is not displayed."


@then(parsers.parse('verify "{text}" text is displayed'))
def check_valid_message_session_details(std_board, text):
    msg_displayed = std_board.is_wifi_relevant_msg_displayed(text)
    assert msg_displayed is True, "Relevant message is not displayed."


@then('verify Retry button should be displayed')
def verify_retry_button(login_in):
    button_displayed = login_in.is_button_displayed("Retry")
    assert button_displayed is True, f"Button Retry is not displayed"
