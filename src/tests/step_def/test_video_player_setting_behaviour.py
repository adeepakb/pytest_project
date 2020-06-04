from pytest_bdd import scenarios, given, when, then, parsers
from POM_Pages.videopage import VideoPage
from Utilities.BasePage import BaseClass
from Utilities.common_methods import CommonMethods
from time import sleep
# from Utilities.API_methods import *

browser = fixture = 'browser'

base_class = BaseClass()
video = VideoPage(browser)
CommonMethods = CommonMethods()


"""storing the feature file name"""
featureFileName = "Video player setting Behaviour"

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


@when(parsers.parse('wait for "{text}" secs'))
def wait_for_secs(text):
    sleep(int(text))
    sleep(int(text))


@then('verify Player screen should be shown with out any player options')
def verify_video_icons_should_disapper(browser):
    video.verify_video_icons_should_disapper(browser)


@then('Verify all the video player icons should disappear')
def verify_video_icons_should_disapper2(browser):
    video.verify_video_icons_should_disapper(browser)


@then('Verify the player layer is up and it should not disappear i.e all the options should be visible')
def verify_video_icons_should_apper(browser):
    video.verify_video_icons_should_apper(browser)


@when('Taps on pause icon')
def tap_on_pause_icon(browser):
    video.tap_on_pause_btn(browser)


@when('tap on the video player layer skin')
def tap_on_player_screen():
    CommonMethods.run('adb shell input tap 40 200')




