from pytest_bdd import scenarios, given, when, then, parsers
from POM_Pages.videopage import VideoPage
from Utilities.BasePage import BaseClass

browser = fixture = 'browser'
baseClass = BaseClass()
video = VideoPage(browser)

count = False


"""storing the feature file name"""
featureFileName = "Videoplayer"

# baseClass.setupLogs(featureFileName)

"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""
scenarios('../features/'+featureFileName+'.feature')


@given("Launch the app online")
def launchAppOnline(browser):
    # global count
    # count = video.login_the_user(browser, count)
    pass
    

@given(parsers.parse('Navigate to "{text}" library chapter list screen'))
def navigateToHomeScreen(browser,text): 
    video.navigate_to_home_screen(browser,text) 
    video.navigate_to_library(browser,text)


@when('Verify video should be played')
@then('Verify video should be played')
def video_should_played(browser):
    video.video_should_played(browser)
 
 
@then('verify video should be played')
def Video_should_played(browser):
    video.Video_should_played(browser) 
   
   
@when('Tap on any video from chapter list screen')
def tapOnAnyVideo(browser): 
    video.tap_on_any_video_in_sub_screen(browser)


@given('Tap on any video from chapter list screen')
def tapOnAnyVideo1(browser): 
    video.tap_on_any_video_in_sub_screen(browser)
    
    
@when('Tap on any video from the video list screen')
def tap_on_video_from_video_list(browser):
    video.tap_on_video_from_video_list(browser)


@then('Verify Video should start playing')   
@when('verify video starts playing')
def verify_video_playing(browser): 
    video.verify_video_playing(browser)


@when('user taps on pause icon')
def enterUnregistedNum3(browser): 
    video.tap_on_pause_btn(browser)
    
    
@then('verify video should be paused')
@when('verify video should be paused')
def verifyVideoStoppedPlaying(browser): 
    video.verify_video_paused(browser)
    
    
@when('tap on play icon')
def tap_on_playbtn(browser):
    video.tap_on_playbtn(browser)
    
    
@then('Verify video should get 10 secs backward from the current time')
@then('Verify video should get 10 secs forward from the current time')
def verify_frwd_10sec(browser): 
    pass


@when('tap on right side 10secs button')
def verify_frwd_10Sec(browser):
    video.verify_frwd_10Sec(browser)
    
    
@when(parsers.parse('wait for the video to complete playing "{text}" secs'))
def wait10Sec(text):
    video.custom_wait(text)
    
    
@when('tap on left side 10secs button')
def verify_video_backwrd_10Sec(browser):
    video.verify_video_backwrd_10Sec(browser)
    
    
@when('tap on device HomeButton')
def tap_on_device_home_btn(browser):
    video.tap_on_device_home_btn(browser)
    
    
@when('take the app to foreground')
def take_app_foreground(browser):
    video.take_app_foreground(browser)
    
    
@then('Verify timer Video should start playing from where it has paused')
def verify_video_playing_from_last_progress(browser): 
    video.verify_video_playing_from_last_progress(browser)
    
    
@then('check the timer')
def checkTime(browser):
    pass
    




 
 
