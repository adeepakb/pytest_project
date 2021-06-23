import pytest
import os
from pytest_bdd import scenarios, given, when, then, parsers
from pages.android.Hamburgermenu import Hamburger
from utilities.BasePage import BaseClass

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

# sys.path.append(PATH('./utilities/'))
# from utilities.common_methods import CommonMethods
# from utilities.BasePage import BaseClass
# 
# sys.path.append(PATH('../../../pages/'))
# from pages.Hamburgermenu import Hamburger

driver = fixture = 'driver'
base_class = BaseClass()
Hamburg = Hamburger(driver)

"""storing the feature file name"""
featureFileName = "Hamburger Menu"

# base_class.setupLogs(featureFileName)

"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""
scenarios('../features/' + featureFileName + '.feature')


@given('Launch the app online')
def loginapp(driver):
    Hamburg.navigate_to_home_screen(driver)


@given('User is in Hamburger menu')
def ham_verify(driver):
    Hamburg.hamburger_verify(driver)


@when('User taps on profile button')
def profile_verify(driver):
    Hamburg.profile_button(driver)


@then('Verify that user should  navigate to profilescreen')
def profile_screen(driver):
    Hamburg.profilescreen_verify(driver)


@pytest.fixture
@when(parsers.parse('user taps on "{text}" option'))
def bookmark_verify(driver, text):
    Hamburg.tap_hamburger_option(driver, text)
    yield text


@then('Verify that user should  navigate to Bookmarks Screen')
def bookmark_page(driver, bookmark_verify):
    Hamburg.Hamburger_page(driver, bookmark_verify)


@pytest.fixture
@when(parsers.parse('user taps on "{text}" option'))
def Notification_verify(driver, text):
    Hamburg.tap_hamburger_option(driver, text)
    yield text


@then('Verify that user should  navigate to  Notification screen')
def Notification_page(driver, Notification_verify):
    Hamburg.Hamburger_page(driver, Notification_verify)


@pytest.fixture
@when(parsers.parse('user taps on "{text}" option'))
def Badges_verify(driver, text):
    Hamburg.tap_hamburger_option(driver, text)
    yield text


@then('Verify that user should  navigate to  Badges screen')
def Badges_page(driver, Badges_verify):
    Hamburg.Hamburger_page(driver, Badges_verify)


@pytest.fixture
@when(parsers.parse('user taps on "{text}" option'))
def parent_verify(driver, text):
    Hamburg.tap_hamburger_option(driver, text)
    yield text


@then('Verify that user should  navigate to  Parent Connect screen')
def parent_page(driver, parent_verify):
    Hamburg.Hamburger_page(driver, parent_verify)


@pytest.fixture
@when(parsers.parse('user taps on "{text}" option'))
def quizzo_verify(driver, text):
    Hamburg.tap_hamburger_option(driver, text)
    yield text


@then('Verify that user should  navigate to  Quizzo screen')
def quizzo_page(driver, quizzo_verify):
    Hamburg.Hamburger_page(driver, quizzo_verify)


@pytest.fixture
@when(parsers.parse('user taps on "{text}" option'))
def share_verify(driver, text):
    Hamburg.tap_hamburger_option(driver, text)
    yield text


@then('Verify that user should  navigate to  share dialog')
def share_page(driver, share_verify):
    Hamburg.Hamburger_page(driver, share_verify)


@pytest.fixture
@when(parsers.parse('user taps on "{text}" option'))
def contact_verify(driver, text):
    Hamburg.tap_hamburger_option(driver, text)
    yield text


@then('Verify that user should  navigate to  contact us screen')
def contact_page(driver, contact_verify):
    # Hamburg.Hamburger_page(driver, share_verify)
    Hamburg.scroll_hamburg_verify(driver, contact_verify)


@pytest.fixture
@when(parsers.parse('user taps on "{text}" option'))
def Terms_verify(driver, text):
    Hamburg.tap_hamburger_option(driver, text)
    yield text


@then('Verify that user should  navigate to  Terms & Conditions screen')
def Terms_page(driver, Terms_verify):
    Hamburg.scroll_hamburg_verify(driver, Terms_verify)


@pytest.fixture
@when(parsers.parse('user taps on "{text}" option'))
def subscribe_verify(driver, text):
    Hamburg.tap_hamburger_option(driver, text)
    yield text


@then('Verify that user should  navigate to  Subscribition  screen')
def subscribe_page(driver, subscribe_verify):
    Hamburg.scroll_hamburg_verify(driver, subscribe_verify)


@pytest.fixture
@when(parsers.parse('user taps on "{text}" option'))
def Redeem_verify(driver, text):
    Hamburg.tap_hamburger_option(driver, text)
    yield text


@then('Verify that user should  navigate to  Redeem Voucher  screen')
def Redeem_page(driver, Redeem_verify):
    Hamburg.scroll_hamburg_verify(driver, Redeem_verify)


@pytest.fixture
@when(parsers.parse('user taps on "{text}" option'))
def colgate_verify(driver, text):
    Hamburg.tap_hamburger_option(driver, text)
    yield text


@then('Verify that user should  navigate to  Colgate Scholarship  screen')
def colgate_page(driver, colgate_verify):
    Hamburg.scroll_hamburg_verify(driver, colgate_verify)


@when('User taps on Enquire Now option')
def r_homeDemo_verify(driver):
    Hamburg.hamburger_enquire_now(driver)


@then('Verify that user should  navigate to  Enquire Now screen')
def home_demo_page(driver):
    Hamburg.enquire_now_page(driver)


@when('User taps on School Super League option')
def ssl_verify(driver):
    Hamburg.hamburger_spl(driver)


@then('Verify that user should  navigate to School Super League  screen')
def ssl_page(driver):
    Hamburg.ssl_verify(driver)
