Feature: Completed Sessions


Scenario: Verify that The completed tab will contain all the past sessions of the student (joined or not joined)
	Given launch the app and navigate to home screen
	And navigate to one to mega home screen
	When tap on completed tab
	And verify text "Completed"
	Then verify tick icon
	And verify date details DD MMM is displayed


Scenario: Verify the elements in the completed sessions tab
	Given launch the app and navigate to home screen
	And navigate to one to mega home screen
	When tap on completed tab
	And verify app back button is displayed
	And verify get help button is displayed
	And verify text "Classes"
	And verify completed session cards should be displayed
	Then verify subject icon in session card
	And verify subject name in the session card is displayed
	And verify topic name in the session card is displayed
	And verify date details DD MMM is displayed


Scenario: Verify that while clicking on the completed card ,user should navigate to session details screen
	Given launch the app and navigate to home screen
	And navigate to one to mega home screen
	When tap on completed tab
	Then verify completed session cards should be displayed
	And tap on completed session card
	And verify user is navigated to session details screen


Scenario: Verify that recently completed session should be shown first in order
	Given launch the app and navigate to home screen
	And navigate to one to mega home screen
	When tap on completed tab
	Then verify completed session cards should be displayed
	And verify that recently completed session should be shown first in order


Scenario: Verify that while clicking on app back button/device back button user should navigate to premium school home page
	Given launch the app and navigate to home screen
	And navigate to one to mega home screen
	When tap on completed tab
	And tap on app back or device back button
	Then verify that user navigates to premium school home page


Scenario: Verify that user should be able to access all post requisites  in completed tab which is attached to session
	Given launch the app and navigate to home screen
	And attach all post requisites for completed session
	And navigate to one to mega home screen
	When tap on completed tab
	And verify completed session cards should be displayed
	Then verify post requisite is attached for completed session
	And verify that user is able to access all post requisites attached to the session