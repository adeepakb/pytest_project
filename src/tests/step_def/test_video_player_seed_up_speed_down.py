from pytest_bdd import scenarios, given, when, then, parsers
from pages.android.videopage import VideoPage
from utilities.BasePage import BaseClass


driver = fixture = 'driver'

base_class = BaseClass()
video = VideoPage(driver)

count = False


"""storing the feature file name"""
featureFileName = "video player seed up -speed down"

# base_class.setupLogs(featureFileName)


"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""
scenarios('../features/' + featureFileName + '.feature')


@given("Launch the app online")
def launch_app_online(driver):
    # global count
    # count = video.login_the_user(driver, count)
    pass


@when(parsers.parse('navigate to "{text}" library chapter list screen'))
def navigateToHomeScreen2(driver, text):
    video.navigate_to_home_screen(driver, text)
    video.navigate_to_library(driver, text)
    
    
@given('Take test from any of the chapter (Precondition)')
def take_test_and_end(driver):
    video.tap_on_test_in_chapter_screen(driver)
    video.tap_on_start_btn_in_test_screen_finish_test(driver)
    
    
@given(parsers.parse('navigate to "{text}" Personalised chapter list screen'))
def navigate_personalised_screen(driver, text):
    video.navigate_to_home_screen(driver, text)
    video.navigate_to_personalised_Screen(driver, text)
    

@given('navigate to home screen')
def navigate_to_home_screen(driver):
    video.navigate_to_home_screen(driver, "Mathematics")
    video.tap_on_skip_btn(driver)


@given(parsers.parse('navigate to "{text}" library chapter list screen'))
def navigateToHomeScreen(driver, text):
    video.navigate_to_home_screen(driver, text)
    video.navigate_to_library(driver, text)


@given('Autoplay option should be enbled for Videos')
def turn_on_auto_play(driver):
    video.turn_on_auto_play(driver)


@given('Tap on any video from chapter list screen')
def tapOnAnyVideo(driver):
    video.tap_on_any_video_in_sub_screen(driver)
    
    
@given('Tap on any journey card')
def tap_on_any_journey_card(driver):
    video.tap_on_any_journey_card_in_sub_screen(driver)
    
    
@when('Tap on the video card')
def tap_on_start_video(driver):
    video.tap_on_start_video(driver)
    
    
@when('Subtopic video slider will open')
def verify_subtopic_video_slider(driver):
    video.verify_subtopic_video_slider(driver)
    
    
@when('Tap on any video')   
def tap_on_any_video(driver):
    video.tap_on_any_video(driver)


@when('Tap on any video from chapter list screen')
def tapOnAnyVideo2(driver):
    video.tap_on_any_video_in_sub_screen(driver)
    

@when('Verify video should be played')
@then('Verify video should be played')
def video_should_played(driver):
    video.video_should_played(driver)
    
    
@when('tap on Playback speed icon')
def tap_on_playback_speed_icon(driver):
    video.tap_on_playback_speed_icon(driver)
    
    
@then('Verify playback speed bottom sheet dialog is displayed')
def verify_playback_speed_buttom_sheet(driver):
    video.verify_playback_speed_buttom_sheet(driver)
    
    
@then(parsers.parse('verify Label "{text}" is present on dialog'))
def verify_text_present(driver, text):
    video.verify_text_present(driver, text)
    
    
@given('on home screen tap on analysis icon')
def tap_on_analysis_icon(driver):
    video.tap_on_analysis_icon(driver)
    
    
@when('Tap on key focus area video')
def tap_on_keyFocus_area(driver):
    video.tap_on_keyFocus_area(driver)
    
    
@then(parsers.parse('Verify Speed options "{text1}" , "{text2}" , "{text3}" , "{text4}" , "{text5}" are present on dialog'))
def verify_playback_speed_dialog(driver, text1, text2, text3, text4, text5):
    video.verify_radio_btn_text_present(driver, text1)
    video.verify_radio_btn_text_present(driver, text2)
    video.verify_radio_btn_text_present(driver, text3)
    video.verify_radio_btn_text_present(driver, text4)
    video.verify_radio_btn_text_present(driver, text5)
    
   
@then(parsers.parse('Verify when Next video is played default option "{text}" should be selected'))
@then(parsers.parse('Verify by default "{text}" option should be selected in  playback speed bottom sheet dialog'))
def verify_selected_playback_speed(driver, text):
    video.verify_selected_playback_speed(driver, text)
    

@when(parsers.parse('tap on "{text}" option'))
def tap_on_playbackspeed(driver, text):
    video.tap_on_text_lnk(driver, text)
    
    
@then('Verify the video play is speed Down compare to normal')
def verify_speed_down_compare_to_normal(driver):
    video.verify_speed_down_compare_to_normal(driver)
    
    
@then('Verify the video play is speed Down compare to 0.75x')
def verify_speed_down_compare_to_075x(driver):
    video.verify_speed_down_compare_to_075x(driver)
    
    
@then('Verify the video play is speed up compare to Normal')
def verify_speed_up_compare_to_normal(driver):
    video.verify_speed_up_compare_to_normal(driver)
    
    
@then('Verify the video play is speed  up  compare to 1.25X')
def verify_speed_up_compare_to_125x(driver):
    video.verify_speed_up_compare_to_125x(driver)
    
    
@when('complete the video')
def complete_video(driver):
    video.complete_video(driver)
    
    
@when('allow to auto load the next video')
def wait_till_autoload_completes(driver):
    video.wait_till_autoload_completes(driver)
    

@then('Autoplay option should be enbled for Videos')    
@when('Autoplay option should be enbled for Videos')
def turn_on_auto_play2(driver):
    video.turn_on_auto_play(driver)
    
    
@when('Tap on the second video in subtopic list screen')
def tap_on_second_video_lnk(driver):
    video.tap_on_second_video_lnk(driver)
    

@given('tap on the practice card')
def tap_on_practice_card(driver):
    video.tap_on_practice_card(driver)
    
    
@when('Progress the practice until tackle video is shown')
def progress_till_video_play(driver):
    video.progress_till_video_play(driver)
    
    

    

    





