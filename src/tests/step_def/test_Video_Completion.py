from pytest_bdd import scenarios, given, when, then, parsers
from POM_Pages.videopage import VideoPage
from Utilities.BasePage import BaseClass
from Utilities.common_methods import CommonMethods

browser = fixture = 'browser'

base_class = BaseClass()
video = VideoPage(browser)
CommonMethods = CommonMethods()

"""storing the feature file name"""
featureFileName = "Video Completion"

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


@when('Tap on any video from the video list screen')
def tap_on_video_from_video_list(browser):
    video.tap_on_video_from_video_list(browser)
    
    
@when('Tap on any video and complete a video')    
@when('Tap on the first video in subtopic list screen  and complete a video')
def tap_on_first_video_and_complete(browser):
    video.tap_on_first_video_lnk_and_complete(browser)
    
    
@then('Verify that on Video Completion Auto loading on Play icon should be seen')
def verify_video_icon_after_completion(browser):
    video.verify_video_icon_after_completion(browser)


@then('Cancel button')
@then('Text Up next followed by next Subtopic/Video name and Chapter name')    
def video_next_icons(browser):
    pass # alredy handled in the previous verify_video_icon_after_completion method 


@then('verify App back arrow in top left corner of the screen.')
def verify_back_arrow_in_video_player(browser):
    check = CommonMethods.isElementPresent(browser, video.video_player_back_btn)
    video.verify_true_or_false(browser, check, 'verify_back_arrow_in_video_player', 'Video Player back button')


@then('Verify auto loading is shown and after completion  next  video in the list should start playing')
def next_video_should_play(browser):
    video.next_video_should_play(browser)
    

@then('verify the highlighter is switched to next video which is playing')
def video_should_be_highlighted(browser):
    video.video_should_highlighted(browser)
    
    
@when('While auto loading is shown tap on cancel button')
def tap_on_cancel_button(browser):
    video.tap_on_cancel_button(browser)
    
    
@then('verify App back arrow in top left corner of the screen.')
def verify_back_btn_on_video(browser):
    video.verify_back_btn_on_video(browser)
    
    
@then('verify Replay icon')
def verify_reply_icon(browser):
    video.verify_reply_icon(browser)
    
    
@then('verify Play Next icon')
def verify_play_next_icon(browser):
    video.verify_play_next_icon(browser)
    
    
@then('verify Current Video name')
def verify_current_video_name(browser):
    video.verify_current_video_name(browser)
    
    
@when('Tap on replay icon')
def tap_on_reply_icon(browser):
    video.tap_on_reply_icon(browser)
    
    
@then('Verify that same video is played again')
def verify_same_video_is_played(browser):
    video.verify_same_video_is_played(browser)
    
    
@when('Tap on Play Next button')
def tap_on_next_btn_in_video_player(browser):
    video.tap_on_next_btn_in_video_player(browser)
                                          

@then('Verify that next video is played')
def verify_next_video_is_played(browser):
    video.verify_next_video_is_played(browser)
    

@then('Verify that previous button should not be shown on video player screen')
def previous_btn_not_shown(browser):
    video.verify_previous_icon_not_on_video(browser)
    
    
@when('Tap on the last  video in subtopic list screen  and complete a video')
def tap_on_last_video_in_list(browser):
    video.tap_on_last_video_in_list_and_complete(browser)
    

@then('Verify that Next button option should not be shown on video player screen')
def verify_video_player_next_btn(browser):
    video.verify_video_player_next_btn_not_present(browser)
    

    

