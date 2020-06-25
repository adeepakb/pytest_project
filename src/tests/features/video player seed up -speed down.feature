Feature: video player seed up -speed down


Scenario: Verify that tapping on Speed Up Speed Down icon respective options should be displayed
	Given Launch the app online
	And navigate to "Biology" library chapter list screen
	When Tap on any video from chapter list screen
	And tap on Playback speed icon
	Then Verify playback speed bottom sheet dialog is displayed
	And Verify Label "Playback Speed" is present on dialog
	And Verify Speed options "0.5x" , "0.75x" , "Normal" , "1.25x" , "1.5x" are present on dialog


Scenario: Verify that by default "Playback Speed" should be 'Normal'
	Given Launch the app online
	And navigate to "Biology" library chapter list screen
	When Tap on any video from chapter list screen
	And tap on Playback speed icon
	Then Verify by default "Normal" option should be selected in  playback speed bottom sheet dialog


Scenario: Verify that if user selects Speed option  0.75x then video should play in Speed Down which is slower than Normal speed
	Given Launch the app online
	And navigate to "Biology" library chapter list screen
	When Tap on any video from chapter list screen
	And tap on Playback speed icon
	And tap on "0.75x" option
	Then Verify the video play is speed Down compare to normal


Scenario: Verify that if user selects Speed option  0.5x then video should play in Speed Down which is slower than Normal speed
	Given Launch the app online
	And navigate to "Biology" library chapter list screen
	When Tap on any video from chapter list screen
	And tap on Playback speed icon
	And tap on "0.5x" option
	Then Verify the video play is speed Down compare to 0.75x


Scenario: Verify that if user selects Speed options 1.25x  then video should play in Speed Up which is faster than Normal speed
	Given Launch the app online
	And navigate to "Biology" library chapter list screen
	When Tap on any video from chapter list screen
	And tap on Playback speed icon
	And tap on "1.25x" option
	Then Verify the video play is speed up compare to Normal


Scenario: Verify that if user selects Speed options 1.5x  then video should play in Speed Up which is faster than Normal speed
	Given Launch the app online
	And navigate to "Biology" library chapter list screen
	When Tap on any video from chapter list screen
	And tap on Playback speed icon
	And tap on "1.5x" option
	Then Verify the video play is speed  up  compare to 1.25X


Scenario: Verify that if user selects any Speed other than 'Normal' say 1.5x speed, watches and completes the video then the next video by default should play in 'Normal' speed
	Given Launch the app online
	And navigate to "Biology" library chapter list screen
	When Tap on any video from chapter list screen
	And Autoplay option should be enbled for Videos
	And tap on Playback speed icon
	And tap on "1.5x" option
	And complete the video
	And allow to auto load the next video
	And tap on Playback speed icon
	Then Verify when Next video is played default option "Normal" should be selected


Scenario: verify user is able to see speed up and speed down option  for journey videos
	Given Launch the app online
	And navigate to "Biology" Personalised chapter list screen
	And Tap on any journey card
	When Tap on the video card
	And tap on Playback speed icon
	Then Verify playback speed bottom sheet dialog is displayed
	And Verify Label "Playback Speed" is present on dialog
	And Verify Speed options "0.5x" , "0.75x" , "Normal" , "1.25x" , "1.5x" are present on dialog


Scenario: verify user is able to see speed up and speed down option for key focus areas videos
	Given Launch the app online
	And on home screen tap on analysis icon
	When Tap on key focus area video
	And tap on Playback speed icon
	Then Verify Label "Playback Speed" is present on dialog
	And Verify Speed options "0.5x" , "0.75x" , "Normal" , "1.25x" , "1.5x" are present on dialog


Scenario: verify user is able to see speed up and speed down option for practice tackle videos
	Given Launch the app online 
	And navigate to "Biology" library chapter list screen 
	And tap on the practice card
	When Progress the practice until tackle video is shown
	And tap on Playback speed icon
	Then Verify Label "Playback Speed" is present on dialog
	And Verify Speed options "0.5x" , "0.75x" , "Normal" , "1.25x" , "1.5x" are present on dialog