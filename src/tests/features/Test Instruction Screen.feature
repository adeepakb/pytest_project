@mobile @tab
Feature: Test Instruction Screen


Scenario: Verify Objective test instruction screen text and attributes
	Given Launch the app and navigate to Home screen
	And Navigate to "Mathematics" chapter list screen
	When Navigate to Objective test instruction screen
	Then Verify Chapter Name and test name should be shown on the screen
	And Verify App back arrow icon should be shown
	And Verify Test icon should be shown top right side of the screen
	And Verify number of Questions with icon should shown along with "Questions" text
	And Verify Minutes with icon should shown along with "Minutes" text
	And Verify "Instructions" label
	And Verify the "Test" button
	And Verify instruction "x mark is awarded for correct attempts and x marks for incorrect attempts." text should shown below the instruction label
	And Verify instruction text "Tap on options to select the correct answer."
	And Verify instruction text "Tap on the Bookmark icon to save interesting questions."
	And Verify instruction icons


Scenario: Verify that tapping on Test button user should navigate to Objective test question screen
	Given Launch the app and navigate to Home screen
	And Navigate to "Civics" chapter list screen
	And Navigate to Objective test instruction screen
	When Tap on "Test" button in instruction screen
	Then Verify user should land on Objective test question screen


Scenario: Verify that tapping on app back on objective test screen should redirect the user to Test list screen
	Given Launch the app and navigate to Home screen
	And Navigate to "History" chapter list screen
	And Navigate to Objective test instruction screen
	When Tap on app back button
	Then Verify that user lands on the "Test List" screen


Scenario: Verify that tapping on device back button on objective test screen should redirect the user to Test list screen
	Given Launch the app and navigate to Home screen
	And Navigate to "Civics" chapter list screen
	And Navigate to Objective test instruction screen
	When Tap on device back button
	Then Verify that user lands on the "Test List" screen


Scenario: OFFLINE MODE:Verify that tapping on Test button user should navigate to Objective test question screen
	Given Launch the app online and navigate to Home screen
	And Navigate to "History" chapter list screen
	And Navigate to Objective test instruction screen
	When disconnect device wifi/mobile data
	And Tap on "Test" button in instruction screen
	Then Verify user should land on Objective test question screen
	And connect device wifi/mobile data


Scenario: Verify Subjective test instruction screen text and attributes
	Given Launch the app and navigate to Home screen
	And Navigate to "Chemistry" chapter list screen
	When Navigate to Subjective test instruction screen
	Then Verify Chapter Name and test name should be shown on the screen
	And Verify App back arrow icon should be shown
	And Verify Test icon should be shown top right side of the screen
	And Verify "Instructions" label
	And Verify the "Continue" button
	And Verify instruction text "This section helps you attempt subjective exams such as school tests, summative assessments and board exams."
	And Verify instruction text "The detailed solutions along with marking scheme for every question is provided to help you better."
	And Verify instruction text "Mark the question for review using the mark for review icon. Report an issue in a question/answer using report an issue icon."
	And Verify instruction icons


Scenario: Verify that tapping on Continue button user should navigate to Subjective test question screen
	Given Launch the app and navigate to Home screen
	And Navigate to "Biology" chapter list screen
	And Navigate to Subjective test instruction screen
	When Tap on "Continue" button in instruction screen
	Then Verify user should land on Subjective test question screen


Scenario: Verify that tapping on app back on subjective test screen should redirect the user to Test list screen
	Given Launch the app and navigate to Home screen
	And Navigate to "Biology" chapter list screen
	And Navigate to Subjective test instruction screen
	When Tap on app back button
	Then Verify that user lands on the "Test List" screen


Scenario: Verify that tapping on device back button on subjective test screen should redirect the user to Test list screen
	Given Launch the app and navigate to Home screen
	And Navigate to "Chemistry" chapter list screen
	And Navigate to Subjective test instruction screen
	When Tap on device back button
	Then Verify that user lands on the "Test List" screen


Scenario: OFFLINE MODE:Verify that tapping on Continue button user should navigate to Subjective test question screen
	Given Launch the app online and navigate to Home screen
	And Navigate to "Mathematics" chapter list screen
	And Navigate to Subjective test instruction screen
	When disconnect device wifi/mobile data
	And Tap on "Continue" button in instruction screen
	Then Verify user should land on Subjective test question screen
	And connect device wifi/mobile data


Scenario: Verify Ncert Exercises test instruction screen text and attributes
	Given Launch the app and navigate to Home screen
	And Navigate to "Biology" chapter list screen
	When Navigate to Ncert Exercises test instruction screen
	Then Verify Chapter Name and test name should be shown on the screen
	And Verify App back arrow icon should be shown
	And Verify Test icon should be shown top right side of the screen
	And Verify "Instructions" label
	And Verify instruction text "This section contains all the NCERT exercise questions from this chapter with detailed solutions."
	And Verify instruction text "Each question is numbered following the NCERT convention, for your reference. "
	And Verify instruction text "Before you view the solutions, we recommend you to try solving it on your own."
	And Verify the "Continue" button


Scenario: Verify that tapping on Test button user should navigate to Ncert Exercises test question screen
	Given Launch the app and navigate to Home screen
	And Navigate to "Mathematics" chapter list screen
	And Navigate to Ncert Exercises test instruction screen
	When Tap on "Continue" button in instruction screen
	Then Verify user should land on Ncert Exercises test question screen


Scenario: Verify Ncert Exemplars test instruction screen text and attributes
	Given Launch the app and navigate to Home screen
	And Navigate to "Biology" chapter list screen
	When Navigate to Ncert Exemplars test instruction screen
	Then Verify Chapter Name and test name should be shown on the screen
	And Verify App back arrow icon should be shown
	And Verify Test icon should be shown top right side of the screen
	And Verify "Instructions" label
	And Verify instruction text "This section contains all the NCERT Exemplar questions from this chapter with detailed solutions. Each question is numbered following the NCERT convention, for your reference."
	And Verify instruction text "Before you view the solutions, we recommend you to try solving it on your own."
	And Verify the "Continue" button


Scenario: Verify that tapping on Test button user should navigate to Ncert Exemplars test question screen
	Given Launch the app and navigate to Home screen
	And Navigate to "Biology" chapter list screen
	And Navigate to Ncert Exemplars test instruction screen
	When Tap on "Continue" button in instruction screen
	Then Verify user should land on Ncert Exemplars test question screen