import time

from pytest_bdd import scenarios, given, when, then, parsers
from pytest import fixture

from constants.constants import Login_Credentials
from constants.load_json import get_data
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
def student2(request):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        student2 = LoginFactory().get_page(None, Platform.ANDROID.value)
        yield student2
    elif Platform.WEB.name in platform_list:
        student2 = LoginFactory().get_page(None, Platform.WEB.value)
        yield student2


@fixture()
def student2_neo(request, student2):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        student2_neo = NeoInClassFactory().get_page(student2.driver, Platform.ANDROID.value)
        yield student2_neo
    elif Platform.WEB.name in platform_list:
        student2_neo = NeoInClassFactory().get_page(student2.driver, Platform.WEB.value)
        yield student2_neo


@fixture()
def student3(request):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        student3 = LoginFactory().get_page(None, Platform.ANDROID.value)
        yield student3
    elif Platform.WEB.name in platform_list:
        student3 = LoginFactory().get_page(None, Platform.WEB.value)
        yield student3


@fixture()
def student3_neo(request, student3):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        student3_neo = NeoInClassFactory().get_page(student3.driver, Platform.ANDROID.value)
        yield student3_neo
    elif Platform.WEB.name in platform_list:
        student3_neo = NeoInClassFactory().get_page(student3.driver, Platform.WEB.value)
        yield student3_neo

@fixture()
def student4(request):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        student4 = LoginFactory().get_page(None, Platform.ANDROID.value)
        yield student4
    elif Platform.WEB.name in platform_list:
        student4 = LoginFactory().get_page(None, Platform.WEB.value)
        yield student4


@fixture()
def student4_neo(request, student4):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        student4_neo = NeoInClassFactory().get_page(student4.driver, Platform.ANDROID.value)
        yield student4_neo
    elif Platform.WEB.name in platform_list:
        student4_neo = NeoInClassFactory().get_page(student4.driver, Platform.WEB.value)
        yield student4_neo


@fixture()
def student5(request):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        student5 = LoginFactory().get_page(None, Platform.ANDROID.value)
        yield student5
    elif Platform.WEB.name in platform_list:
        student5 = LoginFactory().get_page(None, Platform.WEB.value)
        yield student5


@fixture()
def student5_neo(request, student5):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        student5_neo = NeoInClassFactory().get_page(student5.driver, Platform.ANDROID.value)
        yield student5_neo
    elif Platform.WEB.name in platform_list:
        student5_neo = NeoInClassFactory().get_page(student5.driver, Platform.WEB.value)
        yield student5_neo


@fixture()
def student6(request):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        student6 = LoginFactory().get_page(None, Platform.ANDROID.value)
        yield student6
    elif Platform.WEB.name in platform_list:
        student6 = LoginFactory().get_page(None, Platform.WEB.value)
        yield student6


@fixture()
def student6_neo(request, student6):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        student6_neo = NeoInClassFactory().get_page(student6.driver, Platform.ANDROID.value)
        yield student6_neo
    elif Platform.WEB.name in platform_list:
        student6_neo = NeoInClassFactory().get_page(student6.driver, Platform.WEB.value)
        yield student6_neo



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
def step_impl(login_in):
    student1_details = get_data(Login_Credentials, 'neo_login_detail2', 'student3')
    login_in.login_and_navigate_to_home_screen(student1_details['code'], student1_details['mobile_no'], otp=None)


@when("tutor start the session")
@given("tutor start the session")
def step_impl(test_tut):
    test_tut.start_neo_session(login_data="neo_login_detail2", user='student1')


@given('click on "JOIN" button in home page')
@when('click on "JOIN" button in home page')
def step_impl(neo_in_class):
    neo_in_class.home_click_on_join()


@when("student join neo session")
@then("student join neo session")
def step_impl(neo_in_class):
    neo_in_class.join_neo_session()


@then("Verify the raise hand option should present in the screen")
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


@then("Verify the Tutor name should display on the screen")
@then("verify tutor name is shown in tutor box")
def step_impl(neo_in_class):
    detail = neo_in_class.verify_chat_elements_element_wise(element_type=  "Tutor name")
    check.equal(detail.result, True, detail.reason)
    detail = neo_in_class.verify_chat_elements_element_wise(element_type="Tutor tag")
    check.equal(detail.result, True, detail.reason)


@then("Verify that student's count and live chat should be displayed below the Tutor video")
@then("Verify that students count besides chat Forum.")
def step_impl(neo_in_class):
    neo_in_class.verify_chat_elements_element_wise(element_type='students count')


@when("tutor types the chat")
def step_impl(test_tut):
    test_tut.send_message_in_chat(text="Hi I am tutor")


@when("student sends chat message")
def step_impl(neo_in_class):
    neo_in_class.send_chat(text="Hi I am student")


@then("Verify the functionality of the live chat")
@then("verify live chat by tutor and student")
def step_impl(neo_in_class,test_tut):
    test_tut.send_message_in_chat(text="Hi I am tutor")
    time.sleep(2)
    neo_in_class.send_chat("for confirming tutor's message")
    detail = neo_in_class.verify_tutor_messages_are_left_alligned(text="Hi I am tutor")
    check.equal(detail.result, True, detail.reason)
    neo_in_class.send_chat(text="Hi I am student")
    time.sleep(2)
    details = neo_in_class.verify_student_messages_are_right_alligned(text="Hi I am student")
    check.equal(details.result, True, details.reason)


@then("Verify that student should able to ask doubt clicking on the 'Raise hand' option")
@then("Verify that when the user click on the 'raise hand' the hand icon be displayed on the student’s screen")
def step_impl(neo_in_class):
    neo_in_class.raise_hand()
    details = neo_in_class.verify_hand_is_raised()
    check.equal(details.result, True, details.reason)


@then("Verify that the student who is asking the question, his  video should be enlarged compared to other students.")
def step_impl(neo_in_class,test_tut,student2,student2_neo,student3,student3_neo):
    student1_details2 = get_data(Login_Credentials, 'neo_login_detail2', 'student2')
    student2.login_and_navigate_to_home_screen(student1_details2['code'], student1_details2['mobile_no'], otp=None)
    student2_neo.home_click_on_join()
    student2_neo.join_neo_session()
    student1_details3 = get_data(Login_Credentials, 'neo_login_detail2', 'student1')
    student3.login_and_navigate_to_home_screen(student1_details3['code'], student1_details3['mobile_no'], otp=None)
    student3_neo.home_click_on_join()
    student3_neo.join_neo_session()
    student1_details = get_data(Login_Credentials, 'neo_login_detail2', 'student3')
    test_tut.click_on_menu_option(expected_student_name=student1_details['name'], menu_item="Ask Question")
    details = neo_in_class.current_student_has_video_enlarged()
    check.equal(details.result, True, details.reason)


@then("Verify when user hover on the info popup on the top of the screen")
def step_impl(neo_in_class):
    neo_in_class.hover_over_info_button()
    details = neo_in_class.verify_info_pop_up(subject_name = 'Biology: Control and Coordination')
    check.equal(details.result, True, details.reason)
    neo_in_class.close_info_pop_up()

@then("Verify when user hover on the video button")
def step_impl(neo_in_class):
    neo_in_class.turn_on_off_camera(status='on')
    neo_in_class.hover_on_inclass_video_icon()
    check.equal(neo_in_class.is_turn_off_camera_tooltip_present(), True, "")
    neo_in_class.turn_on_off_camera(status='off')
    neo_in_class.hover_on_inclass_video_icon()
    check.equal(neo_in_class.is_turn_on_camera_tooltip_present(), True, "")


@then("Verify when user hover on the audio button")
def step_impl(neo_in_class):
    neo_in_class.turn_on_off_mic(status='on')
    neo_in_class.hover_on_inclass_audio_icon()
    check.equal(neo_in_class.is_turn_off_mic_tooltip_present(), True, "")
    neo_in_class.turn_on_off_mic(status='off')
    neo_in_class.hover_on_inclass_audio_icon()
    check.equal(neo_in_class.is_turn_on_mic_tooltip_present(), True, "")

@then("Verify that a student should not be able to answer other student's questions in the chat")
@then("Verify that student can't control other student's video & mic when they ask questions")
def step_impl(neo_in_class):
    details = neo_in_class.verify_other_student_mic_cam_cannt_be_controlled()
    check.equal(details.result, True, details.reason)

@then("Verify the default reactions when user hover on the reaction (thumbs up)")
def step_impl(neo_in_class):
    neo_in_class.hover_over_reaction_button()
    details = neo_in_class.is_reactions_icons_present()
    check.equal(details.result, True, details.reason)


@then("Verify the Tutor's video should display right side of the screen")
def step_impl(neo_in_class,test_tut):
    test_tut.turn_tutor_video_on_off(status='on')
    details = neo_in_class.is_tutor_video_on()
    check.equal(details.result, True, details.reason)
    test_tut.turn_tutor_video_on_off(status='off')

@then("Verify the student whom the tutor select those students can ask questions")
def step_impl(neo_in_class, test_tut):
    student1_details = get_data(Login_Credentials, 'neo_login_detail2', 'student3')
    test_tut.click_on_menu_option(expected_student_name=student1_details['name'], menu_item="Remove from Ask Question")
    test_tut.click_on_menu_option(expected_student_name=student1_details['name'], menu_item="Ask Question")
    time.sleep((1))
    details = neo_in_class.verify_ask_question_popup_is_displayed()
    check.equal(details.result, True, details.reason)


@then("Verify that alignment of the thumbnail when tutor allow student to ask question")
@then("Verify that student should able to ask doubt when the Tutor allow the student to come on the screen")
def step_impl(neo_in_class,test_tut,student2,student2_neo,student3,student3_neo):
    student1_details = get_data(Login_Credentials,'neo_login_detail2', 'student3')
    test_tut.click_on_menu_option(expected_student_name=student1_details['name'], menu_item="Remove from Ask Question")
    test_tut.click_on_menu_option(expected_student_name=student1_details['name'], menu_item="Ask Question")
    details = neo_in_class.current_student_has_video_enlarged()
    check.equal(details.result, True, details.reason)


@then("Verify that other students should able to hear when a student asks doubts to Tutor")
def step_impl(student2_neo):
    student1_details = get_data(Login_Credentials, 'neo_login_detail2', 'student3')
    student2_neo.get_audio_status_of_student(student_name=student1_details['name'])


@then("Verify that when the Tutor remove a student from ask question , the thumbnail should be realigned")
def step_impl(neo_in_class,test_tut):
    student1_details = get_data(Login_Credentials, 'neo_login_detail2', 'student3')
    test_tut.click_on_menu_option(expected_student_name=student1_details['name'], menu_item="Ask Question")
    test_tut.click_on_menu_option(expected_student_name=student1_details['name'], menu_item="Remove from Ask Question")
    time.sleep(2)
    details = neo_in_class.current_student_has_video_enlarged()
    check.equal(details.result, False, details.reason)


@then("Verify that when a student is on focus mode, five thumbnails should be displayed on the screen.")
def step_impl(student5,student5_neo,student4,student4_neo,student3,student3_neo,test_tut):
    test_tut.select_focus_mode(status= 'on')
    student3_details = get_data(Login_Credentials, 'neo_login_detail1', 'student2')
    student3.login_and_navigate_to_home_screen(student3_details['code'], student3_details['mobile_no'], otp=None)
    student3_neo.home_click_on_join()
    student3_neo.join_neo_session()
    student4_details = get_data(Login_Credentials, 'neo_login_detail1', 'student3')
    student4.login_and_navigate_to_home_screen(student4_details['code'], student4_details['mobile_no'], otp=None)
    student4_neo.home_click_on_join()
    student4_neo.join_neo_session()
    student5_details = get_data(Login_Credentials, 'neo_login_detail1', 'student4')
    student5.login_and_navigate_to_home_screen(student5_details['code'], student5_details['mobile_no'], otp=None)
    student5_neo.home_click_on_join()
    student5_neo.join_neo_session()
    check.equal(student5_neo.verify_alignment_stream_list(),True, "Verified alignment of student's thumbnail when 5 students join")
    test_tut.select_focus_mode(status='off')