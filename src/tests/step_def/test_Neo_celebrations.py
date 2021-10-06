from pytest_bdd import scenarios, given, then, when, parsers
from pytest import fixture
from constants.platform import Platform
from pages.factory.login import LoginFactory
from pages.factory.neo_inclass_factory import NeoInClassFactory
from constants.constants import Login_Credentials
from constants.load_json import get_data
import pytest_check as check
from utilities.neo_tute_mentoring import NeoTute

scenarios('../features/Celebrations.feature')

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
    student1_details = get_data(Login_Credentials, 'neo_login_detail3', 'student1')
    student1_login.login_and_navigate_to_home_screen(student1_details['code'], student1_details['mobile_no'], otp=None)


@given("Launch the application online in mobile")
def login_as_neo_user(student1_login):
    student1_login.login_for_neo_class_mweb('+91-', '2011313229', otp=None)

@given("tutor start the session")
def step_impl(neo_tute):
    neo_tute.start_neo_session(login_data="neo_login_detail3", user='student1')


@when('join neo session')
@then('join neo session')
def join_a_neo_class(student1_neo):
    student1_neo.home_click_on_join()

@when('click on start class')
@then('click on start class')
def join_a_neo_session(student1_neo):
    student1_neo.join_neo_session_student('mic-on', 'cam-on')

@then('click on thumb icon')
def step_impl(student1_neo):
    student1_neo.click_on_thumb_icon()

@then('Verify that the celebrations icon is present in mobile browser')
@then('Verify that student should be able to click celebrations option in website')
def step_impl(student1_neo):
    details = student1_neo.is_celebrations_icons_present()
    check.equal(details.result, True, details.reason)

@then('Verify that the celebrations icon is tappable in mobile browser')
@then('Verify that student should be able to see all 4 celebrations in website')
def step_impl(student1_neo):
    details = student1_neo.is_reactions_icons_present()
    check.equal(details.result, True, details.reason)

@then('Verify that when a student send celebration, other students should be able to see the same')
@then("Verify that when student tap on celebrations icon in website, same emoji's reaction keeps coming")
@then('Verify that 4 celebrations icon appear when student tap on celebration icon when logged in from mobile browser')
@then('Verify the emoji clicking once')
def step_impl(student1_neo):
    # ele_count = student1_neo.get_the_no_of_elements()
    student1_neo.select_any_celebration_symbol('like')
    details = student1_neo.is_floating_emojis_present()
    check.equal(details.result, True, details.reason)


@then('Verify the emoji clicking multiple times')
@then('Verify that student should be able to tap all the 4 celebrations icon')
def step_impl(student1_neo):
    student1_neo.select_any_celebration_symbol('clap')
    student1_neo.select_any_celebration_symbol('heart')
    student1_neo.select_any_celebration_symbol('curious')
    student1_neo.select_any_celebration_symbol('like')
    details = student1_neo.is_floating_emojis_present()
    check.equal(details.result, True, details.reason)


@then('Verify the interval time after sending 5 emojis')
def step_impl(student1_neo):
    student1_neo.click_on_thumb_icon()
    student1_neo.select_any_celebration_symbol('Like')
    details = student1_neo.is_thumb_icon_present()
    check.equal(details.result, False, details.reason)


@then('Verify that set of 4 celebrations should close when student tap outside in mobile browser')
def step_impl(student1_neo):
    student1_neo.click_on_session_topic()
    details = student1_neo.is_reactions_icons_present()
    check.equal(details.result, False, details.reason)


@then('Verify that the celebrations send by students should not reach Tutor side')
def step_impl(neo_tute):
    details = neo_tute.is_floating_emojis_present_in_tute()
    check.equal(details.result, False, details.reason)


@then('Verify that a student is able to send celebration 5 times')
def step_impl(student1_neo):
    student1_neo.select_any_celebration_symbol('like')
    student1_neo.select_any_celebration_symbol('clap')
    student1_neo.select_any_celebration_symbol('heart')
    student1_neo.select_any_celebration_symbol('curious')
    student1_neo.select_any_celebration_symbol('like')
    details = student1_neo.is_floating_emojis_present()
    check.equal(details.result, True, details.reason)


@then('Verify that student should be able to send celebrations in flaky network')
def step_impl(student1_neo):
    student1_neo.set_network_flaky()
    student1_neo.select_any_celebration_symbol('like')
    details = student1_neo.is_floating_emojis_present()
    check.equal(details.result, True, details.reason)


@then('Verify the interval time after sending 5 emojis')
def step_impl(student1_neo):
    student1_neo.select_any_celebration_symbol('like')
    student1_neo.select_any_celebration_symbol('clap')
    student1_neo.select_any_celebration_symbol('heart')
    student1_neo.select_any_celebration_symbol('curious')
    student1_neo.select_any_celebration_symbol('like')
    details = student1_neo.is_reaction_icon_disbled()
    check.equal(details.result, True, details.reason)
    # details = student1_neo.is_reaction_icon_disbled()
    # check.equal(details.result, True, details.reason)

@then("Verify that when student tap on celebrations icon in mobile browser, same emoji's reaction keeps coming")
@then('Verify that same celebration icons are seen when student tap any specific celebration icon multiple times')
def step_impl(student1_neo):
    student1_neo.select_any_celebration_symbol('clap')
    student1_neo.select_any_celebration_symbol('clap')
    student1_neo.select_any_celebration_symbol('clap')
    details = student1_neo.is_floating_emojis_present()
    check.equal(details.result, True, details.reason)

@then('Verify that user should  be able to send multiple celebrations when refresh')
def step_impl(student1_neo):
    student1_neo.refresh_and_join_the_session('mic-on', 'cam-on')
    student1_neo.click_on_thumb_icon()
    student1_neo.select_any_celebration_symbol('heart')
    student1_neo.select_any_celebration_symbol('clap')
    details = student1_neo.is_floating_emojis_present()
    check.equal(details.result, True, details.reason)

@then('Verify that when a student send celebration, other students should be able to see the same')
def step_impl(student1_neo,student2,student2_neo):
    student2.login_and_navigate_to_home_screen('+91-', '2016170445', otp=None)
    student2_neo.home_click_on_join()
    student2_neo.join_neo_session_student('mic-on', 'cam-on')
    student1_neo.select_any_celebration_symbol('clap')
    student1_neo.select_any_celebration_symbol('clap')
    student1_neo.select_any_celebration_symbol('clap')
    student1_neo.select_any_celebration_symbol('clap')
    student1_neo.select_any_celebration_symbol('clap')
    details = student2_neo.is_floating_emojis_present()
    check.equal(details.result, True, details.reason)

@then('Verify user should not be able to send emojis in interval while switching multiple tabs')
def step_impl(student1_neo,student2_neo):
    student1_neo.select_any_celebration_symbol('clap')
    student1_neo.select_any_celebration_symbol('clap')
    student2_neo.select_any_celebration_symbol('clap')
    student2_neo.select_any_celebration_symbol('clap')
    student1_neo.select_any_celebration_symbol('clap')
    student2_neo.select_any_celebration_symbol('clap')
    details = student2_neo.is_floating_emojis_present()
    check.equal(details.result, False, details.reason)