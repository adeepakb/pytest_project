Feature: Premium School Home Screen


Scenario: Verify that elements in premium school home screen.
	Given post-requisite "auto-post-assessment-video" should be tagged for the particular classroom session
	And reset student session if the session is incase completed
	And Launch the app online
	When Click on the Premium school card in the home page
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
	And verify card details


Scenario: Verify that taping on app/device back navigation icon should land back on home screen.
	Given Launch the app online
	When Click on the Premium school card in the home page
	Then Tap on device/app back button
	And verify that user navigates to home screen


Scenario: Verify that taping on "get Help", quick help bottom sheet will open.
	Given Launch the app online
	When Click on the Premium school card in the home page
	Then tap on "Get help" button
	And Verify that quick help bottom sheet opens


Scenario: Verify that tap on cancel, quick help bottom sheet should go off.
	Given Launch the app online
	When Click on the Premium school card in the home page
	Then tap on "Get help" button
	And Tap on Cancel button
	And Verify that quick help bottom sheet goes off


Scenario: Verify that PS Homepage will have a "Get Help" button and two tabs: "For You" and "Completed"
	Given Launch the app online
	When Click on the Premium school card in the home page
	Then Verify Get help button
	And Verify "For you" and "Completed" tabs


Scenario: Verify that user can switch between the tabs on taping on it.
	Given Launch the app online
	When Click on the Premium school card in the home page
	Then verify that user is able to switch between "For you" and "Completed" tabs


Scenario: Verify that on switching to tab, respective cards/content should be load.
	Given Launch the app online
	When Click on the Premium school card in the home page
	Then tap on "For you" tab
	And Verify that For you tab contents are loading
	And tap on "Completed" tab
	And Verify that Completed sessions tab contents are loading