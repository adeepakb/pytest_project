from pytest_bdd import scenarios, given, then, when, parsers
from pytest import fixture
from constants.platform import Platform
from pages.factory.login import LoginFactory
from pages.factory.neo_inclass_factory import NeoInClassFactory
import pytest_check as check
from utilities.neo_tute_mentoring import NeoTute

scenarios('../features/In-Class.feature')


@fixture()
def student1_login(request, driver):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        student1_login = LoginFactory().get_page(driver, Platform.ANDROID.value)
        yield student1_login
    elif Platform.WEB.name in platform_list:
        student1_login = LoginFactory().get_page(driver, Platform.WEB.value)
        yield student1_login


@fixture()
def student1_neo(request, student1_login):
    platform_list = request.config.getoption("--platform")
    if Platform.ANDROID.name in platform_list:
        student1_neo = NeoInClassFactory().get_page(student1_login.driver, Platform.ANDROID.value)
        yield student1_neo
    elif Platform.WEB.name in platform_list:
        student1_neo = NeoInClassFactory().get_page(student1_login.driver, Platform.WEB.value)
        yield student1_neo

@fixture()
def neo_tute(driver):
    neo_tute = NeoTute(driver)
    yield neo_tute

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

@given("Launch the application online")
def login_as_neo_user(student1_login):
    student1_login.login_and_navigate_to_home_screen('+91-', '2011313229', otp=None)
    # login_in.login_and_navigate_to_home_screen('+91-', '2016795330', otp=None)


# @given("Launch the application online as 2nd user")
# def login_as_neo_user(driver):
    # login_in.login_and_navigate_to_home('+91-', '2011313229', otp=None)
    # MultiLogin(driver).login_and_navigate_to_home_screen('+91-', '2011313229', otp=None)


@given("Launch the application online in mobile")
def login_as_neo_user(student1_login):
    student1_login.login_for_neo_class_mweb('+91-', '2011313229', otp=None)


@given("tutor start the session")
def step_impl(neo_tute):
    neo_tute.start_neo_session()


@when('join neo session')
@then('join neo session')
def join_a_neo_class(student1_neo):
    student1_neo.home_click_on_join()


@when('click on start class')
@then('click on start class')
def join_a_neo_session(student1_neo):
    student1_neo.join_neo_session_student('mic-on', 'cam-on')


@then('Verify the display of Focus mode icon')
def step_impl(student1_neo):
    details = student1_neo.is_focus_mode_icon_present()
    check.equal(details.result, True, details.reason)

@then('Verify the text Hand Raised in mobile browser')
def step_impl(student1_neo):
    student1_neo.click_on_hand_raise()
    details = student1_neo.verify_hand_is_raised()
    check.equal(details.result, True, details.reason)


@then('Verify display of subject/ Topicname/focus mode in mobile browser')
def step_impl(student1_neo):
    details = student1_neo.is_session_topic_inclass_present()
    check.equal(details.result, True, details.reason)

@then('Verify the display of weak signal icon in mobile browser')
def step_impl(student1_neo):
    student1_neo.set_network_flaky()
    details = student1_neo.is_weak_signal_present()
    check.equal(details.result, True, details.reason)

@then('Verify the display of controls in fullscreen mode')
def step_impl(student1_neo):
    details = student1_neo.focus_mode_bottom_container_not_active()
    check.equal(details.result, True, details.reason)

@then('Verify the class description in desktop/mobile browser')
def step_impl(student1_neo):
    subject_topic = student1_neo.get_session_topic_name_inclass()
    check.equal(all(ele is not None for ele in subject_topic), True, "Class details present in class info popup")
    student1_neo.click_on_class_info_icon()
    class_info_details_dict = student1_neo.get_classinfo_popup_session_details()
    print(class_info_details_dict)
    check.equal(all(class_info_details_dict.values()), True, "Class details present in class info popup")


@then('Verify the display of student count icon in mobile view')
@then('Verify the display of student count in mobile browser')
@then('Verify the display of student count icon')
def step_impl(student1_neo):
    details = student1_neo.verify_student_count(element_type='students count')
    check.equal(details.result, True, details.reason)


@then('Verify the display of student cards in mobile view')
def step_impl(student1_neo):
    student1_neo.get_students_from_stream_card()

@then('Verify the functionality of minimising window during session and reopening')
def step_impl(student1_neo):
    neo_tute.present_any_slide(1)
    student1_neo.do_full_screen_presentation()
    student1_neo.minimize_full_screen_presentation()
    details = student1_neo.is_minimize_full_screen_present()
    check.equal(details.result, True, details.reason)

@then('Verify the display of screen in desktop during video session')
@then('Verify the display of session video continues without fail')
@then('Verify the display of video session in chrome')
def step_impl(neo_tute, student1_neo):
    neo_tute.neo_tute.present_any_slide(13)
    details = student1_neo.is_video_being_presented()
    check.equal(details.result, True, details.reason)

@then('Verify that user should not able to pause or play video during session')
def step_impl(neo_tute, student1_neo):
    details = student1_neo.is_play_pause_btn_present()
    check.equal(details.result, False, details.reason)

@then('Verify the display of mic and camera during Focus mode')
def step_impl(student1_neo):
    details = student1_neo.mic_cam_status_in_focus_mode()
    check.equal(details.result, True, details.reason)

@then('Verify the display of controls in fullscreen mode')
def step_impl(neo_tute, student1_neo):
    neo_tute.select_focus_mode('on')
    details = student1_neo.hover_over_and_verify_bottom_container_focus_mode()
    check.equal(details.result, True, details.reason)

@then("verify the tutor's video background when student rejoins the session")
@then("Verify the tutor's video background when user refreshes the page")
def step_impl(student1_neo):
    student1_neo.refresh_and_join_the_session('mic-on', 'cam-on')
    details = student1_neo.is_video_being_presented()
    check.equal(details.result, True, details.reason)

@then("Verify the tutor's background video when network is flaky")
def step_impl(student1_neo):
    student1_neo.set_network_flaky()
    details = student1_neo.is_video_being_presented()
    check.equal(details.result, False, details.reason)


@then('Verify that the if a student speaks for less than 2 seconds his thumbnail should not be moved to view port')
def step_impl(student1_neo,student2,student2_neo):
    student2.login_and_navigate_to_home_screen('+91-', '2016170445', otp=None)
    student2_neo.home_click_on_join()
    student2_neo.join_neo_session_student('mic-on', 'cam-on')
    student2_neo.turn_on_off_student_mic('ON')
    student2_neo.turn_on_off_student_mic('OFF')
    details = student1_neo.is_student_speaking()
    check.equal(details.result, False, details.reason)

@then('Verify that the if a student speaks for more than 2 seconds his thumbnail should be moved to view port')
def step_impl(student1_neo,student2_neo):
    student2_neo.turn_on_off_student_mic('ON')
    details = student1_neo.is_student_speaking()
    check.equal(details.result, True, details.reason)

@then('Verify that if any student stays quite for 2 seconds should be removed from view port')
def step_impl(student1_neo,student2_neo):
    student2_neo.turn_on_off_student_mic('OFF')
    student2_neo.turn_on_off_student_mic('OFF')
    details = student1_neo.is_student_speaking()
    check.equal(details.result, True, details.reason)

@then('Verify that when tutor has turned off mic and chat for all students, mic icon on the student thumbnails are greyed out and shown as disabled')
def step_impl(neo_tute, student1_neo):
    neo_tute.present_any_slide(8)
    neo_tute.select_focus_mode('on')
    students_audio_status = student1_neo.get_student_audio_status()
    check.equal(all(audio_status is not None for audio_status in students_audio_status), True,
                "Audio/Mic status is displayed for other students on their thumbnail")

@then('Verify the functionality when student rejoins after"Tutor want to discuss doubt with you" is triggered')
def step_impl(neo_tute, student1_neo):
    neo_tute.present_any_slide(2)
    neo_tute.select_focus_mode('off')
    neo_tute.click_on_menu_option(expected_student_name="Test 6", menu_item="Ask Question")
    details = student1_neo.is_discuss_doubt_msg_present()
    check.equal(details.result, True, details.reason)

# @then('Verify that if multiple students are speaking, the thumbnail should appear in the view port in order of speaking')

@then('Verify the only <=3 students who are speaking should appear in view port in chronological manner')
def step_impl(student3, student3_neo):
    student3.login_and_navigate_to_home_screen('+91-', '2014947581', otp=None)
    student3_neo.home_click_on_join()
    student3_neo.join_neo_session()
    details = student1_neo.verify_users_in_chronological_order()
    check.equal(details.result, True, details.reason)


@then('Verify the display of screens when Tutor changes the slides')
def step_impl(neo_tute, student1_neo):
    neo_tute.present_any_slide(1)
    tute_slide = neo_tute.get_url_of_presented_slide(1)
    stud_slide = student1_neo.get_presented_screen_url()
    check.equal(tute_slide, stud_slide, 'slides donot match')