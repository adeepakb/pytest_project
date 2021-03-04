from pytest_bdd import scenarios, given, when, then, parsers
from POM_Pages.Android_pages.videopage import VideoPage
from Utilities.BasePage import BaseClass

driver = fixture = 'driver'
baseClass = BaseClass()
video = VideoPage(driver)

"""storing the feature file name"""
featureFileName = "videoplayer screen"

# baseClass.setupLogs(featureFileName)

"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""
scenarios('../features/'+featureFileName+'.feature')


@given("Launch the app online")
def launchAppOnline(driver):
    pass


@given(parsers.parse('navigate to "{text}" library chapter list screen'))
def navigateToHomeScreen(driver,text):
    video.navigate_to_home_screen(driver, text)
    video.navigate_to_library(driver, text)
    
    
@when('Tap on any video from chapter list screen')
def tapOnAnyVideo(driver): 
    video.tap_on_any_video_in_sub_screen(driver)
    
    
@when('Subtopic video slider will open')
def verify_subtopic_video_slider(driver):
    video.verify_subtopic_video_slider(driver)
    
    
@when('Tap on any video')   
def tap_on_any_video(driver):
    video.tap_on_any_video(driver)
    
    
@when('change the video orentation from portrait to Landscape by tapping on  landscape icon')
def change_orientation(driver): 
    video.change_orientation_landscape(driver)


@then('Verify App back arrow is present  on the top left corner of the screen')
def verify_backBtn(driver):
    video.verify_video_back_btn(driver)
    
    
@then('verify Speed Up Speed Down icon on video player screen')
def verify_speedBtn(driver):
    video.verify_speedBtn(driver)
    
    
@then('verify Subtitle icon on video player screen')
def verify_subtitile(driver):
    video.verify_subtitile(driver)
    
    
@then('verify Multiple Audio track icon on video player screen')
def verify_multipleAudio(driver):
    video.verify_multipleAudio(driver)
    
    
@then('verify Setting icon on video player screen')
def verify_setting_icon(driver):
    video.verify_setting_icon(driver)
    
    
@then('verify Play/Pause icon in the middle of the Player.')
def verify_play_pause_Icon(driver):
    video.verify_play_pause_Icon(driver)
    
    
@then('verify Fast Forward and Fast Rewind icon on the left and right side of Play/Pause icon with 10s notation.')
def verify_fastFrwd(driver):
    video.verify_fastFrwd(driver)
    video.verify_fast_backwrd_icon(driver)
    
    
@then('verify Seek bar in between Start and End Timer at the bottom of the Player.')
def verify_video_progress_bar(driver):
    video.verify_video_progress_bar(driver)
    
    
@then('verify Full screen mode icon next to End timer.')
def verify_video_fullScreen_icon(driver):
    video.verify_video_fullScreen_icon(driver)
    
    
@when('tap on Pause icon')
def tap_on_pause_btn(driver): 
    video.tap_on_pause_btn(driver)
    
    
@when('Verify video should be played')
def verify_video_should_play(driver):
    video.video_should_played(driver)
    
    
@then('Verify that when video is in paused state pause icon should be replaced with play icon in video player screen')
def verify_play_btn(driver):
    video.verify_play_btn_in_lanscape(driver)
    


