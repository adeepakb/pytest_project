from pytest_bdd import scenarios, given, when, then, parsers
from POM_Pages.videopage import VideoPage
from Utilities.BasePage import BaseClass

browser = fixture = 'browser'
baseClass = BaseClass()
video = VideoPage(browser)

"""storing the feature file name"""
featureFileName = "Video Orientation in Tab"


"""configuring the Logging Files"""
baseClass.setupLogs(featureFileName)


"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""
scenarios('../features/'+featureFileName+'.feature')


@given("Launch the app online")
def launchAppOnline(browser):
    pass


@given(parsers.parse('Navigate to "{text}" library chapter list screen'))
def navigateToHomeScreen(browser,text): 
    video.navigate_to_home_screen(browser, text)
    video.navigate_to_library(browser,text)
    

@when('Tap on any video from chapter list screen')
def tapOnAnyVideo(browser):
    video.tap_on_any_video_in_sub_screen(browser)
    
    
@when('Subtopic video slider will open')
def verify_subtopic_video_slider(browser):
    video.verify_subtopic_video_slider(browser)
    
    
@when('Tap on any video') 
@when('Tap on any video from video list')    
def tap_on_any_video(browser):
    video.tap_on_any_video(browser)
    
    
@when('verify video is played in landscape mode')    
@then('verify video is played in landscape mode')
def verify_video_in_landscape(browser):
    video.verify_video_playing_in_landscape(browser)