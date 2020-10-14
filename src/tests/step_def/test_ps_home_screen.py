from pytest_bdd import scenarios, given, then, when, parsers
from pytest import fixture
from POM_Pages.application_login import Login
from POM_Pages.ps_home_screen import PS_Homescreen
from POM_Pages.homepage import HomePage

scenarios('../features/Premium School Home Screen.feature')


@fixture
def login_in(driver):
    login_in = Login(driver)
    yield login_in


@fixture
def home_screen(driver):
    home_screen = PS_Homescreen(driver)
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


@then(parsers.parse('Verify that "{text}" tab is highlighted by default'))
def is_tab_selected(home_screen, text):
    home_screen.is_tab_selected(text), text + " tab is not selected"


@then(parsers.parse('Verify that user navigates to "{text}" screen'))
@then(parsers.parse('Verify the text "{text}"'))
@then(parsers.parse('Verify that "{text}" Badge on top right hand side of the screen'))
def verify_text(login_in, text):
    assert login_in.text_match(text), "%s text is not displayed " % text


@then(parsers.parse('Verify "{text1}" and "{text2}" tabs'))
def verify_tabs(home_screen, text1, text2):
    home_screen.verify_ps_tabs(text1)
    home_screen.verify_ps_tabs(text2)


@then("Tap on device/app back button")
def tap_device_back(home_screen):
    home_screen.click_back()


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


@then(parsers.parse('tap on "{text}" tab'))
def select_tab(home_screen, text):
    home_screen.tap_on_tab(text)


@then(parsers.parse('verify that user is able to switch between "{text1}" and "{text2}" tabs'))
def select_tab(home_screen, text1, text2):
    home_screen.tap_on_tab(text1)
    assert home_screen.is_tab_selected(text1), text1 + " tab is not selected"
    home_screen.tap_on_tab(text2)
    home_screen.is_tab_selected(text2), text2 + " tab is not selected"


@then('verify card details')
@then('Verify that For you tab contents are loading')
def verify_session_card_details(home_screen):
    home_screen.verify_card_details()


@then(parsers.parse('verify "{text}" button'))
def verify_button(home_screen, text):
    home_screen.verify_button(text)


@then(
    'Verify the upcoming session details card is showed along with Subject name,Topic Name,Date,Month,day of the week and time.')
def verify_session_details_card_loaded(home_screen):
    home_screen.verify_session_details_card_loaded()


@then('Verify that Completed sessions tab contents are loading')
@then(
    'Verify the completed session card along with Subject Name, topic Name and the text "Completed" with date and the session rating given by the user in stars followed by the numeric')
def verify_completed_card_details(home_screen):
    home_screen.verify_completed_card_details()


@then('Verify Get help button')
def is_get_help_present(home_screen):
    assert home_screen.is_get_help_present(), "Get help is not present"


@then('Verify App back button on left hand side of the screen')
def is_back_nav_present(home_screen):
    assert home_screen.is_back_nav_present(), "back navigation icon is not present"


@then(parsers.parse('tap on "{text}" button'))
def tap_button(login_in, text):
    button_status = login_in.button_click(text)
    assert button_status is True, "Unable to find {text} button"
