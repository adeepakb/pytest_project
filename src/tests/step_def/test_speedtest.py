from pytest_bdd import scenarios, given, then, when, parsers
from pytest import fixture
from selenium.common.exceptions import StaleElementReferenceException
from POM_Pages.application_login import Login
from POM_Pages.student_session import StudentSession
from POM_Pages.session_popup import SessionAlert
from POM_Pages.speedtest import SpeedTest
from POM_Pages.homepage import HomePage

scenarios('../features/bandwidth_test.feature')


@fixture
def login_in(browser):
    login_in = Login(browser)
    yield login_in


@fixture()
def speed_test(browser):
    speed_test = SpeedTest(browser)
    yield speed_test


@given("navigate to home page and verify student profile")
def verify_student_session(browser, login_in):
    HomePage(browser).navigate_to_one_to_many_user(browser)
    login_in.click_on_premium_school()


@when('user taps on join session button')
@when(parsers.parse('user should be in speedtest screen'))
def join_session(browser, login_in):
    StudentSession(browser).download_materials_for_session()
    StudentSession(browser).cancel_join_session_dialog()
    login_in.button_click("Join Now")


@then("capture speed test screen")
def capture_speedtest_screen(login_in, speed_test):
    speed_test.capture_speedtest_screen()


@then(parsers.parse('Verify "{text}" text is present'))
def verify_text_present(speed_test, browser, text):
    speed_test.verify_text_present(text)


@then("verify AppBack button")
def verify_back_navigation(speed_test):
    speed_test.verify_appback_button()


@then(parsers.parse('verify "{text}" text'))
def verify_view_text_present(speed_test, text):
    speed_test.verify_view_text_present(text)


@then(parsers.parse('verify "{text}" button'))
def verify_button(speed_test, text):
    speed_test.verify_button(text)


@then("verify that while clicking on the Join button student should navigate to session welcome screen")
def join_session_and_verify_welcome_screen(login_in, browser):
    try:
        StudentSession(browser).speed_test()
        StudentSession(browser).is_tutor_icon_displayed()
        login_in.text_match("Welcome")
        login_in.text_match("Waiting for tutor to join the session")
    except StaleElementReferenceException:
        pass


@then("verify that while clicking on the app back button should navigate to app home screen")
def verify_session_card_details_loaded(login_in, speed_test, browser):
    speed_test.tap_on_appback_button()
    # verify user is back in classroom dashboard
    login_in.text_match("Classroom")


@then(parsers.parse('verify "{text}" text after the speedtest success'))
def text_match(speed_test, text):
    speed_test.text_match_after_speedtest_success(text)


@then(parsers.parse('switch "{text}" the device data'))
def switch_off_data(browser, text):
    Login(browser).toggle_wifi_connection(text)


@then(parsers.parse('verify "{text}" text should be displayed'))
def text_verify(login_in, text):
    text = text.format().encode('utf-8').decode('unicode_escape')
    assert login_in.text_match(text) is True, f"the text {text} does not match any elements"


@then(parsers.parse('tap on "{text}" button'))
def tap_button(login_in, text):
    button_status = login_in.button_click(text)
    assert button_status is True, "Unable to find {text} button"


@then("verify offline related bottom sheet dialog should disappear")
def verify_offline_dialog_sheet_disappeared(speed_test):
    speed_test.verify_offline_dialog_disappeared()


@then("tap outside the dialog layout")
def tap_outside_dialog_layout(speed_test):
    speed_test.tap_outside_dialog_layout()


@given(parsers.parse('send put request for one_to_many_skip_speed_test "{value1}" '
                     'and one_to_many_skip_speed_test_result "{value2}"'))
def send_put_request(speed_test, value1, value2):
    speed_test.send_put_request((value1.lower() == 'true'), (value2.lower() == 'true'))


@then("verify speed test is skipped")
def is_speed_test_screen_not_present(speed_test):
    assert (not speed_test.is_speed_test_screen_present()), "Speed test screen is present"


@given("clear app from recents and relaunch app")
def clear_app_from_recents(speed_test):
    speed_test.clear_app_from_recents_and_relaunch()


@then("verify speed test is not skipped")
def is_speed_test_screen_present(speed_test):
    assert (speed_test.is_speed_test_screen_present()), "Speed test screen is not present"


@then("verify speed test screen supports portrait mode for mobile devices")
def verify_portrait_mode(speed_test):
    speed_test.verify_portrait_mode()
