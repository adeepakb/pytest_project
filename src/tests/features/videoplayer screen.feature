Feature: videoplayer screen


Scenario: Verify all elements  should be Present in Video Landscape Mode when video is playing
	Given Launch the app online
	And navigate to "Chemistry" library chapter list screen
	When Tap on any video from chapter list screen
	And Verify video should be played
	And change the video orentation from portrait to Landscape by tapping on  landscape icon
	Then Verify App back arrow is present  on the top left corner of the screen
	And verify Speed Up Speed Down icon on video player screen
	And verify Subtitle icon on video player screen
	And verify Multiple Audio track icon on video player screen
	And verify Setting icon on video player screen
	And verify Play/Pause icon in the middle of the Player.
	And verify Fast Forward and Fast Rewind icon on the left and right side of Play/Pause icon with 10s notation.
	And verify Seek bar in between Start and End Timer at the bottom of the Player.
	And verify Full screen mode icon next to End timer.


Scenario: Verify that when Video is in Paused state Pause icon should be Replaced with Play icon in Landscape/Portrait Mode
	Given Launch the app online
	And navigate to "Chemistry" library chapter list screen
	When Tap on any video from chapter list screen
	And Verify video should be played
	And change the video orentation from portrait to Landscape by tapping on  landscape icon
	And tap on Pause icon
	Then Verify that when video is in paused state pause icon should be replaced with play icon in video player screen