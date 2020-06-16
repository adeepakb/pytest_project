@mobile
Feature: Video player setting Behaviour

Scenario: Verify that when the Video is playing and if the Player Layer is up on the Video, this Player Layer should disappear after 2 sec
	Given Launch the app online
	And navigate to "Biology" library chapter list screen
	When Tap on any video from chapter list screen 
	And Tap on any video from video list
	And wait for "3" secs
	Then Verify all the video player icons should disappear


Scenario: Verify on Video  Pause state  if the user taps somewhere on the Player Layer screen then the Player Layer screen should be shown and the state of the video should not change
	Given Launch the app online
	And navigate to "Biology" library chapter list screen
	When Tap on any video from chapter list screen 
	And Tap on any video from video list 
	And Taps on pause icon 
	And tap on the video player layer skin
	Then verify Player screen should be shown with out any player options


Scenario: Verify that when the Video is in Pause state and if the Player Layer is up on the Video, this Player Layer should not disappear until the user taps again on the Layer or selects any one option from the Layer
	Given Launch the app online
	And navigate to "Biology" library chapter list screen
	When Tap on any video from chapter list screen 
	And Tap on any video from video list 
	And Taps on pause icon
	Then Verify the player layer is up and it should not disappear i.e all the options should be visible