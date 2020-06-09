Feature: video Autoplay Disabled

Scenario: Verify that if the video is first video in that sub-topic, that video should not have previous button
	Given Launch the app online
	And navigate to "Chemistry" library chapter list screen
	And Tap on any video from chapter list screen
	And Autoplay option should be  disabled for  Videos
	When Tap on first video in subtopic list screen
	And complete the video
	Then Verify that previous button should not be shown on video player screen

Scenario: Verify that if the video is last video in that sub-topic, that video should not have next button
	Given Launch the app online
	And navigate to "Chemistry" library chapter list screen
	And Tap on any video from chapter list screen
	And Autoplay option should be  disabled for  Videos
	When Tap on the last video in video list
	And complete the video
	Then Verify that Next button option should not be shown on video player screen

Scenario: Verify that once the user done watching the video, the next video should not be loaded automatically and the play icon should be replaced by replay icon  and the "Next" and "Previous" buttons should be shown on the video screen
	Given Launch the app online
	And navigate to "Chemistry" library chapter list screen
	And Tap on any video from chapter list screen
	And Autoplay option should be  disabled for  Videos
	When Tap on the second video in subtopic list screen
	And complete the video
	Then Verify that auto loading option should not be seen on video player screen
	And verify Replay icon is shown on the video player screen
	And Verify Previous button ,Next button should be displayed on video player screen

Scenario: Verify that if the user replay the video, the same video should be played from the beginning
	Given Launch the app online
	And navigate to "Chemistry" library chapter list screen
	And Tap on any video from chapter list screen
	And Autoplay option should be  disabled for  Videos
	When Tap on the last video in video list
	And complete the video
	And Tap on replay icon
	Then Verify that same video is played again


Scenario: Verify that if the user taps on "Next"[>I] icon, then the next video should start playing
	Given Launch the app online
	And navigate to "Chemistry" library chapter list screen
	And Tap on any video from chapter list screen
	And Autoplay option should be  disabled for  Videos
	When Tap on the second video in subtopic list screen
	And complete the video
	And Tap on Next icon [>|]
	Then Verify that next video is played


#Scenario: Verify that if the user taps on "Previous"[I<] icon, the previous video should be played from the beginning
#	Given Launch the app online
#	And navigate to "Chemistry" library chapter list screen
#	And Tap on any video from chapter list screen
#	And Autoplay option should be  disabled for  Videos
#	When Tap on the second video in subtopic list screen
#	And complete the video
#	And Tap on Previous icon [|<]
#	Then Verify that previous video is played