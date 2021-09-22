from pytest_bdd import scenarios, given, then, when, parsers
from pytest import fixture
from constants.platform import Platform
from pages.factory.login import LoginFactory
from pages.factory.neo_inclass_factory import NeoInClassFactory
import pytest_check as check
from utilities.neo_tute_mentoring import NeoTute
scenarios('../features/Technical Issues during Session.feature')


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
def neo_in_class(request, driver):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        neo_in_class = NeoInClassFactory().get_page(driver, Platform.ANDROID.value)
        yield neo_in_class
    elif Platform.WEB.name in platform_list:
        neo_in_class = NeoInClassFactory().get_page(driver, Platform.WEB.value)
        yield neo_in_class


@given("launch the application online as neo user and navigate to home screen")
def navigate_to_one_to_many_and_mega_user(login_in):
    login_in.login_and_navigate_to_home_screen('+91-', '2013274689', otp=None)


@given("tutor start the session")
def step_impl(driver):
    NeoTute(driver).start_neo_session()


@when('click on "JOIN" button in home page')
def step_impl(neo_in_class):
    neo_in_class.home_click_on_join()


@when("student join neo session")
def step_impl(neo_in_class):
    neo_in_class.join_neo_session()


@then("Verify that kebab menu icon is present below the video screen [MergedTest]")
def tap_on_premium_card(neo_in_class):
    check.equal(neo_in_class.is_kebab_menu_present(), True, "kebab menu icon is present below the video screen")


@then("Verify that kebab icon is clickable and clicking on the this different options should be displayed [MergedTest]")
def step_impl(neo_in_class):
    neo_in_class.click_on_kebab_menu()
    check.equal(neo_in_class.is_facing_issues_option_present(), True, "Facing Issues? icon is present under kebab menu [MergedTest]")
    check.equal(neo_in_class.is_exit_class_btn_present(), True, "Exit class icon is present under kebab menu [MergedTest]")


@then(parsers.parse("Verify the different issue types present in the popup when user clicks on '{text}' in the kebab menu [MergedTest]"))
def step_impl(neo_in_class, text):
    neo_in_class.button_click(text)
    expected_issues_list = ['Video Stopped playing', 'Video buffering', 'Chat stopped responding', 'Chat player lagging', 'Unable to type responses', 'Unable to switch on audio', 'Unable to switch on video', 'Unable to exit class', 'Unable to view whiteboard', 'Celebrations not working', 'Others']
    actual_issues_list = neo_in_class.get_all_issues_list()
    check.equal(expected_issues_list,actual_issues_list," All expected issues present in popup for user to select")


@then("Verify that the pop up should display on the top of the video screen  clicking the kebab menu [MergedTest]")
def step_impl(neo_in_class):
    check.equal(neo_in_class.verify_issue_popup_present(),True,"Issue pop up displayed on the top of the video screen")


@then("Verify that by-default 'Report Now' button should be disabled [MergedTest]")
def step_impl(neo_in_class):
    details = neo_in_class.is_report_now_btn_enabled()
    check.equal(details.result, False, details.reason)


@then("Verify that once user selects any option the button should be enabled [MergedTest]")
def step_impl(neo_in_class):
    neo_in_class.select_any_option_in_facing_issue('Video Stopped playing')
    details = neo_in_class.is_report_now_btn_enabled()
    check.equal(details.result, True, details.reason)


@then('Verify that user should able to select multiple options [MergedTest]')
def step_impl(neo_in_class):
    options_list = ['Video Stopped playing', 'Video buffering', 'Chat stopped responding', 'Chat player lagging',
                    'Unable to type responses']
    for option in options_list:
        neo_in_class.select_any_option_in_facing_issue(option)
        details = neo_in_class.verify_issue_checked(option)
        check.equal(details.result, True, details.reason)


@then('Verify that the selected option toggle should display in sky colour [MergedTest]')
def step_impl(neo_in_class):
    details = neo_in_class.get_selected_issue_radio_btn_color('rgba(63, 81, 181, 1)')
    check.equal(details.result, True, details.reason)


@then(parsers.parse('Verify that once select any option the "{text}" should be displayed below the issue [MergedTest]'))
def step_impl(neo_in_class, text):
    details = neo_in_class.verify_extra_tips(text)
    check.equal(details.result, True, details.reason)


@then("Verify that once user select any option , that option should be highlighted with bold text [MergedTest]")
def step_impl(neo_in_class):
    details = neo_in_class.verify_bold_font_selected_issue()
    check.equal(details.result, True, details.reason)


@then('Verify the pop should be scrollable [MergedTest]')
def step_impl(neo_in_class):
    neo_in_class.join_neo_session()
    neo_in_class.click_on_kebab_menu()
    neo_in_class.button_click("Facing issues?")
    neo_in_class.scroll_down_facing_issues_popup(8)


@then('Verify that close icon is present the popup and its clickable [MergedTest]')
def step_impl(neo_in_class):
    check.equal(neo_in_class.is_close_icon_in_facing_issues_present(),True,"close icon is present")


@then('Verify that popup should close when user clicks on the close icon [MergedTest]')
def step_impl(neo_in_class):
    neo_in_class.click_on_close_icon_for_facing_issues_popup()


@then(parsers.parse('Verify that "{text}" text should be displayed [MergedTest]'))
def step_impl(neo_in_class, text):
    check.equal(neo_in_class.is_text_match(text), True, "%s text should be displayed " % text)


@then(parsers.parse('Verify when user selects the issue type as "{issue_text}" one text box should be appear with '
                    'ghost text "{default_label_text}" [MergedTest]'))
def step_impl(neo_in_class, issue_text, default_label_text):
    neo_in_class.select_any_option_in_facing_issue(issue_text)
    check.equal(neo_in_class.is_text_match(default_label_text), True,"%s text should is displayed " % default_label_text)


@then(parsers.parse('Verify the alignment of the email icon on the popup after user writes "{comment_text}" in the text box and clicks on "{button_text}" button [MergedTest]'))
def step_impl(neo_in_class,comment_text,button_text):
    neo_in_class.provide_other_comments(comment_text)
    neo_in_class.button_click(button_text)
    global values
    values = neo_in_class.is_email_icon_present_and_text()
    check.equal(values[0], True,"email icon is present on the popup")


@then(parsers.parse('Verify that when the user clicks on report now button,"{text}" popup should be displayed [MergedTest]'))
def step_impl(text):
    check.equal(values[1], text, "%s text popup should be displayed " % text)


@then('Verify the popup should be disappeared automatically in 5 secs [MergedTest]')
def step_impl(neo_in_class):
    check.equal(neo_in_class.submitted_popup_disappear(),False,"Submitted issue popup disappeared automatically")


@then('Verify the popup when user refresh the page [MergedTest]')
def step_impl(neo_in_class):
    neo_in_class.click_on_kebab_menu()
    neo_in_class.button_click('Facing issues?')
    check.equal(neo_in_class.page_refresh_issue_popup_disappear(),False,"popup is not present after user refresh the page")


@then('Verify the popup should be disappeared if user refresh the page [MergedTest]')
def step_impl(neo_in_class):
    neo_in_class.click_on_kebab_menu()
    neo_in_class.button_click("Facing issues?")
    check.equal(neo_in_class.page_refresh_issue_submitted_issue_popup_disappear(),False,"popup is not present after user refresh the page")


@then('Verify the alignment of the suggested  tips. [MergedTest]')
def step_impl(neo_in_class):
    check.equal(neo_in_class.extra_tips_alignment(),True,"suggested tips is left aligned and has block display as expected")