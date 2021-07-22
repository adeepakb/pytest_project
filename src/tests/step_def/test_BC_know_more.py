from pytest_bdd import scenarios, when, then
from pytest import fixture
from pytest_check import check

from constants.platform import Platform
from pages.android.Hamburgermenu import Hamburger

feature_file_name = 'BYJUS CLASSES - Know More option in left navigation'

scenarios('../features/' + feature_file_name + '.feature')


@fixture
def know_more(driver, request):
    platform_list = request.config.getoption("platform")
    from pages.factory.know_more import KnowMoreTestFactory
    if Platform.ANDROID.name.lower() == platform_list[-1].lower():
        m_class = KnowMoreTestFactory().get_page(driver, Platform.ANDROID.value)
        yield m_class
    else:
        raise NotImplementedError()


@then('verify that web page opened through webview which should show all the information wrt "BYJU’S CLASSES"')
def ham_verify(driver, know_more):
    check.equal(know_more.validate_know_more_webview().result, True, know_more.validate_know_more_webview().reason)
