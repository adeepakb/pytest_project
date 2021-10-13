from pytest_bdd import scenarios
from pytest_bdd import scenarios, given, then, when, parsers
from pytest import fixture
import pytest_check as check
from constants.constants import Login_Credentials
from constants.load_json import get_data
from constants.platform import Platform
from pages.factory.login import LoginFactory
from pages.factory.neo_inclass_factory import NeoInClassFactory

scenarios('../features/Pre_Class.feature')


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


@given("launch the application online as neo user and navigate to home screen")
def step_impl(student1_login):
    student1_details = get_data(Login_Credentials, 'neo_login_detail1', 'student1')
    student1_login.login_and_navigate_to_home_screen(student1_details['code'], student1_details['mobile_no'], otp=None)


@when("student join neo session for next day")
@given("student join neo session for next day")
def step_impl(student1_neo):
    student1_neo.navigate_to_byjus_classes_screen()
    student1_neo.join_not_started_session()


@then("Verify the Student's greeting message on the landing screen.")
def step_impl(student1_neo):
    student1_details = get_data(Login_Credentials, 'neo_login_detail1', 'student1')
    student_name = student1_details['name']
    details = student1_neo.preclass_verify_greeting_message(name = student_name)
    check.equal(details.result, True, details.reason)


@then("Verify the list of students bubble on the screen before the class starts.")
def step_impl(student1_neo):
    details = student1_neo.preclass_verify_bubbles()
    check.equal(details.result, True, details.reason)