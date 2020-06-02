from pytest_bdd import scenarios, given, when, then, parsers
from POM_Pages.videopage import VideoPage
from Utilities.BasePage import BaseClass

browser = fixture = 'browser'
baseClass = BaseClass()
video = VideoPage(browser)


"""storing the feature file name"""
featureFileName = "video Autoplay Disabled"


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
    
    
@when('Tap on the first video in subtopic list screen')
def tap_on_first_video_lnk(browser):
    video.start_the_video(browser)
    
    
@when('Tap on the first video in subtopic list screen  and complete a video')
def tap_on_first_video_and_complete(browser):
    video.tap_on_first_video_lnk_and_complete(browser)
    
    
@when('Subtopic video slider will open')
def verify_subtopic_video_slider(browser):
    video.verify_subtopic_video_slider(browser)
    
    
@then('Verify that previous button should not be shown on video player screen')
def previous_btn_not_shown(browser):
    video.verify_previous_icon_not_on_video(browser)
    

@when('Tap on any video')   
def tap_on_any_video(browser):
    video.tap_on_any_video(browser)
    
     
@when('Tap on the second video in subtopic list screen')
def tap_on_second_video_lnk(browser):
    video.tap_on_second_video_lnk(browser)


@given('Tap on any video from chapter list screen')
def tapOnAnyVideo(browser): 
    video.tap_on_any_video_in_sub_screen(browser)    
    
    
@given('Autoplay option should be  disabled for  Videos')
def turn_off_auto_play(browser):
    video.turn_off_auto_play(browser)  
    

@then('Verify that previous button should not be shown on video player screen')
def verify_video_player_previous_btn(browser):
    video.verify_video_player_previous_btn(browser)
    
    
@when('Tap on the last  video in subtopic list screen')  
def tap_on_last_video_lnk(browser):
    video.click_on_video_last_lnk(browser)
    
     
@when('Tap on the last  video in subtopic list screen and complete a video')
def tap_on_last_video_in_list(browser):
    video.tap_on_last_video_in_list_and_complete(browser)
    
    
@then('Verify that Next button option should not be shown on video player screen')
def verify_video_player_next_btn(browser):
    video.verify_video_player_next_btn_not_present(browser)
    

@when('Tap on the second video in subtopic list screen') 
def tap_on_2nd_video_lnk(browser):
    video.click_on_2nd_video_lnk(browser)

    
@when('Tap on the second video in subtopic list screen and complete and video')
def tap_on_2nd_video_lnk_and_complete(browser):
    video.tap_on_2nd_video_lnk_and_complete(browser)
    
    
@then('Verify that auto loading option should not be seen on video player screen')
def verify_auto_loading_not_present(browser):
    video.verify_auto_loading_not_present(browser)
    
    
@when('Autoplay option should be disabled for Videos')
def turn_off_auto_play2(browser):
    video.turn_off_auto_play(browser)
    
    
@then('verify Replay icon is shown on the video player screen')
def verify_reply_icon_is_shown(browser):
    video.verify_reply_icon_is_shown(browser)
    

@when('complete the video')
def complete_video(browser):
    video.complete_video(browser)


@then('Verify Previous button ,Next button should be displayed on video player screen')
def verify_previour_next_icon_is_shown(browser):
    video.verify_previour_next_icon_is_shown(browser)
    

@when('Tap on replay icon')
def tap_on_reply_icon(browser):
    video.tap_on_reply_icon(browser)
    
    
@then('Verify that same video is played again')
def verify_same_video_is_played(browser):
    video.verify_same_video_is_played(browser)
    
    
@when('Tap on Next icon [>|]')
def tap_on_next_btn_in_video_player(browser):
    video.tap_on_next_btn_in_video_player(browser)


@when('Tap on Previous icon [|<]') 
def tap_on_previous_icon(browser):
    video.tap_on_previous_icon_in_video_player(browser) 
    
    
@then('Verify that next video is played')
def verify_next_video_is_played(browser):
    video.verify_next_video_is_played(browser)
    

@then('Verify that previous video is played')
def verify_previous_video_is_played(browser):
    video.verify_previous_video_is_played(browser)
