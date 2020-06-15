Feature: Personalized chapter list screen

Scenario: Verify that trending journey card is highlighted in personalized chapter list screen
	Given Launch the app online
	When User is in Personalized chapter list screen
	Then Verify that trending journey card should be highlighted


Scenario: Verify the fields in personalized chapter list screen when trending journey is highlighted in first two rows
	Given Device is white listed for search experiment
	And Launch the app online
	And User is new user
	And User is in Personalized chapter list screen
	When Trending journey card is highlighted in first two rows of chapter
	Then Verify back arrow on top left corner of the screen
	And Library button along with the text library at the top right side of the screen
	And Search button on top right corner of the screen
	And Subject name followed by number of Chapters and Journeys
	And Hero image
	And Below that resume where you left card with the journey/video name followed by forward icon(->)
	And Below that all the topics with respective journey cards ,test cards and practice cards
	And Ensure that each chapters in the journey screen should be separated by thin line


Scenario: Verify the fields in personalized chapter list screen  when trending journey is highlighted in third row
	Given Device is white listed for search experiment
	And Launch the app online
	When User is in personalized chapter list screen.
	And Trending journey card is highlighted after third row of chapter
	Then Verify back arrow on top left corner of the screen
	And Subject name center aligned
	And back Button on top right corner of the screen
	And Search button on top right corner of the screen
	And Sticky card with recently taken chapter name followed by forward arrow
#
#
Scenario: Verify the fields in personalized chapter list screen when trending journey is highlighted in first two rows with some user data
	Given Device is white listed for search experiment
	And Launch the app online
	When User is in Personalized chapter list screen
	And Trending journey card is highlighted in first two rows of chapter
	Then Verify that App back button on top left side of the screen
	And Library button along with the text library at the top right side of the screen
	And Subject name followed by number of Chapters and Journeys
	And Hero image
	And Below that resume where you left card with the journey/video name followed by forward icon(->)
	And Below that all the topics with respective journey cards ,test cards and practice cards
	And Ensure that each chapters in the journey screen should be separated by thin line


Scenario: Verify the fields in personalized chapter list screen when trending journey is highlighted after third row of chapter
	Given Device is white listed for search experiment
	Launch the app online
	When User is in personalized chapter list screen.
	And Trending journey card is highlighted after third row of chapter
	Then Verify back arrow on top left corner of the screen
	And Subject name center aligned
	And back Button on top right corner of the screen
	And Search button on top right corner of the screen
	And Sticky card with recently taken chapter name followed by forward arrow


Scenario: Verify that library button in the personalized screen should change to personalized button, when user switches to Library Mode.
	Given Launch the app online
	When User is in Personalized chapter list screen
	And User taps on library button
	Then Verify that user should be switched to library chapter list screen


Scenario: Verify that tapping on back arrow  in personalized chapter list screen should navigate back to home screen.
	Given Launch the app online
	When User is in Personalized chapter list screen
	And User taps on back arrow in personalized chapter list screen
	Then Verify that user should be navigate back to home screen


Scenario: Verify that tapping on search icon on personalized chapter list screen should be navigates to search screen
	Given Device is white listed for search experiment
	And Launch the app online
	And User is in Personalized chapter list screen
	When User taps on search button
	Then Verify that user should be navigate to <SearchScreen>


Scenario: Verify that tapping on resume where you left  card should be navigate to particular journey
	Given Launch the app online
	And User is in Personalized chapter list screen
	When User taps on resume where you left card
	Then Verify that user should be navigate to particular journey


Scenario: Verify that tapping on resume the practice card should be navigate to particular practice
	Given Launch the app online
	And User is in Personalized chapter list screen
	When User taps on resume the practice card
	Then Verify that user should be navigate to particular practice


Scenario: Verify that tapping on resume the test card should be navigate to particular test
	Given Launch the app online
	And User is in Personalized chapter list screen
	When User taps on resume the test card
	Then Verify that user should be navigate to particular test


Scenario: Verify that journey card should have journey icon and journey name.
	Given Launch the app online
	When User is in Personalized chapter list screen
	Then Verify that journey card should have journey icon and journey name


#Scenario: Verify that each topic can have multiple journeys and each journey can displayed on individual card.
#	Given Launch the app online
#	When User is in Personalized chapter list screen
#	Then Verify that number of journey cards under each topic on personalized chapter list screen should be based on back end
#
#
##Scenario: Verify that apart from journeys each chapter should consists of practice and free tests
##	Given Launch the app online
##	When User is in Personalized chapter list screen
##	Then Verify that each chapter should consists of tests and practices and should be based on back end


Scenario: Verify the fields in chapter if subject do not have any videos
	Given Launch the app online
	When User is in Personalized chapter list screen
	Then Verify that user should be able to see only chapter name and test card and practice card
#

Scenario: Verify that scrolling upwards the top label should be minimized
	Given Device is white listed for search experiment
	And Launch the app online
	When User is in personalized chapter list screen.
	Then Verify that scrolling upwards the top label should be minimized
	And Verify back arrow on top left corner of the screen
	And Subject name center aligned
	And back Button on top right corner of the screen
	And Search button on top right corner of the screen
	And Sticky card with recently taken chapter name followed by forward arrow


Scenario: Verify that tapping on journey card of particular chapter should be navigate to journey loading and journey map screen
	Given Launch the app online
	And User is in Personalized chapter list screen
	When User taps on journey card
	Then Verify that user navigates to journey loading screen first and then journey map screen of particular topic


Scenario: Verify that tapping on journey card without network and user should be navigate  back to personalized chapter list screen
	Given Launch the app online
	And User is in Personalized chapter list screen
	And User is in Offline
	When User taps on a journey card
	Then Verify that "Please connect to network and try again later." toast message should be shown
	And user should be navigate back to chapter list screen


Scenario: Verify that tapping on test card under particular chapter should be navigate to test screen
	Given Launch the app online
	And User is in Personalized chapter list screen
	When User taps on test card
	Then Verify that user should be navigates to <TestScreen> of particular topic


Scenario: Verify that tapping on practice card under particular chapter should be navigate to practice screen
	Given Launch the app online
	And User is in Personalized chapter list screen
	When User taps on practice card
	Then Verify that user should be navigate to <PracticeScreen> of particular topic