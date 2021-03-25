Feature: Premium School Home Screen


Scenario: Verify that elements in premium school home screen.
	Given post-requisite "auto-post-assessment-video" should be tagged for the particular classroom session
	reset student session if the session is incase completed
	And Launch the app online
	When Click on the Premium school card in the home page
	And navigate to one to mega homescreen
	Then Verify App back button on left hand side of the screen
	And Verify Get help button
	And Verify the text "Classes"
	And Verify "For you" and "Completed" tabs
	And Verify that "For you" tab is highlighted by default
	And tap on "Completed" tab
	And Verify the completed session card along with Subject Name, topic Name and the text "Completed" with date and the session rating given by the user in stars followed by the numeric
	And Verify the text "REVISION MATERIAL"
	And Verify the Video card along with Video Name "K12 video" and the text "Video" along with Video icon and forward Arrow button
	And Verify that "assessment" shown in the prerequisites card
	And tap on "For you" tab
	And Verify that "Up Next" Badge on top right hand side of the screen
	And verify "Join now" button
	And Verify the text "Session started"
	And Verify the text "Don’t miss the learning"
	And verify card details