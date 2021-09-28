Feature: Monthly Test


Scenario: Verify that student should be able to take the test at regular session time
	Given launch the app and navigate to home screen
	And navigate to one to mega home screen
	When Verify that the test session card should be present
	Then Verify that monthly test start button should be enabled at exact session time
	And verify that user should be able to take test at session time


Scenario: Verify the assessment card UI
	Given The session should be converted to a unit test
	And login as user with unit test scheduled
	And navigate to byju's classes home screen
	Then Verify that the title of the test(unit test/monthly test) should be present
	And verify the date and time format


Scenario: Verify the session card at the assessment start time
	Given The session should be converted to a unit test
	And login as user with unit test scheduled
	And navigate to byju's classes home screen
	When Verify that the test session card should be present
	Then Verify that the title of the test(unit test/monthly test) should be present
	And verify that the session topic should be present
	And verify the date and time format
	And verify that the test icon should be present
	And verify that the text "Good luck for the test" should be present
	And verify that the "Start" button should be present


Scenario: Verify the instruction screen upon click start button
	Given The session should be converted to a unit test
	And login as user with unit test scheduled
	And navigate to byju's classes home screen
	When the user is in For you Tab
	Then click on "Start Test" button and verify user landed on instruction screen


Scenario: Verify the start button in instruction screen
	Given The session should be converted to a unit test
	And login as user with unit test scheduled
	And navigate to byju's classes home screen
	When the user is in For you Tab
	Then click on "Start Test" button and verify user landed on instruction screen
	And verify "Start" button is displayed on instruction screen


Scenario: Verify the text displayed on the start assessment card at the test time
	Given The session should be converted to a unit test
	And navigate to byju's classes home screen
	When Verify that the test session card should be present
	And the user is in For you Tab
	And click on test session card
	And verify session details page is displayed
	Then Verify that the text "Good luck for your test" should be displayed in details screen
	And verify that the "Start Test" button should be present in details screen


Scenario: Verify the exit assessment button in assessment screen
	Given The session should be converted to a unit test
	And login as user with unit test scheduled
		And navigate to byju's classes home screen
	When the user is in For you Tab
		And Verify that the test session card should be present
		And click on "Start Test" button
		And user starts assessment and land on final question
	Then Verify the exit assessment button on the final screen


Scenario: Verify the elements in assessment screen
	Given The session should be converted to a unit test
		And login as user with unit test scheduled
		And navigate to byju's classes home screen
	When the user is in For you Tab
		And Verify that the test session card should be present
		And click on "Start Test" button
	Then verify elements in assessment screen


Scenario: Verify the session card after the student comes out of the session while it's in progress
	Given The session should be converted to a unit test
		And login as user with unit test scheduled
		And navigate to byju's classes home screen
	When click on "Start Test" button
	And user starts assessment and land on final question
		And press back and land on student dashboard screen
	Then verify that "Resume" button is displayed on the screen


Scenario: Verify the confirmation pop up while submitting the assessment
	Given The session should be converted to a unit test
	    And login as user with unit test scheduled
	    And navigate to byju's classes home screen
	When click on "Start Test" button
	    And user starts assessment and land on final question
	Then Verify the exit assessment button on the final screen
	    And tap on exit assessment and verify confirmation pop up


Scenario: Verify the session card after the session is over without student taking the assessment
	Given The masterclass session should be converted to a monthly test for 3+1 user
	And navigate to byju's classes home screen
	When user should not attend the test
	And test session should be ended 
	And expire the test session from the backend
	Then #	todo:doubt
	verify "Not Attempted" text should be displayed
		And verify text "Test Expired. It was supposed to be taken during session time" should be displayed


Scenario: Verify the session card after exiting the session without submitting the assessment
	Given The session should be converted to a unit test
		And login as user with unit test scheduled
		And navigate to byju's classes home screen
	When the user is in For you Tab
		And Verify that the test session card should be present
		And click on "Start Test" button
		And user starts assessment and land on final question
	Then press back and land on student dashboard screen
		And verify that "Resume" button is displayed on the screen


Scenario: Verify that Start button should not be enabled until the time of the assessment.
	Given The session should be converted to a monthly test for ps user 1
	    And navigate to byju's classes home screen
	When Verify that the test session card should be present
	Then verify that "Start Test" button should not be enabled for the assessment


Scenario: Verify that "Start" button highlighted automatically at the start time
	Given The session should be converted to a monthly test for ps user 1
	#    todo: setup the job
	    And login post the "available_starting" time
	    And navigate to byju's classes home screen
	When click on test session card
	    And Verify that the "Start Test" button should be enabled automatically in the session card
	Then verify that the text "Good luck for the test" should be present
	    And verify that the "Start" button should be present
	    And click on "Start Test" button and verify user landed on instruction screen


Scenario: Verify the session card after student has finished the assessment and session has ended
	Given The session should be converted to a monthly test for ps user 1
	  And Precondition : "send_results_at" is set to the past date
	  And navigate to byju's classes home screen
	When Verify that the test session card should be present
	  And verify that student has completed the session
	  And verify that session has reached end time
	Then verify text "Check your performance" should be displayed
	  And verify that the "Results" button should be displayed
	  And verify that the session card is moved to completed tab


Scenario: Verify that if user as quit the assessment in between on app and user should be allowed to take the assessment on any other platform
	Given The session should be converted to a unit test
		And navigate to byju's classes home screen
	When the user is in For you Tab
		And Verify that the test session card should be present
		And click on "Start Test" button
		And user starts assessment and land on final question
		And quit the assessment in between on app
		And take the assessment on the web
	Then test status should be in Resume state


Scenario: Verify that when internet is turned off while taking the test assessment,status should be changed to resume
	Given The session should be converted to a unit test
		And login as user with unit test scheduled
		And navigate to byju's classes home screen
	When the user is in For you Tab
		And Verify that the test session card should be present
		And click on "Start Test" button
	Then Verify that when the internet is turned off while taking the test assessment
		And verify that status should be changed to resume


Scenario: Verify the test submission status when internet is turned off.
	Given The session should be converted to a unit test
		And login as user with unit test scheduled
		And navigate to byju's classes home screen
	When the user is in For you Tab
		And Verify that the test session card should be present
		And click on "Start Test" button
	Then submit the assessment in offline
		Then Verify that internet error message is displayed


Scenario: Verify that when post requisites are not available results button should be shown on for you tab
	Given The session should be converted to a monthly test with no post requisite for ps user 1
	     And Precondition : "send_results_at" is set to the past date
	     And navigate to byju's classes home screen
	When Verify that the test session card should be present
	Then verify that the "Results" button should be displayed


Scenario: Verify the session card after student has finished the assessment before session end
	Given The session should be converted to a monthly test for ps user 1
	  And navigate to byju's classes home screen
	When Verify that the test session card should be present
	  And verify that student has completed the session
	  And verify that session has reached end time
	Then #  todo: implement this step below 
	verify text "Your test is completed. We are working on results" is displayed


Scenario: verify the  test requisite type Unit Test/ Monthly Test/ Half Yearly Test
	Given launch the application online
	When click on the hamburger menu
	  And tap on byjus classes card
	Then verify the user is navigated to the PS screen
	  And tap on "Join Now" button
	  And user completes the session
	  And tap on "Okay" button
	  And tap on back navigation icon 
	verify that user should get autobook option