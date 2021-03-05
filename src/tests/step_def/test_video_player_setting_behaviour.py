from pytest_bdd import scenarios, given, when, then, parsers
from pom_pages.android_pages.videopage import VideoPage
from utilities.BasePage import BaseClass
from utilities.common_methods import CommonMethods
from time import sleep
# from utilities.API_methods import *

driver = fixture = 'driver'

base_class = BaseClass()
video = VideoPage(driver)
CommonMethods = CommonMethods()


"""storing the feature file name"""
featureFileName = "Video player setting Behaviour"

# base_class.setupLogs(featureFileName)

"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""
scenarios('../features/' + featureFileName + '.feature')




@given("Launch the app online")
def launchAppOnline(driver):
    pass


@when(parsers.parse('navigate to "{text}" library chapter list screen'))
def navigateToHomeScreen2(driver, text):
    video.navigate_to_home_screen(driver, text)
    video.navigate_to_library(driver, text)


@given(parsers.parse('navigate to "{text}" library chapter list screen'))
def navigateToHomeScreen(driver, text):
    video.navigate_to_home_screen(driver, text)
    video.navigate_to_library(driver, text)


@given('Tap on any video from chapter list screen')
def tapOnAnyVideo(driver):
    video.tap_on_any_video_in_sub_screen(driver)


@when('Tap on any video from chapter list screen')
def tapOnAnyVideo2(driver):
    video.tap_on_any_video_in_sub_screen(driver)


@when('Subtopic video slider will open')
def verify_subtopic_video_slider(driver):
    video.verify_subtopic_video_slider(driver)


@when('Verify video should be played')
@then('Verify video should be played')
def video_should_played(driver):
    video.video_should_played(driver)


@when('Tap on any video')
@when('Tap on any video from video list')
def tap_on_any_video(driver):
    video.tap_on_any_video(driver)


@when(parsers.parse('wait for "{text}" secs'))
def wait_for_secs(text):
    sleep(int(text))
    sleep(int(text))


@then('verify Player screen should be shown with out any player options')
def verify_video_icons_should_disapper(driver):
    video.verify_video_icons_should_disapper(driver)


@then('Verify all the video player icons should disappear')
def verify_video_icons_should_disapper2(driver):
    video.verify_video_icons_should_disapper(driver)


@then('Verify the player layer is up and it should not disappear i.e all the options should be visible')
def verify_video_icons_should_apper(driver):
    video.verify_video_icons_should_apper(driver)


@when('Taps on pause icon')
def tap_on_pause_icon(driver):
    video.tap_on_pause_btn(driver)


@when('tap on the video player layer skin')
def tap_on_player_screen():
    CommonMethods.run('adb shell input tap 40 200')




