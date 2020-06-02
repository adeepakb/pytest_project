from pytest_bdd import scenarios, given, when, then, parsers
from POM_Pages.videopage import VideoPage
from Utilities.BasePage import BaseClass

browser = fixture = 'browser'
baseClass = BaseClass()
video = VideoPage(browser)

"""storing the feature file name"""
featureFileName = "Videoplayer"

"""configuring the Logging Files"""
baseClass.setupLogs(featureFileName)

"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""
scenarios('../features/'+featureFileName+'.feature')


@given("Launch the app online")
def launchAppOnline(browser):
    pass
    

@given(parsers.parse('Navigate to "{text}" library chapter list screen'))
def navigateToHomeScreen(browser,text): 
    video.navigate_to_home_screen(browser,text) 
    video.navigate_to_library(browser,text)
    
    
@when('Tap on any video from chapter list screen')
def tapOnAnyVideo(browser): 
    video.tap_on_any_video_in_sub_screen(browser)
    
    



@when('Verify video should be played')
@then('Verify video should be played')
def video_should_played(browser):
    video.video_should_played(browser)