import pytest
from pytest_bdd import scenarios, given, then, when, parsers
from constants.platform import Platform
from pages.factory.login import LoginFactory
from pytest import fixture
scenarios('../features/Login Screen.feature')


@pytest.fixture()
def login_in(request, driver):
    # please provide platform based on enum names
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        login_in = LoginFactory().get_page(driver, Platform.ANDROID.value)
        yield login_in
    elif Platform.WEB.name in platform_list:
        login_in = LoginFactory().get_page(driver, Platform.WEB.value)
        yield login_in

@fixture
def login(driver, request):
    platform_list = request.config.getoption("platform")
    from pages.factory.application_login_factory import Login
    if Platform.ANDROID.name.lower() == platform_list[-1].lower():
        login_in = Login().get_page(driver, Platform.ANDROID.value)
        yield login_in
    else:
        raise NotImplementedError()

@given("Navigate to Login screen")
@when("Navigate to Login screen")
def tap_on_premium_card(login):
    if login.toggle_wifi_connection('on'):
        login.driver.close_app()
        login.driver.activate_app(login.driver.capabilities['appPackage'])
    login.implicit_wait_for(15)
    login.navigate_to_login_screen()


@given('Launch the app online')
def launch_app(login):
    if login.toggle_wifi_connection('on'):
        login.driver.close_app()
        login.driver.activate_app(login.driver.capabilities['appPackage'])
    login.implicit_wait_for(15)
