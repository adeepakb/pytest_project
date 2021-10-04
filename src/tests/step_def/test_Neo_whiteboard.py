from pytest_bdd import scenarios, given, then, when, parsers
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


@given("launch the application online as neo user and navigate to home screen")
def navigate_to_one_to_many_and_mega_user(login_in):
    student1_details = get_data(Login_Credentials, 'neo_login_detail1', 'student1')
    login_in.login_and_navigate_to_home_screen(student1_details['code'], student1_details['mobile_no'], otp=None)


@given("tutor start the session")
def step_impl(neo_tute):
    neo_tute.start_neo_session()


@when('click on "JOIN" button in home page')
def step_impl(neo_in_class):
    neo_in_class.home_click_on_join()


@when("student join neo session")
def step_impl(neo_in_class):
    neo_in_class.join_neo_session()


@then("Verify the elements in default whiteboard screen when user lands on.")
def step_impl(neo_in_class):
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
    details = neo_in_class.is_tutor_video_on()
    check.equal(details.result, False,details.reason)


@then("Verify the tutor's audio/video quality when network is flaky.")
def step_impl(neo_tute,neo_in_class):
    neo_tute.turn_tutor_video_on_off(status='on')
    neo_in_class.set_wifi_connection_off()
    tutor_video_details =neo_in_class.is_tutor_video_on()
    check.equal(tutor_video_details.result, True, tutor_video_details.reason)
    tutor_audio_details = neo_in_class.is_tutor_mute()
    check.equal(tutor_audio_details.result == False, True,tutor_audio_details.reason)


# need to update
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
    check.equal(neo_in_class.global_video_icon_present() == neo_in_class.global_audio_icon_present() == False,
                True, "Student cant control other student's camera & mic")


@then("Verify that if student joins the session during Whiteboard presentation, already entered texts, shapes, markers are also visible to the students")
def verify_whiteboard_contents(neo_tute,neo_in_class):
    neo_tute.toggle_draw_option('on')
    neo_tute.click_on_clear_icon()
    neo_tute.draw_shapes_on_neo_tutor_whiteboard()
    neo_tute.perform_text_action_on_neo_tutor_whiteboard('Welcome')
    check.equal(neo_in_class.verify_shapes_in_student_whiteboard(['circle', 'square', 'rectangle', 'triangle']), True,
                "Whiteboard presentation shapes are also visible to the students")
    check.equal(neo_in_class.get_text_from_image_and_verify('Welcome'), True,
                "Whiteboard presentation text visible to the students")


@then('Verify that alignment of texts, handwritten shapes, markers on Whiteboard presentation in different browser window sizes')
def step_impl(neo_in_class):
    verify_whiteboard_contents()
    neo_in_class.change_browser_size(1600, 900)
    verify_whiteboard_contents()
    neo_in_class.change_browser_size(800, 450)
    verify_whiteboard_contents()
    neo_in_class.change_browser_size()


@then('Verify that contents presented on Whiteboard is available if user refreshes/rejoins the session')
def step_impl(neo_in_class):
    neo_in_class.refresh_and_join_the_session('mic-on', 'cam-on')
    check.equal(neo_in_class.get_text_from_image_and_verify('Welcome'), True, "Whiteboard presentation text visible to the students")
    check.equal(neo_in_class.verify_shapes_in_student_whiteboard(['circle', 'square', 'rectangle', 'triangle']), True,
                "Whiteboard presentation shapes are also visible to the students")


@then('Verify that contents presented on Whiteboard is available if reconnection happens')
def step_impl(neo_in_class):
    neo_in_class.set_wifi_connection_off()
    neo_in_class.set_wifi_connection_on()
    check.equal(neo_in_class.get_text_from_image_and_verify('Welcome'), True, "Whiteboard presentation text visible to the students")
    check.equal(neo_in_class.verify_shapes_in_student_whiteboard(['circle', 'square', 'rectangle', 'triangle']), True,
                "Whiteboard presentation shapes are also visible to the students")


