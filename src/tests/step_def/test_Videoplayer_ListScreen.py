from pytest_bdd import scenarios, given, when, then, parsers
from POM_Pages.videopage import VideoPage
from Utilities.BasePage import BaseClass
from Utilities.common_methods import CommonMethods

# browser = fixture = 'browser'
browser = fixture = 'browser'

base_class = BaseClass()
video = VideoPage(browser)
CommonMethods = CommonMethods()

"""storing the feature file name"""
featureFileName = "Videoplayer List Screen"

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


@when('Verify video should be played')
@then('Verify video should be played')
def video_should_played(browser):
    video.video_should_played(browser)

    
@given('Video should be played')
def verify_video_playing3(browser):
    video.video_should_played(browser)


@then('Video should be played')
def verify_video_playing2(browser):
    video.video_should_played(browser)


@then(parsers.parse('verify "{text}" text tag should be displayed below the list video'))
def verify_playingTxt_tag(browser, text):
    video.verify_playingTxt_tag(browser, text)


@then('watched Video name in the list should be highlighted')
def video_should_highlighted(browser):
    video.video_should_highlighted(browser)


@then('complete the video')
@then('Video should be played completely without performing any actions like forward and seeking')
def video_should_complete(browser):
    video.complete_video(browser)
    
    
@then('complete the video till end')
def Complete_the_video_till_end(browser):
    video.Complete_the_video_till_end(browser)


@then('Verify the start timer of the video should be 00:00')
def verify_start_time(browser):
    video.verify_start_time(browser)


@then('verify  End time  of the video should be total duration of video')
def verify_end_time(browser):
    video.verify_end_time(browser)


@given(parsers.parse('Tap on forward "{text}" secs button'))
def tap_forward(browser):
    video.tap_forward(browser)


@given(parsers.parse('verify video is forwarded to "{text}" secs'))
def tap_forward2(browser):
    video.verify_fwrd_time(browser)


@given('verify video is played in potrait mode')
def verify_video_in_potrait(browser):
    video.video_should_played(browser)
    
    
@when('Tap on device back button')
def tap_on_device_back_btn(browser):
    video.tap_on_device_back_btn(browser)


@given('Verify that video starts playing')
def verify_video_playing(browser):
    video.video_should_played(browser)


@given('Tap on Landscape option in video')
def change_video_to_landscape(browser):
    video.change_orientation_landscape(browser)
    
    
@given('verify video is played in landscape mode')
def verify_video_in_landscape(browser):
    video.verify_video_playing_in_landscape(browser)
    
    
@then('Verify that video orentation should change to potrait mode')
def verify_video_in_potrait2(browser):
    video.verify_video_in_potrait(browser)


@when('Tap on Landscape option in video player screen')
def change_video_to_landscape2(browser):
    video.change_orientation_landscape(browser)
    
    
@when('Tap on potrait mode option in video player screen')
def change_video_to_potrait(browser):
    video.change_orientation_potrait(browser)


@then('Verify video continues to play with out pausing when user switches to any of the modes')
def verify_video_continue_without_pausing(browser):
    video.verify_video_continue_without_pausing(browser)


@then('Verify video should be played in Landscape mode with out any interruption')
def verify_video_in_landscape3(browser):
    video.verify_video_in_landscape(browser)
    
    
@then('verify video continues to play without any interruption')
def video_play_without_any_interruption_in_landscape(browser):
    video.video_play_without_any_interruption_in_landscape(browser)


@given(parsers.parse('Tap on "{topic}" video card from "{chapter}" chapter'))
def select_topic(browser, topic, chapter):
    video.select_topic(browser, topic, chapter)


@when(parsers.parse('Tap on "{topic}" video card from "{chapter}" chapter'))
def select_topic1(browser, topic, chapter):
    video.select_topic(browser, topic, chapter)


@then(parsers.parse('Verify that user is landed on "{text}" video list screen'))
def verify_video_chapter_name(browser, text):
    video.verify_video_chapter_name(browser, text)


@when(parsers.parse('verify "{text}" video starts playing'))
@then(parsers.parse('verify "{text}" video starts playing'))
def verify_video_subtitle_name(browser, text):
    video.verify_video_subtitle_name(browser, text)


@then('Verify that Topic video should be displayed in List view')
def verify_list_view(browser):
    video.verify_list_view(browser)


@then('verify video name')
def verify_video_name(browser):
    video.verify_video_name(browser)


@then('verify Video Thumbnail')
def verify_video_thumbnail(browser):
    video.verify_video_thumbnail(browser)


@then('verify total Duration of video')
def verify_video_duration(browser):
    video.verify_video_duration(browser)


# @then('Verify XX min followed by completed text is displayed below the subtopic name in the video list')
# def verify_min_completed(browser):
#     video.verify_min_completed(browser)


@when('tap on same video')
@then('tap on same video')
def tap_on_same_video(browser):
    video.tap_on_same_video(browser)


@then(parsers.parse('verify Video progression should always be shown "{text}"'))
def video_progression(browser, text):
    video.video_progression(browser, text)


@when('Tap on pause icon')
def tap_pause_btn(browser):
    video.tap_pause_btn(browser)


@when('verify video is paused')
def verify_video_paused(browser):
    video.verify_pause_btn(browser)


@when('Tap on the same video')
def tap_on_the_same_video(browser):
    video.tap_on_same_video(browser)
    
    
# @then('verify  video is resumed from where it as stopped')
# def verify_video_where_it_stopped(browser):
#     video.verify_video_where_it_stopped(browser)


@then('verify  video is resumed from where it as stopped')
def verify_video_resumed_from_same_point(browser):
    video.verify_video_resumed_from_same_point(browser)


@then('verify Video Player  is present on the top 40% of the screen')
def verify_video_size_40_percent(browser):
    video.verify_video_size_40_percent(browser)


@then('verify Below that Subtopic name of the current playing video')
def verify_subtopic_name(browser):
    video.verify_subtopic_name(browser)


@then('verify Share and Bookmarks icon')
def verify_share_bookmerks_icon(browser):
    video.verify_share_bookmerks_icon(browser)


@then('Topic videos')
def verify_topic_videos(browser):
    video.verify_topic_videos(browser)


@then('A label Chapter name in subject theme color')
def verify_chapter_name_color(browser):
    video.verify_chapter_name_color(browser)


@then(parsers.parse('verify "{text}" card'))
def verify_card_lnk(browser,text):
    video.verify_card_lnk(browser,text)


@then('video progression')
def video_progression2(browser):
    video.video_progression(browser)


@then('A label Chapter name in subject theme color')
def verify_chapter_name_color_with_subject_theme(browser):
    video.verify_chapter_name_color_with_subject_theme(browser)


@then('Verify XX min followed by completed text is displayed below the subtopic name in the video list')
def veify_xxmin_followed_completed(browser):
    video.verify_min_completed(browser)
    

@given(parsers.parse('Switch to "{text}" grade'))
def switch_to_grade(browser, text):
    video.switch_to_grade(browser, text)    
    
    
@when(parsers.parse('on Home screen tap on "{text}" button'))
def tap_on_chapter(browser, text):
    video.tap_on_chapter(browser, text)
    
    
@then(parsers.parse('Verify coming Soon video is displayed under "{text}" chapter'))
def verify_comming_soon_on_video_card(browser, text):
    video.verify_comming_soon_on_video_card(browser, text)  
    
    
@then(parsers.parse('tap on the video card under "{text}" chapter'))
def tap_on_comming_soon_on_video_card(browser, text):
    video.tap_on_comming_soon_on_video_card(browser, text)  
    
    
@then('verify Coming soon text tag is displayed under subtopic video list')
def verify_comming_soon_dialog(browser):
    video.verify_comming_soon_dialog(browser)
    
    
@then('verify Test card')   
@then('Verify Test card is present in Subtopic list')
def verify_test_card_is_present(browser):
    video.verify_test_card_is_present(browser)
    
    
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
    
@then('Verify that user is Redirected to that particular chapter test list screen')
def verify_chapter_in_test_screen(browser):
    video.verify_chapter_in_test_screen(browser)
    
    
@when('Navigate to Chapter test list screen')
def navigate_to_test_screen(browser):
    video.navigate_to_test_screen(browser)
    
    
@then('Verify that user is Redirected to that particular chapter  list screen')
def verify_redirect_to_chapter_screen(browser):
    video.verify_redirect_to_chapter_screen(browser)


@then('verify practice card')
@then('Verify Practice card is present in subtopic video list')
def verify_practice_card_is_present(browser):
    video.verify_practice_card_is_present(browser)
    
    
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
    
    
@when(parsers.parse('Tap on Practice card present in "{text}" chapter'))
def tap_on_practice_card(browser, text):
    video.tap_on_practice_card2(browser, text)
    
    
@then(parsers.parse('Verify that user is on "{text}" practice Home screen'))
def verifyTextInScreen(browser,text):
    video.verifyTextPresent(browser,text)
    
    
@then('verify Practice button is displayed')
def verify_practice_btn(browser):
    video.verify_practice_btn(browser)
    
    
@then('Scroll and verify the video list screen up and down')
def scroll_video_list_up_and_down(browser):
    video.scroll_video_list_up_and_down(browser)
    
    
@then('Verify user is redirected to chapter list screen')
def verify_user_is_in_chapter_screen(browser):
    video.verify_user_is_in_chapter_screen(browser)
    

@given('remove all the Booksmarks in bookmarks screen')
def delete_all_bookmark(browser):
    video.tap_on_bookmark_menu(browser)
    video.delete_all_bookmark(browser)
    

@when('Tap on Bookmark icon')
def tap_on_bookmark_icon(browser):
    video.tap_on_bookmark_icon(browser)
    
@then('Verify user is able to book mark the current playing video')
def verify_user_is_able_to_bookmark(browser):
    video.verify_user_is_able_to_bookmark(browser)
    
    
@then(parsers.parse('verify the toast message "{text}" is displayed'))
def verify_toast_msg(browser,text):
    video.verify_toast_msg(browser,text)
    
@then('A label Chapter name in subject theme color')
def verify_chapter_subject_theme_color(browser):
    video.verify_chapter_subject_theme_color(browser)
    
    
@then('Verify the bookmark icon is highlighted in subject theme color')
def verify_the_bookmark_icon_color_with_subject(browser):
    video.verify_the_bookmark_icon_color_with_subject(browser)
    