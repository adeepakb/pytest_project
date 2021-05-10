from pytest_bdd import scenarios, given, then, when, parsers
from pytest import fixture
from constants.platform import Platform
from pages.android.homepage import HomePage
from pages.factory.instruction_dialog import InstructionDialog
from pages.factory.login import LoginFactory

scenarios('../features/Start Test Instruction Dialog.feature')


@fixture()
def login_in(request, driver):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        login_in = LoginFactory().get_page(driver, Platform.ANDROID.value)
        yield login_in
    elif Platform.WEB.name in platform_list:
        login_in = LoginFactory().get_page(driver, Platform.WEB.value)
        yield login_in


@fixture
def instruction_dialog(request, driver):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        instruction_dialog = InstructionDialog().get_page(driver, Platform.ANDROID.value)
        yield instruction_dialog
    elif Platform.WEB.name in platform_list:
        instruction_dialog = InstructionDialog().get_page(driver, Platform.WEB.value)
        yield instruction_dialog

@given("launch the app and navigate to home screen")
def login_as_one_mega_user(driver):
    HomePage(driver).navigate_to_one_to_many_and_mega_user(driver)


@when("tap on premium card")
def tap_on_premium_card(login_in):
    login_in.click_on_premium_school()


@then("navigate to one to mega homescreen")
def navigate_to_one_to_mega_homescreen(login_in):
    login_in.select_premium_school()


@then('verify that in the For you tab, post requisite card is present')
def is_requisite_list(instruction_dialog):
    assert instruction_dialog.is_requisite_list(), "requisite is not displayed"


@then(parsers.parse('tap on "{text}" link'))
@then(parsers.parse('tap on "{text}" for the assessment added'))
def tap_on_link(login_in, text):
    login_in.click_on_link(text)


@then(parsers.parse(
    'verify that if the assessment time is not reached to session time then "{text}" link should not be visible'))
@then(parsers.parse('verify "{text}" option is not displayed if the post requisite contain only 2 resource type'))
def verify_text(login_in, text):
    assert (not login_in.text_match(text)), "%s text is displayed" % text


@then('verify that on pop up close icon is displayed')
def is_close_instruction_displayed(instruction_dialog):
    assert instruction_dialog.is_close_instruction_displayed(), "close icon is not displayed"


@then('verify on tap of the close icon pop up should close')
def tap_on_close_instruction(instruction_dialog, login_in):
    instruction_dialog.tap_on_close_instruction()
    assert not login_in.text_match("Test Instructions"), "Pop up did not get closed"


@then(parsers.parse('tap on "{text}" button'))
def tap_button(login_in, text):
    button_status = login_in.button_click(text)
    assert button_status is True, "Unable to find {text} button"


@then(parsers.parse('verify that open the test on the web'))
def is_assessment_popup_present(instruction_dialog):
    assert instruction_dialog.is_assessment_popup_present(), "assessment popup is not displayed"


@then("tap on device back button")
def tap_device_back(instruction_dialog):
    instruction_dialog.click_back()


@then("verify the user is navigated to the PS screen")
def is_user_in_ps_page(instruction_dialog):
    assert instruction_dialog.is_user_in_ps_page(), "user is not in the PS screen"


@then('end the test')
def end_test(instruction_dialog):
    instruction_dialog.end_test()


@then('verify that score should be shown')
def verify_score_present(instruction_dialog):
    assert instruction_dialog.verify_score_present(), "assessment score is not shown"


@then(parsers.parse('verify "{text}" button is displayed'))
def button_verify(login_in, text):
    button_displayed = login_in.is_button_displayed(text)
    assert button_displayed is True, f"Button {text} is not displayed"


@then('tap on Continue Assessment button')
@then('the user is able to continue with the assessment')
@then('tap on Start Assessment button')
def tap_on_begin_assessment(instruction_dialog):
    instruction_dialog.tap_on_begin_assessment()


@then('verify start test instruction dialogue should not be shown')
def is_start_assessment_popup(login_in):
    assert not login_in.text_match("Test Instructions"), "Pop up did not get closed"


@given('set the start time which is not reached for the assessment')
def set_future_assessment_start_date(instruction_dialog):
    global date
    date = instruction_dialog.set_future_assessment_start_date()


@given('verify available until date should be set on tllms backend for assessment tagged')
def get_assessment_available_until_date(instruction_dialog):
    global date
    date = instruction_dialog.get_assessment_available_until_date()


@given('set expired assessment end time in tllms')
def set_expired_assessment_end_date(instruction_dialog):
    instruction_dialog.set_expired_assessment_end_date()


@then(parsers.parse('verify the text "{text}"'))
@then(parsers.parse('verify that it should show "{text}" popup'))
def is_text_present(login_in, text):
    if "{date}" in text:
        text = text.format(date=date).encode('utf-8').decode('unicode_escape')
    assert login_in.text_match(text), "%s text is not displayed" % text


@given(parsers.parse('post-requisite "{assessment_name}" should be tagged for the particular classroom session'))
def attach_post_requisite(instruction_dialog, assessment_name):
    instruction_dialog.attach_post_requisite(assessment_name)


@then('reset assessment start date as today')
def set_assessment_start_date_today(instruction_dialog):
    instruction_dialog.set_assessment_start_date_today()


@then('reset back assessment end date')
def reset_future_end_date(instruction_dialog):
    instruction_dialog.reset_future_end_date()


@then(parsers.parse('take screenshot of assessment "{text}"'))
def capture_screenshot_of_assessment(instruction_dialog, text):
    instruction_dialog.capture_screenshot_of_assessment(text)


@then(parsers.parse('compare both images "{img1}" and "{img2}" to verify user is able to continue with the '
                    'assessment where the user was paused'))
def verify_images(instruction_dialog, img1, img2):
    assert instruction_dialog.image_diff(img1, img2) is None, "User did not resume same place where assessment was " \
                                                              "exited previously "
