import time

from pytest_bdd import scenarios, given, then, when
from pytest import fixture
from constants.constants import Login_Credentials
from constants.load_json import get_data
from constants.platform import Platform
from pages.factory.login import LoginFactory
from pages.factory.neo_inclass_factory import NeoInClassFactory
import pytest_check as check
from utilities.neo_tute_mentoring import NeoTute

scenarios('../features/Whiteboard.feature')


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



@given("launch the application online as neo user and navigate to home screen")
def navigate_to_one_to_many_and_mega_user(login_in):
    student1_details = get_data(Login_Credentials, 'neo_login_detail1', 'student1')
    login_in.login_and_navigate_to_home_screen(student1_details['code'], student1_details['mobile_no'], otp=None)


@given("tutor start the session")
def step_impl(neo_tute):
    neo_tute.start_neo_session(login_data="neo_login_detail1", user='student1')


@when('click on "JOIN" button in home page')
def step_impl(neo_in_class):
    neo_in_class.home_click_on_join()


@when("student join neo session")
def step_impl(neo_in_class):
    neo_in_class.join_neo_session_student('mic-on', 'cam-on')


@then("Verify the elements in default whiteboard screen when user lands on.")
def step_impl(neo_tute,neo_in_class):
    n = 1
    neo_tute.present_any_slide(n)
    neo_tute.click_on_add_slide()
    neo_tute.present_any_slide(n + 1)
    details = neo_in_class.presentation_alignment()
    check.equal(details.result, True, details.reason)


@then('Verify the full screen mode option in whiteboard.')
def step_impl(neo_in_class):
    neo_in_class.hover_over_full_screen_toggle()
    check.equal(neo_in_class.get_full_screen_toggle_visibility() =='visible',True,"When control is on video window,full screen icon is displayed")


@then('Verify the whiteboard screen when user selects full screen mode.')
def step_impl(neo_in_class):
    neo_in_class.do_full_screen_presentation()
    details = neo_in_class.verify_presentation_dimension_ratio()
    check.equal(details.result, True, details.reason)
    neo_in_class.minimize_full_screen_presentation()


@then('Verify the whiteboard when focused mode is turned on.')
def step_impl(neo_tute,neo_in_class):
    neo_tute.select_focus_mode('on')
    check.equal(neo_in_class.is_full_screen_presentation_present(), True, "Focus mode enabled and screen transitioned to full screen")
    neo_tute.select_focus_mode('off')


@then("Verify the tutor's video section when video of the tutor is turned off in the right side.")
def step_impl(neo_tute,neo_in_class):
    neo_tute.turn_tutor_video_on_off(status='off')
    neo_in_class.verify_tutor_ui_elements()
    tutor_video_details = neo_in_class.is_tutor_video_on()
    check.equal(tutor_video_details.result, False,tutor_video_details.reason)


@then("Verify the tutor's audio/video quality when network is flaky.")
def step_impl(neo_tute,neo_in_class):
    neo_tute.turn_tutor_video_on_off(status='on')
    neo_in_class.set_wifi_connection_off()
    neo_in_class.verify_tutor_ui_elements()
    tutor_video_details =neo_in_class.is_tutor_video_on()
    check.equal(tutor_video_details.result, True, tutor_video_details.reason)
    tutor_audio_details = neo_in_class.is_tutor_mute()
    check.equal(tutor_audio_details.result == False, True,tutor_audio_details.reason)


@then('Verify the "Lower Hand" button doesnt change if reconnection happens due to flaky network.')
def step_impl(neo_in_class):
    check.equal(neo_in_class.verify_hand_raised(),True,"User able to hand raise")
    neo_in_class.set_wifi_connection_on()


@then('Verify the like emoji "thumbs up" below the whiteboard.')
def step_impl(neo_in_class):
    check.equal(neo_in_class.is_thumb_icon_present(), True, "Thumb icon present below the whiteboard.")


@then('Verify that student can select like emoji.')
def step_impl(neo_in_class):
    neo_in_class.click_on_thumb_icon()
    check.equal(neo_in_class.select_any_celebration_symbol('heart'), True, "User able to send celebration")


@then("Verify that like emoji should be highlighted when student clicks on thumbs up icon.")
def step_impl(neo_in_class):
    flag = neo_in_class.celebration_highlighted('heart')
    check.equal(flag, True, "emoji should be highlighted when student clicks on thumbs up icon")


@then("Verify that student cant control other student's camera & mic.")
def step_impl(neo_in_class):
    check.equal(neo_in_class.global_video_icon_present() == neo_in_class.global_audio_icon_present() == False,True, "Student cant control other student's camera & mic")


@then("Verify that if student joins the session during Whiteboard presentation, already entered texts, shapes, markers are also visible to the students")
def verify_whiteboard_contents(neo_tute,neo_in_class):
    neo_tute.toggle_draw_option('on')
    neo_tute.click_on_clear_icon()
    neo_tute.draw_shapes_on_neo_tutor_whiteboard()
    neo_tute.perform_text_action_on_neo_tutor_whiteboard('Welcome')
    check.equal(neo_in_class.get_text_from_image_and_verify('Welcome'), True,"Whiteboard presentation text visible to the students")
    check.equal(neo_in_class.verify_shapes_in_student_whiteboard(['circle', 'rectangle', 'triangle']), True,"Whiteboard presentation shapes are also visible to the students")


@then('Verify that alignment of texts, handwritten shapes, markers on Whiteboard presentation in different browser window sizes')
def step_impl(neo_in_class):
    neo_in_class.change_browser_size(1024, 768)
    check.equal(neo_in_class.get_text_from_image_and_verify('Welcome'), True,"Whiteboard presentation text visible to the students")
    check.equal(neo_in_class.verify_shapes_in_student_whiteboard(['circle', 'rectangle', 'triangle']), True,"Whiteboard presentation shapes are also visible to the students")
    neo_in_class.change_browser_size(1080,800)
    check.equal(neo_in_class.get_text_from_image_and_verify('Welcome'), True,"Whiteboard presentation text visible to the students")
    check.equal(neo_in_class.verify_shapes_in_student_whiteboard(['circle', 'rectangle', 'triangle']), True,"Whiteboard presentation shapes are also visible to the students")
    neo_in_class.change_browser_size('default','default')


@then('Verify that contents presented on Whiteboard is available if user refreshes/rejoins the session')
def step_impl(neo_in_class):
    neo_in_class.refresh_and_join_the_session('mic-on', 'cam-on')
    check.equal(neo_in_class.get_text_from_image_and_verify('Welcome'), True, "Whiteboard presentation text visible to the students")
    check.equal(neo_in_class.verify_shapes_in_student_whiteboard(['circle', 'rectangle', 'triangle']), True,"Whiteboard presentation shapes are also visible to the students")


@then('Verify that contents presented on Whiteboard is available if reconnection happens')
def step_impl(neo_in_class):
    neo_in_class.set_wifi_connection_off()
    neo_in_class.set_wifi_connection_on()
    check.equal(neo_in_class.get_text_from_image_and_verify('Welcome'), True, "Whiteboard presentation text visible to the students")
    check.equal(neo_in_class.verify_shapes_in_student_whiteboard(['circle', 'rectangle', 'triangle']), True,"Whiteboard presentation shapes are also visible to the students")


@then("Verify that if other students in the class raises hand, a hand icon should be displayed beside the mic icon on the student's thumbnail.")
def step_impl(neo_in_class,student2,student2_neo):
    student2_details = get_data(Login_Credentials, 'neo_login_detail1', 'student2')
    student2.login_and_navigate_to_home_screen(student2_details['code'], student2_details['mobile_no'], otp=None)
    student2_neo.home_click_on_join()
    student2_neo.join_neo_session()
    student2_neo.raise_hand()
    details = neo_in_class.verify_hand_is_raised_for_student(student_name=student2_details['name'])
    check.equal(details.result,True, details.reason)



@then(
    "Verify that if other students in the class lower hand, the hand icon should be removed from the student's thumbnail.")
def step_impl(neo_in_class, student2_neo):
    student2_details = get_data(Login_Credentials, 'neo_login_detail1', 'student2')
    student2_neo.unraise_hand()
    time.sleep(1)
    details = neo_in_class.verify_hand_is_raised_for_student(student_name=student2_details['name'])
    check.equal(details.result, False, details.reason)


@then('Verify that user should be able to use "Raise Hand" functionality anytime during the session')
def step_impl(neo_in_class):
    neo_in_class.raise_hand()
    details = neo_in_class.verify_hand_is_raised()
    check.equal(details.result, True, details.reason)


@then('Verify that user should be able to use "Lower Hand" functionality anytime during the session.')
def step_impl(neo_in_class):
    neo_in_class.unraise_hand()
    details = neo_in_class.verify_hand_is_raised()
    check.equal(details.result, False, details.reason)


@then('Verify that students thumbnail is not displayed when the focused mode is turned on for full screen.')
def step_impl(neo_in_class,neo_tute):
    neo_tute.select_focus_mode(status='on')
    neo_tute.present_any_slide(select_slide_num= 2)
    time.sleep(5)
    numb = neo_in_class.get_no_of_student_cards_displayed()
    flag = (numb == 1)
    check.equal(flag, True, "Student thumbnails are displayed in foucs mode")
    neo_tute.select_focus_mode(status='off')
    neo_in_class.do_full_screen_presentation()
    time.sleep(3)
    numb = neo_in_class.get_no_of_student_cards_displayed()
    flag = (numb == 1)
    check.equal(flag, True, "Student thumbnails are displayed in full screen")
    neo_tute.present_any_slide(select_slide_num=2)
    neo_in_class.minimize_full_screen_presentation()



@then("Verify that mic/camera icon is displayed when the focused mode is turned on for full screen.")
def step_impl(neo_in_class,neo_tute):
    neo_tute.select_focus_mode(status='on')
    neo_tute.present_any_slide(select_slide_num=2)
    time.sleep(5)
    details = neo_in_class.mic_cam_status_in_focus_mode()
    check.equal(details.result, True, details.reason+"in focus mode")
    neo_tute.select_focus_mode(status='off')
    neo_in_class.do_full_screen_presentation()
    details = neo_in_class.mic_cam_status_in_focus_mode()
    check.equal(details.result, True, details.reason+"in full screen")
    neo_in_class.minimize_full_screen_presentation()


@then("Verify that raise hand option is available when whiteboard is in focused mode for full screen.")
def step_impl(neo_in_class,neo_tute):
    neo_tute.select_focus_mode(status='on')
    details = neo_in_class.is_hand_raise_icon_present()
    details1 = neo_in_class.verify_hand_raised()
    flag = any((details.result, details1.result))
    check.equal(flag, True, "Raise hand option is not displayed in fous mode")
    neo_tute.select_focus_mode(status='off')
    neo_in_class.do_full_screen_presentation()
    details = neo_in_class.is_hand_raise_icon_present()
    details1 = neo_in_class.verify_hand_raised()
    flag = any((details.result, details1.result))
    check.equal(flag, True, "Raise hand option is not displayed in full screen")
    neo_in_class.minimize_full_screen_presentation()