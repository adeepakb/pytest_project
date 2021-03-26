Feature: Pre requisites and its resource type


Scenario: Verify the elements in premium school home page
	Given launch the app and navigate to home screen
	And last session should be ended and should not be rated
	And attach all pre and post requisites for completed session in the backend
	And attach all pre and post requisites for up next session in the backend
	And navigate to one to mega home screen
	When verify text "Classes"
	Then verify app back button
	And verify get help button
	And verify for you sessions tab is highlighted
	And verify the toggle sessions for you and completed sessions
	And verify the completed session card with all details
	And verify that for completed session both pre and post requisites are displayed
	And verify the up next session card with all details
	And verify that for up next session pre requisites are displayed
	And verify the future session card with all details


Scenario: Verify the elements in the pre-requisites card
	Given attach all pre and post requisites for up next session in the backend
	And launch the app and navigate to home screen
	And navigate to one to mega home screen
	When verify text "Classes"
	Then verify app back button
	And verify get help button
	And verify for you sessions tab is highlighted
	And verify the toggle sessions for you and completed sessions
	And verify text "PREPARE FOR THE CLASS"
	And tap on up next session card
	And verify pre requisite card details
	And verify the future session card with all details


Scenario: Verify that while clicking on app back button user should navigate to app home screen
	Given attach all pre and post requisites for up next session in the backend
	And launch the app and navigate to home screen
	And navigate to one to mega home screen
	When tap on app back button
	Then verify app home is displayed


Scenario: Verify that while clicking on Get Help button Get help screen should open
	Given attach all pre and post requisites for up next session in the backend
	And launch the app and navigate to home screen
	And navigate to one to mega home screen
	Then click on get help button and verify that user navigates to get help screen


Scenario: Verify that while clicking on device back button,user should navigate to app home screen
	Given attach all pre and post requisites for up next session in the backend
	And launch the app and navigate to home screen
	And navigate to one to mega home screen
	When tap on device back button
	Then verify app home is displayed


Scenario: Verify that while clicking on premium school user should navigate to premium school home page.
	Given attach all pre and post requisites for up next session in the backend
	And launch the app and navigate to home screen
	And navigate to one to mega home screen
	Then verify user is navigated one to mega home screen