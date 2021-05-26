import time

from pytest import fixture
from pytest_bdd import given, when, then, parsers, scenarios
import pytest_check as check
from constants.platform import Platform
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


# reshma ask
@when('verify that the web page opened through webview which should show all the information wrt "BYJU’S CLASSES"')
@then('verify that the web page opened through webview which should show all the information wrt "BYJU’S CLASSES"')
@then('verify that web page opened through webview which should show all the information wrt "BYJU’S CLASSES"')
@when('verify that web page opened through webview which should show all the information wrt "BYJU’S CLASSES"')
def step_impl(driver, know_more):
    details= know_more.validate_know_more_webview()
    check.equal(details.result, True, details.reason)


@then('Verify that "BYJUS CLASSES" web view consist of "Book a free class" card')
def step_impl(driver, know_more):
    details= know_more.validate_book_a_free_class_card()
    check.equal(details.result, True, details.reason)


@then('tap of "Book a free class" card')
def step_impl(driver, know_more):
    details = know_more.validate_book_a_free_class_card()
    check.equal(details.result, True, details.reason)


@then('tap of "Book a free class" card')
def step_impl(driver, know_more):
    detail = know_more.tap_on_book_card()
    check.equal(detail.result, True, detail.reason)


@then('verify "Book a free class" card is responsive')
def step_impl(driver, std_board):
     assert std_board.is_one_to_mega_screen_displayed(),"user is not navigated to student dashboard on click of 'Book a free class' in know more webview"



