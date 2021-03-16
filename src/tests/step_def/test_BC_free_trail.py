from pytest_bdd import scenarios, given, then, when, parsers
from pytest import fixture
from constants.platform import Platform
from pom_pages.factory.login import LoginFactory
from pom_pages.android_pages.homepage import HomePage
from pom_pages.factory.ps_home_screen import PSHomescreenFactory

scenarios('../features/Multiple Free Trail Bookings.feature')


@fixture()
def login_in(request, driver):
    platform_list = 'ANDROID'
    # platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        login_in = LoginFactory().get_page(driver, Platform.ANDROID.value)
        yield login_in
    elif Platform.WEB.name in platform_list:
        login_in = LoginFactory().get_page(driver, Platform.WEB.value)
        yield login_in


@fixture()
def home_screen(request, driver):
    platform_list = 'ANDROID'
    # platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        home_screen = PSHomescreenFactory().get_page(driver, Platform.ANDROID.value)
        yield home_screen
    elif Platform.WEB.name in platform_list:
        home_screen = PSHomescreenFactory().get_page(driver, Platform.WEB.value)
        yield home_screen


@given(parsers.parse('post-requisite "{assessment_name}" should be tagged for the particular classroom session'))
def attach_post_requisite(home_screen, driver, assessment_name):
    home_screen.attach_post_requisite_with_assessement(driver, assessment_name)


@given("Launch the app online")
def navigate_to_one_to_many_and_mega_user(driver):
    HomePage(driver).navigate_to_one_to_many_and_mega_user(driver)


@when("tap on premium school card")
def tap_on_premium_card(login_in):
    login_in.click_on_premium_school()


@when("click on the hamburger menu")
def tap_on_premium_card(login_in):
    login_in.click_on_hamburger()


@when("navigate to one to mega homescreen")
def navigate_to_one_to_mega_homescreen(login_in):
    login_in.select_premium_school()


@then("verify the user is navigated to the PS screen")
def is_user_in_ps_page(home_screen):
    assert home_screen.is_user_in_ps_page(), "user is not in the PS screen"


@then('verify "Recommended Classes" section is present')
def scroll_to_text(home_screen):
    home_screen.scroll_to_text("Recommended Classes")


@then(parsers.parse('Verify the text "{text}"'))
def verify_text(login_in, text):
    assert login_in.text_match(text), "%s text is not displayed " % text


@then("Tap on device/app back button")
def tap_device_back(home_screen):
    home_screen.click_back()


@then(parsers.parse('verify "{text}" button'))
def verify_button(home_screen, text):
    assert home_screen.verify_button(text), "button is not present"


@then('Verify App back button on left hand side of the screen')
def is_back_nav_present(home_screen):
    assert home_screen.is_back_nav_present(), "back navigation icon is not present"


@then(parsers.parse('tap on "{text}" button'))
def tap_button(login_in, text):
    button_status = login_in.button_click(text)
    assert button_status is True, "Unable to find {text} button"


@then('verify that Free trial sessions should not be displayed in recommended section')
def is_book_button_present(home_screen):
    assert not home_screen.verify_button("Book"), "Free trial sessions is displayed in recommended section"


@then('verify that "3" is number of free trails to be booked')
def verify_three_trail_classes(home_screen):
    assert home_screen.verify_three_trail_classes() == 3, "Number of free trails to be booked is not 3"

@then('verify card details')
@then('Verify that For you tab contents are loading')
def verify_session_card_details(home_screen):
    home_screen.verify_card_details()

@then(parsers.parse('tap on "{text}" tab'))
def select_tab(home_screen, text):
    home_screen.tap_on_tab(text)
