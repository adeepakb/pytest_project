from pytest_bdd import scenarios, given, then, when, parsers
from pytest import fixture
from constants.platform import Platform
from pages.factory.login import LoginFactory
from pages.factory.neo_inclass_factory import NeoInClassFactory
import pytest_check as check
from utilities.neo_tute_mentoring import NeoTute

scenarios('../features/Celebrations.feature')


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

@then('click on thumb icon')
def step_impl(neo_in_class):
    neo_in_class.click_on_thumb_icon()

@then('Verify that the celebrations icon is present in mobile browser')
@then('Verify that student should be able to click celebrations option in website')
def step_impl(neo_in_class):
    details = neo_in_class.is_celebrations_icons_present()
    check.equal(details.result, True, details.reason)

@then('Verify that the celebrations icon is tappable in mobile browser')
@then('Verify that student should be able to see all 4 celebrations in website')
def step_impl(neo_in_class):
    details = neo_in_class.is_reactions_icons_present()
    check.equal(details.result, True, details.reason)

@then('Verify that when a student send celebration, other students should be able to see the same')
@then("Verify that when student tap on celebrations icon in website, same emoji's reaction keeps coming")
@then('Verify that 4 celebrations icon appear when student tap on celebration icon when logged in from mobile browser')
@then('Verify the emoji clicking once')
def step_impl(neo_in_class):
    ele_count = neo_in_class.get_the_no_of_elements()
    # neo_in_class.click_on_thumb_icon()
    neo_in_class.select_any_celebration_symbol('like')
    ele_count2 = neo_in_class.get_the_no_of_elements()
    check.greater(ele_count2, ele_count, "celebration is not clicked")


@then('Verify the emoji clicking multiple times')
@then('Verify that student should be able to tap all the 4 celebrations icon')
def step_impl(neo_in_class):
    neo_in_class.wait_until_enabled()
    neo_in_class.select_any_celebration_symbol('clap')
    neo_in_class.select_any_celebration_symbol('heart')
    neo_in_class.select_any_celebration_symbol('curious')
    neo_in_class.select_any_celebration_symbol('like')
    details = neo_in_class.is_floating_emojis_present()
    check.equal(details.result, True, details.reason)

# @then('Verify the emoji clicking multiple times')
# def step_impl(neo_in_class):
#     # neo_in_class.click_on_thumb_icon()
#     neo_in_class.select_any_celebration_symbol('Like')
#     details = neo_in_class.is_thumb_icon_present()
#     check.equal(details.result, False, details.reason)

@then('Verify the interval time after sending 5 emojis')
def step_impl(neo_in_class):
    neo_in_class.click_on_thumb_icon()
    neo_in_class.select_any_celebration_symbol('Like')
    details = neo_in_class.is_thumb_icon_present()
    check.equal(details.result, False, details.reason)


@then('Verify that set of 4 celebrations should close when student tap outside in mobile browser')
def step_impl(neo_in_class):
    neo_in_class.click_on_session_topic()
    details = neo_in_class.is_reactions_icons_present()
    check.equal(details.result, True, details.reason)


@then('Verify that the celebrations send by students should not reach Tutor side')
def step_impl(neo_in_class):
    neo_in_class.switch_to_alt_window()
    details = neo_in_class.is_floating_emojis_present()
    check.equal(details.result, False, details.reason)


@then('Verify that a student is able to send celebration 5 times')
def step_impl(neo_in_class):
    neo_in_class.select_any_celebration_symbol('like')
    neo_in_class.select_any_celebration_symbol('clap')
    neo_in_class.select_any_celebration_symbol('heart')
    neo_in_class.select_any_celebration_symbol('curious')
    neo_in_class.select_any_celebration_symbol('like')
    details = neo_in_class.is_floating_emojis_present()
    check.equal(details.result, True, details.reason)


@then('Verify that student should be able to send celebrations in flaky network')
def step_impl(neo_in_class):
    neo_in_class.set_network_flaky()
    neo_in_class.select_any_celebration_symbol('like')
    details = neo_in_class.is_floating_emojis_present()
    check.equal(details.result, False, details.reason)


@then('Verify the interval time after sending 5 emojis')
def step_impl(neo_in_class):
    neo_in_class.select_any_celebration_symbol('like')
    neo_in_class.select_any_celebration_symbol('clap')
    neo_in_class.select_any_celebration_symbol('heart')
    neo_in_class.select_any_celebration_symbol('curious')
    neo_in_class.select_any_celebration_symbol('like')
    details = neo_in_class.is_reaction_icon_disbled()
    check.equal(details.result, True, details.reason)
    neo_in_class.wait_until_enabled()
    details = neo_in_class.is_reaction_icon_disbled()
    check.equal(details.result, True, details.reason)

@then("Verify that when student tap on celebrations icon in mobile browser, same emoji's reaction keeps coming")
@then('Verify that same celebration icons are seen when student tap any specific celebration icon multiple times')
def step_impl(neo_in_class):
    neo_in_class.wait_until_enabled()
    neo_in_class.select_any_celebration_symbol('clap')
    neo_in_class.select_any_celebration_symbol('clap')
    neo_in_class.select_any_celebration_symbol('clap')
    details = neo_in_class.is_floating_emojis_present()
    check.equal(details.result, True, details.reason)

@then('Verify that user should  be able to send multiple celebrations when refresh')
def step_impl(neo_in_class):
    neo_in_class.refresh_and_join_the_session('mic-on', 'cam-on')
    neo_in_class.click_on_thumb_icon()
    neo_in_class.select_any_celebration_symbol('heart')
    neo_in_class.select_any_celebration_symbol('clap')
    details = neo_in_class.is_floating_emojis_present()
    check.equal(details.result, True, details.reason)
