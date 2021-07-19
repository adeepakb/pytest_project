from pytest_bdd import scenarios, given, then, when, parsers
from pytest import fixture
from constants.platform import Platform
from pages.factory.login import LoginFactory
from pages.android.homepage import HomePage
from utilities.staging_tlms import Stagingtlms
from pages.factory.ps_home_screen import PSHomescreenFactory
import pytest_check as check

scenarios('../features/Premium School Home Screen.feature')


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
def home_screen(request, driver):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        home_screen = PSHomescreenFactory().get_page(driver, Platform.ANDROID.value)
        yield home_screen
    elif Platform.WEB.name in platform_list:
        home_screen = PSHomescreenFactory().get_page(driver, Platform.WEB.value)
        yield home_screen


@given(parsers.parse('post-requisite "{assessment_name}" should be tagged for the particular classroom session'))
def attach_post_requisite(home_screen, driver, assessment_name):
    home_screen.attach_post_requisite(driver, assessment_name)


@given("Launch the app online")
def navigate_to_one_to_many_and_mega_user(driver):
    HomePage(driver).navigate_to_one_to_many_and_mega_user(driver)


@when("Click on the Premium school card in the home page")
def tap_on_premium_card(login_in):
    login_in.click_on_premium_school()


@when("navigate to one to mega homescreen")
def navigate_to_one_to_mega_homescreen(login_in):
    login_in.select_premium_school()


@then(parsers.parse('Verify that "{text}" tab is highlighted by default'))
def is_tab_selected(home_screen, text):
    details = home_screen.is_tab_selected(text)
    check.equal(details.result, True, details.reason)


@then(parsers.parse('Verify that "{text}" shown in the prerequisites card'))
@then(parsers.parse('Verify that user navigates to "{text}" screen'))
@then(parsers.parse('Verify the text "{text}"'))
@then(parsers.parse('Verify that "{text}" Badge on top right hand side of the screen'))
def verify_text(login_in, text):
    details = login_in.text_match(text)
    check.equal(details.result, True, details.reason)


@then(parsers.parse('Verify the Video card along with Video Name "{text1}" and the text "{text2}" along with Video '
                    'icon and forward Arrow button'))
def verify_post_req_video_elements(login_in, home_screen, text1, text2):
    details_1 =login_in.text_match(text1)
    check.equal(details_1.result, True, details_1.reason)
    details_2 = login_in.text_match(text2)
    check.equal(details_2.result, True, details_2.reason)
    details_3 = home_screen.verify_arrow_present_for_each_requisite()
    check.equal(details_3.result,True,details_3.reason)


@then(parsers.parse('Verify "{text1}" and "{text2}" tabs'))
def verify_tabs(home_screen, text1, text2):
    details_1 = home_screen.verify_ps_tabs(text1)
    check.equal(details_1.result,True,details_1.reason)
    details_2 = home_screen.verify_ps_tabs(text2)
    check.equal(details_2.result, True,details_2.reason)


@then("Tap on device/app back button")
def tap_device_back(home_screen):
    home_screen.click_back()


@then('tap on "Get help" button')
def tap_on_get_help(home_screen):
    home_screen.tap_on_get_help()


@then('Verify that quick help bottom sheet opens')
def verify_bottom_sheet(home_screen):
    details = home_screen.is_bottom_sheet_present()
    check.equal(details.result, True,details.reason)


@then('Tap on Cancel button')
def close_get_help(home_screen):
    home_screen.close_get_help()


@then('Verify that quick help bottom sheet goes off')
def verify_bottom_sheet_not_present(home_screen):
    details = home_screen.is_bottom_sheet_present()
    check.equal(details.result, False, details.reason)


@then(parsers.parse('tap on "{text}" tab'))
def select_tab(home_screen, text):
    home_screen.tap_on_tab(text)


@then(parsers.parse('verify that user is able to switch between "{text1}" and "{text2}" tabs'))
def select_tab(home_screen, text1, text2):
    home_screen.tap_on_tab(text1)
    details_1 = home_screen.is_tab_selected(text1)
    check.equal(details_1.result,True,details_1.reason)
    home_screen.tap_on_tab(text2)
    details_2 = home_screen.is_tab_selected(text2)
    check.equal(details_2.result,True,details_2.reason)


@then('verify card details')
@then('Verify that For you tab contents are loading')
def verify_session_card_details(home_screen):
    home_screen.verify_card_details()


@given("reset student session if the session is incase completed")
def reset_session(driver):
    Stagingtlms(driver).reset_session()


@when(parsers.parse('verify "{text}" button'))
@then(parsers.parse('verify "{text}" button'))
def verify_button(home_screen, text):
    details = home_screen.verify_button(text)
    check.equal(details.result, True, details.reason)


@then('Verify that Completed sessions tab contents are loading')
@then('Verify the completed session card along with Subject Name, topic Name and the text "Completed" with date and the '
    'session rating given by the user in stars followed by the numeric')
def verify_completed_card_details(home_screen):
    details_dict = home_screen.verify_completed_card_details()
    condition = all(v is not None for v in [details_dict['Subject'], details_dict['Topic'], details_dict['Schedule Date'],details_dict['Session status']]) and details_dict['Session status'] == "Completed"
    check.equal(condition,True,"Completed Session card details not loaded")

@then('Verify Get help button')
def is_get_help_present(home_screen):
    details = home_screen.is_get_help_present()
    check.equal(details.result,True,details.reason)


@then('Verify App back button on left hand side of the screen')
def is_back_nav_present(home_screen):
    details = home_screen.is_back_nav_present()
    check.equal(details.result,True,details.reason)


@then(parsers.parse('tap on "{text}" button'))
def tap_button(login_in, text):
    button_status = login_in.button_click(text)
    check.equal(button_status.result, True, button_status.reason)


@when("verify user is in BYJU's Classes pop up screen")
def verify_bottom_sheet(home_screen):
    details = home_screen.verify_bottom_sheet()
    check.equal(details.result,True,details.reason)


@then('verify byjus classes banner is present')
def verify_banner(home_screen):
    details = home_screen.verify_banner()
    check.equal(details.result,True,details.reason)


@given('clear cache and login')
def reset_and_login_with_otp(driver):
    HomePage(driver).reset_and_login_with_otp(driver)


@when(parsers.parse('tap on "{name}" text'))
def tap_on_link(login_in,name):
    login_in.click_on_link(name)


@then('verify that user navigates to home screen')
def verify_home_screen(home_screen):
    home_screen.verify_home_screen()