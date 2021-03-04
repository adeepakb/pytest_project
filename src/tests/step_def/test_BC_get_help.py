from pytest_bdd import scenarios, given, then, when, parsers
from pytest import fixture
from Constants.platform import Platform
from POM_Pages.Factory.login import LoginFactory
from POM_Pages.Android_pages.homepage import HomePage
from POM_Pages.Factory.ps_home_screen import PSHomescreenFactory

scenarios('../features/Get Help.feature')


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


@given("Launch the app online")
def navigate_to_one_to_many_and_mega_user(driver):
    HomePage(driver).navigate_to_one_to_many_and_mega_user(driver)


@when("Click on the Premium school card in the home page")
def tap_on_premium_card(login_in):
    login_in.click_on_premium_school()


@when("navigate to one to mega homescreen")
def navigate_to_one_to_mega_homescreen(login_in):
    login_in.select_premium_school()


@then(parsers.parse('Verify that user navigates to "{text}" screen'))
@then(parsers.parse('Verify the text "{text}"'))
def verify_text(login_in, text):
    assert login_in.text_match(text), "%s text is not displayed " % text


@then("Tap on device/app back button")
def tap_device_back(home_screen):
    home_screen.click_back()

@then('verify get help button is responsive')
@then('tap on "Get help" button')
def tap_on_get_help(home_screen):
    home_screen.tap_on_get_help()


@then('Verify that quick help bottom sheet opens')
def verify_bottom_sheet(home_screen):
    assert home_screen.is_bottom_sheet_present(), "quick help bottom sheet did not show up"


@then('Tap on Cancel button')
def close_get_help(home_screen):
    home_screen.close_get_help()


@then('Verify that quick help bottom sheet goes off')
def verify_bottom_sheet_not_present(home_screen):
    assert not home_screen.is_bottom_sheet_present(), "quick help bottom sheet did not go off"



@then(parsers.parse('verify "{text}" button'))
def verify_button(home_screen, text):
    home_screen.verify_button(text)


@then('Verify that in landing screen get help link is present')
def is_get_help_present(home_screen):
    assert home_screen.is_get_help_present(), "Get help is not present"


@then('Verify App back button on left hand side of the screen')
def is_back_nav_present(home_screen):
    assert home_screen.is_back_nav_present(), "back navigation icon is not present"


@then(parsers.parse('tap on "{text}" button'))
def tap_button(login_in, text):
    button_status = login_in.button_click(text)
    assert button_status is True, "Unable to find {text} button"


@then('verify cancel icon is present on chat box')
def verify_get_help_close(home_screen):
    assert home_screen.verify_get_help_close(), "close icon is not present"


@then("tap outside chat layout")
def close_chat(home_screen):
    home_screen.tap_outside_dialog_layout()
