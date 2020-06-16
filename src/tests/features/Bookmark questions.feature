@mobile @tab
Feature: Bookmark questions


Scenario: Verify the elements of bookmarked questions from test
	Given Launch the app online and navigate to Home screen
	And Navigate to "Chemistry" library screen
	And Bookmark a question
	When Navigate to bookmark home screen
	Then Verify that bookmarked question should be present in Bookmark home screen under All tab
	And Verify below that chapter name and "Chemistry" subject name
	And Verify the bookmark icon on bookmark home screen
	And Verify that bookmarked question should be present under "Chemistry" tab
	And Verify below that chapter name and "Chemistry" subject name on bookmark subject screen
	And Verify the bookmark icon on bookmark subject screen


Scenario: Verify that in the test instruction screen "Tap on review icon to review and attempt later." message should not be present.
	Given Launch the app online and navigate to Home screen
	And Navigate to "Biology" library screen
	When Navigate to test instruction screen
	Then Verify that in the test instruction screen "Tap on review icon to review and attempt later." message should not be shown.


Scenario: Verify that in the test instruction screen "Tap on the Bookmark icon to save interesting questions." message should be present.
	Given Launch the app online and navigate to Home screen
	And Navigate to "Physics" library screen
	When Navigate to test instruction screen
	Then Verify that in the test instruction screen "Tap on the Bookmark icon to save interesting questions." message should be shown.


Scenario: Verify that in Question screen bookmark icon appears on the top right corner of the screen.
	Given Launch the app online and navigate to Home screen
	And Navigate to "Mathematics" library screen
	When Navigate to test instruction screen
	And Tap on Test button in Instruction screen
	Then Verify that Bookmark icon should be present in the test screen


Scenario: Verify that in the question screen if the user bookmark  any question then the bookmark icon color should be same as subject theme color and "Bookmarked" toast  message should be shown
	Given Launch the app online and navigate to Home screen
	And Navigate to "Chemistry" library screen
	When Navigate to test instruction screen
	And Tap on Test button in Instruction screen
	And Tap on Bookmark icon in test question screen
	Then Verify that "Bookmarked" toast message should be displayed at the bottom of the screen
	And Verify that bookmark icon color should be same as subject theme color

Scenario: Verify that if the user unbookmark the bookmarked question in bookmarked question screen then "Bookmark removed" toast message should be shown and that particular question should be removed from the bookmark home screen.
	Given Launch the app online and navigate to Home screen
	And Navigate to "Physics" library screen
	When Navigate to test instruction screen
	And Tap on Test button in Instruction screen
	And Bookmark a test question and once again tap on same bookmark icon
	Then Verify that "Bookmark Removed" toast message should be displayed at the bottom of the screen
	And Verify unbookmarked question should not be displayed in the bookmark home screen under All tab
	And Verify unbookmarked question should not be displayed under "Physics" tab


Scenario: Verify that selecting the bookmarked option in the test  solution filter screen should display only bookmarked  questions
	Given Launch the app online and navigate to Home screen
	And Navigate to "Biology" library screen
	And Navigate to Highlights screen
	When Tap on "View Solution" button
	And Tap on filter icon on top right corner
	And Tap on "Bookmarked" option from the filter list
	Then Verify that bookmarked questions should be displayed on solution screen


Scenario: Verify that user should be able to bookmark practice  questions
	Given Launch the app online and navigate to Home screen
	And Navigate to "Mathematics" library screen
	And Navigate to practice question screen
	And Bookmark a practice question
	When Navigate to bookmark home screen
	Then Verify that bookmarked question should be present in Bookmark home screen under All tab
	And Verify that bookmarked question should be present under "Mathematics" tab


Scenario: Verify that in the question screen if the user bookmark  any question then the bookmark icon color should be  same as subject theme color and "Bookmarked" toast  message should be shown
	Given Launch the app online and navigate to Home screen
	And Navigate to "Chemistry" library screen
	And Navigate to practice question screen
	When Tap on Bookmark icon in practice question screen
	Then Verify that "Bookmarked" toast message should be displayed at the bottom of the screen
	And Verify that bookmark icon color should be same as subject theme color


Scenario: Verify that if the user unbookmark the bookmarked practice question then "Bookmark removed" toast message should be shown and that particular question should be removed from the bookmark home screen.
	Given Launch the app online and navigate to Home screen
	And Navigate to "Chemistry" library screen
	And Navigate to practice question screen
	When Bookmark a practice question and once again tap on same bookmark icon
	Then Verify that "Bookmark removed" toast message should be displayed at the bottom of the screen
	And Verify unbookmarked question should not be displayed in the bookmark home screen under All tab
	And Verify unbookmarked question should not be displayed under "Chemistry" tab


Scenario: Verify that tapping on bookmarked question user should navigate to bookmark question screen
	Given Launch the app online and navigate to Home screen
	And Navigate to "Mathematics" library screen
	And Bookmark a question
	When Navigate to bookmark home screen
	When Tap on bookmarked question
	Then User should navigate to bookmark question screen


Scenario: Verify the elements of bookmarked question screen
	Given Launch the app online and navigate to Home screen
	And Navigate to "Chemistry" library screen
	And Bookmark a question
	When Navigate to bookmark home screen
	And Tap on bookmarked question
	Then Verify that App back should be present at the button at the top left corner of the screen
	#And Verify Share icon
	And Verify Bookmark icon
	And Verify label Concept followed by chapter name
	And Verify bookmarked question with solution


Scenario: Verify that if the user tap on app back button in bookmark question screen user should navigate back to bookmark home screen
	Given Launch the app online and navigate to Home screen
	And Navigate to "Physics" library screen
	And Navigate to bookmark question screen
	When Tap on app back button
	Then Verify that user should navigate to bookmark home screen


Scenario: Verify that if the user tap on device back button in bookmark question screen user should navigate back to bookmark home screen
	Given Launch the app online and navigate to Home screen
	And Navigate to "Biology" library screen
	And Navigate to bookmark question screen
	When Tap on device back button
	Then Verify that user should navigate to bookmark home screen


Scenario: Verify that if the user unbookmark the bookmarked question in bookmark question screen then "Bookmark removed" toast message should be shown and that particular question should be removed from the bookmark home screen.
	Given Launch the app online and navigate to Home screen
	And Navigate to "Chemistry" library screen
	And Bookmark a question
	When Navigate to bookmark home screen
	And Tap on bookmarked question
	And Unbookmark the question in bookmark question screen
	Then Verify that "Bookmark Removed" toast message should be displayed at the bottom of the screen
	And Verify that particular question should be removed from the bookmark home screen under All tab
	And Verify that question should be removed under "Chemistry" tab


Scenario: Verify that if the user unbookmark the bookmarked question in bookmark home screen then "Bookmark removed" toast message along with Undo option should be shown.
	Given Launch the app online and navigate to Home screen
	And Navigate to "Biology" library screen
	And Navigate to bookmark home screen after bookmarking a question
	When Unbookmark the question in bookmark home screen
	Then Verify that "Bookmark Removed" snackbar message should be displayed at the bottom of the screen
	And Verify "UNDO" option should be shown along with the snackbar message


Scenario: Verify that tapping on the undo option removed bookmark question should reappear in the bookmark home screen
	Given Launch the app online and navigate to Home screen
	And Navigate to "Physics" library screen
	And Navigate to bookmark home screen after bookmarking a question
	And Unbookmark the question in bookmark home screen
	When Tap on UNDO option
	Then Verify that removed question should reappear in the bookmark home screen
	And Verify that bookmarked question should be present under "Physics" tab


Scenario: Verify the elements of bookmarked questions from practice
	Given Launch the app online and navigate to Home screen
	And Navigate to "Physics" library screen
	And Navigate to practice question screen
	And Bookmark a practice question
	When Navigate to bookmark home screen
	Then Verify that bookmarked question should be present in Bookmark home screen under All tab
	And Verify below that chapter name and "Physics" subject name
	And Verify the bookmark icon on bookmark home screen
	And Verify that bookmarked question should be present under "Physics" tab
	And Verify below that chapter name and "Physics" subject name on bookmark subject screen
	And Verify the bookmark icon on bookmark subject screen


Scenario: Verify that if the user unbookmark the bookmarked question in bookmark subject screen then "Bookmark removed" toast message along with Undo option should be shown.
	Given Launch the app online and navigate to Home screen
	And Navigate to "Mathematics" library screen
	And Bookmark a question and navigate to bookmark "Mathematics" screen
	When Unbookmark the question in subject bookmark screen
	Then Verify that "Bookmark Removed" snackbar message should be displayed at the bottom of the screen
	And Verify "UNDO" option should be shown along with the snackbar message


Scenario: Verify that tapping on the undo option removed bookmark question should reappear in the bookmark subject screen
	Given Launch the app online and navigate to Home screen
	And Navigate to "Chemistry" library screen
	And Bookmark a question and navigate to bookmark "Chemistry" screen
	And Unbookmark the question in subject bookmark screen
	When Tap on UNDO option
	Then Verify that removed question should reappear in the bookmark subject screen
	And Verify that question should be present under All tab