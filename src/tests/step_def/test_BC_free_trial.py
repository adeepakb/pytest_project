from pytest_bdd import scenarios, given, then, when, parsers
from pytest import fixture
from constants.platform import Platform
from pages.factory.login import LoginFactory
from pages.factory.ps_home_screen import PSHomescreenFactory
from pages.factory.trial_class import TrialClassFactory
from utilities.mentor_session import MentorSession
from utilities.staging_tllms import Stagingtllms

scenarios('../features/Multiple Free Trail Bookings.feature')


class Context:
    pass


@fixture
def db():
    context = Context()
    yield context


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
def trial_class(request, driver):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        trial_class = TrialClassFactory().get_page(driver, Platform.ANDROID.value)
        yield trial_class
    elif Platform.WEB.name in platform_list:
        trial_class = TrialClassFactory().get_page(driver, Platform.WEB.value)
        yield trial_class


@fixture
def mentor_session(driver):
    mentor_session = MentorSession(driver)
    yield mentor_session


@given("launch the application online")
def navigate_to_one_to_many_and_mega_user(login_in):
    login_in.navigate_to_home_screen()


@when("tap on byjus classes card")
@then("tap on byjus classes card")
def tap_on_premium_card(login_in):
    login_in.click_on_premium_school()


@when("click on the hamburger menu")
def click_on_hamburger_menu(login_in):
    login_in.click_on_hamburger()


@then("verify the user is navigated to the PS screen")
def is_user_in_ps_page(home_screen):
    assert home_screen.is_user_in_ps_page(), "user is not in the PS screen"


@then(parsers.parse('tap on "{text}" button'))
def tap_button(login_in, text):
    button_status = login_in.button_click(text)
    assert button_status is True, "Unable to find {text} button"


@then("tap on back navigation icon")
def tap_device_back(trial_class):
    trial_class.back_navigation()


@then('verify "Recommended Classes" section is present')
def scroll_to_text(trial_class):
    trial_class.verify_rcmnded_section_ispresent()


@then('verify that user should get book option for free trial sessions in recommended section')
def verify_book_option_for_free_trail(trial_class):
    details = trial_class.is_book_present_for_free_trail_classes()
    assert details.result, details.reason


@then('verify that user should not be able to book multiple free trail session at same time')
def verify_book_option_for_multiple(trial_class):
    details = trial_class.is_book_present_for_free_trail_classes()
    assert not details.result, details.reason


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


@then('verify free trail class should not be displayed in completed tab')
def is_upnext_trial_class_completed(trial_class):
    details = trial_class.is_upnext_trial_class_completed()
    assert details.result, details.reason


@then('verify that free trail completed card should displayed in For you section')
def verify_completed_trial_cards(trial_class):
    assert trial_class.verify_completed_trial_cards(), "completed trial card message is not displayed"


@then('verify that masterclasses are scheduled should be displayed in recommended section')
def is_master_class_present(trial_class):
    details = trial_class.is_master_class_present()
    assert details.result, details.reason


@then('verify that no master card available to book')
def is_master_class_present(trial_class):
    details = trial_class.is_master_class_present()
    assert not details.result, details.reason


@then('verify that user missed booked session')
def verify_user_missed_session(trial_class):
    details = trial_class.verify_user_missed_session()
    assert details.result, details.reason


@then('book masterclass session')
@then('Verify that user can book multiple masterclass sessions')
def book_multiple_master_class(trial_class, db):
    assert trial_class.book_master_class(db), "Master class was not booked"


@then('book special master class')
def book_special_master_class(trial_class):
    trial_class.book_special_master_class()


@then('verify that user should get Rebook option')
def is_rebook_option_available(home_screen):
    assert home_screen.verify_button("Rebook"), "Rebook button is not displayed"


@then('verify that user should get autobook option')
def is_autobook_present(trial_class):
    details = trial_class.is_autobook_present()
    assert details.result, details.reason


@given('reset completed free trial and masterclass sessions')
def delete_completed_sessions(trial_class):
    assert trial_class.delete_completed_sessions() == 200, "free trial sessions reset is unsuccessful"


@given("launch the application online and login as expired user")
def login_as_expired_user(login_in):
    login_in.login_as_free_user()


@given('expire free trail subscriptions for user')
def expire_free_trail_subscriptions(trial_class):
    assert trial_class.expire_free_trail_subscriptions() == 200, "free trial subscription expire is unsuccessful"


@then('verify expected message is shown once user reaches maximum free trail class limit')
def verify_free_trial_message(trial_class):
    assert trial_class.verify_free_trial_message(), "expected message is not displayed"

# @then(parsers.parse('Verify the text "{text}"'))
# def verify_text(login_in, text):
#     assert login_in.text_match(text), "%s text is not displayed " % text
#
#
# @then(parsers.parse('verify "{text}" button'))
# def verify_button(home_screen, text):
#     assert home_screen.verify_button(text), "button is not present"
