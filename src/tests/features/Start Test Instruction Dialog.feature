Feature: Start Test Instruction Dialog


Scenario: Verify that when tap on start test for the first time, should show "test instructions" popup.
	Given post-requisite "auto-post-assessment-video" should be tagged for the particular classroom session
	And launch the application and navigate to home screen
	When tap on premium card
	Then navigate to one to mega homescreen
	And verify the user is navigated to the PS screen
	And verify that in the For you tab, post requisite card is present
	And verify "See more" option is not displayed if the post requisite contain only 2 resource type
	And tap on "Start Now" for the assessment added
	And verify that it should show "Test Instructions" popup


Scenario: Verify that on start instruction pop up following text message should be displayed
	Given launch the application and navigate to home screen
	When tap on premium card
	Then navigate to one to mega homescreen
	And verify that in the For you tab, post requisite card is present
	And tap on "Start Now" for the assessment added
	And verify that it should show "Test Instructions" popup
	And verify the text "No marks will be awarded for unattempted questions or incorrect answers"
	And verify the text "There are multiple questions with different marking schemes"
	And verify the text "Save or mark questions to attempt later"
	And verify "Start" button is displayed


Scenario: Verify that taping on cancel icon, test instructions dialog should go off.
	Given launch the application and navigate to home screen
	When tap on premium card
	Then navigate to one to mega homescreen
	And verify that in the For you tab, post requisite card is present
	And tap on "Start Now" for the assessment added
	And verify that it should show "Test Instructions" popup
	And verify that on pop up close icon is displayed
	And verify on tap of the close icon pop up should close


Scenario: Verify that taping on "Start", should open the test in web.
	Given launch the application and navigate to home screen
	When tap on premium card
	Then navigate to one to mega homescreen
	And tap on "Start Now" for the assessment added
	And tap on "Start" button
	And verify that open the test on the web


Scenario: Verify that based on the result date given results should be shown
	Given verify available until date should be set on tllms backend for assessment tagged
	launch the application and navigate to home screen
	When tap on premium card
	Then navigate to one to mega homescreen
	And verify the user is navigated to the PS screen
	And verify that in the For you tab, post requisite card is present
	And verify the text "Available till {date}"


Scenario: Verify that if assessment end time is completed "Expire" message should be shown
	Given set expired assessment end time in tllms
	launch the application and navigate to home screen
	When tap on premium card
	Then navigate to one to mega homescreen
	And verify the user is navigated to the PS screen
	And verify that in the For you tab, post requisite card is present
	And verify the text "Expired"
	And reset back assessment end date


Scenario: Verify that if start time for the assessment is not reached then following text message should be displayed
	Given set the start time which is not reached for the assessment
	launch the application and navigate to home screen
	When tap on premium card
	Then navigate to one to mega homescreen
	And verify the user is navigated to the PS screen
	And verify that in the For you tab, post requisite card is present
	And tap on "assessment" link
	And verify the text "This assessment is not available currently. Check back at {date}"


Scenario: Verify that start button should be disabled based on the timing
	Given launch the application and navigate to home screen
	When tap on premium card
	Then navigate to one to mega homescreen
	And verify the user is navigated to the PS screen
	And verify that in the For you tab, post requisite card is present
	And verify that if the assessment time is not reached to session time then "Start Now" link should not be visible
	And reset assessment start date as today


Scenario: Verify that taping on resume, should resume the test from where it is paused.
	Given launch the application and navigate to home screen
	When tap on premium card
	Then navigate to one to mega homescreen
	And verify the user is navigated to the PS screen
	And tap on "Start Now" for the assessment added
	And tap on "Start" button
	And tap on Start Assessment button
	And take screenshot of assessment "Image1"
	And tap on device back button
	And verify the user is navigated to the PS screen
	And tap on "Resume" link
	And tap on Continue Assessment button
	And take screenshot of assessment "Image2"
	And compare both images "Image1" and "Image2" to verify user is able to continue with the assessment where the user was paused


Scenario: Verify that taping on resume, test instruction dialog should not be shown again.
	Given launch the application and navigate to home screen
	When tap on premium card
	Then navigate to one to mega homescreen
	And verify the user is navigated to the PS screen
	And tap on "Resume" link
	And tap on Continue Assessment button
	And verify start test instruction dialogue should not be shown


Scenario: Verify that if user quit the test in the middle and come back to PS home screen, then on assessment card "Resume" should be replaced with "Start" button.
	Given launch the application and navigate to home screen
	When tap on premium card
	Then navigate to one to mega homescreen
	And tap on "Resume" link
	And the user is able to continue with the assessment


Scenario: Verify that after the end of the test, on the assessment card, score should be shown.
	Given launch the application and navigate to home screen
	When tap on premium card
	Then navigate to one to mega homescreen
	And tap on "Resume" link
	And tap on Continue Assessment button
	And end the test
	And tap on "View Results" link
	And verify that score should be shown