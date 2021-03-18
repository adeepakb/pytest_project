from pytest_bdd import scenarios, given, then, when, parsers
from pytest import fixture
from constants.platform import Platform
from pom_pages.factory.login import LoginFactory
from pom_pages.android_pages.homepage import HomePage
from pom_pages.factory.ps_home_screen import PSHomescreenFactory
from pom_pages.android_pages.trialclass import TrailClass
from utilities.mentor_session import MentorSession
from utilities.staging_tlms import Stagingtlms

scenarios('../features/Multiple Free Trail Bookings.feature')


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


@fixture()
def trail_class(request, driver):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        trail_class = TrailClass(driver)
        yield trail_class


@given("Launch the app online")
def navigate_to_one_to_many_and_mega_user(driver):
    # HomePage(driver).navigate_to_one_to_many_and_mega_user(driver)
    pass


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


@then(parsers.parse('Verify the text "{text}"'))
def verify_text(login_in, text):
    assert login_in.text_match(text), "%s text is not displayed " % text


@then(parsers.parse('verify "{text}" button'))
def verify_button(home_screen, text):
    assert home_screen.verify_button(text), "button is not present"


@then(parsers.parse('tap on "{text}" button'))
def tap_button(login_in, text):
    button_status = login_in.button_click(text)
    assert button_status is True, "Unable to find {text} button"


@then('verify "Recommended Classes" section is present')
def scroll_to_text(home_screen):
    home_screen.scroll_to_text("Recommended Classes")


@then('verify that user should get book option for free trial sessions in recommended section')
def verify_book_option_for_free_trail(trail_class):
    assert trail_class.is_book_present_for_free_trail_classes(), "book option is not displayed for free trial sessions in recommended section"


@then('verify that user booked the trial session')
def is_trail_class_booked(trail_class):
    is_present = trail_class.is_trail_class_booked()
    assert is_present, "verify that user booked free trial session"


@then('verify that until user completes session')
def tutor_taps_on_end_session(driver):
    MentorSession(driver).start_tutor_session()
    MentorSession(driver).tutor_end_session()


@when('verify and add slot for master class booking')
def step_impl(driver):
    Stagingtlms(driver).verify_and_add_slot()
