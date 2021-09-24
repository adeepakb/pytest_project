from pytest_bdd import scenarios, given, then, when, parsers
from pytest import fixture
from constants.platform import Platform
from pages.factory.login import LoginFactory
from pages.factory.neo_inclass_factory import NeoInClassFactory
import pytest_check as check
from pages.web.multi_login import MultiLogin
from utilities.neo_tute_mentoring import NeoTute

scenarios('../features/In-Class.feature')


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


@given("Launch the application online")
def login_as_neo_user(login_in):
    login_in.login_and_navigate_to_home_screen('+91-', '2011313229', otp=None)
    # login_in.login_and_navigate_to_home_screen('+91-', '2016795330', otp=None)


@given("Launch the application online as 2nd user")
def login_as_neo_user(login_in):
    login_in.login_and_navigate_to_home('+91-', '2011313229', otp=None)
    MultiLogin(driver).login_and_navigate_to_home_screen('+91-', '2011313229', otp=None)

@given("Launch the application online in mobile")
def login_as_neo_user(login_in):
    login_in.login_for_neo_class_mobile('+91-', '2016795330', otp=None)


@given("tutor start the session")
def step_impl(driver):
    NeoTute(driver).start_neo_session()

@when('join neo session')
@then('join neo session')
def join_a_neo_class(neo_in_class):
    neo_in_class.home_click_on_join()

@when('click on start class')
@then('click on start class')
def join_a_neo_session(neo_in_class):
    # neo_in_class.switch_to_alt_window('window_before')
    neo_in_class.join_neo_session_student('mic-on', 'cam-on')

@then('Verify the display of Focus mode icon')
def step_impl(neo_in_class):
    details = neo_in_class.is_focus_mode_icon_present()
    check.equal(details.result, True, details.reason)

@then('Verify the display of student count icon in mobile view')
@then('Verify the display of student count icon ')
def step_impl(neo_in_class):
    details = neo_in_class.verify_student_count()
    check.equal(details.result, True, details.reason)

@then('Verify the text Hand Raised in mobile browser')
def step_impl(neo_in_class):
    neo_in_class.raise_hand()
    details = neo_in_class.verify_hand_is_raised()
    check.equal(details.result, True, details.reason)


@then('Verify the display of student cards in mobile view')
def step_impl(neo_in_class):
    neo_in_class.get_students_from_stream_card()

@then('Verify display of subject/ Topicname/focus mode in mobile browser')
def step_impl(neo_in_class):
    details = neo_in_class.verify_session_topic_name_inclass()
    check.equal(details.result, True, details.reason)

@then('Verify the display of weak signal icon in mobile browser')
def step_impl(neo_in_class):
    neo_in_class.set_network_flaky()
    details = neo_in_class.verify_weak_signal_on_screen()
    check.equal(details.result, True, details.reason)

@then('Verify the display of controls in fullscreen mode')
def step_impl(neo_in_class):
    neo_in_class.do_full_screen_presentation()
    details = neo_in_class.verify_controls_on_full_screen()
    check.equal(details.result, True, details.reason)