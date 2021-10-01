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
    neo_tute.present_any_slide(4)


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


@then("Verify that the student can enable/disable their A/V during the session using the camera and mic buttons")
@then("Verify that audio/video state transition is smooth when user toggles the controls ON/OFF")
@then("Verify that audio/video state transition is maintained when students toggle the controls ON/OFF who are not present on active screen")
def step_impl(student1_neo):
    student1_neo.turn_on_off_student_mic('OFF')
    student1_neo.turn_on_off_student_video('OFF')
    check.equal(student1_neo.get_student_video_status()['You'] is False and student1_neo.get_student_audio_status()['You'] is False, True,
                "Current student's camera and mic controls are displayed with correct status at the bottom of the session screen")

    student1_neo.turn_on_off_student_mic('ON')
    student1_neo.turn_on_off_student_video('ON')
    check.equal(student1_neo.get_student_video_status()['You'] is True and student1_neo.get_student_audio_status()['You'] is True, True,
                "Current student's camera and mic controls are displayed with correct status at the bottom of the session screen")


@then("Verify that video of student is not displayed when camera is turned off by the student")
def step_impl(student1_neo):
    student1_neo.turn_on_off_student_video('OFF')
    check.equal(student1_neo.get_student_video_status()['You'] is False,"Student is not displayed when camera is turned off by the student")


@then("Verify that student is muted when mic is turned off by the student")
def step_impl(student1_neo):
    student1_neo.turn_on_off_student_mic('OFF')
    check.equal(student1_neo.get_student_audio_status()['You'] is False,True,"Student is muted when mic is turned off by the student")


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
    check.equal(student1_neo.is_tutor_video_on(), False," Video of the tutor is turned off")


@then("Verify that tutor's audio is muted when mic of the tutor is turned off")
def step_impl(neo_tute,student1_neo):
    neo_tute.turn_tutor_audio_on_off(status='off')
    check.equal(student1_neo.is_tutor_unmute(), False," Audio of the tutor is turned off")

@then('Verify that if the student has turned off their camera and do not have their profile picture set, initials of their first name should be displayed on the thumbnail')
@then('Verify that if the student has turned off their camera and have their profile picture set, profile picture should be displayed on the thumbnail')
def step_impl(student1_neo):
    check.equal('.png' or '.jpg' in student1_neo.get_profile_cards(), True, "Profile picture should be displayed on the thumbnail")


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
    check.equal(len(student_names) == 2, True, "student names displayed on thumbnails")


@then("Verify that audio/video state transition is smooth when many students toggle the controls ON/OFF at different times")
def step_impl(student2_neo):
    student2_neo.turn_on_off_student_mic('OFF')
    student2_neo.turn_on_off_student_video('OFF')
    check.equal(student2_neo.get_student_video_status()['You'] is False and student2_neo.get_student_audio_status()['You'] is False, True,
                "Current student's camera and mic controls are displayed with correct status at the bottom of the session screen")

    student2_neo.turn_on_off_student_mic('ON')
    student2_neo.turn_on_off_student_video('ON')
    check.equal(student2_neo.get_student_video_status()['You'] is True and student2_neo.get_student_audio_status()['You'] is True, True,
                "Current student's camera and mic controls are displayed with correct status at the bottom of the session screen")


@then("Verify the browser's performance during In-class when one or more students have A/V enabled")
def step_impl(student2_neo):
    check.equal(student2_neo.is_presentation_displayed(),True,"Verified browser's performance when one or more students have A/V enabled")


@then("Verify that there are no glitches when one or many students are casting A/V and the network is flaky")
def step_impl(student2_neo):
    student2_neo.set_wifi_connection_off()
    check.equal(student2_neo.is_presentation_displayed(), True, "Verified browser's performance when one or more students have A/V enabled and the network is flaky")
    student2_neo.set_wifi_connection_on()


@then("Verify the browser's performance during In-class when all students have A/V disabled")
def step_impl(student1_neo,student2_neo):
    student1_neo.turn_on_off_student_mic('OFF')
    student1_neo.turn_on_off_student_video('OFF')
    student2_neo.turn_on_off_student_mic('OFF')
    student2_neo.turn_on_off_student_video('OFF')
    check.equal(student2_neo.is_presentation_displayed(),True,"Verified browser's performance when one or more students have A/V enabled")


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


#deepak


@given("Student launches in-class and navigate to home page")
def step_impl(login_in):
    student1_details = get_data(Login_Credentials, 'neo_login_detail2', 'student3')
    login_in.login_and_navigate_to_home_screen(student1_details['code'], student1_details['mobile_no'], otp=None)


@given("student navigates to byjus classes screen")
def step_impl(neo_in_class):
    neo_in_class.navigate_to_byjus_classes_screen()


@when("student join neo session")
@then("student join neo session")
def step_impl(neo_in_class):
    neo_in_class.join_neo_session()


@given("tutor start the session")
def step_impl(test_tut):
    test_tut.start_neo_session(login_data="neo_login_detail2", user='student1')


@when("tutor turns off his video")
def step_impl(test_tut):
    test_tut.turn_tutor_video_on_off(status= 'off')


@when("tutor turns off his audio")
def step_impl(test_tut):
    test_tut.turn_tutor_audio_on_off(status= 'off')


@given('click on "JOIN" button in home page')
@when('click on "JOIN" button in home page')
def step_impl(neo_in_class):
    neo_in_class.home_click_on_join()


@then("Verify the tutor's video section when video of the tutor is turned off")
def step_impl(neo_in_class,test_tut):
    details = neo_in_class.is_tutor_video_on()
    check.equal(details.result , False, details.reason)
    details = test_tut.get_video_status()
    check.equal(details.result, False, details.reason)


@then("Verify that tutor's video is not displayed when camera of the tutor is turned off")
def step_impl(neo_in_class,test_tut):
    details = neo_in_class.is_tutor_video_on()
    check.equal(details.result, False, details.reason)
    details = test_tut.get_video_status()
    check.equal(details.result, False, details.reason)


@then("Verify that tutor's audio is muted when mic of the tutor is turned off")
def step_impl(neo_in_class,test_tut):
    details = neo_in_class.is_tutor_mute()
    check.equal(details.result, True, details.reason)


@then("Verify that tutor's audio/video is not playing when both camera and mic of the tutor is turned off")
def step_impl(neo_in_class,test_tut):
    details = neo_in_class.is_tutor_mute()
    check.equal(details.result, True, details.reason)
    details = neo_in_class.is_tutor_video_on()
    check.equal(details.result, False, details.reason)
    details = test_tut.get_video_status()
    check.equal(details.result, False, details.reason)


@then("Verify that Tutor's first name is displayed on the tutor's video thumbnail")
def step_impl(neo_in_class):
    detail = neo_in_class.verify_chat_elements_element_wise(element_type=  "Tutor name")
    check.equal(detail.result, True, detail.reason)


@then("Verify that 'Tutor' text is displayed on the tutor's video thumbnail below tutor's name")
def step_impl(neo_in_class):
    detail = neo_in_class.verify_chat_elements_element_wise(element_type="Tutor tag")
    check.equal(detail.result, True, detail.reason)


@then("Verify that students cannot control tutor's camera/mic")
def step_impl(neo_in_class):
    detail = neo_in_class.click_on_camera_mic_disabled()
    check.equal(detail.result, True, detail.reason)


@then("Verify that correct Subject name and Topic name followed by info icon is displayed on the top left corner of "
      "session window")
def step_impl(neo_in_class):
    detail = neo_in_class.is_session_topic_inclass_present()
    check.equal(detail,True,"Subject topic name is not displayed")
    neo_in_class.verify_session_topic_name_inclass(topictext="Control and Coordination")


@when("student hover over the info button")
def step_impl(neo_in_class):
    neo_in_class.hover_over_info_button()


@then("Verify that clicking on info icon should open Class info popup with correct information/details on the active "
      "session")
def step_impl(neo_in_class):
    detail = neo_in_class.verify_info_pop_up(subject_name='Biology: Control and Coordination')
    check.equal(detail.result, True, detail.reason)


@when("user dismisses info popup")
def step_impl(neo_in_class):
    neo_in_class.close_info_pop_up()


@when("student scrolls right on students cards")
def step_impl(neo_in_class):
    neo_in_class.scroll_students_card(towards = 'right')


@then("Verify that clicking on info icon or anywhere else on the screen, while Class Info pop up is open, "
      "should dismiss the pop-up")
def step_impl(neo_in_class):
    detail = neo_in_class.verify_info_pop_up()
    check.equal(detail.result, False, detail.reason)


@then("Verify that when few students drop and total count drops below 7, previous (<) and next (>) icon disappears from below the students video thumbnails")
@then("Verify that students count who have joined session is <=6, previous (<) and next (>) icon should not appear below the student video thumbnails")
def step_impl(neo_in_class):
    detail = neo_in_class.are_steam_student_arrow_button_displayed()
    check.equal(detail.result, False, detail.reason)


@then("Verify that when more than 6 students have joined previous (<) and next (>) icon appear below the students video thumbnails")
def step_impl(neo_in_class):
    detail = neo_in_class.are_steam_student_arrow_button_displayed()
    check.equal(detail.result, False, detail.reason)


@then("Verify that clicking on next (>) icon should scroll the students thumbnails towards the right and screen should update left most column moving out of the screen and new column appearing on the right")
def step_impl(neo_in_class):
    #use this method without scrolling
    details = neo_in_class.verify_students_after_scrolling_right()
    check.equal(details.result, True, details.reason)


@then("Verify that next (>) icon is clickable until all thumbnails of students have been displayed")
def step_impl(neo_in_class):
    details = neo_in_class.scroll_till_end_on_student_card()
    check.equal(details.result, True, details.reason)

@then("Verify that previous (<) icon is clickable until the user reaches the first column of the thumbnails")
def step_impl(neo_in_class):
    details = neo_in_class.scroll_till_left_end_on_student_card()
    check.equal(details.result, True, details.reason)

@then("Verify that previous (<) and next (>) icons change (disabled state) when they reach first and last page respectively")
def step_impl(neo_in_class):
    details = neo_in_class.scroll_till_end_on_student_card()
    check.equal(details.result, True, details.reason)
    details = neo_in_class.scroll_till_left_end_on_student_card()
    check.equal(details.result, True, details.reason)


@then('Verify that "Raise Hand" button is present at the bottom of the screen next to camera and mic controls')
def step_impl(neo_in_class):
    check.equal(neo_in_class.is_hand_raise_icon_present(),True, "Raise hand is not present")


@then('Verify that when student clicks on "Raise Hand" button, button should change to "Lower Hand" button. Also on the chat forum same should be notified as "You raised hand" ')
@then('Verify that user should be able to use "Raise Hand" functionality anytime during the session')
def step_impl(neo_in_class):
    neo_in_class.raise_hand()
    details = neo_in_class.verify_hand_is_raised()
    check.equal(details.result, True, details.reason)


@then("Verify the Lower Hand button doesn't change if reconnection happens due to flaky network")
def step_impl(neo_in_class):
    neo_in_class.raise_hand()
    neo_in_class.set_wifi_connection_off()
    neo_in_class.set_wifi_connection_on()
    details = neo_in_class.verify_hand_is_raised()
    check.equal(details.result, True, details.reason)


@then('Verify the state of "Lower Hand" button if user leaves and then rejoins the session')
def step_impl(neo_in_class):
    neo_in_class.raise_hand()
    login_in.login_and_navigate_to_home_screen('+91-', '2013795859', otp=None)
    neo_in_class.home_click_on_join()
    neo_in_class.join_neo_session()
    details = neo_in_class.verify_hand_is_raised()
    check.equal(details.result, True, details.reason)


@then('Verify that user should be able to use "Lower Hand" functionality anytime during the session')
def step_impl(neo_in_class):
    neo_in_class.raise_hand()
    neo_in_class.unraise_hand()
    detail = neo_in_class.verify_hand_is_raised()
    check.equal(detail.result, False, detail.reason)


@then('Verify that when student clicks on "Lower Hand" button, button should change to "Raise Hand" button. Also on the chat forum same should be notified as "You lowered hand"')
def step_impl(neo_in_class):
    neo_in_class.raise_hand()
    neo_in_class.unraise_hand()
    detail = neo_in_class.verify_hand_is_raised()
    check.equal(detail.result, False, detail.reason)


@then('Verify that if a student has raised hand and the tutor lowers the hand for that student, text "Lower Hand" button should again change to "Raise Hand" and button goes to default state')
def step_impl(neo_in_class):
    student1_details = get_data(Login_Credentials, 'neo_login_detail2', 'student3')
    neo_in_class.raise_hand()
    test_tut.click_on_menu_option(expected_student_name=student1_details['name'], menu_item='Hands Down')
    detail = neo_in_class.verify_hand_is_raised()
    check.equal(detail.result, False, detail.reason)



@then("Verify that if other students in the class raises hand, a hand icon should be displayed beside the mic icon on the student's thumbnail")
def step_impl(neo_in_class, student2_neo, student2):
    student2_details = get_data(Login_Credentials, 'neo_login_detail2', 'student4')
    student2.login_and_navigate_to_home_screen(student2_details['code'], student2_details['mobile_no'], otp=None)
    student2_neo.home_click_on_join()
    student2_neo.join_neo_session()
    student2_neo.raise_hand()
    detail = neo_in_class.verify_hand_is_raised_for_student(student_name=student2_details['name'])
    check.equal(detail.result, True, detail.reason)


@then("Verify that if other students in the class lower hand, the hand icon should be removed from the student's thumbnail")
def step_impl(neo_in_class, student2_neo, student2):
    student2_details = get_data(Login_Credentials, 'neo_login_detail2', 'student4')
    student2.login_and_navigate_to_home_screen(student2_details['code'], student2_details['mobile_no'], otp=None)
    student2_neo.home_click_on_join()
    student2_neo.join_neo_session()
    student2_neo.unraise_hand()
    detail = neo_in_class.verify_hand_is_raised_for_student(student_name=student2_details['name'])
    check.equal(detail.result, False, detail.reason)

@then('Verify the status of "Lower Hand" button if a student has raised hand and then drops from session, the tutor lowers the hand for that student and then the student rejoins the class')
def step_impl(neo_in_class, student2_neo, student2,test_tut):
    student2_details = get_data(Login_Credentials, 'neo_login_detail2', 'student4')
    student2.login_and_navigate_to_home_screen(student2_details['code'], student2_details['mobile_no'], otp=None)
    student2_neo.home_click_on_join()
    student2_neo.join_neo_session()
    student2_neo.raise_hand()
    test_tut.click_on_menu_option(expected_student_name=student2_details['name'], menu_item='Hands Down')
    detail= student2_neo.verify_hands_down_message()
    check.equal(detail.result, False, detail.reason)

@then('Verify that "Thumbs Up" button is present at the bottom of the screen')
def step_impl(neo_in_class):
    detail = neo_in_class.verify_thumbs_reaction_icon_displayed()
    check.equal(detail.result,True, detail.reason)


@then('Verify that clicking on "Thumbs Up" icon expands the expression tab and list of expressions are displayed')
def step_impl(neo_in_class):
    neo_in_class. click_on_reaction_thumb_icon()
    detail = neo_in_class.is_reactions_icons_present()
    check.equal(detail.result, True, detail.reason)


@then("Verify that animation of the expressions on the session screen ")
@then('Verify that student is able to send expression during the session')
def step_impl(neo_in_class):
    neo_in_class.select_any_celebration_symbol(celeb_symbol='clap')
    detail = neo_in_class.are_emojis_displayed()
    check.equal(detail.result, True, detail.reason)