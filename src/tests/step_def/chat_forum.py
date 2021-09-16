from pytest_bdd import scenarios, given, when, then, parsers
from pytest import fixture

from constants.platform import Platform
from pages.factory.neo_inclass_factory import NeoInClassFactory
from utilities.neo_tute_mentoring import NeoTute

feature_file_name = 'Chat Forum'
import pytest_check as check

scenarios('../features/' + feature_file_name + '.feature')


@fixture
def test_tut(driver):
    test_tut = NeoTute(driver)
    yield test_tut

@fixture
def test_tut_tutor(driver):
    test_tut_tutor = NeoTute(driver)
    yield test_tut_tutor


@fixture()
def neo_in_class(request, driver):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        neo_in_class = NeoInClassFactory().get_page(driver, Platform.ANDROID.value)
        yield neo_in_class
    elif Platform.WEB.name in platform_list:
        neo_in_class = NeoInClassFactory().get_page(driver, Platform.WEB.value)
        yield neo_in_class


@given("Student launches in-class and navigate to home page")
def step_impl(test_tut):
    test_tut.launch_student_webiste(mobile_number="2013795859")


@given("student navigates to byjus classes screen")
def step_impl(test_tut):
    test_tut.navigate_to_byjus_classes_screen()


@when("student joins sessions")
@given("student joins sessions")
def step_impl(test_tut):
    test_tut.join_neo_session_from_classes_page_paid()


@then("verify chat sestion is displayed in class")
def step_impl(test_tut):
    test_tut.verify_chat_elements()


@then("Verify that students count besides chat Forum.")
def step_impl(test_tut):
    test_tut.verify_chat_elements_element_wise(element_type='students count')


@then(parsers.parse('Verify that "{text}" in chat Forum.'))
def step_impl(test_tut, text):
    test_tut.verify_chat_elements_element_wise(element_type=text)


@then("Verify alphanumeric messages are sent in chat")
def step_impl(test_tut):
    test_tut.send_chat(text='a1!2% N n')
    detail = test_tut.verify_a_text_in_chat(text='a1!2% N n')
    check.equal(detail.result, True, detail.reason)


@then(
    "Verify that text wrapping should happen without truncation or spill over the window when texts include multiple lines.")
def step_impl(test_tut):
    test_tut.send_chat(text='HI I am \n Tester')
    detail = test_tut.verify_a_text_in_chat(text='HI I am')
    check.equal(detail.result, True, detail.reason)
    detail = test_tut.verify_a_text_in_chat(text='Tester')
    check.equal(detail.result, True, detail.reason)


@when(
    "Student sends sticker")
def step_impl(test_tut):
    test_tut.send_sticker()


@then(
    "Verify sticker is shown in chat")
def step_impl(test_tut):
    test_tut.send_sticker()
    detail = test_tut.verify_sticker_displayed()
    check.equal(detail.result, True, detail.reason)


@when('student raises hand')
def step_impl(test_tut):
    test_tut.raise_hand()


@when('student lower hand')
def step_impl(test_tut):
    test_tut.unraise_hand()


@then('verify student hand is raised')
def step_impl(test_tut):
    detail = test_tut.verify_hand_is_raised()
    check.equal(detail.result, True, detail.reason)


@then('verify lower hand message is displayed')
def step_impl(test_tut):
    detail = test_tut.verify_lower_hand_text_is_displayed()
    check.equal(detail.result, True, detail.reason)


@then('student rejoins the session')
def step_impl(test_tut):
    test_tut.launch_student_webiste(mobile_number="2013795859")
    test_tut.navigate_to_byjus_classes_screen()
    test_tut.join_neo_session_from_classes_page_paid()


@given("tutor start the session")
def step_impl(test_tut_tutor):
    test_tut_tutor.start_neo_session()


@when('tutor unraises hand for student')
def step_impl(test_tut, neo_in_class):
    profile_cards = neo_in_class.click_on_menu_option(expected_student_name='Viviktha', menu_item='Hands Down')


@then("student's hand is unraised")
def step_impl(test_tut):
    detail = test_tut.verify_hand_is_raised()
    check.equal(detail.result, True, detail.reason)


@when("wifi is turned off")
def step_impl(test_tut):
    test_tut.set_wifi_connection_off()


@when("students types random chat message")
def step_impl(test_tut):
    test_tut.type_chat("Hi Test")


@when("click on sticker icon")
def step_impl(test_tut):
    test_tut.click_on_sticker_icon()


@then("verify no message is sent in the chat")
def step_impl(test_tut):
    detail = test_tut.verify_wifi_off_inchat_displayed()
    check.equal(detail.result, True, detail.reason)


@then("two rows of stickers are shown in the chat")
def step_impl(test_tut):
    detail = test_tut.verify_no_of_default_stickers()
    check.equal(detail.result, True, detail.reason)


@when("tutor types the chat")
def step_impl(test_tut_tutor):
    test_tut_tutor.send_message_in_chat(text="Hi I am tutor")


@when("student sends chat message")
def step_impl(test_tut):
    test_tut.send_chat(text="Hi I am student")



@when("another student joins the session")
def step_impl(test_tut_tutor):
    test_tut_tutor.launch_student_webiste(mobile_number="2017607448")
    test_tut_tutor.navigate_to_byjus_classes_screen()
    test_tut_tutor.join_neo_session_from_classes_page_paid()


@when("another student sends a chat")
def step_impl(test_tut_tutor):
    test_tut_tutor.send_chat("Hi I am another student")


@then("verify tutor messages are left alligned")
def step_impl(test_tut):
    detail = test_tut.verify_tutor_messages_are_left_alligned(text="Hi I am tutor")
    check.equal(detail.result, True, detail.reason)


@then("verify other student chats are left alligned")
def step_impl(test_tut):
    detail = test_tut.verify_other_student_messages_are_left_alligned(text= "Hi I am another student")
    check.equal(detail.result, True, detail.reason)


@then("verify student chat is left alligned")
def step_impl(test_tut):
    test_tut.verify_student_messages_are_right_alligned(text="Hi I am student")


@then("verify tutor name is shown in tutor box")
def step_impl(test_tut):
    detail = test_tut.verify_chat_elements_element_wise(element_type=  "Tutor name")
    check.equal(detail.result, True, detail.reason)
    detail = test_tut.verify_chat_elements_element_wise(element_type="Tutor tag")
    check.equal(detail.result, True, detail.reason)

