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
featureFileName = "Practice video player in Tab"


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
    
    
@given('tap on the practice card')
def tap_on_practice_card(browser):
    video.tap_on_practice_card(browser)
    
    
@when('Progress the practice until tackle video is shown')
def progress_till_video_play(browser):
    video.progress_till_video_play(browser)
    
    
@then('Verify that video screen is open')
def verify_video_screen(browser):
    video.verify_video_screen(browser)
    
    
@then('Verify App back button on top left corner')
def verify_video_back_btn(browser):
    video.verify_video_back_btn(browser)
    

@then('Verify speed up/down icon should be shown')
def verify_speedBtn(browser):
    video.verify_speedBtn(browser)

    
@then('Verify play , pause icon should shown')
def verify_play_pause_Icon(browser):
    video.verify_play_pause_Icon(browser)
    
    
@then('Verify audio tracks icon should shown')
def verify_multipleAudio(browser):
    video.verify_multipleAudio(browser)
    
    
@then('Verify 10 sec forward/10 sec backward "button" should be shown')
def verify_fastFrwd(browser):
    video.verify_fastFrwd(browser)
    video.verify_fast_backwrd_icon(browser)
    
    
    

    
    
    

    
    

    
    
