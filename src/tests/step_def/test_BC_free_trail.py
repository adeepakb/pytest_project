from pytest_bdd import scenarios, given, then, when, parsers
from pytest import fixture
from constants.platform import Platform
from pages.factory.login import LoginFactory
from pages.android.homepage import HomePage
from pages.factory.ps_home_screen import PSHomescreenFactory
from pages.android.trialclass import TrailClass
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


class Context:
    pass


@fixture
def db():
    context = Context()
    yield context


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
def trial_class(request, driver):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        trial_class = TrailClass(driver)
        yield trial_class


@fixture
def mentor_session(driver):
    mentor_session = MentorSession(driver)
    yield mentor_session


@given("Launch the application online")
def navigate_to_one_to_many_and_mega_user(driver):
    HomePage(driver).navigate_to_home_screen(driver)
    # HomePage(driver).navigate_to_one_to_many_and_mega_user(driver)


@given("launch the application online and login as expired user")
def login_as_expired_user(driver):
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


@then("tap on back navigation icon")
def tap_device_back(dashboard):
    dashboard.back_navigation()

@then('verify "Recommended Classes" section is present')
def scroll_to_text(home_screen):
    home_screen.scroll_to_text("Recommended Classes")


@then('verify that user should get book option for free trial sessions in recommended section')
def verify_book_option_for_free_trail(trial_class):
    assert trial_class.is_book_present_for_free_trail_classes(), "book option is not displayed for free trial sessions in recommended section"


@then('verify that user should not be able to book multiple free trail session at same time')
def verify_book_option_for_multiple(trial_class):
    assert not trial_class.is_book_present_for_free_trail_classes(), "user able to book multiple free trail session at a time"


@then('verify that user booked the trial session')
def is_trial_class_booked(trial_class):
    is_present = trial_class.is_trial_class_booked()
    assert is_present, "verify that user booked free trial session"


@given('ensure tutor has started the session')
def start_tutor_session(mentor_session):
    mentor_session.start_tutor_session(course='ternary')


@then('user completes the session')
def tutor_taps_on_end_session(mentor_session):
    mentor_session.tutor_end_session()

@given('verify and add slot for trial class booking')
def step_impl(driver):
    Stagingtlms(driver).verify_and_add_slot()


@then('user book one trial class')
def book_trial_class(trial_class):
    trial_class.book_trial_class()


@then('verify that user booked the trial session')
def is_trail_class_booked(trial_class):
    assert trial_class.is_trial_class_booked(), "Trial class is not booked"


@then('verify free trail class should not be displayed in completed tab')
def select_tab(trial_class):
    assert not trial_class.is_upnext_trial_class_completed(), "free trail class is displayed in completed tab"


@then('verify that free trail completed card should displayed in For you section')
def verify_completed_trial_cards(login_in):
    assert login_in.text_match("Completed your free trial class?"), " text is not displayed"
    assert login_in.text_match("Explore our free workshops!"), " text is not displayed"


@then('verify that masterclasses are scheduled should be displayed in recommended section')
def is_master_class_present(trial_class):
    assert trial_class.is_master_class_present(), "Masterclasses are scheduled not displayed in recommended section"


@then('verify that user missed booked session')
def verify_user_missed_session(trial_class):
    assert trial_class.verify_user_missed_session(), "No missed booked session present"


@then('book masterclass session')
@then('Verify that user can book multiple masterclass sessions')
def book_multiple_master_class(trial_class, db):
    assert trial_class.book_master_class(db), "Master class was not booked"


@then('verify that user should get Rebook option')
def is_rebook_option_available(home_screen):
    assert home_screen.verify_button("Rebook"), "Rebook button is not displayed"


@then('verify that user should get autobook option')
def is_autobook_present(trial_class):
    assert trial_class.is_autobook_present(), "autobook option is not present"


@given('reset completed free trial and masterclass sessions')
def delete_completed_sessions(trial_class):
    assert trial_class.delete_completed_sessions() == 200, "free trial sessions reset is unsuccessful"
