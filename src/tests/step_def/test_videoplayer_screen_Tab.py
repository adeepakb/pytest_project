from pytest_bdd import scenarios, given, when, then, parsers
from POM_Pages.videopage import VideoPage
from Utilities.BasePage import BaseClass

browser = fixture = 'browser'
baseClass = BaseClass()
video = VideoPage(browser)

"""storing the feature file name"""
featureFileName = "videoplayer screen in Tab"

"""configuring the Logging Files"""
baseClass.setupLogs(featureFileName)

"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""
scenarios('../features/'+featureFileName+'.feature')


@given("Launch the app online")
def launchAppOnline(browser):
    pass


@given(parsers.parse('navigate to "{text}" library chapter list screen'))
def navigateToHomeScreen(browser,text):
    video.navigate_to_home_screen(browser, text)
    video.navigate_to_library(browser, text)
    
    
@when('Tap on any video from chapter list screen')
def tapOnAnyVideo(browser): 
    video.tap_on_any_video_in_sub_screen(browser)
    
    
@when('Subtopic video slider will open')
def verify_subtopic_video_slider(browser):
    video.verify_subtopic_video_slider(browser)
    
    
@when('Tap on any video')   
def tap_on_any_video(browser):
    video.tap_on_any_video(browser)
    

@then('Verify App back arrow is present  on the top left corner of the screen')
def verify_backBtn(browser):
    video.verify_video_back_btn(browser)
    
    
@then('verify Speed Up Speed Down icon on video player screen')
def verify_speedBtn(browser):
    video.verify_speedBtn(browser)
    
    
@then('verify Subtitle icon on video player screen')
def verify_subtitile(browser):
    video.verify_subtitile(browser)
    
    
@then('verify Multiple Audio track icon on video player screen')
def verify_multipleAudio(browser):
    video.verify_multipleAudio(browser)
    
    
@then('verify Setting icon on video player screen')
def verify_setting_icon(browser):
    video.verify_setting_icon(browser)
    
    
@then('verify Play/Pause icon in the middle of the Player.')
def verify_play_pause_Icon(browser):
    video.verify_play_pause_Icon(browser)
    
    
@then('verify Fast Forward and Fast Rewind icon on the left and right side of Play/Pause icon with 10s notation.')
def verify_fastFrwd(browser):
    video.verify_fastFrwd(browser)
    video.verify_fast_backwrd_icon(browser)
    
    
@then('verify Seek bar in between Start and End Timer at the bottom of the Player.')
def verify_video_progress_bar(browser):
    video.verify_video_progress_bar(browser)
    
    
@then('verify Full screen mode icon next to End timer.')
def verify_video_fullScreen_icon(browser):
    video.verify_video_fullScreen_icon(browser)
    
    
@when('tap on Pause icon')
def tap_on_pause_btn(browser): 
    video.tap_on_pause_btn(browser)
    
    
@when('Verify video should be played')
def verify_video_should_play(browser):
    video.video_should_played(browser)
    
    
@then('Verify that when video is in paused state pause icon should be replaced with play icon in video player screen')
def verify_play_btn(browser):
    video.verify_play_btn_in_lanscape(browser)