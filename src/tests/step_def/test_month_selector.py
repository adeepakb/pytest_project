from pytest import fixture
from pytest_bdd import scenarios, given, when, then, parsers
from src.POM_Pages.application_login import Login
from src.POM_Pages.choose_topic import ChooseTopic
from src.POM_Pages.dropdown_month_select import DropDownSelect
from src.POM_Pages.session_popup import SessionAlert
from src.POM_Pages.student_dashboard import StudentDashboard

feature_file_name = 'month_selector'

scenarios('../features/' + feature_file_name + '.feature')


@fixture
def std_board(browser):
    stud_b = StudentDashboard(browser)
    yield stud_b


@fixture
def login_in(browser):
    login_in = Login(browser)
    yield login_in


@fixture
def month_selector(browser):
    month_selector = DropDownSelect(browser)
    yield month_selector


@given('Launch the tutor app online')
def launch_app(login_in):
    login_in.implicit_wait_for(15)


@given('navigate to one to many student dashboard screen')
def given_navigate_dashboard_screen(login_in, browser):
    try:
        login_in.click_on_premium_school()
        pop_up_displayed = SessionAlert(browser)
        pop_up_displayed.cancel_join_session()
    except AssertionError:
        login_in.click_on_one_to_many()


@when('Verify month selector icon with dropdown icon shown on student dashboard')
def verify_month_dropdown_icon(month_selector):
    icon_displayed = month_selector.is_dropdown_icon_displayed()
    assert icon_displayed is True, "Month drop-down may not be displayed!"


@then('tap on month dropdown icon')
@when('tap on month dropdown icon')
def click_drop_down(month_selector):
    month_selector.select_dropdown()


@then('verify month list should be shown')
def verify_month_list_displayed(month_selector):
    drop_list_displayed = month_selector.is_dropdown_list_displayed()
    assert drop_list_displayed is True, "Dropdown list may not be displayed."


@then('verify month list should be in sorted order')
def verify_month_list_sorted(month_selector):
    list_sorted = month_selector.is_month_list_sorted()
    assert list_sorted is True, "DropDown list may not be sorted or not in the format"


@when('verify by default current month should be highlighted')
def verify_current_month_selected(month_selector):
    current_month_highlighted = month_selector.is_current_month_highlighted()
    assert current_month_highlighted is True, "Current month is not highlighted."


@then('verify on taping on other month name respective month should get highlighted')
def verify_respective_details_displayed(month_selector):
    details_displayed = month_selector.is_respective_details_displayed()
    assert details_displayed is True, "Details mismatch!"


@then('verify on taping on outside any where in the screen dropdown should disappear')
def verify_dropdown_not_displayed(month_selector):
    drop_down_displayed = month_selector.is_drop_down_displayed()
    assert drop_down_displayed is False, "Drop down is still visible"


@then('tap on any month from the dropdown and verify respective details of that month should be displayed')
def then_tap_and_verify_any_month_details(month_selector):
    verify_respective_details_displayed(month_selector)


@then(parsers.parse('switch "{text}" the device data'))
def toggle_wifi_off(month_selector, text):
    if text == 'off':
        month_selector.toggle_wifi_connection('off')
    elif text == 'on':
        month_selector.toggle_wifi_connection('on')
