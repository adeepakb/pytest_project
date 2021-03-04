from pytest_bdd import scenarios, given, when, then, parsers
from POM_Pages.Android_pages.videopage import VideoPage
from Utilities.BasePage import BaseClass

driver = fixture = 'driver'
baseClass = BaseClass()
video = VideoPage(driver)

"""storing the feature file name"""
featureFileName = "Video  Orientation"


# baseClass.setupLogs(featureFileName)


"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""
scenarios('../features/'+featureFileName+'.feature')


@given("Launch the app online")
def launchAppOnline(driver):
    pass


@given(parsers.parse('Navigate to "{text}" library chapter list screen'))
def navigateToHomeScreen(driver,text):
    video.navigate_to_home_screen(driver, text)
    video.navigate_to_library(driver,text)


@when('Tap on any video from chapter list screen')
def tapOnAnyVideo(driver):
    video.tap_on_any_video_in_sub_screen(driver)


@when('Tap on Landscape option in video')
def change_video_to_landscape(driver):
    video.change_orientation_landscape(driver)


@when('Subtopic video slider will open')
def verify_subtopic_video_slider(driver):
    video.verify_subtopic_video_slider(driver)


@when('Tap on any video')
@when('Tap on any video from video list')
def tap_on_any_video(driver):
    video.tap_on_any_video(driver)


@when('verify video is played in landscape mode')
@then('verify video is played in landscape mode')
def verify_video_in_landscape(driver):
    video.verify_video_playing_in_landscape(driver)


@then('verify video continues to play without any interruption in landscape')
def video_play_without_any_interruption_in_landscape(driver):
    video.video_play_without_any_interruption_in_landscape(driver)


@then('verify video continues to play without any interruption in potrait')
def video_play_without_any_interruption_in_potrait(driver):
    video.video_play_without_any_interruption_in_potrait(driver)


@then('Tap on potrait mode option in video player screen')
def change_video_to_potrait(driver):
    video.change_orientation_potrait(driver)


@when('verify video is played in potrait mode')
def verify_video_in_potrait(driver):
    video.verify_video_in_potrait(driver)


@when('Tap on device back button')
def tap_on_device_back_btn(driver):
    video.tap_on_device_back_btn(driver)

