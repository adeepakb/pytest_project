import pytest
from pytest_bdd import scenarios, given, then, when, parsers
from constants.platform import Platform
from pages.factory.login import LoginFactory
from pytest import fixture
import pytest_check as check

from utilities.interrupt import set_connection_type

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
        login = Login().get_page(driver, Platform.ANDROID.value)
        yield login
    else:
        raise NotImplementedError()


@given("user is in Premium login screen")
@given('Launch the app online and Navigate to Premium Login screen.')
@given('Launch the app online and Navigate to Login screen')
@given('Launch the app online and navigate to Login screen')
@given("Navigate to Login screen")
@when("Navigate to Login screen")
@when("User Navigate to Login screen")
@given("User Navigate to Login screen")
@given("User navigates to Login screen")
@when("User navigates to Login screen")
@given("Navigate to Premium Login screen")
def tap_on_premium_card(login):
    if login.toggle_wifi_connection('on'):
        login.driver.close_app()
        login.driver.activate_app(login.driver.capabilities['appPackage'])
    login.implicit_wait_for(15)
    login.navigate_to_login_screen()


@given("launch the app online.")
@given('Launch the app online')
def launch_app(login):
    if login.toggle_wifi_connection('on'):
        login.driver.close_app()
        login.driver.activate_app(login.driver.capabilities['appPackage'])
    login.implicit_wait_for(15)


@given("Launch the app in offline")
def launch_app(login):
    if login.toggle_wifi_connection('on'):
        login.driver.close_app()
        login.driver.activate_app(login.driver.capabilities['appPackage'])
    login.implicit_wait_for(15)
    set_connection_type(login.driver, "OFFLINE")


@then(parsers.re('"(?P<text>(.*))" button.*'))
@then(parsers.re('Verify the "(?P<text>(.*))" button is shown.*'))
@then(parsers.re('verify the text "(?P<text>(.*))"..*'))
@then(parsers.re('Verify the text "(?P<text>(.*))"..*'))
@then(parsers.re('Verify the "(?P<text>(.*))" text.*'))
@then(parsers.re('Verify the "(?P<text>(.*))" text is shown.*'))
@then(parsers.re('Verify the text "(?P<text>(.*))" is shown.*'))
@then(parsers.re('verify the "(?P<text>(.*))" text.*'))
def verify_text(login, text):
    details = login.verify_login_screen_elements(text=text)
    check.equal(details.result, True, details.reason)


@then(parsers.re('Verify "(?P<text>(.*))" link.*'))
@then(parsers.re('Verify "(?P<text>(.*))" button.*'))
@then(parsers.re('Verify the "(?P<text>(.*))" Button.*'))
def verify_text(login, text):
    details = login.verify_login_screen_elements(text=text)
    check.equal(details.result, True, details.reason)


@then("verify that the Mobile Number text field is shown.")
def verify_text(login):
    details = login.verify_login_screen_elements(text='Mobile Number text field')
    check.equal(details.result, True, details.reason)


@then("verify that auto-filled country code drop-down field is shown.")
@given("Mobile Number field with auto filled country code")
@then("Mobile Number field with auto filled country code")
def verify_text(login):
    details = login.verify_login_screen_elements(text='autofill')
    check.equal(details.result, True, details.reason)


@then('Verify the "Byjus the learning app" app icon.')
def verify_text(login):
    details = login.verify_login_screen_elements(text='icon')
    check.equal(details.result, True, details.reason)


@given("Device id is not saved in server")
@given('User is new to the app and device ID is not saved in the server')
def step_impl(login):
    details = login.clear_app_data_and_relaunch_the_app()
    check.equal(details.result, True, details.reason)


@when('On Login screen tap on country code drop down')
@when('User taps on Country Code menu')
def step_impl(login):
    login.click_on_country_code_dropdown()


@then('Verify Country Code should be a drop down menu')
def step_impl(login):
    details = login.is_dropdown_displayed_without_clicking()
    check.equal(details.result, True, details.reason)


@then('By default "India(+91)" should be selected in the drop down menu.')
def step_impl(login):
    details = login.is_default_country_in_dropdown()
    check.equal(details.result, True, details.reason)


# @then('select any  from the drop down')
# @when('select any  from the drop down')
# def verify_text(login):
#     login.select_country_code(expected_text="Kuwait")
#     print()


@then(parsers.re(
    'verify these listed countries are displayed first and in the same order as mentioned "(?P<text>(.*))".*'))
def step_impl(login, text):
    details = login.verify_country_codes_in_dropdown(text=text)
    check.equal(details.result, True, details.reason)


@then('verify all the  other countries apart from 8 are displayed in Alphabetical order')
def step_impl(login):
    details = login.verify_country_codes_in_dropdown_in_alphabetical_manner()
    check.equal(details.result, True, details.reason)


@then('Verify numeric keypad gets activated')
def step_impl(login):
    details = login.is_numeric_pad_displayed()
    check.equal(details.result, True, details.reason)


@when('User taps on Mobile Number field')
def step_impl(login):
    login.click_on_mobile_number_field()


@then("should accept only Numeric values")
def step_impl(login):
    details = login.check_numeric_input_in_phone()
    check.equal(details.result, True, details.reason)


@then('Verify error message "Please enter valid mobile number" is displayed below mobile number field')
def step_impl(login):
    check.equal(login.validate_error_msg(expected_text='Please enter valid mobile number'), True,
                "Error message is not shown or invalid")


@when("Enters  Mobile Number field")
def enter_invalid_phone_number(login):
    login.enter_phone(phone_num="12345")


@when("User enters valid  having multiple accounts")
@when("User enters valid")
def enter_valid_phone_number(login):
    mob = login.user_mobile
    login.enter_phone(phone_num=mob)


@when("enters  in Mobile Number field")
def enter_invalid_phone_number(login):
    login.enter_phone(phone_num="1234567890121233")


@given("taps on Next Button")
@when("taps on Next Button")
@then(parsers.parse('tap on "NEXT" button'))
def click_on_next(login_in):
    login_in.click_on_next()


@then("Verify for the new users mobile number Field should be empty on Login Screen.")
def step_impl(login):
    details = login.phone_number_field_is_empty()
    check.equal(details.result, True, details.reason)


@given("Device id is saved in server")
def step_impl(login):
    details = login.login_for_new_user()
    check.equal(details.result, True, details.reason)
    details = login.log_out_from_home_page_or_login_page()
    check.equal(details.result, True, details.reason)


@then("Previously logged in user  should be prefilled on Login Screen")
def step_impl(login):
    details = login.check_mobile_number_field_is_prefilled_with_previous_logged_in_account()
    check.equal(details.result, True, details.reason)


@then("User should navigate to LoginOTPVerificationScreen")
def step_impl(login):
    details = login.is_otp_screen_shown()
    check.equal(details.result, True, details.reason)


@when("taps on Device back button")
@then("taps on Device back button")
def step_impl(login):
    login.tap_bck_btn()


@then("Verify app should be closed")
@then("Verify  should be closed")
def step_impl(login):
    details = login.is_app_on_screen()
    check.equal(details.result, False, details.reason)


@given(parsers.parse("User enters {number} in Mobile Number Field"))
@given(parsers.parse("User enters {number} in Mobile Number Field"))
@when("User enters  in Mobile Number Field")
@given("User enters  in Mobile Number Field")
def step_impl(login):
    login.enter_phone(phone_num='9875643247')


@when("Tap on 'Byjus the Learning App' icon")
@when("Tap on 'Byjus the Learning App' icon.")
@when("Tap on 'Byjus the Learning App' icon .")
def step_impl(login):
    login.tap_on_byju_icon()


@then(
    "Verify that tapping on 'Byjus the Learning App' app icon, navigates the user to Play store 'Byju's The Learning App.'")
def step_impl(login):
    details = login.user_navigates_to_play_store()
    check.equal(details.result, True, details.reason)


@when("enter valid otp in Verify OTP Screen.")
@then("enter valid otp in Verify OTP Screen")
@when("enter valid otp in Verify OTP Screen")
@then("enter valid OTP in OTP field")
def enter_otp(login):
    login.enter_otp(login.otp)


@then("The bottom sheet appears.")
@when("The bottom sheet is displayed.")
@when('Verify the "This phone number is not registered with a premium account" bottom sheet dialog.')
@then("The bottom sheet is displayed.")
@then('Verify the "This phone number is not registered with a premium account" bottom sheet dialog.')
def step_impl(login):
    details = login.verify_login_screen_elements(text="This phone number is not registered with a premium account")
    check.equal(details.result, True, details.reason)


@then("Verify that the bottom sheet is dismissed.")
@then('Verify "Phone number is not registered with a premium account" bottom sheet dialog dismissed')
def step_impl(login):
    details = login.verify_login_screen_elements(text="This phone number is not registered with a premium account")
    check.equal(details.result, False, details.reason)


@then('tap outside the dialog')
def step_impl(login):
    login.close_dropdown()


@then('login screen should be displayed.')
def step_impl(login):
    login.verify_login_screen()


@then(parsers.parse("tap on '{text}' button"))
@then(parsers.parse('tap on "{text}" link'))
@when(parsers.parse('tap on "{text}" link'))
@when(parsers.parse("tap on '{text}' link"))
@when(parsers.parse("tap on the '{text}' button"))
@then(parsers.parse("tap on the '{text}' button"))
@when(parsers.parse('tap on "{text}" button'))
@then(parsers.parse('tap on "{text}" button'))
def step_impl(login, text):
    login.tap_on_button(text=text)


@then('Verify user is redirected to Premium Login screen with empty user mobile number field.')
def step_impl(login):
    details = login.verify_login_screen()
    check.equal(details.result, True, details.reason)
    details = login.phone_number_field_is_empty()
    check.equal(details.result, True, details.reason)


@then('Verify user is redirected to Phone dialer with Phone number prefilled(+91-9241333666)')
def step_impl(login):
    details = login.verify_dialer()
    check.equal(details.result, True, details.reason)
    details = login.verify_dialer_with_number(number="+91 9241333666")
    check.equal(details.result, True, details.reason)


@when("navigates to a sibling screen.")
@then("navigates to a sibling screen.")
@when("navigates to Siblings screen.")
@then("navigates to Siblings screen.")
@when("navigates to sibling page.")
@then("navigates to sibling page.")
@then("Verify that User navigates to Sibling page having below mentioned text.")
@then("Verify that User navigates to Sibling screen which list multiple accounts")
def step_impl(login):
    details = login.verify_sibling_screen()
    check.equal(details.result, True, details.reason)


@then("Verify that User navigates to Sibling page having list of accounts with name and grade")
def step_impl(login):
    details = login.verify_sibling_screen_profiles()
    check.equal(details.result, True, details.reason)


@then("Verify that the radio button is present for users having multiple accounts in the sibling screen.")
def step_impl(login):
    details = login.verify_sibling_screen_radio_buttons()
    check.equal(details.result, True, details.reason)


@then("Verify that user clicks on 'Continue' button without selecting the account, it will display error toast "
      "message as 'Please select account to Login'.")
def step_impl(login):
    details= login.click_on_continue_button()
    check.equal(details.result, True, details.reason)
    details = login.verify_sibling_screen()
    check.equal(details.result, True, details.reason)


@when("Click on 'Continue' button")
@then("Click on 'Continue' button")
def step_impl(login):
    details= login.click_on_continue_button()
    check.equal(details.result, True, details.reason)


@then('Select the account from the list of multiple accounts.')
@when('Select the account from the list of multiple accounts.')
def step_impl(login):
    login.switch_profile()


@when('navigates Welcome Screen')
@then('Verify the user navigates Welcome Screen')
def step_impl(login):
    details =login.verify_welcome_screen_text()
    check.equal(details.result, True, details.reason)


@then("Verify the user should be navigating to Home Screen")
def step_impl(login):
    login.verify_home_screen()


@when("select any  from the drop down")
@then("select any  from the drop down")
def step_impl(login):
    login.select_country_code("+682")



@then("Verify selected  should be shown in country code field")
def step_impl(login):
    login.verify_country_code(country_code="+682")



