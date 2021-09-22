from pytest_bdd import scenarios, given, then, when, parsers
from pytest import fixture
from constants.platform import Platform
from pages.factory.login import LoginFactory
from pages.factory.neo_inclass_factory import NeoInClassFactory
import pytest_check as check
from utilities.neo_tute_mentoring import NeoTute

scenarios('../features/Video Session.feature')


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
    login_in.login_and_navigate_to_home_screen('+91-', '2013274689', otp=None)


@given("tutor start the session")
def step_impl(neo_tute):
    neo_tute.start_neo_session()


@when('click on "JOIN" button in home page')
def step_impl(neo_in_class):
    neo_in_class.home_click_on_join()


@then("student join neo session")
def step_impl(neo_in_class):
    neo_in_class.join_neo_session()


@then("tutor play video in the session and turn off focus mode")
def step_impl(neo_tute,neo_in_class):
    neo_tute.present_any_slide(6)
    neo_tute.select_focus_mode('off')
    neo_in_class.turn_on_off_student_mic('ON')


@then("Verify that default layout of the screen when session video is playing (not Focused)")
def step_impl(neo_in_class):
    details = neo_in_class.video_alignment()
    check.equal(details.result, True, details.reason)


@then("Verify that aspect ratio of the session video window is 16:9 through out the session")
@then('Verify that video plays without any issue during full screen or windowed mode, video should not be stretched, shrinked or cropped')
@then('Verify that aspect ratio of video is maintained in full screen mode')
@then('Verify that aspect ratio of video is maintained in focused mode')
def step_impl(neo_in_class):
    details = neo_in_class.verify_presentation_dimension_ratio()
    check.equal(details.result, True, details.reason)


@then("Verify that smaller thumbnails of the students are displayed below the video window")
def step_impl(neo_in_class):
    student_names = neo_in_class.get_all_student_names()
    check.equal(all(student_name is not None for student_name in student_names), True,"Smaller thumbnails of the students are displayed below the video window")


@then(parsers.parse("Verify that during video session the student's name is not displayed on the thumbnails except for the current student where '{text}' is displayed at the bottom left corner of the thumbnail"))
def step_impl(neo_in_class,text):
    student_names = neo_in_class.get_all_student_names()
    check.equal(student_names[0] == text, True, "current student where %s is displayed on the thumbnail"%text)


@then("Verify that mic's status is displayed for other students on their thumbnail")
def step_impl(neo_in_class):
    students_audio_status = neo_in_class.get_student_audio_status()
    check.equal(all(audio_status is not None for audio_status in students_audio_status), True, "Audio/Mic status is displayed for other students on their thumbnail")


@then('Verify that student video/audio is playing if they have turned their camera/mic ON during the session')
def step_impl(neo_in_class):
    neo_in_class.turn_on_off_student_mic('ON')
    neo_in_class.turn_on_off_student_video('ON')
    students_video_status = neo_in_class.get_student_video_status()
    students_audio_status = neo_in_class.get_student_audio_status()
    check.equal(students_video_status['You'] is True and students_audio_status['You'] is True, True ,"Current Student's video/audio is playing if they have turned their camera/mic ON during the session")


@then("Verify that current student's camera and mic controls are displayed "
      "with correct status at the bottom of the session screen")
def step_impl(neo_in_class):
    neo_in_class.turn_on_off_student_mic('OFF')
    neo_in_class.turn_on_off_student_video('OFF')
    students_video_status = neo_in_class.get_student_video_status()
    students_audio_status = neo_in_class.get_student_audio_status()
    check.equal(students_video_status['You'] is False and students_audio_status['You'] is False, True , "Current student's camera and mic controls are displayed with correct status at the bottom of the session screen")


@then('Verify that if students have turned off their camera, only the '
      'initials of their name is displayed on the thumbnail')
def step_impl(neo_in_class):
    students_video_status = neo_in_class.get_student_video_status()
    check.equal(students_video_status['You'] is False, True , "Student turned off their camera, only the initials of their name is displayed on the thumbnail")


@then('Verify that when control is not on the video window, '
      'full screen icon is not displayed at the bottom right corner of video window')
def step_impl(neo_in_class):
    check.equal(neo_in_class.get_full_screen_toggle_visibility() == 'hidden',True,"When control is not on video window,full screen icon is not displayed")


@then('Verify that hovering/clicking over the video window(not during focused mode) should show full screen icon at '
      'the bottom right corner of video window')
def step_impl(neo_in_class):
    neo_in_class.hover_over_full_screen_toggle()
    check.equal(neo_in_class.get_full_screen_toggle_visibility() =='visible',True,"When control is on video window,full screen icon is displayed")


@then('Verify that clicking on full screen icon should enlarge the video window to full screen')
def step_impl(neo_in_class):
    neo_in_class.do_full_screen_presentation()


@then('Verify that when full screen mode is active the full screen icon should '
      'transition to shrink/windowed mode button')
def step_impl(neo_in_class):
    check.equal(neo_in_class.is_minimize_full_screen_present(),True,"full screen icon transitioned to shrink/windowed mode")

@then('Verify that clicking on shrink/windowed mode button should shrink the video to default windowed mode')
def step_impl(neo_in_class):
    neo_in_class.minimize_full_screen_presentation()


@then('Verify that on hovering/clicking over the video screen while playback is happening in full screen mode, should show all controls; camera, mic, Raise/Lower hand and thumbs up icons')
def step_impl(neo_in_class):
    details = neo_in_class.hover_over_and_verify_bottom_container_full_screen()
    check.equal(details.result, True, details.reason)


@then('Verify that all above buttons function as intended even when video is playing in full screen mode')
def step_impl(neo_in_class):
    check.equal(neo_in_class.verify_hand_raised(),True,"User able to hand raise")
    neo_in_class.click_on_thumb_icon()
    check.equal(neo_in_class.select_any_celebration_symbol('heart'),True,"User able to send celebration")
    neo_in_class.turn_on_off_student_mic('ON')
    neo_in_class.turn_on_off_student_video('ON')
    students_video_status = neo_in_class.get_student_video_status()
    students_audio_status = neo_in_class.get_student_audio_status()
    check.equal(students_video_status['You'] is True and students_audio_status['You'] is True, True,"Current student's camera and mic controls are displayed with correct status at the bottom of the session screen")
    neo_in_class.click_on_kebab_menu()
    check.equal(neo_in_class.is_facing_issues_option_present() and neo_in_class.is_exit_class_btn_present(),
                True, "Kebab menu is clickable and options are present")


@then("Verify that Subject and Topic name is displayed at the top left corner of the video window, "
      "also verify that click in 'i' icon should display the class details")
def step_impl(neo_in_class):
    subject_topic = neo_in_class.get_session_topic_name_inclass()
    check.equal(all(ele is not None for ele in subject_topic), True, "Class details present in class info popup")
    neo_in_class.click_on_class_info_icon()
    class_info_details_dict = neo_in_class.get_classinfo_popup_session_details()
    print(class_info_details_dict)
    check.equal(all(class_info_details_dict.values()), True, "Class details present in class info popup")


@then("Verify that clicking on info icon or anywhere else on the screen, while Class Info pop up is open, should dismiss the pop-up")
def step_impl(neo_in_class):
    neo_in_class.tap_outside_dialog_layout()
    check.equal(neo_in_class.is_class_info_popup_present(),False,"Class Info pop up not dismissed, on clicking outside pop-up")


@then("Verify that there is a kebab menu at the bottom corner of the session window beside the thumbs up icon which is clickable")
def step_impl(neo_in_class):
    neo_in_class.click_on_kebab_menu()


@then('Verify that clicking on kebab menu should show "Facing Issue" and "Exit Class" options')
def step_impl(neo_in_class):
    check.equal(all([neo_in_class.is_exit_class_btn_present(),neo_in_class.is_facing_issues_option_present()]),True,'kebab menu shows "Facing Issue" and "Exit Class" options')


@then('Verify that clicking on "Exit Class" option should open confirmation popup')
def step_impl(neo_in_class):
    neo_in_class.click_on_exit_class_in_student()
    check.equal(neo_in_class.verify_header_in_exit_class_popup(),True,"Exit Class confirmation popup opened up")


@then('Verify the content of "Exit Class" confirmation popup')
def step_impl(neo_in_class):
    check.equal(all([neo_in_class.is_exit_image_in_exit_popup_present(),
                     neo_in_class.is_stayback_in_exit_popup_present(), neo_in_class.is_exitclass_in_exit_popup_present()]),
                True,'content of "Exit Class" confirmation popup present as expected')


@then('Verify that clicking on "Stay Back" option on "Exit Class" confirmation popup, should take the user back to session')
def step_impl(neo_in_class):
    neo_in_class.click_on_stayback_in_exit_popup()
    details = neo_in_class.is_video_being_presented()
    check.equal(details.result, True, details.reason)


@then("Verify that clicking on 'Exit Class' option on 'Exit Class' confirmation popup, should exit the session to Byju's classes page")
def step_impl(neo_in_class):
    neo_in_class.click_on_kebab_menu()
    neo_in_class.click_on_exit_class_in_student()
    neo_in_class.click_on_exit_class_in_exit_popup()
    check.equal(neo_in_class.verify_header_in_rating_popup(),True,"User able to exit Class and it shows rating popup")
    neo_in_class.close_rating_popup()


@then('Verify that user is able to rejoin the session after exiting the session')
def step_impl(neo_in_class):
    neo_in_class.home_click_on_join()
    details = neo_in_class.is_video_being_presented()
    check.equal(details.result,True,details.reason)


@then('Verify that the student is able to "Raise Hand" any time during the video session')
def step_impl(neo_in_class):
    check.equal(neo_in_class.verify_hand_raised(),True,"User able to hand raise")


@then('Verify that the student is able to "Lower Hand" after raising hand, any time during the video session')
def step_impl(neo_in_class):
    check.equal(neo_in_class.verify_lower_hand_tooltip(),True,"User able to lower hand raise")


@then('Verify that when focus mode is enabled by tutor the transition of screen from windowed to full screen mode is smooth')
def step_impl(neo_tute,neo_in_class):
    neo_tute.select_focus_mode('on')
    check.equal(neo_in_class.is_full_screen_presentation_present(), True, "Focus mode enabled and screen transitioned to full screen")


@then('Verify that student should not be able to exit focus mode')
def step_impl(neo_in_class):
    check.equal(neo_in_class.focus_mode_switch_present(),False, "student cannot exit focus mode")


@then("Verify that if reconnection happens due to network issue, "
      "focus mode is retained when student is back in the session")
def step_impl(neo_in_class):
    neo_in_class.set_wifi_connection_off()
    neo_in_class.set_wifi_connection_on()
    check.equal(neo_in_class.is_full_screen_presentation_present() and neo_in_class.is_focus_mode_icon_present(), True,"After reconnecting,focus mode is retained")


@then("Verify that if reconnection happens due to network issue while focus mode is on, "
      "mic state of students are still turned off after the student is back in the session")
def step_impl(neo_in_class):
    neo_in_class.set_wifi_connection_off()
    neo_in_class.set_wifi_connection_on()
    check.equal(neo_in_class.get_inclass_student_audio_status() == "DISABLED", True,'Camera and Mic are turned off for the students while focus mode is on')


@then('Verify that mic control is disabled for the students while focus mode is on')
def step_impl(neo_in_class):
    student_audio_status = neo_in_class.get_inclass_student_audio_status()
    check.equal(student_audio_status == "DISABLED",True,'Mic is turned off for the students while focus mode is on')


@then('Verify that mic is turned off for the students while focus mode is on')
def step_impl(neo_in_class):
    students_audio_status = neo_in_class.get_student_audio_status()
    check.equal(students_audio_status['You'] is False, True,"Student's  mic is turned off for the students while focus mode is on")


@then('Verify that focus mode icon is displayed on the top left corner of the screen when '
      'same is turned on and controls are not active on screen')
def step_impl(neo_in_class):
    neo_in_class.is_focus_mode_icon_present()
    details = neo_in_class.focus_mode_bottom_container_not_active()
    check.equal(details.result,True,details.reason)


@then(parsers.parse('Verify that on click/hover on the screen indication is present on the '
                    'screen while focus mode is on, "{text}" text is added after the session name on top left corner of the screen'))
def step_impl(neo_in_class,text):
    class_info = neo_in_class.focus_mode_class_info()
    check.equal(class_info[1] == text and class_info[0] is not None, True,'Focus Mode and session name is displayed on top left corner')


@then('Verify that all controls are displayed when the student hovers/clicks in the screen while focus mode is on')
def step_impl(neo_in_class):
    details = neo_in_class.hover_over_and_verify_bottom_container_focus_mode()
    check.equal(details.result, True, details.reason)


@then('Verify that Camera, "Raise/Lower Hand", "Thumbs Up" and Kebab Menu are the only controls that is accessible while focus mode is on')
def step_impl(neo_in_class):
    check.equal(neo_in_class.verify_hand_raised(),True,"User able to hand raise")
    neo_in_class.click_on_thumb_icon()
    check.equal(neo_in_class.select_any_celebration_symbol('heart'),True,"User able to send celebration")
    neo_in_class.tap_outside_dialog_layout()
    neo_in_class.turn_on_off_student_video('OFF')
    students_video_status = neo_in_class.get_student_video_status()
    check.equal(students_video_status['You'] is False, True,"User able to update camera status")
    neo_in_class.turn_on_off_student_video('ON')
    neo_in_class.click_on_kebab_menu()
    check.equal(neo_in_class.is_facing_issues_option_present() and neo_in_class.is_exit_class_btn_present(),True, "Kebab menu is clickable and options are present")
    neo_in_class.tap_outside_dialog_layout()


@then('Verify the animation of the reactions when students send reactions while on full screen mode, verify that these should not cover the content video or distort the A/V of the on going session')
@then('Verify the animation of the reactions when students send reactions while focus mode is on, verify that these should not cover the content video or distort the A/V of the on going session')
def step_impl(neo_in_class):
    neo_in_class.click_on_thumb_icon()
    neo_in_class.select_any_celebration_symbol('heart')
    neo_in_class.tap_outside_dialog_layout()
    details = neo_in_class.verify_presentation_dimension_ratio()
    check.equal(details.result, True, details.reason)
    check.equal(neo_in_class.get_video_src() is not None,True,'Video is being played')


@then('Verify the transition of student video is smooth when same dismisses from screen')
def step_impl(neo_in_class):
    value = neo_in_class.focus_mode_transition()
    check.equal(all([value is not None,value is not False]), True ,"Verify student's video thumbnail not visible while focus mode is on")


@then('Verify the state of the session if the user exits and joins the session again while focus mode is on')
def step_impl(neo_in_class):
    neo_in_class.click_on_kebab_menu()
    neo_in_class.click_on_exit_class_in_student()
    neo_in_class.click_on_exit_class_in_exit_popup()
    neo_in_class.close_rating_popup()
    neo_in_class.home_click_on_join()
    neo_in_class.join_neo_session()
    check.equal(neo_in_class.is_full_screen_presentation_present() and neo_in_class.is_focus_mode_icon_present(), True,"User is in Focus mode")


@then('Verify the transition of session is smooth when focus mode is turned off by the tutor')
def step_impl(neo_tute,neo_in_class):
    neo_tute.select_focus_mode('off')
    check.equal(neo_in_class.is_full_screen_presentation_present(), False,"Focus mode is disabled and screen transitioned to default screen")


@then('Verify that mic controls of the students become enabled after focus mode is turned off, but the state of button should be off')
def step_impl(neo_in_class):
    student_audio_status = neo_in_class.get_inclass_student_audio_status()
    check.equal(student_audio_status == "OFF", True, 'Mic is turned off,not disabled for the students while focus mode is off')


@then('Verify that camera status of students is retained as it was before focus mode was on after focus mode is turned off')
def step_impl(neo_in_class):
    students_video_status = neo_in_class.get_inclass_student_video_status()
    check.equal(students_video_status == "ON", True, "Student's mic is turned on while focus mode is off")
