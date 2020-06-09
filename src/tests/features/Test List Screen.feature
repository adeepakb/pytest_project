Feature: Test List Screen


Scenario: Verify that elements of  test List screen should be available
	Given Launch the app and navigate to Home screen
	And Navigate to "Biology" library screen
	When Tap on the "Test" option
	Then Verify that user lands on the "Test List" screen
	And Verify App back arrow icon should be shown
	And Verify Chapter Name should shown in the header of the screen
	And Verify Chapter icon should be shown top right side of the screen
	And Verify "Objective Tests " label
	And Verify Objective test card should be display below the objective test label
	And Verify "Subjective Tests " label
	And Verify Subjective test card should be display below the Subjective Test label
	And Verify "Ncert Exemplars " label
	And Verify Ncert Exemplars test card should be display below the Ncert Exemplars label
	And Verify "Ncert Exercises " label
	And Verify Ncert Exercises card should be display below the Ncert Exercises label


Scenario: Verify that elements of Objective test card should be present
	Given Launch the app and navigate to Home screen
	And Navigate to "Physics" library screen
	When Tap on the "Test" option
	And Verify that user lands on the "Test List" screen
	Then Verify objective tests should be named "Objective Test 0x"
	And Verify where x being numbers in ascending order of objective test
	And Verify "Start" button should shown in front of objective test


Scenario: Verify that If the user has already taken the test then Start button should be replaced with Analyse text and Retake test icon.
	Given Launch the app and navigate to Home screen
	And Navigate to "Biology" library screen
	And Tap on the "Test" option
	And Verify that user lands on the "Test List" screen
	When Tap on Start button
	And Take a test
	And Submit the test
	Then Verify "Start" button should be replaced with "Analyse" text
	And Verify retake test icon should be shown before Analyse text with chevron icon


Scenario: Verify that tapping on Retake test icon  should redirect the user to Instruction screen followed by tapping on test button should take the user to particular objective test Question screen
	Given Launch the app and navigate to Home screen
	And Navigate to "History" library screen
	And Tap on the "Test" option
	And Verify that user lands on the "Test List" screen
	When Tap on retake test icon
	Then Verify user should redirect to Instruction screen
	And Tap on "Test" button in instruction screen
	And Verify user redirect to objective test Question screen


Scenario: Verify that user should redirect to the highlights  screen on tapping analyse button
	Given Launch the app and navigate to Home screen
	And Navigate to "Physics" learn screen
	When Tap on the test card which is present in learn screen
	And Verify that user lands on the "Test List" screen
	And Tap on Analyse button
	Then Verify that user should redirect to the highlights screen


Scenario: Verify Subjective Test elements in the screen
	Given Launch the app and navigate to Home screen
	And Navigate to "Chemistry" library screen
	When Tap on the "Test" option
	And Verify that user lands on the "Test List" screen
	Then Verify subjective tests should be named "Subjective Test 0x" format
	And Verify where x being numbers in ascending order of subjective test
	And Verify "Revise" button should be appear front of Subjective test


Scenario: Verify user should land on test list screen if user taps on test card from the learn screen
	Given Launch the app and navigate to Home screen
	And Navigate to "Geography" learn screen
	When Tap on the test card which is present in learn screen
	Then Verify that user lands on the "Test List" screen


Scenario: Verify on tapping test card user should navigate to test list screen from the library screen
	Given Launch the app and navigate to Home screen
	And Navigate to "Civics" library screen
	When Tap on the "Test" option
	Then Verify that user lands on the "Test List" screen


Scenario: Verify user should land on test list screen on tapping NSTSE test card from the special subjects
	Given Launch the app and navigate to Home screen
	And Navigate to "Competitive Exam - Mocks" library screen
	When Tap on the "Test" option
	Then Verify that user lands on the "Test List" screen


Scenario: Verify the elements of test list screen of special subjects
	Given Launch the app and navigate to Home screen
	And Navigate to "Previous Years Papers" library screen
	When Tap on the "Test" option
	And Verify that user lands on the "Test List" screen
	Then Verify App back arrow icon should be shown
	And Verify Chapter Name should shown in the header of the screen
	And Verify Chapter icon should be shown top right side of the screen
	And Verify "Tests " label
	And Verify Test cards should be display below the Tests label


Scenario: Verify on tapping start button user should  lands on instruction screen
	Given Launch the app and navigate to Home screen
	And Navigate to "Biology" library screen
	And Tap on the "Test" option
	And Verify that user lands on the "Test List" screen
	When Tap on Start button
	Then Verify user should redirect to Instruction screen


Scenario: Verify user should land on test list screen if user taps on test card from the video list screen
	Given Launch the app and navigate to Home screen
	And Navigate to "Physics" library screen
	When Tap on video card
	And Tap on Test list card on video list screen
	Then Verify that user lands on the "Test List" screen


Scenario: Verify tapping on app back button on test list screen should redirect the user to library chapter list screen, if the user navigated to test
	Given Launch the app and navigate to Home screen
	And Navigate to "Chemistry" library screen
	When Tap on video card
	And Tap on Test list card on video list screen
	And Verify that user lands on the "Test List" screen
	And Tap on app back button
	Then Verify that user is in Library chapter list screen


Scenario: Verify tapping on app back button on test list screen should redirect the user to library chapter list screen, if the user navigated to test list screen via library chapter list screen
	Given Launch the app and navigate to Home screen
	And Navigate to "Mathematics" library screen
	When Tap on the "Test" option
	And Verify that user lands on the "Test List" screen
	And Tap on app back button
	Then Verify that user is in Library chapter list screen


Scenario: Verify tapping on app back button on test list screen should redirect the user to learn chapter list screen, if the user navigated to test list screen via learn chapter list screen
	Given Launch the app and navigate to Home screen
	And Navigate to "Civics" learn screen
	When Tap on the test card which is present in learn screen
	And Verify that user lands on the "Test List" screen
	And Tap on app back button
	Then Verify that user is in Learn chapter list screen

Scenario: Verify on tapping Revise button user should  lands on instruction screen.
	Given Launch the app and navigate to Home screen
	And Navigate to "Biology" library screen
	And Tap on the "Test" option
	And Verify that user lands on the "Test List" screen
	When Tap on Revise button
	Then Verify user should redirect to Instruction screen


Scenario: OFFLINE MODE: Verify that tapping on Start button on objective test card displays an toaster message 'Please connect to network and try again later.' if the test is not downloaded.
	Given Launch the app and navigate to Home screen
	And Navigate to "Geography" library screen
	When Tap on the "Test" option
	And Verify that user lands on the "Test List" screen
	And disconnect device wifi/mobile data
	And Tap on Start button
	Then Verify text message "Please connect to network and try again later." shown at the bottom of the test list screen
	And connect device wifi/mobile data


Scenario: OFFLINE MODE: Verify that tapping on Revise button on subjective test card displays an toaster message 'Please connect to network and try again later.' if the test is not downloaded.
	Given Launch the app and navigate to Home screen
	And Navigate to "Physics" library screen
	When Tap on the "Test" option
	And Verify that user lands on the "Test List" screen
	And disconnect device wifi/mobile data
	And Tap on Revise button
	Then Verify text message "Please connect to network and try again later." shown at the bottom of the test list screen
	And connect device wifi/mobile data


Scenario: OFFLINE MODE: Verify that user should redirect to the highlights screen on tapping analyse button
	Given Launch the app and navigate to Home screen
	And Navigate to "History" learn screen
	When Tap on the test card which is present in learn screen
	And Verify that user lands on the "Test List" screen
	And disconnect device wifi/mobile data
	And Tap on Analyse button
	Then Verify that user should redirect to the highlights screen
	And connect device wifi/mobile data


Scenario: OFFLINE MODE: Verify that tapping on Retake test icon  should redirect the user to Instruction screen followed by tapping on test button should take the user to   particular objective test Question screen
	Given Launch the app and navigate to Home screen
	And Navigate to "Physics" library screen
	And Tap on the "Test" option
	And Verify that user lands on the "Test List" screen
	When disconnect device wifi/mobile data
	And Tap on retake test icon
	Then Verify user should redirect to Instruction screen
	And connect device wifi/mobile data