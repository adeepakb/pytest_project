Feature: Post Requisites and its resource type


Scenario: Verify that post requisites card should shown in the "For you" tab.
	Given launch the app and navigate to home screen
	And last session should be ended and should not be rated
	And attach all post requisites for completed session
	And navigate to one to mega home screen
	When verify for you sessions tab is highlighted
	And verify completed session cards should be displayed
	Then verify post requisite is attached for completed session


Scenario: Verify that elements in the post requisites card.
	Given launch the app and navigate to home screen
	And navigate to one to mega home screen
	When verify for you sessions tab is highlighted
	And verify completed session cards should be displayed
	Then verify post requisite is attached for completed session
	And verify text "REVISION MATERIAL"
	And verify forward icons are displayed
	And verify the attached assessment is present
	And verify the attached video is present
	And verify if more then two requisites are attached "see more" option is displayed


Scenario: Verify that if the post requisite contain only 2 resource type, then "See more" should not be present on the card.
	Given attach two post requisites for completed session
	And launch the app and navigate to home screen
	And navigate to one to mega home screen
	When verify for you sessions tab is highlighted
	And verify completed session cards should be displayed
	Then verify post requisite is attached for completed session
	And verify "see more" option is not displayed if the post requisite contain only two resource type


Scenario: Verify that if the post requisites having more than 2 resource types, then "see more" should be shown on the card.
	Given attach all post requisites for completed session
	And launch the app and navigate to home screen
	And navigate to one to mega home screen
	When verify for you sessions tab is highlighted
	And verify completed session cards should be displayed
	Then verify if more then two requisites are attached "see more" option is displayed


Scenario: Verify that taping on "See more", should open in the new screen, where all the tagged resource types are shown.
	Given launch the app and navigate to home screen
	And navigate to one to mega home screen
	When verify for you sessions tab is highlighted
	And verify completed session cards should be displayed
	Then verify if more then two requisites are attached "see more" option is displayed
	And on tap of see more option
	And verify the user is navigated to the session details screen where all the tagged resource types are shown


Scenario: Verify that taping on device/app back icon, should come back and land on "For you" tab.
	Given launch the app and navigate to home screen
	And navigate to one to mega home screen
	When verify for you sessions tab is highlighted
	And verify completed session cards should be displayed
	Then on tap of see more option
	And verify user is navigated to session details screen
	And tap on app back button
	And verify for you sessions tab is highlighted
	And on tap of see more option
	And verify user is navigated to session details screen
	And tap on device back button
	And verify for you sessions tab is highlighted


Scenario: Verify that "rate session" card with "Rate now" button shown, if not rated the session post session completion.
	Given launch the app and navigate to home screen 
	And last session should be ended and should not be rated and verify feedback screen
	When verify for you sessions tab is highlighted
	Then verify rate now button is displayed


Scenario: Verify that completed card withPost requisites and not rated is the first card in the " For you" tab.
	Given launch the app and navigate to home screen
	And attach all post requisites for today session
	And last session should be ended and should not be rated
	When verify for you sessions tab is highlighted
	Then verify that completed session is the first card in the for you tab
	And verify that user is able to access all post requisites attached to the session


Scenario: Verify that taping on video resource type card, should open in the new screen and start playing the video.
	Given launch the app and navigate to home screen
	And attach pre requisites video for up next session
	And navigate to one to mega home screen
	When tap on up next session card
	Then verify a video card should be shown in the session detail screen
	And tap on the video
	And verify the video is playing
	And verify user is able to complete the video


Scenario: Verify that video can be playable in both portrait and landscape modes.
	Given launch the app and navigate to home screen 
	And navigate to one to mega home screen
	When tap on up next session card
	Then verify a video card should be shown in the session detail screen
	And tap on the video
	And verify the video is playing
	And verify that user should be able to watch video in portrait and landscape modes


Scenario: Verify that the video player should have all standard video player controls like play/pause, seek bar.
	Given launch the app and navigate to home screen 
	And navigate to one to mega home screen
	When tap on up next session card
	Then verify a video card should be shown in the session detail screen
	And tap on the video
	And verify the video is playing
	And verify all video player elements