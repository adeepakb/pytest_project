from pytest_bdd import scenarios, given, then, when
from pytest import fixture
from constants.constants import Login_Credentials
from constants.load_json import get_data
from constants.platform import Platform
from pages.factory.login import LoginFactory
from pages.factory.neo_inclass_factory import NeoInClassFactory
import pytest_check as check
from utilities.neo_tute_mentoring import NeoTute

scenarios('../features/Assets.feature')


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


@fixture()
def neo_tute(driver):
    neo_tute = NeoTute(driver)
    yield neo_tute


@given("launch the application online as neo user and navigate to home screen")
def navigate_to_one_to_many_and_mega_user(login_in):
    student1_details = get_data(Login_Credentials, 'neo_login_detail1', 'student1')
    login_in.login_and_navigate_to_home_screen(student1_details['code'], student1_details['mobile_no'], otp=None)


@when("tutor start the session")
def step_impl(neo_tute):
    neo_tute.start_neo_session(login_data="neo_login_detail1", user='student1')


@when('click on "JOIN" button in home page')
def step_impl(neo_in_class):
    neo_in_class.home_click_on_join()


@when("student join neo session")
def step_impl(neo_in_class):
    neo_in_class.join_neo_session()


@then("Verify that the volume slider is displayed when Tutor keeps cursor on the volume icon of Video")
def step_impl(neo_tute, neo_in_class):
    neo_tute.click_on_tab_item(tab_name="Session Slides")
    neo_tute.select_focus_mode('off')
    neo_tute.set_students_camera('on')
    neo_tute.set_students_mic('on')
    neo_in_class.turn_on_off_student_mic('ON')
    expected_video_slide_num = neo_tute.find_video_slide()
    active_slide_number = neo_tute.active_presentation_slide_number()
    if expected_video_slide_num != active_slide_number:
        neo_tute.present_any_slide(expected_video_slide_num)
        neo_tute.select_focus_mode('off')
    check.equal(neo_tute.is_volume_slider_present(), True, "Volume slider is displayed when Tutor "
                                                           "keeps cursor on the volume icon of Video")


@then("Verify that User should be able to increase or decrease volume accordingly")
def step_impl(neo_tute):
    check.equal(neo_tute.select_volume('decrement', 2), True, 'User able to increase volume')
    check.equal(neo_tute.select_volume('increment', 2), True, 'User able to decrease volume')


@then('Verify that Audio Mute icon should be displayed when User mutes the audio')
def step_impl(neo_tute, neo_in_class):
    neo_in_class.turn_on_off_student_mic('OFF')
    student_details = get_data(Login_Credentials, 'neo_login_detail1', 'student1')
    expected_student_name = student_details['name']
    students_audio_status = neo_tute.get_student_audio_status()
    check.equal(students_audio_status[expected_student_name], False,
                "Audio Mute icon should be displayed when User mutes the audio")


@then('Verify that Video Mute icon should display when User mutes the video')
def step_impl(neo_tute, neo_in_class):
    neo_in_class.turn_on_off_student_video('OFF')
    student_details = get_data(Login_Credentials, 'neo_login_detail1', 'student1')
    expected_student_name = student_details['name']
    students_video_status = neo_tute.get_student_video_status()
    check.equal(students_video_status[expected_student_name], False,
                "Video Mute icon should display when User mutes the video")


@then("Verify that the first letter of the Student will be displayed as profile picture incase the Student haven't uploaded any photo")
def step_impl(neo_in_class,neo_tute):
    neo_in_class.upload_profile_photo_api("../../../files/SamplePNG.png")
    neo_tute.click_on_tab_item(tab_name="Class Forum")
    neo_tute.click_on_tab_item(tab_name="Student Details")
    student_details = get_data(Login_Credentials, 'neo_login_detail1', 'student1')
    expected_student_name = student_details['name']
    neo_tute.reject_profile_pic(expected_student_name)
    neo_tute.click_on_tab_item(tab_name="Session Slides")
    all_profile_card_details = neo_tute.get_img_src_for_all_students()
    for profile_card in all_profile_card_details.values():
        actual_student_name = profile_card[0]
        if expected_student_name == actual_student_name:
            actual_profile_src = profile_card[1]
            expected_profile_src = "https://static.tllms.com/assets/k12/premium_online/byjus_classes/common/initial_avatars/%s.png" % \
                                   expected_student_name[0]
            flag = (expected_profile_src == actual_profile_src)
            check.equal(flag, True, "Student first letter is present in the case when user not uploaded any image")


@then("Verify that question mark icon should appear in the profile thumbnail when Tute asks question")
def step_impl(neo_tute):
    student_details = get_data(Login_Credentials, 'neo_login_detail1', 'student1')
    expected_student_name = student_details['name']
    if not neo_tute.is_ask_question_icon_displayed(expected_student_name):
        neo_tute.click_on_menu_option(expected_student_name=expected_student_name, menu_item="Ask Question")
    check.equal(neo_tute.is_ask_question_icon_displayed(expected_student_name), True,
                "Question mark icon appeared in the profile thumbnail when Tutor asks question")


@then('Verify that raise hand icon should appear in the profile thumbnail when Student clicks Raise Hand')
def step_impl(neo_tute, neo_in_class):
    student_details = get_data(Login_Credentials, 'neo_login_detail1', 'student1')
    expected_student_name = student_details['name']
    neo_in_class.verify_hand_raised()
    check.equal(neo_tute.is_hand_raise_icon_displayed(expected_student_name), True,
                "Raise hand icon appeared in the profile thumbnail when Student clicks Raise Hand")


@then("Verify that Video and Audio Mute icon should display when tutor mutes the video and audio")
def step_impl(neo_tute):
    neo_tute.turn_tutor_video_on_off(status='off')
    tute_video_details_tutor = neo_tute.get_tutor_video_status()
    check.equal(tute_video_details_tutor.result, False, tute_video_details_tutor.reason)
    neo_tute.turn_tutor_audio_on_off(status='off')
    tute_audio_details_tutor = neo_tute.get_tutor_audio_status()
    check.equal(tute_audio_details_tutor.result, False, tute_audio_details_tutor.reason)


@then('Verify that if the Student have uploaded a profile photo, then same should be displayed as Profile Thumbnail')
def step_impl(neo_in_class, neo_tute):
    neo_in_class.upload_profile_photo_api("../../../files/SamplePNG.png")
    neo_tute.click_on_tab_item(tab_name="Student Details")
    student1_details = get_data(Login_Credentials, 'neo_login_detail1', 'student1')
    neo_tute.approve_profile_pic(student1_details['name'])
    neo_tute.click_on_tab_item(tab_name="Session Slides")
    all_profile_card_details = neo_tute.get_img_src_for_all_students()
    for profile_card in all_profile_card_details.values():
        actual_student_name = profile_card[0]
        student_details = get_data(Login_Credentials, 'neo_login_detail1', 'student1')
        expected_student_name = student_details['name']
        if expected_student_name == actual_student_name:
            actual_profile_src = profile_card[1]
            flag = ('https://tutoring-doubts-bucket.s3.ap-southeast-1.amazonaws.com/user_profile_images/students/' in actual_profile_src)
            check.equal(flag, True, "Profile photo is uploaded and present in thumbnail")
            break
