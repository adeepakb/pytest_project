from pytest_bdd import scenarios, given, when, then, parsers
from pytest import fixture

from constants.platform import Platform
from pages.factory.login import LoginFactory
from pages.factory.neo_inclass_factory import NeoInClassFactory
from utilities.neo_tute_mentoring import NeoTute

feature_file_name = 'Chat Forum'
import pytest_check as check

scenarios('../features/' + feature_file_name + '.feature')


@fixture
def test_tut(driver):
    test_tut = NeoTute(driver)
    yield test_tut


@fixture()
def test_student_2(request, driver):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        test_student_2 = NeoInClassFactory().get_page(driver, Platform.ANDROID.value)
        yield test_student_2
    elif Platform.WEB.name in platform_list:
        test_student_2 = NeoInClassFactory().get_page(driver, Platform.WEB.value)
        yield test_student_2


@fixture()
def neo_in_class(request, driver):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        neo_in_class = NeoInClassFactory().get_page(driver, Platform.ANDROID.value)
        yield neo_in_class
    elif Platform.WEB.name in platform_list:
        neo_in_class = NeoInClassFactory().get_page(driver, Platform.WEB.value)
        yield neo_in_class


@fixture()
def login_in(request, driver):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        login_in = LoginFactory().get_page(driver, Platform.ANDROID.value)
        yield login_in
    elif Platform.WEB.name in platform_list:
        login_in = LoginFactory().get_page(driver, Platform.WEB.value)
        yield login_in



@given("Student launches in-class and navigate to home page")
def step_impl(login_in):
    login_in.login_and_navigate_to_home_screen('+91-', '2013795859', otp=None)


@given("student navigates to byjus classes screen")
def step_impl(neo_in_class):
    neo_in_class.navigate_to_byjus_classes_screen()


@when("student joins sessions")
@given("student joins sessions")
def step_impl(neo_in_class):
    neo_in_class.join_neo_session_from_classes_page_paid()


@then("verify chat sestion is displayed in class")
def step_impl(neo_in_class):
    neo_in_class.verify_chat_elements()


@then("Verify that students count besides chat Forum.")
def step_impl(neo_in_class):
    neo_in_class.verify_chat_elements_element_wise(element_type='students count')


@then(parsers.parse('Verify that "{text}" in chat Forum.'))
def step_impl(neo_in_class, text):
    neo_in_class.verify_chat_elements_element_wise(element_type=text)


@then("Verify alphanumeric messages are sent in chat")
def step_impl(neo_in_class):
    neo_in_class.send_chat(text='a1!2% N n')
    detail = neo_in_class.verify_a_text_in_chat(text='a1!2% N n')
    check.equal(detail.result, True, detail.reason)


@then(
    "Verify that text wrapping should happen without truncation or spill over the window when texts include multiple lines.")
def step_impl(neo_in_class):
    neo_in_class.send_chat(text='HI I am \n Tester')
    detail = neo_in_class.verify_a_text_in_chat(text='HI I am')
    check.equal(detail.result, True, detail.reason)
    detail = neo_in_class.verify_a_text_in_chat(text='Tester')
    check.equal(detail.result, True, detail.reason)


@when(
    "Student sends sticker")
def step_impl(neo_in_class):
    neo_in_class.send_sticker()


@then(
    "Verify sticker is shown in chat")
def step_impl(neo_in_class):
    neo_in_class.send_sticker()
    detail = neo_in_class.verify_sticker_displayed()
    check.equal(detail.result, True, detail.reason)


@when('student raises hand')
def step_impl(neo_in_class):
    neo_in_class.raise_hand()


@when('student lower hand')
def step_impl(neo_in_class):
    neo_in_class.unraise_hand()


@then('verify student hand is raised')
def step_impl(neo_in_class):
    detail = neo_in_class.verify_hand_is_raised()
    check.equal(detail.result, True, detail.reason)


@then('verify lower hand message is displayed')
def step_impl(neo_in_class):
    detail = neo_in_class.verify_lower_hand_text_is_displayed()
    check.equal(detail.result, True, detail.reason)


@then('student rejoins the session')
def step_impl(neo_in_class,login_in):
    login_in.login_and_navigate_to_home_screen('+91-', '2016490550', otp=None)
    neo_in_class.home_click_on_join()
    neo_in_class.join_neo_session()


@given("tutor start the session")
def step_impl(test_tut):
    test_tut.start_neo_session()


@when('tutor unraises hand for student')
def step_impl(test_tut):
    profile_cards = test_tut.click_on_menu_option(expected_student_name='Viviktha', menu_item='Hands Down')


@then("student's hand is unraised")
def step_impl(neo_in_class):
    detail = neo_in_class.verify_hand_is_raised()
    check.equal(detail.result, True, detail.reason)


@when("wifi is turned off")
def step_impl(neo_in_class):
    neo_in_class.set_wifi_connection_off()


@when("students types random chat message")
def step_impl(neo_in_class):
    neo_in_class.type_chat("Hi Test")


@when("click on sticker icon")
def step_impl(neo_in_class):
    neo_in_class.click_on_sticker_icon()


@then("verify no message is sent in the chat")
def step_impl(neo_in_class):
    detail = neo_in_class.verify_wifi_off_inchat_displayed()
    check.equal(detail.result, True, detail.reason)


@then("two rows of stickers are shown in the chat")
def step_impl(neo_in_class):
    detail = neo_in_class.verify_no_of_default_stickers()
    check.equal(detail.result, True, detail.reason)


@when("tutor types the chat")
def step_impl(test_tut):
    test_tut.send_message_in_chat(text="Hi I am tutor")


@when("student sends chat message")
def step_impl(neo_in_class):
    neo_in_class.send_chat(text="Hi I am student")


@when("another student joins the session")
def step_impl(test_student_2):
    test_student_2.launch_student_webiste(mobile_number="2017607448")
    test_student_2.navigate_to_byjus_classes_screen()
    test_student_2.join_neo_session_from_classes_page_paid()


@when("another student sends a chat")
def step_impl(test_student_2):
    test_student_2.send_chat("Hi I am another student")


@then("verify tutor messages are left alligned")
def step_impl(neo_in_class):
    detail = neo_in_class.verify_tutor_messages_are_left_alligned(text="Hi I am tutor")
    check.equal(detail.result, True, detail.reason)


@then("verify other student chats are left alligned")
def step_impl(neo_in_class):
    detail = neo_in_class.verify_other_student_messages_are_left_alligned(text= "Hi I am another student")
    check.equal(detail.result, True, detail.reason)


@then("verify student chat is left alligned")
def step_impl(neo_in_class):
    neo_in_class.verify_student_messages_are_right_alligned(text="Hi I am student")


@then("verify tutor name is shown in tutor box")
def step_impl(neo_in_class):
    detail = neo_in_class.verify_chat_elements_element_wise(element_type=  "Tutor name")
    check.equal(detail.result, True, detail.reason)
    detail = neo_in_class.verify_chat_elements_element_wise(element_type="Tutor tag")
    check.equal(detail.result, True, detail.reason)

