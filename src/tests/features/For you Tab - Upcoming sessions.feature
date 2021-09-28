Feature: For you Tab - Upcoming sessions


Scenario: Verify that For You tab will contain the last completed session's card and next 6 (14 for 11-12th) upcoming sessions for the user.
	Given last session should be ended and should not be rated
	When verify for you sessions tab is highlighted
	And verify text "Completed"
	Then verify that the "For You" tab will contain the next 6 (14 for 11-12th) upcoming sessions for the user


Scenario: Verify that the last completed session card and 1 upcoming card will be in expanded state in the "For You" tab to show post requisite and pre-requisite respectively
	Given last session should be ended and should not be rated
	And attach all post requisites for completed session
	And navigate to one to mega home screen
	When verify for you sessions tab is highlighted
	And verify completed session cards should be displayed
	Then verify if more then two requisites are attached "see more" option is displayed
	And verify that for completed session post requisite is displayed
	And tap on app back button
	And attach all pre requisites for up next session
	And navigate to one to mega home screen 
	
	And verify up next session is displayed
	And verify if more then two requisites are attached "see more" option is displayed
	And verify that for up coming session pre requisite are displayed


Scenario: Verify that if Last Session has Post Requisites and Last Session is Not Rated then should Show Last completed session card in "For You" Screen with Post requisites and "Ratings Stars"
	Given last session should be ended and should not be rated
	And attach all post requisites for completed session
	And navigate to one to mega home screen
	When verify for you sessions tab is highlighted
	And verify completed session cards should be displayed
	And verify post requisite is attached for completed session
	Then verify that rate now the card is displayed
	And verify text "Rate Your Session" is displayed
	And verify text "Let us know your experience" is displayed


Scenario: Verify that if Last Session has Post Requisites and Last Session is Rated then  should Show Last completed session card in "For You" Screen with Post requisites and show rating provided by the user on the card.
	Given last session should be ended and should be rated
	And attach all post requisites for completed session
	And navigate to one to mega home screen
	When verify for you sessions tab is highlighted
	And verify completed session cards should be displayed
	Then verify post requisite is attached for completed session
	And verify for completed session rated count is displayed
	And verify date, subject name and completed text should be displayed


Scenario: Verify that if Last Session has no Post Requisites and Last Session is Rated then should not show the last session card in "For You" Section
	Given last session should be ended and should be rated
	And delete requisite attachment
	And navigate to one to mega home screen
	And verify that in "For you" tab last completed session should not be displayed
	When tap on completed tab
	Then verify completed tab is highlighted
	And verify that the last completed session should be displayed in the "Completed session" tab
	And verify date, subject name and completed text should be displayed


Scenario: Verify that if Last Session has no Post Requisites and Last Session is Not Rated then should Show Last completed session card in "For you" screen with "Ratings Star" Options.
	Given last session should be ended and should not be rated
	And delete requisite attachment
	And launch the app and navigate to home screen
	And navigate to one to mega home screen
	When verify for you sessions tab is highlighted
	And verify completed session cards should be displayed
	Then verify that rate now the card is displayed
	And verify text "Rate Your Session" is displayed
	And verify text "Let us know your experience" is displayed