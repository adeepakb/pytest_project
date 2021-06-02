import time

from pytest import fixture
from pytest_bdd import given, when, then, parsers, scenarios
from constants.platform import Platform
import pytest_check as check
from pages.factory.know_more import KnowMoreTestFactory

feature_file_name = 'BYJUS CLASSES - Know More option in left navigation'

scenarios('../features/' + feature_file_name + '.feature')


@fixture
def std_board(driver, request):
    platform_list = request.config.getoption("platform")
    from pages.factory.student_dashboard_otm_factory import StudentDashboardOneToMegaFactory
    if Platform.ANDROID.name.lower() == platform_list[-1].lower():
        std_board = StudentDashboardOneToMegaFactory().get_page(driver, Platform.ANDROID.value)
        yield std_board
    else:
        raise NotImplementedError()


@fixture
def know_more(request, driver):
    platform_list = request.config.getoption("platform")
    if Platform.ANDROID.name.lower() == platform_list[-1].lower():
        know_more = KnowMoreTestFactory().get_page(driver, Platform.ANDROID.value)
        yield know_more
    else:
        raise NotImplementedError()



@when('verify that the web page opened through webview which should show all the information wrt "BYJU’S CLASSES"')
@then('verify that the web page opened through webview which should show all the information wrt "BYJU’S CLASSES"')
@then('verify that web page opened through webview which should show all the information wrt "BYJU’S CLASSES"')
@when('verify that web page opened through webview which should show all the information wrt "BYJU’S CLASSES"')
def step_impl(driver, know_more):
    time.sleep(10)
    details = know_more.validate_webview_without_details()
    check.equal(details.result, True, details.reason)


@then('Verify that "BYJUS CLASSES" consist of its elements')
def step_impl(driver, know_more):
    details = know_more.validate_know_more_webview()
    check.equal(details.result, True, details.reason)

@when('Verify that the "BYJUS CLASSES" web view consist of the "Book a free class" card')
@then('Verify that the "BYJUS CLASSES" web view consist of the "Book a free class" card')
@then('Verify that "BYJUS CLASSES" web view consist of "Book a free class" card')
@then('Verify that the "BYJUS CLASSES" web view consist of the "Book a free class" card')
def step_impl(driver, know_more):
    details = know_more.validate_book_a_free_class_card()
    check.equal(details.result, True, details.reason)


@then('Verify that "BYJUS CLASSES" consist of "View Class details" card')
@then('Verify that the "BYJUS CLASSES" web view consist of "view details" card')
@when('Verify that the "BYJUS CLASSES" web view consist of "view details" card')
@then('Verify that "BYJUS CLASSES" web view consist of "view details" card')
@when('Verify that "BYJUS CLASSES" web view consist of "view details" card')
def step_impl(driver, know_more):
    details = know_more.validate_book_a_free_class_card(text ="View class details")
    check.equal(details.result, True, details.reason)


@then('tap of "Book a free class" card')
def step_impl(driver, know_more):
    details = know_more.validate_book_a_free_class_card(text='View class details')
    check.equal(details.result, True, details.reason)

@when('tap of "Book a free class" card')
@then('tap of "Book a free class" card')
def step_impl(driver, know_more):
    detail = know_more.tap_on_book_card()
    check.equal(detail.result, True, detail.reason)


@then('tap of "View Class details" card')
@then('tap of "view Class details" card')
def step_impl(driver, know_more):
    detail = know_more.tap_on_book_card(text='View class details')
    check.equal(detail.result, True, detail.reason)


@then('verify "Book a free class" card is responsive')
def step_impl(driver, know_more):
    time.sleep(5)
    detail = know_more.verify_book_free_class_screen()
    check.equal(detail.result,True,detail.reason)


@then('verify "View Class details" card is responsive')
def step_impl(driver, know_more):
    time.sleep(5)
    detail = know_more.verify_book_free_class_screen(expected_activity='OneToMegaHomeActivity')
    check.equal(detail.result,True,detail.reason)


@then('verify that user is navigated to Premium school classroom session screen')
def step_impl(driver, know_more):
    time.sleep(5)
    detail = know_more.verify_book_free_class_screen()
    check.equal(detail.result,True,detail.reason)

