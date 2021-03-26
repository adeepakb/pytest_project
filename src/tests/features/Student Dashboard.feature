Feature: Student Dashboard

@BVT 
Scenario: verify that user should be able see For You and Completed Sessions tabs are displayed on premium school screen
	Given launch the app and navigate to home screen
	And navigate to one to mega home screen
	When verify text "Classes"
	Then verify text "For you"
	And verify text "Completed"
	And verify app back button

@BVT 
Scenario: verify that user should be able to navigate premium school screen when he/she is enrolled to one to mega subscription
	Given launch the app and navigate to home screen
	When on home screen tap on premium school card
	Then verify user is navigated one to mega home screen

@BVT 
Scenario: verify that user should able to see "You will be to join 30 mins before session start" message on tapping on feature session card
	Given launch the app and navigate to home screen
	And navigate to one to mega home screen
	When tap on tomorrow session card
	Then verify text "You will be able to join 30 mins before session start time"
	And verify text "Session Details"
	And verify subject name is displayed
	And verify topic name is displayed
	And verify calendar icon followed by date format DD MMM,Day is displayed
	And verify clock icon followed by time format HH:MM AM/PM details are displayed
	And verify topic description is displayed
	And verify get help button is displayed
	And verify app back button is displayed

@BVT 
Scenario: verify session card contains all necessary details
	Given launch the app and navigate to home screen
	And navigate to one to mega home screen
	When verify future session cards are displayed under 'For you' tab
	Then verify subject icon in session card
	And verify subject name in the session card is displayed
	And verify topic name in the session card is displayed
	And verify time details DD MMM, DAY,HH:MM AM/PM is displayed

@BVT 
Scenario: verify tapping on join now button in offline mode should display offline related message
	Given launch the app and navigate to home screen
	And navigate to one to mega home screen
	When verify future session cards are displayed under 'For you' tab
	And verify join now button is displayed on ongoing sessions
	And switch off the device wifi
	Then tap on join now button
	And verify text "You are not connected to internet. Please check your connection and try again." on bottom sheet dialog
	And verify okay button is present on offline bottom sheet dialog
	And switch on the device wifi
	And tap on okay button
	And verify offline bottom sheet dialog is dismissed

@BVT 
Scenario: verify tapping on future session cards in offline mode should display  offline related message
	Given launch the app and navigate to home screen
	And navigate to one to mega home screen
	When verify future session cards are displayed under 'For you' tab
	And switch off the device wifi
	Then tap on any future session card
	And verify text "Oops! Something went wrong"
	And verify text "Please check internet connection and try again"
	And verify Retry button
	And verify app back button

@BVT 
Scenario: verify tapping on Retry button on future session card in online mode should display the session details
	Given launch the app and navigate to home screen
	And navigate to one to mega home screen
	When verify future session cards are displayed under 'For you' tab
	And switch off the device wifi
	Then tap on any future session card
	And verify text "Oops! Something went wrong"
	And verify text "Please check internet connection and try again"
	And verify Retry button
	And switch on the device wifi
	And tap on Retry back button
	And verify session related details should be loaded on the screen

@BVT 
Scenario: verify that already completed session cards should be displayed under completed sessions tab
	Given launch the app and navigate to home screen
	And navigate to one to mega home screen
	When tap on completed tab
	Then verify completed session cards should be displayed

@BVT 
Scenario: verify that completed text should be present on the completed session cards along with the tick mark
	Given launch the app and navigate to home screen
	And navigate to one to mega home screen
	When tap on completed tab
	Then verify completed session cards should be displayed
	And verify text "Completed"
	And verify tick icon

@BVT 
Scenario: verify that on tapping on the completed session card should redirect to session details screen
	Given launch the app and navigate to home screen
	And navigate to one to mega home screen
	When tap on completed tab
	Then verify completed session cards should be displayed
	And tap on completed session card
	And verify user is navigated to session details screen

@BVT 
Scenario: verify the completed session details screen should have all the following details
	Given launch the app and navigate to home screen
	And navigate to one to mega home screen
	When tap on completed tab
	And verify completed session cards should be displayed
	And tap on completed session card
	Then verify user is navigated to session details screen
	And verify text "Session Details"
	And verify text "Completed"
	And verify topic name in the session card is displayed
	And verify time details DD MMM, DAY,HH:MM AM/PM is displayed

@BVT 
Scenario: verify that on tapping on app back button on session details screen user should land on premium School screen
	Given launch the app and navigate to home screen
	And navigate to one to mega home screen
	When tap on completed tab
	And verify completed session cards should be displayed
	And tap on completed session card
	And verify user is navigated to session details screen
	And tap on app back button
	Then verify user is landed on premium school screen
	And verify completed sessions tab is highlighted

@BVT 
Scenario: verify user should be able to see pre requisites video for tomorrow sessions
	Given launch the app and navigate to home screen
	And attach pre requisites video for tomorrow session
	And navigate to one to mega home screen
	When tap on tomorrow session card
	Then verify a video card should be shown in the session detail screen
	And verify text "Prepare for the Session"

@BVT 
Scenario: verify user should be able to see pre and post requisites in completed sessions tabs
	Given launch the app and navigate to home screen
	And attach all pre and post requisites for completed session
	And navigate to one to mega home screen
	When tap on completed tab
	And verify completed session cards should be displayed
	And tap on any completed session card
	Then verify that for completed session both pre and post requisites are displayed

@BVT 
Scenario: verify user should be able to see pre requisites assignment for tomorrow sessions
	Given launch the app and navigate to home screen
	And attach pre requisites assessment for up next session in the backend
	And navigate to one to mega home screen
	When tap on up next session card
	Then verify text "Prepare for the Session"
	And verify a test card is shown in the session detail screen

@BVT 
Scenario: verify user should be able to take pre requisites assignment for tomorrow sessions
	Given launch the app and navigate to home screen
	And attach pre requisites assessment for up next session in the backend
	And navigate to one to mega home screen
	When tap on up next session card
	Then verify and complete the assessment
	And verify user is navigated to session details screen

@BVT 
Scenario: verify user is able to play the pre requisites video
	Given launch the app and navigate to home screen
	And attach pre requisites video for up next session
	And navigate to one to mega home screen
	When tap on tomorrow session card
	Then verify a video card should be shown in the session detail screen
	And tap on the video
	And verify the video is playing
	And verify user is able to complete the video