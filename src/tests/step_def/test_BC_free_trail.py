from pytest_bdd import scenarios, given, then, when, parsers
from pytest import fixture
from constants.platform import Platform
from pages.factory.login import LoginFactory
from pages.factory.ps_home_screen import PSHomescreenFactory
from pages.factory.trial_class import TrialClassFactory
from utilities.mentor_session import MentorSession
from utilities.staging_tlms import Stagingtlms
import pytest_check as check

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


@when("tap on back navigation icon")
@then("tap on back navigation icon")
def tap_device_back(trial_class):
    trial_class.back_navigation()


@then('verify "Recommended Classes" section is present')
def scroll_to_text(trial_class):
    details = trial_class.verify_rcmnded_section_ispresent()
    assert details.result, details.reason


@then('Verify that book option should display for free trial session')
@then('verify that user should get book option for free trial sessions in recommended section')
def verify_book_option_for_free_trail(trial_class):
    details = trial_class.is_book_present_for_free_trail_classes()
    assert details.result, details.reason


@then('verify that user should not be able to book multiple free trail session at same time')
def verify_book_option_for_multiple(trial_class):
    details = trial_class.is_book_present_for_free_trail_classes()
    assert not details.result, details.reason


@then('Verify that class is booked and user lands back on schedule/session page if booking is successful')
@then('Verify that user is able to book the session 30 mins before the session starts')
@then('Verify that user is able to book from available slots')
@then('verify that user booked the trial session')
def is_trial_class_booked(trial_class):
    details = trial_class.is_trial_class_booked()
    assert details.result, details.reason


@given('ensure tutor has started the session')
def start_tutor_session(mentor_session):
    mentor_session.start_tutor_session(course='ternary')


@then('user completes the session')
def tutor_taps_on_end_session(mentor_session):
    mentor_session.tutor_end_session()


@then('user book one trial class')
def book_trial_class(trial_class):
    trial_class.book_trial_class()


@then('verify free trail class should not be displayed in completed tab')
def is_upnext_trial_class_completed(trial_class):
    details = trial_class.is_upnext_trial_class_completed()
    assert details.result, details.reason


@then('verify that free trail completed card should displayed in For you section')
def verify_completed_trial_cards(trial_class):
    details = trial_class.verify_completed_trial_cards()
    assert details.result, details.reason


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
    details = trial_class.book_master_class(db)
    assert details.result, details.reason


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
    details = trial_class.delete_completed_sessions()
    assert details.result, details.reason


@given("launch the application online and login as expired user")
def login_as_expired_user(login_in):
    login_in.login_as_free_user()


@given('expire free trail subscriptions for user')
def expire_free_trail_subscriptions(trial_class):
    details = trial_class.expire_free_trail_subscriptions()
    assert details.result, details.reason


@then('verify expected message is shown once user reaches maximum free trail class limit')
def verify_free_trial_message(trial_class):
    details = trial_class.verify_free_trial_message()
    assert details.result, details.reason


@when('User in booking screen page')
def verify_booking_page(home_screen):
    details = home_screen.verify_booking_page()
    assert details.result, details.reason



@then('Verify that the free classes should available under regular class section.')
@then('Verift that free trial classes are availabe under Regular Classes section under booking screen')
def verify_free_trial_message(trial_class):
    details = trial_class.is_free_trial_class_present_under_reg_class()
    assert details.result, details.reason


@then('Verift that master classes are availabe under Master Classes section under booking screen')
def is_master_class_present_under_master_class_section(trial_class):
    details = trial_class.is_master_class_present_under_master_class_section()
    assert details.result, details.reason


@then('Verify that all availabe slots for subject/topic are listed on the tile as per zeplin UI')
@then('Verify that subject name and subject title should display in free regular class title')
@then('verify that Free class subject name, title name , time ,date, duration , other slots time , day should display.')
def verify_free_trial_class_details(trial_class):
    details = trial_class.is_free_trial_class_details_present_under_reg_class()
    assert details.result, details.reason


@then('Verify that subject name and subject title should display in Master class title')
def verify_subname_subtitle_of_master_class(trial_class):
    details = trial_class.is_master_class_details_present_under_master_class()
    assert details.result, details.reason


@when('Click on Book option for a regular class')
@when('try to book the session 30 mins before the session starts')
def click_on_book_option_for_reg_class(trial_class):
    trial_class.click_on_book_btn_reg_class()


@then('verify that class date and time selection popup should display when user click on book option.')
def verify_the_date_and_time_popup(trial_class):
    details = trial_class.is_date_and_time_popup_present()
    assert details.result, details.reason


@then("verify that 'confirm & book' and cancel option should display in the selection popup")
def verify_select_date_time_buttons(trial_class):
    details = trial_class.verify_select_date_time_buttons()
    assert details.result, details.reason


@when("click on 'Confirm & Book' button in the selection popup")
def click_on_confirm_and_book_btn(trial_class):
    trial_class.click_on_confirm_n_book_btn()


@when(parsers.parse("click on '{text}' button"))
def click_on_link(login_in, text):
    login_in.click_on_link(text)


@then('Verify that class is not booked and user lands back on booking page if cancel button is selected')
def trial_class_not_booked(trial_class):
    details = trial_class.is_trial_class_booked()
    assert not details.result, details.reason


@when('close the application')
def close_the_browser(trial_class):
    trial_class.close_application()


@when('re-login to application')
def re_login(login_in):
    login_in.navigate_to_home_screen()


@when('dismiss byjus classes book a free trail bottom sheet')
def dismiss_trail_popup(trial_class):
    trial_class.dismiss_trail_popup()


@when('book regular trial session')
def book_regular_trial_class(login_in, trial_class):
    trial_class.click_on_book_btn_reg_class()
    login_in.button_click("Confirm & Book")


@then('Verify that confirmation message should display when user book a session')
def verify_trial_class_confirmation_msg(trial_class):
    details = trial_class.verify_trial_class_confirmation_msg()
    assert details.result, details.reason


@then('Verify that session title , date , day , time should display.')
def verify_booking_screen(trial_class):
    details = trial_class.verify_booking_screen()
    assert details.result, details.reason


@then('Verify that timer should display in confirmation page , when user book a session.')
@then('Verify that session starts in time should display')
def verify_timer(trial_class):
    details = trial_class.verify_timer()
    assert details.result, details.reason


@then('Verify that okay button should display')
def verify_okay_button_present(trial_class):
    details = trial_class.verify_okay_button_present()
    assert details.result, details.reason


@then('verify that the the timer should display in HH.MM.SS format')
def verify_timer_format(trial_class):
    details = trial_class.verify_timer_format()
    assert details.result, details.reason


@then('Verify the slot avaliblity indicator(Filling Fast)')
def is_filling_fast_present(trial_class):
    details = trial_class.is_filling_fast_present()
    assert details.result, details.reason


@then('All unique sessions should have only one session card listed and should not be any duplicate session cards '
      'with same session name')
def is_card_unique_in_booking_page(trial_class):
    details = trial_class.is_trial_card_unique_in_booking_page()
    assert details.result, details.reason


@given('get current slot details from backend')
def get_free_course_details(driver):
    global course_details
    course_details = Stagingtlms(driver).get_free_course_details()


@then('Verify that correct slot is displayed on regular class date and time selection pop-up')
def verify_upnext_free_class_details(trial_class):
    trial_class.verify_upnext_free_class_details(course_details)


@given('add slot in backend which starts in less than 30 mins')
def add_slot(driver):
    global added_slot_time
    added_slot_time = Stagingtlms(driver).login_and_add_slot(minutes=-5, course_id=294)


@then('Verify that user is unable to book the session less than 30 mins before the session starts')
def is_free_trial_card_not_present(trial_class):
    trial_class.is_free_trial_card_not_present(added_slot_time)