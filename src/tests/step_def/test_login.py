import pytest
from pytest_bdd import scenarios, given, then, when, parsers
from constants.platform import Platform
from pom_pages.factory.login import LoginFactory

scenarios('../features/Login.feature')


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

@given("Launch the platform")
def navigate_to_one_to_many_and_mega_user(login_in):
    login_in.launch_and_navigate_to_login_page()


@when("enter valid mobile number in sign in page")
def enter_phone_number(login_in):
    login_in.enter_phone()


@then(parsers.parse('tap on "NEXT" button'))
def click_on_next(login_in):
    login_in.click_on_next()


@then("enter valid OTP in OTP field")
def enter_otp(login_in):
    login_in.enter_otp()


@then('verify is navigated to byjus home page successfully')
def verify_home_page(login_in):
    assert login_in.verify_home_page_loaded(), "User is not in byjus home page"


@when("Click on the Premium school card in the home page")
def tap_on_premium_card(login_in):
    login_in.click_on_premium_school()
