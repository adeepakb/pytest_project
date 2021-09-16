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
    login_in.login_for_neo_class_mobile('+91-', '2011313229', otp=None)


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
    neo_in_class.join_neo_session_student()
