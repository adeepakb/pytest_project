from pytest_bdd import scenarios, given, when, then, parsers
from POM_Pages.videopage import VideoPage
from Utilities.BasePage import BaseClass

driver = fixture = 'driver'
baseClass = BaseClass()
video = VideoPage(driver)

count = False


"""storing the feature file name"""
featureFileName = "Videoplayer"

# baseClass.setupLogs(featureFileName)

"""scenario is initialized so no need to give feature file name each time in @scenario annotation"""
scenarios('../features/'+featureFileName+'.feature')


@given("Launch the app online")
def launchAppOnline(driver):
    # global count
    # count = video.login_the_user(driver, count)
    pass
    

@given(parsers.parse('Navigate to "{text}" library chapter list screen'))
def navigateToHomeScreen(driver,text): 
    video.navigate_to_home_screen(driver,text) 
    video.navigate_to_library(driver,text)


@when('Verify video should be played')
@then('Verify video should be played')
def video_should_played(driver):
    video.video_should_played(driver)
 
 
@then('verify video should be played')
def Video_should_played(driver):
    video.Video_should_played(driver) 
   
   
@when('Tap on any video from chapter list screen')
def tapOnAnyVideo(driver): 
    video.tap_on_any_video_in_sub_screen(driver)


@given('Tap on any video from chapter list screen')
def tapOnAnyVideo1(driver): 
    video.tap_on_any_video_in_sub_screen(driver)
    
    
@when('Tap on any video from the video list screen')
def tap_on_video_from_video_list(driver):
    video.tap_on_video_from_video_list(driver)


@then('Verify Video should start playing')   
@when('verify video starts playing')
def verify_video_playing(driver): 
    video.verify_video_playing(driver)


@when('user taps on pause icon')
def enterUnregistedNum3(driver): 
    video.tap_on_pause_btn(driver)
    
    
@then('verify video should be paused')
@when('verify video should be paused')
def verifyVideoStoppedPlaying(driver): 
    video.verify_video_paused(driver)
    
    
@when('tap on play icon')
def tap_on_playbtn(driver):
    video.tap_on_playbtn(driver)
    
    
@then('Verify video should get 10 secs backward from the current time')
@then('Verify video should get 10 secs forward from the current time')
def verify_frwd_10sec(driver): 
    pass


@when('tap on right side 10secs button')
def verify_frwd_10Sec(driver):
    video.verify_frwd_10Sec(driver)
    
    
@when(parsers.parse('wait for the video to complete playing "{text}" secs'))
def wait10Sec(text):
    video.custom_wait(text)
    
    
@when('tap on left side 10secs button')
def verify_video_backwrd_10Sec(driver):
    video.verify_video_backwrd_10Sec(driver)
    
    
@when('tap on device HomeButton')
def tap_on_device_home_btn(driver):
    video.tap_on_device_home_btn(driver)
    
    
@when('take the app to foreground')
def take_app_foreground(driver):
    video.take_app_foreground(driver)
    
    
@then('Verify timer Video should start playing from where it has paused')
def verify_video_playing_from_last_progress(driver): 
    video.verify_video_playing_from_last_progress(driver)
    
    
@then('check the timer')
def checkTime(driver):
    pass
    




 
 
