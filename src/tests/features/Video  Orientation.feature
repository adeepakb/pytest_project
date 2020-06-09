Feature: Video  Orientation


Scenario: Verify that user should be able to play the video in both Portrait and landscape mode
	Given Launch the app online
	And navigate to "Chemistry" library chapter list screen
	When Tap on any video from chapter list screen
	And verify video is played in potrait mode
	And Tap on Landscape option in video
	Then verify video is played in landscape mode


Scenario: Verify that on changing the orientation from Portrait to landscape and Vice versa video should continue playing from the same point and should not pause
	Given Launch the app online
	And navigate to "Chemistry" library chapter list screen
	When Tap on any video from chapter list screen
	And verify video is played in potrait mode
	And Tap on Landscape option in video
	Then verify video continues to play without any interruption in landscape
	And Tap on potrait mode option in video player screen
	And verify video continues to play without any interruption in potrait


Scenario: Verify that tapping on full screen mode in Video player should continue playing the video in landscape mode
	Given Launch the app online
	And navigate to "Chemistry" library chapter list screen
	When Tap on any video from chapter list screen
	And verify video is played in potrait mode
	And Tap on Landscape option in video
	Then verify video continues to play without any interruption in landscape

Scenario: On video player screen if user taps on device back button then orientation of the video should change to Portrait mode
   Given Launch the app online
   And navigate to "Chemistry" library chapter list screen
   When Tap on any video from chapter list screen
   And Tap on Landscape option in video
   And verify video is played in landscape mode
   And Tap on device back button
   Then verify video continues to play without any interruption in potrait