from pytest_bdd import scenarios, given, when, then, parsers
from pytest import fixture

from constants.platform import Platform
from pages.factory.login import LoginFactory
from pages.factory.neo_inclass_factory import NeoInClassFactory
from utilities.neo_tute_mentoring import NeoTute

feature_file_name = "Ask Question"
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
def test_student_3(request, driver):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        test_student_3 = NeoInClassFactory().get_page(driver, Platform.ANDROID.value)
        yield test_student_3
    elif Platform.WEB.name in platform_list:
        test_student_3 = NeoInClassFactory().get_page(driver, Platform.WEB.value)
        yield test_student_3


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


@given("launch the application online as neo user and navigate to home screen")
def navigate_to_one_to_many_and_mega_user(login_in):
    login_in.login_and_navigate_to_home_screen('+91-', '2013795859', otp=None)


@when("tutor start the session")
@given("tutor start the session")
def step_impl(test_tut):
    test_tut.start_neo_session()


@given('click on "JOIN" button in home page')
@when('click on "JOIN" button in home page')
def step_impl(neo_in_class):
    neo_in_class.home_click_on_join()


@when("student join neo session")
@then("student join neo session")
def step_impl(neo_in_class):
    neo_in_class.join_neo_session()


@then("verify raise hand is present in the screen")
def step_impl(neo_in_class):
    check.equal(neo_in_class.is_hand_raise_icon_present(),True, "Raise hand is not present")


@then("verify user is able to raise hand and ask question")
def step_impl(neo_in_class):
    neo_in_class.raise_hand()
    details = neo_in_class.verify_hand_is_raised()
    check.equal(details.result, True, details.reason)


@given("another student joins the session")
@when("another student joins the session")
def step_impl(test_student_2):
    login_in.login_and_navigate_to_home_screen('+91-', '2013795859', otp=None)
    test_student_2.home_click_on_join()
    test_student_2.join_neo_session()


@when("tutor start the session")
@given("tutor start the session")
def step_impl(test_tut):
    test_tut.start_neo_session()


@when("tutor allows student to ask question")
def step_impl(test_tut):
    test_tut.click_on_menu_option(expected_student_name= "Swastika1",menu_item= "Ask Question")


@given("another second student joins the session")
@when("another second student joins the session")
def step_impl(test_student_3):
    login_in.login_and_navigate_to_home_screen('+91-', '2013795859', otp=None)
    test_student_3.home_click_on_join()
    test_student_3.join_neo_session()


@then("verify user asking question has enlarged video")
def step_impl(neo_in_class):
    details = neo_in_class.current_student_has_video_enlarged()
    check.equal(details.result, True, details.reason)


@when("student hover over the info button")
def step_impl(neo_in_class):
    neo_in_class.hover_over_info_button()


@then("verify info pop_up is shown")
def step_impl(neo_in_class):
    details = neo_in_class.verify_info_pop_up(subject_name = 'Biology: Control and Coordination')
    check.equal(details.result, True, details.reason)


@when("student hover over video button")
def step_impl(neo_in_class):
    neo_in_class.hover_on_inclass_video_icon()


@when("student hover over mic button")
def step_impl(neo_in_class):
    neo_in_class.hover_on_inclass_audio_icon()


@when(parsers.parse('student turn "{text}" camera'))
def step_impl(neo_in_class, text):
    if text.lower() == 'on':
        neo_in_class.turn_on_off_camera(status='on')
    else:
        neo_in_class.turn_on_off_camera(status='off')


@then(parsers.parse('verify tool tip message "{text}" is being displayed'))
def step_impl(neo_in_class, text):
    if text.lower() == 'turn on camera':
        check.equal(neo_in_class.is_turn_on_camera_tooltip_present(),True, "{} is not present".format(text))
    elif text.lower() == 'turn off camera':
        check.equal(neo_in_class.is_turn_off_camera_tooltip_present(), True, "{} is not present".format(text))
    elif text.lower() == 'turn off microphone':
        check.equal(neo_in_class.is_turn_off_mic_tooltip_present(), True, "{} is not present".format(text))
    elif text.lower() == 'turn on microphone':
        check.equal(neo_in_class.is_turn_on_mic_tooltip_present(), True, "{} is not present".format(text))



@when(parsers.parse('student turn "{text}" mic'))
def step_impl(neo_in_class, text):
    if text.lower() == 'on':
        neo_in_class.turn_on_off_mic(status='on')
    else:
        neo_in_class.turn_on_off_mic(status='off')


@when("student hover over reaction button")
def step_impl(neo_in_class):
    neo_in_class.hover_over_reaction_button()


@then("default reactions are shown")
def step_impl(neo_in_class):
    details = neo_in_class.are_emojis_displayed()
    check.equal(details.result, True, details.reason)


@when("tutor turns on his video")
def step_impl(test_tut):
    test_tut.turn_tutor_video_on_off(status= 'on')


@then("tutor videos should be displayed")
def step_impl(neo_in_class):
    details = neo_in_class.is_tutor_video_on()
    check.equal(details.result, True, details.reason)


@then("ask question pop up is displayed")
def step_impl(neo_in_class):
    details = neo_in_class.verify_ask_question_popup_is_displayed()
    check.equal(details.result, True, details.reason)


@then("verify tutor name is shown in tutor box")
def step_impl(neo_in_class):
    detail = neo_in_class.verify_chat_elements_element_wise(element_type=  "Tutor name")
    check.equal(detail.result, True, detail.reason)
    detail = neo_in_class.verify_chat_elements_element_wise(element_type="Tutor tag")
    check.equal(detail.result, True, detail.reason)


@then("Verify that students count besides chat Forum.")
def step_impl(neo_in_class):
    neo_in_class.verify_chat_elements_element_wise(element_type='students count')


@when("tutor types the chat")
def step_impl(test_tut):
    test_tut.send_message_in_chat(text="Hi I am tutor")


@when("student sends chat message")
def step_impl(neo_in_class):
    neo_in_class.send_chat(text="Hi I am student")


@then("verify live chat by tutor and student")
def step_impl(neo_in_class):
    detail = neo_in_class.verify_tutor_messages_are_left_alligned(text="Hi I am tutor")
    check.equal(detail.result, True, detail.reason)
    details = neo_in_class.verify_student_messages_are_right_alligned(text="Hi I am student")
    check.equal(details.result, True, details.reason)


#another student impletation needed
@then("Verify that other students should able to hear when a student asks doubts to Tutor ")
def step_impl(neo_in_class):
    neo_in_class.get_audio_status_of_student(student_name="Swastika1")