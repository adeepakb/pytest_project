from pytest_bdd import scenarios, given, when, then, parsers
from pytest import fixture

from utilities.neo_tute_mentoring import NeoTute

feature_file_name = 'Chat Forum'
import pytest_check as check

scenarios('../features/' + feature_file_name + '.feature')


@fixture
def test_tut(driver):
    test_tut = NeoTute(driver)
    yield test_tut


@given("Student launches in-class and navigate to home page")
def step_impl(test_tut):
    test_tut.launch_student_webiste(mobile_number="5444389143")


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
    test_tut.verify_chat_elements()


@then(parsers.parse('Verify that "{text}" in chat Forum.'))
def step_impl(test_tut, text):
    test_tut.verify_chat_elements_element_wise(element_type=text)


@then("Verify alphanumeric messages are sent in chat")
def step_impl(test_tut):
    test_tut.send_chat(text='a1!2% N n')
    detail  =test_tut.verify_a_text_in_chat(text='a1!2% N n')
    check.equal(detail.result, True, detail.reason)




@then(
    "Verify that text wrapping should happen without truncation or spill over the window when texts include multiple lines.")
def step_impl(test_tut):
    test_tut.send_chat(text='HI I am \n Tester')
    detail  =test_tut.verify_a_text_in_chat(text='HI I am')
    check.equal(detail.result,True,detail.reason)
    detail  =test_tut.verify_a_text_in_chat(text='Tester')
    check.equal(detail.result, True, detail.reason)

@when(
    "Student sends sticker")
def step_impl(test_tut):
    test_tut.send_sticker()

@then(
    "Verify sticker is shown in chat")
def step_impl(test_tut):
    test_tut.send_sticker()
    detail  =test_tut.verify_sticker_displayed()
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
    test_tut.launch_student_webiste(mobile_number="5444389143")
    test_tut.navigate_to_byjus_classes_screen()
    test_tut.join_neo_session_from_classes_page_paid()

@given("login as tutor")
def step_impl(test_tut):
    test_tut.start_neo_session()


