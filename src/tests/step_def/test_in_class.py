from pytest_bdd import scenarios, given, when, then, parsers
from pytest import fixture

from constants.platform import Platform
from pages.factory.login import LoginFactory
from pages.factory.neo_inclass_factory import NeoInClassFactory
from utilities.neo_tute_mentoring import NeoTute

feature_file_name = 'InClass'
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


@given("Student launches in-class and navigate to home page")
def step_impl(login_in):
    login_in.login_and_navigate_to_home_screen('+91-', '2013795859', otp=None)


@given("student navigates to byjus classes screen")
def step_impl(neo_in_class):
    neo_in_class.navigate_to_byjus_classes_screen()


@when("student join neo session")
@then("student join neo session")
def step_impl(neo_in_class):
    neo_in_class.join_neo_session()


@given("tutor start the session")
def step_impl(test_tut):
    test_tut.start_neo_session()


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
    neo_in_class.raise_hand()
    test_tut.click_on_menu_option(expected_student_name='Swastika1', menu_item='Hands Down')
    detail = neo_in_class.verify_hand_is_raised()
    check.equal(detail.result, False, detail.reason)


@then("Verify that if other students in the class raises hand, a hand icon should be displayed beside the mic icon on the student's thumbnail")
def step_impl(neo_in_class):
    detail = neo_in_class.verify_hand_is_raised_for_student(student_name='Test 7')
    check.equal(detail.result, False, detail.reason)