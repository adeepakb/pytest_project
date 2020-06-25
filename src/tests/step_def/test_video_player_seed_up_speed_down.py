from pytest_bdd import scenarios, given, when, then, parsers
from POM_Pages.videopage import VideoPage
from Utilities.BasePage import BaseClass 


browser = fixture = 'browser'

base_class = BaseClass()
video = VideoPage(browser)

count = False


"""storing the feature file name"""
featureFileName = "video player seed up -speed down"

# base_class.setupLogs(featureFileName)


"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""
scenarios('../features/' + featureFileName + '.feature')


@given("Launch the app online")
def launch_app_online(browser):
    # global count
    # count = video.login_the_user(browser, count)
    pass


@when(parsers.parse('navigate to "{text}" library chapter list screen'))
def navigateToHomeScreen2(browser, text):
    video.navigate_to_home_screen(browser, text)
    video.navigate_to_library(browser, text)
    
    
@given('Take test from any of the chapter (Precondition)')
def take_test_and_end(browser):
    video.tap_on_test_in_chapter_screen(browser)
    video.tap_on_start_btn_in_test_screen_finish_test(browser)
    
    
@given(parsers.parse('navigate to "{text}" Personalised chapter list screen'))
def navigate_personalised_screen(browser, text):
    video.navigate_to_home_screen(browser, text)
    video.navigate_to_personalised_Screen(browser, text)
    

@given('navigate to home screen')
def navigate_to_home_screen(browser):
    video.navigate_to_home_screen(browser, "Mathematics")
    video.tap_on_skip_btn(browser)


@given(parsers.parse('navigate to "{text}" library chapter list screen'))
def navigateToHomeScreen(browser, text):
    video.navigate_to_home_screen(browser, text)
    video.navigate_to_library(browser, text)


@given('Autoplay option should be enbled for Videos')
def turn_on_auto_play(browser):
    video.turn_on_auto_play(browser)


@given('Tap on any video from chapter list screen')
def tapOnAnyVideo(browser):
    video.tap_on_any_video_in_sub_screen(browser)
    
    
@given('Tap on any journey card')
def tap_on_any_journey_card(browser):
    video.tap_on_any_journey_card_in_sub_screen(browser)
    
    
@when('Tap on the video card')
def tap_on_start_video(browser):
    video.tap_on_start_video(browser)
    
    
@when('Subtopic video slider will open')
def verify_subtopic_video_slider(browser):
    video.verify_subtopic_video_slider(browser)
    
    
@when('Tap on any video')   
def tap_on_any_video(browser):
    video.tap_on_any_video(browser)


@when('Tap on any video from chapter list screen')
def tapOnAnyVideo2(browser):
    video.tap_on_any_video_in_sub_screen(browser)
    

@when('Verify video should be played')
@then('Verify video should be played')
def video_should_played(browser):
    video.video_should_played(browser)
    
    
@when('tap on Playback speed icon')
def tap_on_playback_speed_icon(browser):
    video.tap_on_playback_speed_icon(browser)
    
    
@then('Verify playback speed bottom sheet dialog is displayed')
def verify_playback_speed_buttom_sheet(browser):
    video.verify_playback_speed_buttom_sheet(browser)
    
    
@then(parsers.parse('verify Label "{text}" is present on dialog'))
def verify_text_present(browser, text):
    video.verify_text_present(browser, text)
    
    
@given('on home screen tap on analysis icon')
def tap_on_analysis_icon(browser):
    video.tap_on_analysis_icon(browser)
    
    
@when('Tap on key focus area video')
def tap_on_keyFocus_area(browser):
    video.tap_on_keyFocus_area(browser)
    
    
@then(parsers.parse('Verify Speed options "{text1}" , "{text2}" , "{text3}" , "{text4}" , "{text5}" are present on dialog'))
def verify_playback_speed_dialog(browser, text1, text2, text3, text4, text5):
    video.verify_radio_btn_text_present(browser, text1)
    video.verify_radio_btn_text_present(browser, text2)
    video.verify_radio_btn_text_present(browser, text3)
    video.verify_radio_btn_text_present(browser, text4)
    video.verify_radio_btn_text_present(browser, text5)
    
   
@then(parsers.parse('Verify when Next video is played default option "{text}" should be selected'))
@then(parsers.parse('Verify by default "{text}" option should be selected in  playback speed bottom sheet dialog'))
def verify_selected_playback_speed(browser, text):
    video.verify_selected_playback_speed(browser, text)
    

@when(parsers.parse('tap on "{text}" option'))
def tap_on_playbackspeed(browser, text):
    video.tap_on_text_lnk(browser, text)
    
    
@then('Verify the video play is speed Down compare to normal')
def verify_speed_down_compare_to_normal(browser):
    video.verify_speed_down_compare_to_normal(browser)
    
    
@then('Verify the video play is speed Down compare to 0.75x')
def verify_speed_down_compare_to_075x(browser):
    video.verify_speed_down_compare_to_075x(browser)
    
    
@then('Verify the video play is speed up compare to Normal')
def verify_speed_up_compare_to_normal(browser):
    video.verify_speed_up_compare_to_normal(browser)
    
    
@then('Verify the video play is speed  up  compare to 1.25X')
def verify_speed_up_compare_to_125x(browser):
    video.verify_speed_up_compare_to_125x(browser)
    
    
@when('complete the video')
def complete_video(browser):
    video.complete_video(browser)
    
    
@when('allow to auto load the next video')
def wait_till_autoload_completes(browser):
    video.wait_till_autoload_completes(browser)
    

@then('Autoplay option should be enbled for Videos')    
@when('Autoplay option should be enbled for Videos')
def turn_on_auto_play2(browser):
    video.turn_on_auto_play(browser)
    
    
@when('Tap on the second video in subtopic list screen')
def tap_on_second_video_lnk(browser):
    video.tap_on_second_video_lnk(browser)
    

@given('tap on the practice card')
def tap_on_practice_card(browser):
    video.tap_on_practice_card(browser)
    
    
@when('Progress the practice until tackle video is shown')
def progress_till_video_play(browser):
    video.progress_till_video_play(browser)
    
    

    

    





