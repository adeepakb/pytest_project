from pytest_bdd import scenarios, given, then, when, parsers
from pytest import fixture
from constants.constants import Login_Credentials
from constants.load_json import get_data
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


@given("launch the application online as neo user and navigate to home screen")
def step_impl(student1_login):
    student1_details = get_data(Login_Credentials, 'neo_login_detail1', 'student1')
    student1_login.login_and_navigate_to_home_screen(student1_details['code'], student1_details['mobile_no'], otp=None)


@given("tutor start the session")
def step_impl(neo_tute):
    neo_tute.start_neo_session()
    # neo_tute.present_any_slide(1)


@when('click on "JOIN" button in home page')
def step_impl(student1_neo):
    student1_neo.home_click_on_join()


@when("student join neo session")
def step_impl(student1_neo):
    student1_neo.join_neo_session()


@then("Verify the alignment of student's thumbnail when only one student joins and enters the class")
def step_impl(student1_neo):
    check.equal(student1_neo.verify_alignment_stream_list(),True, "Verified alignment of student's thumbnail when only 1 student")


@then("Verify that camera and mic controls are present at the bottom left side on the screen")
def step_impl(student1_neo):
    student1_audio_status = student1_neo.get_inclass_student_audio_status()
    student1_video_status = student1_neo.get_inclass_student_video_status()
    check.equal(student1_audio_status is not None and student1_video_status is not None, True, 'Camera and mic controls are present at the bottom left side on the screen')


@then("Verify that camera and mic states are retained with the state they are set before joining the session")
def step_impl(student1_neo):
    student1_audio_status = student1_neo.get_inclass_student_audio_status()
    student1_video_status = student1_neo.get_inclass_student_video_status()
    check.equal(student1_audio_status == student1_video_status == "ON", True, 'Camera and mic states are retained with the state they are set before joining the session')


@then("Verify the alignment of Tutor's video when student joins the class")
def step_impl(student1_neo):
    details = student1_neo.verify_presentation_dimension_ratio()
    check.equal(details.result, True, details.reason)


@then("Verify that the student can enable/disable their A/V during the session using the camera and mic buttons")
@then("Verify that audio/video state transition is smooth when user toggles the controls ON/OFF")
@then("Verify that audio/video state transition is maintained when students toggle the controls ON/OFF who are not present on active screen")
def step_impl(student1_neo):
    student1_neo.turn_on_off_student_mic('OFF')
    student1_neo.turn_on_off_student_video('OFF')
    students_audio_status = student1_neo.get_student_audio_status()
    students_video_status = student1_neo.get_student_video_status()
    check.equal(students_video_status['You'] is False and students_audio_status['You'] is False, True , "Current student's camera and mic controls are displayed with correct status at the bottom of the session screen")

    student1_neo.turn_on_off_student_mic('ON')
    student1_neo.turn_on_off_student_video('ON')
    students_audio_status = student1_neo.get_student_audio_status()
    students_video_status = student1_neo.get_student_video_status()
    check.equal(students_video_status['You'] is True and students_audio_status['You'] is True, True , "Current student's camera and mic controls are displayed with correct status at the bottom of the session screen")


@then("Verify that video of student is not displayed when camera is turned off by the student")
def step_impl(student1_neo):
    student1_neo.turn_on_off_student_video('OFF')
    student_video_status = student1_neo.get_student_video_status()
    check.equal(student_video_status['You'] is False,True,"Student is not displayed when camera is turned off by the student")


@then("Verify that student is muted when mic is turned off by the student")
def step_impl(student1_neo):
    student1_neo.turn_on_off_student_mic('OFF')
    student_audio_status = student1_neo.get_student_audio_status()
    check.equal(student_audio_status['You'] is False,True,"Student is muted when mic is turned off by the student")


@then("Verify that camera and mic icons change when same are toggled On/Off")
def step_impl(student1_neo):
    student1_neo.turn_on_off_student_mic('ON')
    check.equal(student1_neo.get_inclass_student_audio_status()=='ON',True,"Student is muted when mic is turned off by the student")
    student1_neo.turn_on_off_student_video('ON')
    check.equal(student1_neo.get_inclass_student_video_status() == 'ON', True,"Student is muted when mic is turned off by the student")


@then("Verify that a translucent window encases the student's name on their thumbnail")
def step_impl(student1_neo):
    student_names = student1_neo.get_all_student_names()
    check.equal(all(student_name is not None for student_name in student_names), True,"student names displayed on thumbnails")


@then("Verify the tutor's video section when video of the tutor is turned off")
def step_impl(neo_tute,student1_neo):
    neo_tute.turn_tutor_video_on_off(status='off')
    details = student1_neo.is_tutor_video_on()
    check.equal(details.result, False,details.reason)


@then("Verify that tutor's audio is muted when mic of the tutor is turned off")
def step_impl(neo_tute,student1_neo):
    neo_tute.turn_tutor_audio_on_off(status='off')
    details = student1_neo.is_tutor_mute()
    check.equal(details.result, True,details.reason)


@then('Verify that if the student has turned off their camera and do not have their profile picture set, initials of their first name should be displayed on the thumbnail')
def step_impl(student1_neo):
    student1_neo.turn_on_off_student_video('OFF')
    profile_card_details = student1_neo.get_profile_cards()
    check.equal('https://static.tllms.com/assets/k12/premium_online/byjus_classes/common/initial_avatars/' in profile_card_details[0], True, "Profile picture is not displayed on the thumbnail")
    student1_neo.turn_on_off_student_video('ON')

@then("Verify the default alignment of student's thumbnails when two students join and enter the class")
def step_impl(student2,student2_neo):
    student2_details = get_data(Login_Credentials, 'neo_login_detail1', 'student2')
    student2.login_and_navigate_to_home_screen(student2_details['code'], student2_details['mobile_no'], otp=None)
    student2_neo.home_click_on_join()
    student2_neo.join_neo_session()
    check.equal(student2_neo.verify_alignment_stream_list(),True, "Verified alignment of student's thumbnail when 2 students join")


@then("Verify that the student's thumbnails update dynamically when any new student joins while session is in progress")
def step_impl(student2_neo):
    student_names = student2_neo.get_all_student_names()
    check.equal(len(student_names) >= 2, True, "student names displayed on thumbnails")


@then("Verify that audio/video state transition is smooth when many students toggle the controls ON/OFF at different times")
def step_impl(student2_neo):
    student2_neo.turn_on_off_student_mic('OFF')
    student2_neo.turn_on_off_student_video('OFF')
    check.equal(student2_neo.get_student_audio_status()['You'] is False and student2_neo.get_student_video_status()['You'] is False, True,
                "Current student's camera and mic controls are displayed with correct status at the bottom of the session screen")

    student2_neo.turn_on_off_student_mic('ON')
    student2_neo.turn_on_off_student_video('ON')
    check.equal(student2_neo.get_student_audio_status()['You'] is True and student2_neo.get_student_video_status()['You'] is True, True,
                "Current student's camera and mic controls are displayed with correct status at the bottom of the session screen")


@then("Verify the browser's performance during In-class when one or more students have A/V enabled")
def step_impl(student2_neo):
    details  = student2_neo.is_presentation_displayed()
    check.equal(details.result,True,details.reason)


@then("Verify that there are no glitches when one or many students are casting A/V and the network is flaky")
def step_impl(student2_neo):
    student2_neo.set_wifi_connection_off()
    details = student2_neo.is_presentation_displayed()
    check.equal(details.result, True,details.reason)
    student2_neo.set_wifi_connection_on()


@then("Verify the browser's performance during In-class when all students have A/V disabled")
def step_impl(student1_neo,student2_neo):
    student1_neo.turn_on_off_student_mic('OFF')
    student1_neo.turn_on_off_student_video('OFF')
    student2_neo.turn_on_off_student_mic('OFF')
    student2_neo.turn_on_off_student_video('OFF')
    details = student2_neo.is_presentation_displayed()
    check.equal(details.result, True, details.reason)


@then("Verify that camera and mic button's states are retained with the state they are set when network is lost and then connection is established again")
def step_impl(student2_neo):
    student2_neo.set_wifi_connection_off()
    student2_neo.set_wifi_connection_on()
    student2_audio_status = student2_neo.get_inclass_student_audio_status()
    student2_video_status = student2_neo.get_inclass_student_video_status()
    check.equal(student2_audio_status == student2_video_status == "OFF", True,
                'Camera and mic states are retained with the state with the state they are set when network is lost and connection is established again')


@then("Verify that audio and video states are retained with the state they are set when network is lost and then connection is established again")
def step_impl(student2_neo):
    student2_neo.set_wifi_connection_off()
    student2_neo.set_wifi_connection_on()
    student2_audio_status = student2_neo.get_student_audio_status()
    student2_video_status = student2_neo.get_student_video_status()
    check.equal(student2_video_status['You'] is False and student2_audio_status['You'] is False, True,
                "Audio and video states are retained when network is lost and connection is established again")


@then(parsers.parse("Verify that current student's name is not displayed on the thumbnail, instead '{text}' text is displayed at the bottom left corner of the thumbnail"))
def step_impl(student2_neo,text):
    student_names = student2_neo.get_all_student_names()
    check.equal(student_names[0] == text, True, "current student where %s is displayed on the thumbnail"%text)


@then("Verify that, for current student, other student's name are displayed at the bottom left corner of the thumbnail")
def step_impl(student2_neo):
    student_names = student2_neo.get_all_student_names()
    check.equal(all(student_name is not None for student_name in student_names), True,"Smaller thumbnails of the students are displayed below the video window")


@then("Verify the default alignment of student's thumbnails when three students join and enter the class")
def step_impl(student3,student3_neo):
    student3_details = get_data(Login_Credentials, 'neo_login_detail1', 'student3')
    student3.login_and_navigate_to_home_screen(student3_details['code'], student3_details['mobile_no'], otp=None)
    student3_neo.home_click_on_join()
    student3_neo.join_neo_session()
    check.equal(student3_neo.verify_alignment_stream_list(), True,"Verified alignment of student's thumbnail when 3 students join")


@then("Verify the default alignment of student's thumbnails when four students join and enter the class")
def step_impl(student4,student4_neo):
    student4_details = get_data(Login_Credentials, 'neo_login_detail1', 'student4')
    student4.login_and_navigate_to_home_screen(student4_details['code'], student4_details['mobile_no'], otp=None)
    student4_neo.home_click_on_join()
    student4_neo.join_neo_session()
    check.equal(student4_neo.verify_alignment_stream_list(), True, "Verified alignment of student's thumbnail when 3 students join")


@then("Verify the default alignment of student's thumbnails when five students join and enter the class")
def step_impl(student5,student5_neo):
    student5_details = get_data(Login_Credentials, 'neo_login_detail1', 'student5')
    student5.login_and_navigate_to_home_screen(student5_details['code'], student5_details['mobile_no'], otp=None)
    student5_neo.home_click_on_join()
    student5_neo.join_neo_session()
    check.equal(student5_neo.verify_alignment_stream_list(),True, "Verified alignment of student's thumbnail when 5 students join")


@then("Verify the default alignment of student's thumbnails(six students) when they join and enter the class")
def step_impl(student6,student6_neo):
    student6_details = get_data(Login_Credentials, 'neo_login_detail1', 'student6')
    student6.login_and_navigate_to_home_screen(student6_details['code'], student6_details['mobile_no'], otp=None)
    student6_neo.home_click_on_join()
    student6_neo.join_neo_session()
    check.equal(student6_neo.verify_alignment_stream_list(), True,"Verified alignment of student's thumbnail when 6 students join")


@given("Launch the application online")
def login_as_neo_user(student1_login):
    student1_login.login_and_navigate_to_home_screen('+91-', '2011313229', otp=None)
    # login_in.login_and_navigate_to_home_screen('+91-', '2016795330', otp=None)

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

@then('Verify that if multiple students are speaking, the thumbnail should appear in the view port in order of speaking')
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