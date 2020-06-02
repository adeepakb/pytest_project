from pytest_bdd import scenarios, given, when, then, parsers
from POM_Pages.videopage import VideoPage
from Utilities.BasePage import BaseClass
from Utilities.common_methods import CommonMethods

browser = fixture = 'browser'

base_class = BaseClass()
video = VideoPage(browser)
CommonMethods = CommonMethods()

"""storing the feature file name"""
featureFileName = "Videoplayer subtitles"

"""configuring the Logging Files"""
base_class.setupLogs(featureFileName)

"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""
scenarios('../features/' + featureFileName + '.feature')


@given("Launch the app online")
def launchAppOnline(browser):
    pass


@when(parsers.parse('navigate to "{text}" library chapter list screen'))
def navigateToHomeScreen2(browser, text):
    video.navigate_to_home_screen(browser, text)
    video.navigate_to_library(browser, text)


@given(parsers.parse('navigate to "{text}" library chapter list screen'))
def navigateToHomeScreen(browser, text):
    video.navigate_to_home_screen(browser, text)
    video.navigate_to_library(browser, text)


@given('Tap on any video from chapter list screen')
def tapOnAnyVideo(browser):
    video.tap_on_any_video_in_sub_screen(browser)


@when('Tap on any video from chapter list screen')
def tapOnAnyVideo2(browser):
    video.tap_on_any_video_in_sub_screen(browser)


@when('Subtopic video slider will open')
def verify_subtopic_video_slider(browser):
    video.verify_subtopic_video_slider(browser)
    
    
@when('Verify video should be played')
@then('Verify video should be played')
def video_should_played(browser):
    video.video_should_played(browser)
    
    
@when('Tap on any video') 
@when('Tap on any video from video list')    
def tap_on_any_video(browser):
    video.tap_on_any_video(browser)