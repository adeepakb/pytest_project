@mobile
Feature: Videoplayer

Scenario: Verify that tapping on pause icon on the Video player should pause the current playing Video
	Given Launch the app online
	And navigate to "Physics" library chapter list screen
	When Tap on any video from chapter list screen
	And verify video starts playing
	And user taps on pause icon
	Then verify video should be paused


Scenario: Verify that video continues to play when tapped on resume button
	Given Launch the app online
	And navigate to "Physics" library chapter list screen
	When Tap on any video from chapter list screen
	And Tap on any video from the video list screen
	And Verify video should be played
	And user taps on pause icon
	And verify video should be paused
	And tap on play icon
	Then verify video should be played

Scenario: Verify that on tapping on  right side 10 secs button,it should forward the video to 10 secs
	Given Launch the app online
	And navigate to "Chemistry" library chapter list screen
	When Tap on any video from chapter list screen
	And Tap on any video from the video list screen
	And Verify video should be played
	And tap on right side 10secs button
	Then Verify video should get 10 secs forward from the current time


Scenario: Verify that on tapping on  Left side 10 secs button,it should backward  the video to 10 secs
	Given Launch the app online
	And navigate to "Chemistry" library chapter list screen
	When Tap on any video from chapter list screen
	And Verify video should be played
	And  wait for the video to complete playing "20" secs
	And tap on left side 10secs button
	Then Verify video should get 10 secs backward from the current time

#Scenario: Verify that when Video is playing if user backgrounds the app the Video should pause
#	Given Launch the app online
#	And navigate to "Physics" library chapter list screen
#	When Tap on any video from chapter list screen
#	And Verify video should be played
#	And tap on device HomeButton
#	And take the app to foreground
#	Then verify video should be paused
#
#
#Scenario: Verify that Video should start playing from the same point where it was paused
#	Given Launch the app online
#	And navigate to "Physics" library chapter list screen
#	When Tap on any video from chapter list screen
#	And Verify video should be played
#	And tap on device HomeButton
#	And take the app to foreground
#	And verify video should be paused
#	And tap on play icon
#	Then Verify timer Video should start playing from where it has paused


#Scenario: Verify that video should start playing after connecting back the device to wifi/data
#	Given Launch the app online
#	And navigate to physics Library chapter list screen
#	When Tap on any video card
#	And while video starts playing disconnect the device wifi/data
#	And verify that  "Please connect to the network and try again " toast message is displayed
#	And connect back the device to wifi/data
#	Then Verify that video should start playing after connecting back the device to wifi/data