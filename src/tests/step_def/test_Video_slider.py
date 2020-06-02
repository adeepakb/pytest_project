from pytest_bdd import scenarios, given, when, then, parsers
from POM_Pages.videopage import VideoPage
from Utilities.BasePage import BaseClass

browser = fixture = 'browser'
baseClass = BaseClass()
video = VideoPage(browser)

"""storing the feature file name"""
featureFileName = "Video Slider in Tab"


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
    
    
@given('Tap on any video from chapter list screen')
def tapOnAnyVideo(browser): 
    video.tap_on_any_video_in_sub_screen(browser)
    
    
@when('Tap on any video')
def tap_on_any_video(browser): 
    video.tap_on_any_video(browser)
    
    
@when('Subtopic video slider will open')
def verify_subtopic_video_slider(browser):
    video.verify_subtopic_video_slider(browser)
    
    
@when('Video should be played')
@then('Video should be played')
@when('Verify video should be played')
@then('Verify video should be played')
def video_should_played(browser):
    video.video_should_played(browser)
    
    
@when('Open subtopic video slider')   
@then('Open subtopic video slider')
def open_subtopic_video_slider(browser):
    video.open_subtopic_video_slider(browser)
    
    
@then('Verify watched Video in the subtopic video slider should be highlighted')
def video_should_highlighted(browser):
    video.video_should_highlighted(browser)
    
    
@then('Verify the start timer of the video should be 00:00')
def verify_start_time(browser):
    video.verify_start_time(browser)


@then('verify  End time  of the video should be total duration of video')
def verify_end_time(browser):
    video.verify_end_time(browser)


@then('verify video is played in landscape mode')
def verify_video_in_landscape(browser):
    video.verify_video_playing_in_landscape(browser)    
    
    
@when(parsers.parse('Tap on forward "{text}" secs button'))
def tap_forward(browser):
    video.tap_forward(browser)


@when(parsers.parse('verify video is forwarded to "{text}" secs'))
def tap_forward2(browser):
    video.verify_fwrd_time(browser)
    

@then('Verify video should be played in Landscape mode with out any interruption')
def verify_video_playing_in_landscape(browser):
    video.verify_video_playing_in_landscape(browser)
    
    
@then('Verify that chapter video should be displayed in List view')
def verify_list_view(browser):
    video.verify_list_view(browser)
    
    
@then('verify Test card')   
@then('Verify Test card is present in Subtopic list')
def verify_test_card_is_present(browser):
    video.verify_test_card_is_present(browser)
    
    
@then('verify practice card')
@then('Verify Practice card is present in subtopic video list')
def verify_practice_card_is_present(browser):
    video.verify_practice_card_is_present(browser)
    
    
    
@then('Verify subtopic videos should available')
def verify_subtopic_videos(browser):
    video.verify_subtopic_videos(browser)
    
    
@then('Verify back button should available with right arrow icon')
def verify_back_btn_in_subtopic_video_lst(browser):
    video.verify_back_btn_in_subtopic_video_lst(browser)
    
    
@when('complete the video')
@then('Video should be played completely without performing any actions like forward and seeking')
def video_should_complete(browser):
    video.complete_video(browser)
    
    
@then('Verify XX min followed by completed text is displayed below the subtopic name in the video list')
def veify_xxmin_followed_completed(browser):
    video.verify_min_completed(browser)
    
    
@then('Verify progression of video is 100% in video list screen')
def verify_progression_100_percent(browser):
    video.verify_progression_100_percent(browser)
    
    
@when('Tap on pause icon')
def tap_pause_btn(browser):
    video.tap_pause_btn(browser)


@when('verify video is paused')
def verify_video_paused(browser):
    video.verify_pause_btn(browser)
    
    
@when('Tap on the play icon')
def tap_play_btn(browser):
    video.play_video(browser)
    

@then('verify  video is resumed from where it as stopped')
def verify_video_resumed_from_same_point(browser):
    video.verify_video_resumed_from_same_point(browser)
    
    
@then('verify Test icon is present')
def verify_test_icon_is_present(browser):
    video.verify_test_icon_is_present(browser)
    
    
@then('verify Label Test is present')
def verify_test_label_is_present(browser):
    video.verify_test_label_is_present(browser)
    
    
@then('verify X test is present')
def verify_x_test_is_present(browser):
    video.verify_x_test_is_present(browser)
    
    
@then('Forward icon')
def verify_forward_icon_test(browser):
    video.verify_forward_icon_test(browser)
    
    
@when('tap on Test card from the subtopic video list')
def tap_on_test_on_video_sub_list(browser):
    video.tap_on_test_on_video_sub_list(browser)
    
    
@then('Verify user should be navigated to that particular chapter Practice home screen')    
@then('Verify that user is Redirected to that particular chapter test list screen')
def verify_chapter_in_test_screen(browser):
    video.verify_chapter_in_test_screen(browser)
    
    
@when('Tap on back arrow icon')
def tap_on_back_arrow_btn(browser):
    video.tap_on_back_arrow_btn(browser)
    
        
@when('Tap on device back button')
def tap_on_device_back_btn(browser):
    video.tap_on_device_back_btn(browser)
    
    
@then('Verify that user is Redirected to that particular chapter  list screen')
def verify_redirect_to_chapter_screen(browser):
    video.verify_redirect_to_chapter_screen(browser)
    
    
@then('verify Practice icon')
def verify_practice_icon_is_present(browser):
    video.verify_practice_icon_is_present(browser)
    
    
@then('verify Label practice')
def verify_practice_label_is_present(browser):
    video.verify_practice_label_is_present(browser)
    
    
@then('verify Stage Name')
def verify_pratice_stage_name_is_present(browser):
    video.verify_pratice_stage_name_is_present(browser)
    

@then('verify practice Forward icon')
def verify_forward_icon_practice(browser):
    video.verify_forward_icon_practice(browser)
    
    
@when('tap on practice card from the subtopic video list')
def tap_on_practice_on_video_sub_list(browser):
    video.tap_on_practice_on_video_sub_list(browser)
    
   
@then('Scroll and verify the video list screen up and down')
def scroll_video_list_up_and_down(browser):
    video.scroll_video_list_up_and_down(browser)
    

    
    
    
