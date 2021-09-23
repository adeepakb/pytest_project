Feature: 3+1


Scenario: Verify that for Regular classes that are scheduled for the student for which student can't change topic of the class
	Given launch the app online as 3+1 user and navigate to home screen
	When tap on premium school card
	Then verify that the classroom screen consists of "For You" tab
	And verify that for mandatory session user should not be able to change the topic


Scenario: Verify that tutor classroom should consist of following elements
	Given launch the app online as 3+1 user and navigate to home screen
	When tap on premium school card
	Then verify that the classroom screen consists of "For You" tab
	And verify "For you" and "Completed" tabs
	And verify that in "For you" tab both mandatory and optional session is displayed


Scenario: Verify that the revision session consist of following elements
	Given launch the app online as 3+1 user and navigate to home screen
	When tap on premium school card
	Then verify that the classroom screen consists of "For You" tab
	And verify that in "For you" tab both mandatory and optional session is displayed
	And verify in "Up next" tab the revision topic should be displayed with tag "SELECT A TOPIC"
	And verify date and time is displayed
	#And verify "+" icon is present
	And verify back icon is present


Scenario: Verify that revision topic consist of fixed date and time
	Given launch the app online as 3+1 user and navigate to home screen
	When tap on premium school card
	Then verify that the classroom screen consists of "For You" tab
	And verify that in "For you" tab both mandatory and optional session is displayed
	And verify the revision session consist of both fixed date, time and date-time format


Scenario: Verify that on tap of revision session user is navigated to session details screen
	Given launch the app online as 3+1 user and navigate to home screen
	When tap on premium school card
	Then verify that the classroom screen consists of "For You" tab
	And verify that in "For you" tab both mandatory and optional session is displayed
	And tap on revision session
	And verify that the session details screen consist of text "Session Details"


Scenario: Verify session details consist of following elements
	Given launch the app online as 3+1 user and navigate to home screen
	When tap on premium school card
	Then verify that the classroom screen consists of "For You" tab
	And verify that in "For you" tab both mandatory and optional session is displayed
	And tap on revision session
	And verify that the session details screen consist of text "Session Details"
	And verify text "Select A Topic"
	And verify text "Extra Personalised Session"
	And verify "date" is displayed with the calendar icon
	And verify "time" is displayed with the timestamp
	And verify text "Choose your topic"
	And verify text "Select a topic to continue learning"
	And verify forward icon
	And verify back icon is present


Scenario: Verify that on tap of choose topic card user is navigated to choose topic screen successfully
	Given launch the app online as 3+1 user and navigate to home screen
	When tap on premium school card
	Then verify that the classroom screen consists of "For You" tab
	And verify that in "For you" tab both mandatory and optional session is displayed
	And tap on revision session
	And verify that the session details screen consist of text "Session Details"
	And verify text "Choose your topic"
	And tap on choose topic card user is navigated to choose the topic screen


Scenario: Verify that the choose topic screen should consist of following elements
	Given launch the app online as 3+1 user and navigate to home screen
	When tap on premium school card
	Then verify that the classroom screen consists of "For You" tab
	And verify that in "For you" tab both mandatory and optional session is displayed
	And tap on revision session
	And verify that the session details screen consist of text "Session Details"
	And verify text "Choose your topic"
	And tap on choose topic card user is navigated to choose the topic screen
	And verify choose topic screen consist of the topic list with radio button
	And verify "Done" button is present
	And verify back icon is present
	And tap on back icon user is navigated to session details screen


Scenario: Verify that revision session should not be displayed on completed session
	Given launch the app online as 3+1 user and navigate to home screen
	When tap on premium school card
	Then verify that the classroom screen consists of "For You" tab
	And verify that in "For you" tab both mandatory and optional session is displayed
	And tap on device back button
	And tap on "Completed" tab
	And verify revision session not booked is not displayed in a completed session tab


Scenario: Verify that For any revision session the list of topics to be selected from should contain topics which are mandatory && occurred in past
	Given launch the app online as 3+1 user and navigate to home screen
	When tap on premium school card
	Then verify that the classroom screen consists of "For You" tab
	And verify that in "For you" tab both mandatory and optional session is displayed
	And find latest mandatory topic
	And tap on revision session
	And verify that the session details screen consist of text "Session Details"
	And tap on choose topic card user is navigated to choose the topic screen
	And verify that topic list consist of topics which are mandatory && occurred in past


Scenario: Verify that selected topic should display on revision session
	Given launch the app online as 3+1 user and navigate to home screen
	When tap on premium school card
	Then verify that the classroom screen consists of "For You" tab
	And verify that in "For you" tab both mandatory and optional session is displayed
	And tap on revision session
	And verify that the session details screen consist of text "Session Details"
	And tap on choose topic card user is navigated to choose the topic screen
	And select first topic from the list
	And tap on "Done" button
	And verify in "For you" tab the revision topic should be displayed with tag "EXTRA SESSION"
	And verify "date" is displayed with the calendar icon
	And verify "time" is displayed with the timestamp


Scenario: Verify that session details screen consist of following elements after extra session is booked
	Given launch the app online as 3+1 user and navigate to home screen
	When tap on premium school card
	Then verify that the classroom screen consists of "For You" tab
	And tap on booked revision class
	And verify "date" is displayed with the calendar icon
	And verify "time" is displayed with the timestamp
	And verify text "Change Your Topic"
	And verify the selected topic summary is displayed


Scenario: Verify that user can change the revision topic n times within the freeze period
	Given launch the app online as 3+1 user and navigate to home screen
	When tap on premium school card
	Then verify that the classroom screen consists of "For You" tab
	And tap on booked revision class
	And verify text "Change Your Topic"
	And verify that within the freeze period the user is able to change the revision topic