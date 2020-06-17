
Feature: Library chapter list screen


Scenario: Verify that tapping on app back arrow should redirect the user to home screen.
	Given Launch the app online 
	And User is in Personalized Chapter list screen
	When User taps on app back button
	Then Verify that user should be navigate to home screen


Scenario: Verify the fields in library chapter list  screen
	Given Launch the app online
	When User is in Library Chapter list screen
	Then Verify the App back button on top left corner of the screen
	And Personalized button along with the text "personalized" at the top right of the screen.
	And Search button should be shown next to personalized button.
	And Subject Name followed by number of Videos and Tests
	And Below the top layout, a label Chapters and list of chapters(Library carousel) below it


Scenario: Verify that personalized button in the Library mode should change to library button, when user switches to personalized mode
	Given Launch the app online
	When User is in Library Chapter list screen
	And User taps on personalized button
	Then Verify that user switches to personalized mode chapter list screen


Scenario: Verify the fields in video carousel of library chapter list screen
	Given Launch the app online
	When User is in Library Chapter list screen
	Then Verify that chapter name and total number of video count
	And Video card with video thumbnail and Video Progression below the video thumbnail
	And Test Button and Practice Button


Scenario: Verify that each chapter in the subject should have video carousel in Library chapter list screen.
	Given Launch the app online
	When User is in Library Chapter list screen
	Then Verify that each chapter in the subject should have video carousel in Library chapter list screen.


Scenario: Verify that tapping on Video card in chapter list screen should navigate the user to video list screen of that particular chapter
	Given Launch the app online
	When User is in Library Chapter list screen
	And User taps on video card in Library chapter list screen of particular chapter
	Then Verify that user should be navigates to video list screen of particular topic


Scenario: Verify that tapping on test button should redirect the user to test list screen of that particular chapter.
	Given Launch the app online
	When User is in Library Chapter list screen
	And User taps on test button on library chapter list screen of particular chapter
	Then Verify that user should be navigates to test list screen of particular topic


Scenario: Verify that tapping on practice button should redirect the user to practice screen of that particular chapter
	Given Launch the app online
	When User is in Library Chapter list screen
	And User taps on practice button on library chapter list screen of particular chapter
	Then Verify that user should be navigates to practice list screen of particular topic


Scenario: Verify that tapping on app back arrow should redirect the user to home screen
	Given Launch the app online
	When User is in Library Chapter list screen
	And User taps on back button on library chapter list screen
	Then Verify that user should be navigate to home screen


Scenario: Verify that tapping any subject on home screen should navigate to library chapter list screen,if it is set to library mode .
	Given Launch the app online
	When User is in Library Chapter list screen
	And User taps on back button on library chapter list screen 
	And User taps on same subject card
	Then Verify that user should be navigate to library chapter list screen