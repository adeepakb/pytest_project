from pytest_bdd import scenarios, given, when, then, parsers
import os

from POM_Pages.videopage import VideoPage
from Utilities.BasePage import BaseClass

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))


browser = fixture = 'browser'
baseClass = BaseClass()
video = VideoPage(browser)


"""storing the feature file name"""
featureFileName = "video Autoplay Enabled"


"""configuring the Logging Files"""
baseClass.setupLogs(featureFileName)


"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""
scenarios('../features/'+featureFileName+'.feature')


@given("Launch the app online")
def launchAppOnline(browser):
    pass 


@given(parsers.parse('Navigate to "{text}" library chapter list screen'))
def navigateToHomeScreen(browser, text): 
    video.navigate_to_home_screen(browser, text)
    video.navigate_to_library(browser,text)
    
    
@given('Tap on any video from chapter list screen')
def tapOnAnyVideo(browser): 
    video.tap_on_any_video_in_sub_screen(browser)
    
    
@when('Tap on any video')
def tap_on_any_video(browser): 
    video.tap_on_any_video(browser)
   
   
@when('Tap on setting icon')
def tap_on_video_player_setting_icon(browser):
    video.tap_on_video_player_setting_icon(browser)
    

@when('Subtopic video slider will open')
def verify_subtopic_video_slider(browser):
    video.verify_subtopic_video_slider(browser)
    
    
@when('Autoplay option should be disabled for Videos')
def turn_off_auto_play(browser):
    video.turn_off_auto_play(browser)
    
    
@then('Verify that settings bottom sheet dialog is shown')
def verify_setting_bottom_sheet(browser):
    video.verify_setting_bottom_sheet(browser)
    

@when('Tap on the first video in subtopic list screen')
@when('Tap on the first video in subtopic list screen  and complete a video')
def tap_on_first_video_and_complete(browser):
#     video.tap_on_first_video_lnk_and_complete(browser)
    video.tap_on_first_video_lnk(browser)
    
    
@when('While auto loading is shown tap on cancel button')
def tap_on_cancel_button(browser):
    video.tap_on_cancel_button(browser)
    

@given('Autoplay option should be enbled for Videos')
def turn_on_auto_play(browser):
    video.turn_on_auto_play(browser)  
    
@then('Autoplay option should be enbled for Videos')    
@when('Autoplay option should be enbled for Videos')
def turn_on_auto_play2(browser):
    video.turn_on_auto_play(browser)
    
    
@then('verify toggle button should be in purple colour')
def verify_purple_color(browser):
    video.verify_purple_color(browser)


@when('Tap on the last  video in subtopic list screen')
def tap_on_last_video_in_list(browser):
    video.tap_on_last_video_in_list(browser)
    

@then('Verify that auto loading option should not be seen on video player screen')
def verify_auto_loading_not_present(browser):
    video.verify_auto_loading_not_present(browser)
    

@then('Verify the up next chapter text and cancel button should not be displayed on video player screen')
def verify_previous_cancel_btn_not_present(browser):
    video.verify_video_player_previous_cancel_btn(browser)
    
    
@then('verify that replay icon should be displayed on video player screen')
@then('Verify replay icon is shown on video player screen')
def verify_video_player_reply_icon(browser):
    video.verify_video_player_reply_icon(browser)
    
    
@then('verify App back arrow in top left corner of the screen.')
def verify_back_btn_on_video(browser):
    video.verify_back_btn_on_video(browser)
    
    
@then('Verify replay icon is shown on video player screen')    
@then('verify Previous  button in left hand side of Replay icon.')
def verify_previous_icon_on_video(browser):
    video.verify_previous_icon_on_video(browser)
    
    
@when('Tap on  first video')
def tap_on_first_video(browser):
    video.tap_on_first_video_lnk(browser)
    
    
@then('enable the toggle button')
def enable_toggle_btn(browser):
    video.enble_toggle_btn(browser)
    
    
@when(parsers.parse('Tap on forward "{text}" secs button'))
def tap_forward(browser):
    video.tap_forward(browser)
    
    
@when(parsers.parse('verify video is forwarded to "{text}" secs'))
def verify_fwrd_10_sec(browser):
    video.verify_fwrd_time(browser)
    
    
@when('tap on 10 secs backward icon')
def tap_backward_10sec(browser):
    video.tap_backward_10sec(browser)
    
    
@then('Verify that video is moved backward 10 secs')
def verify_backward_10sec(browser):
    video.verify_backward_10sec(browser)
    
    
@given('tap on the practice card')
def tap_on_practice_card(browser):
    video.tap_on_practice_card(browser) 
    
    
@when('Progress the practice until tackle video is shown')
def progress_till_video_play(browser):
    video.progress_till_video_play(browser)
    
       
@then('Verify that setting icon should not be seen')
def verify_setting_icon_not_seen(browser):
    video.verify_setting_icon_not_seen(browser)


@when('complete the video')
def complete_video(browser):
    video.complete_video(browser)
    

@given('on home screen tap on analysis icon')
def tap_on_analysis_icon(browser):
    video.tap_on_analysis_icon(browser)
    
    
@when('Tap on key focus area video')
def tap_on_keyFocus_area(browser):
    video.tap_on_keyFocus_area(browser)
    
    
@when('Tap on any video')    
@when('Tap on the second video in subtopic list screen')
def tap_on_second_video_lnk(browser):
    video.tap_on_second_video_lnk(browser)
    

@then('verify Replay icon ,next button and previous button option is displayed on video player screen')
def verify_reply_next_previous_btn(browser):
    video.verify_reply_next_previous_btn(browser)
    
    
@when('Tap on replay icon')
def tap_on_reply_icon(browser):
    video.tap_on_reply_icon(browser)
    
    
@when('Verify that same video is played again')
@then('Verify that same video is played again')
def verify_same_video_is_played(browser):
    video.verify_same_video_is_played(browser)  
    

@when('verify video is played ,complete the video')
def verify_video_played_and_complete(browser):
    video.video_should_played(browser)
    video.complete_video(browser)
    
    
@then('Verify that next video is auto loaded and played successfully')
def verify_autoloded_and_played(browser):
    video.verify_autoloded_and_played(browser)
    
    
@then('verify the toggle button colour should be in grey')
def verify_grey_color(browser):
    video.verify_grey_color(browser)

