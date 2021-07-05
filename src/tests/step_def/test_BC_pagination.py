from pytest_bdd import scenarios, given, then, when, parsers
from pytest import fixture
from constants.platform import Platform
from pages.android.session_popup import SessionAlert
from pages.android.student_dashboard_otm import StudentDashboardOneToMega
from pages.factory.classnotes import ClassNotesFactory
from pages.factory.login import LoginFactory
from pages.android.homepage import HomePage
from pages.factory.ps_home_screen import PSHomescreenFactory
import pytest_check as check
from pages.factory.trial_class import TrialClassFactory
from utilities.mentor_session import MentorSession
from utilities.staging_tlms import Stagingtlms

scenarios('../features/Pagination.feature')


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

@fixture()
def classnotes(request, driver):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        classnotes = ClassNotesFactory().get_page(driver, Platform.ANDROID.value)
        yield classnotes
    elif Platform.WEB.name in platform_list:
        classnotes = ClassNotesFactory().get_page(driver, Platform.WEB.value)
        yield classnotes

@fixture
def mentor_session(driver):
    mentor_session = MentorSession(driver)
    yield mentor_session


@given("launch the application online")
def navigate_to_one_to_many_and_mega_user(driver):
    HomePage(driver).navigate_to_one_to_many_and_mega_user(driver)


@when("tap on byjus classes card")
def tap_on_premium_card(login_in):
    login_in.click_on_premium_school()


@when("navigate to one to mega homescreen")
def navigate_to_one_to_mega_homescreen(login_in):
    login_in.select_premium_school()


@then("verify the user is navigated to the PS screen")
def is_user_in_ps_page(home_screen):
    details = home_screen.is_user_in_ps_page()
    check.equal(details.result, True, details.reason)


@then("verify that 2 upcoming session cards are shown")
def verify_upcoming_session(home_screen):
    details = home_screen.verify_two_upcoming_sessions_present()
    check.equal(details.result, True, details.reason)


@then('verify that See all option with down arrow present')
def verify_see_all_present(home_screen):
    details = home_screen.verify_see_all_present()
    check.equal(details.result, True, details.reason)


@then(parsers.parse('switch "{text}" the device data'))
def switch_off_data(login_in, text):
    login_in.toggle_wifi_connection(text)


@then('tap on See all option')
def tap_on_see_all(home_screen):
    home_screen.tap_on_see_all()


@then(parsers.parse('verify that navigates to "{text}" screen'))
@then(parsers.parse('verify that "{text}" option present on the card'))
@then(parsers.parse('verify "{text}" should be displayed'))
def verify_text_is_present(login_in, text):
    details = login_in.text_match(text)
    check.equal(details.result, True, details.reason)


@then(parsers.parse('verify "{text}" button should be displayed'))
def button_verify(login_in, text):
    details = login_in.is_button_displayed(text)
    check.equal(details.result, True, details.reason)


@then(parsers.parse('verify "{text}" button is not displayed'))
def button_verify(login_in, text):
    details = login_in.is_button_displayed(text)
    check.equal(details.result, False, details.reason)


@then(parsers.parse('tap on "{text}" button'))
def tap_button(login_in, text):
    login_in.button_click(text)


@then('get session details')
def get_details(driver):
    global details_dict
    details_dict = SessionAlert(driver).content_card_loaded()
    print(details_dict)


@then('verify completed session moved to Completed tab')
def verify_session_moved_to_completed_tab(home_screen, driver):
    home_screen.tap_on_tab('Completed')
    session_details = SessionAlert(driver).content_card_loaded()
    check.equal(details_dict, session_details,"Completed session not present under Completed tab")


@then('verify that the session cards in upnext and for you should be identical with session details, requisites, requisites status')
def verify_session_cards( driver):
    session_details = SessionAlert(driver).content_card_loaded()
    check.equal(details_dict, session_details,"verify that the session cards in upnext and for you not be identical with session details, requisites, requisites status")


@then('user should land on up next screen')
def verify_up_next_screen(home_screen):
    details = home_screen.verify_up_next_screen()
    check.equal(details.result, True, details.reason)


@then('verify that each page will load with 20 sessions cards in up next screen')
@then('verify that the up next screen should contain all the upcoming sessions')
@then('verify all the elements in the Up next screen')
def verify_up_next_screen(home_screen):
    details = home_screen.verify_elements_and_up_next_pagination()
    check.equal(details.result, True, details.reason)


@then('verify that each page will load with 20 sessions cards in completed screen')
def verify_completed_screen(home_screen):
    details = home_screen.verify_elements_and_completed_pagination()
    check.equal(details.result, True, details.reason)

@then("tap on device back button")
def tap_device_back(home_screen):
    home_screen.click_back()


@then(parsers.parse('verify that should come back to "{text}" tab'))
def is_tab_selected(home_screen, text):
    details = home_screen.is_tab_selected(text)
    check.equal(details.result, True, details.reason)


@then(
    'verify along with normal/3+1 sessions below the see all, recommended sessions (Workshop sessions) are also present')
def is_master_class_present(trial_class):
    details = trial_class.is_master_class_present()
    check.equal(details.result, True, details.reason)


@then(parsers.parse('tap on "{text}"'))
def tap_on_premium_card(login_in, text):
    login_in.click_on_link(text)


@given(parsers.parse('post-requisite "{requisite_name}" should be tagged for the particular classroom session'))
def attach_post_requisite(home_screen, driver, requisite_name):
    home_screen.attach_post_requisite(driver, requisite_name)


@then('verify the elements present in session details screen')
def all_tagged_resource_types(home_screen):
    details = home_screen.all_tagged_resource_types()
    check.equal(details.result, True, details.reason)


@then('verify that user can book masterclass session')
def book_multiple_master_class(trial_class, db):
    details = trial_class.book_master_class(db)
    check.equal(details.result, True, details.reason)


@given("reset student session if the session is incase completed")
def reset_session(driver):
    Stagingtlms(driver).reset_session()


@then('verify user is landed on tutor session screen')
def verify_user_in_session(home_screen):
    details = home_screen.verify_user_in_session()
    check.equal(details.result, True, details.reason)


@given('ensure tutor has started the session')
def start_tutor_session(mentor_session):
    mentor_session.start_tutor_session()

@then('tutor ends session')
def tutor_taps_on_end_session(mentor_session):
    mentor_session.tutor_end_session()


@then(parsers.parse('tap on "{text}" tab'))
def select_tab(home_screen, text):
    home_screen.tap_on_tab(text)


@then('verify completed session cards should be displayed')
def then_verify_completed_session(driver):
    details = StudentDashboardOneToMega(driver).is_completed_sessions_displayed()
    check.equal(details.result, True,details.reason)


@then('verify that session cards with details should be identical in both for you and up next screens.')
def verify_for_you_up_next_screen(home_screen):
    details = home_screen.verify_for_you_and_next_screen()
    check.equal(details.result, True, details.reason)


@then('tap on class notes download icon')
def click_on_download(classnotes):
    classnotes.download_from_session_detals()


@then('verify class notes downloaded state along with forward icon')
def click_on_download(classnotes):
    details = classnotes.verify_forward_icon_present()
    check.equal(details.result, True, details.reason)


@then('click on first session card')
def click_on_completed_card(login_in):
    login_in.click_on_completed_card(0)