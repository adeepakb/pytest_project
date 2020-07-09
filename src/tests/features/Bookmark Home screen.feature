Feature: Bookmark Home screen

Scenario: Verify that tapping on bookmarks option on hamburger menu should navigate user to bookmarks screen
	Given Launch the app online
	And User is in Hamburger menu
	When User taps on "Bookmarks" option
	Then Verify that user should  navigate to Bookmarks Screen


Scenario: Verify the elements on bookmark home screen
	Given Launch the app online
	And User is in Hamburger menu
	When User taps on "Bookmarks" option
	Then Verify that user should  navigate to Bookmarks Screen
	And Verify that app back button at the top left corner of the screen should be present
	And verify "No Bookmarks" text
	And Verify "Filter" option
	And Verify  "All" text  followed by Subjects tab

Scenario: Verify that the page with no bookmark message should be displayed when there are no bookmarks in bookmark screen.
	Given Launch the app online
	And Navigate to bookmark home screen
	And Remove existing bookmarks
	When Check for bookmarked content
	Then verify "No Bookmarks" message should be shown when there are no bookmarks


Scenario: Verify that once the user bookmark any video then in the bookmark home screen "No bookmark" message should be replaced by the bookmarked contents
	Given Launch the app online
	And navigate to home screen
	When Bookmark any video
	And navigate back to bookmark screen
	Then verify bookmark  is present
	And verify "No Bookmarks" message not shown in all tab


Scenario: Verify that user should be able to switch between the tabs
	Given Launch the app online
	When navigate to bookmark home screen
	Then Tap on "Mathematics" subject
	And Verify that user should navigate to "Mathematics" tab
	And tap on "Physics" subject
	And Verify that user should navigate to "Physics" tab
	And tap on "Chemistry" subject
	And Verify that user should navigate to "Chemistry" tab
	And tap on "Biology" subject
	And Verify that user should navigate to "Biology" tab
	And tap on "History" subject
	And Verify that user should navigate to "History" tab
	Then tap on "Civics" subject
	And Verify that user should navigate to "Civics" tab
	Then tap on "Geography" subject
	And Verify that user should navigate to "Geography" tab

Scenario: Verify that if the user tap on app  back button in bookmark home screen user should  navigate back to home screen
	Given Launch the app online
	And Navigate to bookmark home screen
	When tap on app back button
	Then Verify that user should navigate to home screen

Scenario: Verify that if the user tap on device back button in bookmark home screen user should  navigate back to home screen
	Given Launch the app online
	And Navigate to bookmark home screen
	When tap on device back button
	Then Verify that user should navigate to home screen

#Scenario: Verify that tapping on bookmark tab under More Menu should navigate to bookmark home screen.
#	Given Launch the app
#	And Navigate to Home screen.
#	And tap on More Menu on the bottom navigation bar.
#	When Tap on Bookmark tab
#	Then Should be navigated to Bookmark home screen.
#
#
#Scenario: Verify that tapping on app back button in bookmark home screen user should  navigate back to More Menue home screen.
#	Given Launch the app
#	And Navigate to bookmark home screen
#	When Tap on app back button
#	Then Verify that user should navigate to More Menue home screen