Feature: Pagination

@BVT 
Scenario: Verify that See all option is present in For You tab.
	Given launch the application online
	When tap on byjus classes card
	Then verify the user is navigated to the PS screen
	And verify that 2 upcoming session cards are shown
	And verify that See all option with down arrow present

@BVT 
Scenario: Verify that on tap of see all option user should navigate to up next screen successfully
	Given launch the application online
	When tap on byjus classes card
	Then verify the user is navigated to the PS screen
	And verify that 2 upcoming session cards are shown
	And verify that See all option with down arrow present
	And switch "off" the device data
	And tap on See all option
	And verify "Oops! Something went wrong" should be displayed
	And verify "Please check internet connection and try again" should be displayed
	And verify "Retry" button should be displayed
	And switch "on" the device data
	And tap on "Retry" button
	And verify all the elements in the Up next screen

@BVT 
Scenario: Verify that up next screen consist of following elements
	Given launch the application online
	When tap on byjus classes card
	Then verify the user is navigated to the PS screen
	And verify that 2 upcoming session cards are shown
	And verify that See all option with down arrow present
	And tap on See all option
	And verify all the elements in the Up next screen
	And tap on device back button
	And verify that should come back to "For you" tab

@BVT 
Scenario: Verify that in For you tab along with paid session unbooked Recommended classes are present
	Given launch the application online
	When tap on byjus classes card
	Then verify the user is navigated to the PS screen
	And verify that 2 upcoming session cards are shown
	And verify along with normal/3+1 sessions below the see all, recommended sessions (Workshop sessions) are also present

@BVT 
Scenario: Verify that up next screen should contain all the upcoming sessions.
	Given launch the application online
	When tap on byjus classes card
	Then verify the user is navigated to the PS screen
	And verify that 2 upcoming session cards are shown
	And verify that See all option with down arrow present
	And tap on See all option
	And verify that the up next screen should contain all the upcoming sessions

@BVT 
Scenario: Verify that on tap of see more option user should navigate to session details screen
	Given post-requisite "auto-post-classnotes-video" should be tagged for the particular classroom session
	And launch the application online
	When tap on byjus classes card
	Then verify the user is navigated to the PS screen
	And verify that "See more" option present on the card
	And tap on "See more"
	And verify that navigates to "Session Details" screen

@BVT 
Scenario: Verify that session details screen should consist of following elements
	Given launch the application online
	When tap on byjus classes card
	Then verify the user is navigated to the PS screen
	And verify that "See more" option present on the card
	And tap on "See more"
	And verify that navigates to "Session Details" screen
	And verify the elements present in session details screen

@BVT 
Scenario: Verify that user should be able to view pre post requisite on the card in up next screen
	Given launch the application online
	When tap on byjus classes card
	Then verify the user is navigated to the PS screen
	And verify that 2 upcoming session cards are shown
	And verify that See all option with down arrow present
	And tap on See all option
	And verify that "See more" option present on the card
	And tap on "See more"
	And verify that navigates to "Session Details" screen
	And verify the elements present in session details screen

@BVT 
Scenario: Verify that Classnotes download in session details screen status should get updated in up next session card.
	Given launch the application online
	When tap on byjus classes card
	Then verify the user is navigated to the PS screen
	And click on first session card
	And tap on class notes download icon
	And tap on device back button
	And verify class notes downloaded state along with forward icon
	And verify that See all option with down arrow present
	And tap on See all option
	And verify class notes downloaded state along with forward icon

@BVT 
Scenario: Verify that status of pre/post requisite resource types should be same in For you tab, completed tab and up next screen.
	Given launch the application online
	When tap on byjus classes card
	Then verify the user is navigated to the PS screen
	And tap on "See more"
	And verify the elements present in session details screen
	And tap on device back button
	And verify that 2 upcoming session cards are shown
	And verify that See all option with down arrow present
	And tap on See all option
	And tap on "See more"
	And verify the elements present in session details screen
	And tap on device back button
	And tap on device back button
	And tap on "Completed" tab
	And tap on "See more"
	And verify the elements present in session details screen

@BVT 
Scenario: Verify that in up next and completed screens all the upcoming and completed sessions should be listed.
	Given launch the application online
	When tap on byjus classes card
	Then verify the user is navigated to the PS screen
	And verify that 2 upcoming session cards are shown
	And verify that See all option with down arrow present
	And tap on See all option
	And tap on "See more"
	And verify the elements present in session details screen
	And tap on device back button
	And tap on device back button
	And tap on "Completed" tab
	And tap on "See more"
	And verify the elements present in session details screen

@BVT 
Scenario: Verify that when user is in offline if user taps on see all option "oops something went wrong please check internet connection and try again" message with "retry " button should be displayed
	Given launch the application online
	When tap on byjus classes card
	Then verify the user is navigated to the PS screen
	And verify that 2 upcoming session cards are shown
	And switch "off" the device data
	And tap on See all option
	And verify "Oops! Something went wrong" should be displayed
	And verify "Please check internet connection and try again" should be displayed
	And verify "Retry" button should be displayed
	And switch "on" the device data
	And tap on "Retry" button
	And verify all the elements in the Up next screen


Scenario: Verify that user should be able to book master classes from recommended section
	Given launch the application online
	When tap on byjus classes card
	Then verify the user is navigated to the PS screen
	And verify along with normal/3+1 sessions below the see all, recommended sessions (Workshop sessions) are also present
	And verify that user can book masterclass session

@BVT 
Scenario: Verify that on tap of session card from up next pagination screen user should navigate to session details screen successfully.
	Given launch the application online
	And reset student session if the session is incase completed
	When tap on byjus classes card
	Then verify the user is navigated to the PS screen
	And verify that 2 upcoming session cards are shown
	And verify that See all option with down arrow present
	And tap on See all option
	And user should land on up next screen
	And tap on "See more"
	And verify that navigates to "Session Details" screen
	And tap on device back button
	And user should land on up next screen
	And tap on device back button
	And verify that should come back to "For you" tab

@BVT 
Scenario: Verify that join button should be enabled on card before 30 minutes of session start time in both For you tab and in Up next pagination screen.
	Given launch the application online
	When tap on byjus classes card
	Then verify the user is navigated to the PS screen
	And click on first session card
	And verify "Join Now" button should be displayed
	And tap on device back button
	And tap on "For you" tab
	And verify that 2 upcoming session cards are shown
	And verify that See all option with down arrow present
	And tap on See all option
	And user should land on up next screen
	And click on first session card
	And verify "Join Now" button should be displayed


Scenario: Verify that user should be able to join the session from up next pagination screen successfully.
	Given launch the application online
	When tap on byjus classes card
	Then verify the user is navigated to the PS screen
	And verify that 2 upcoming session cards are shown
	And verify that See all option with down arrow present
	And tap on See all option
	And user should land on up next screen
	And click on first session card
	And tap on "Join Now" button
	And verify user is landed on tutor session screen


Scenario: Verify that untill next up coming session completed session should be displayed in For you tab and moved to completed tab
	Given launch the application online
	And ensure tutor has started the session
	When tap on byjus classes card
	Then verify the user is navigated to the PS screen
	And verify that 2 upcoming session cards are shown
	And verify that See all option with down arrow present
	And tap on See all option
	And user should land on up next screen
	And get session details
	And click on first session card
	And tap on "Join Now" button
	And verify user is landed on tutor session screen
	And tutor ends session
	And tap on "Okay" button
	And tap on device back button
	And tap on device back button
	And verify completed session moved to Completed tab

@BVT 
Scenario: Verify that when session end "Join now" button should be disabled in both For you and up next pagination screen.
	Given launch the application online
	When tap on byjus classes card
	Then verify the user is navigated to the PS screen
	And click on first session card
	And verify "Join Now" button is not displayed
	And tap on device back button
	And tap on "For you" tab
	And verify that 2 upcoming session cards are shown
	And verify that See all option with down arrow present
	And tap on See all option
	And user should land on up next screen
	And click on first session card
	And verify "Join Now" button is not displayed

@BVT 
Scenario: Verify that rate now card should be displayed in For you screen, Completed tab and in up next pagination after session end.
	Given launch the application online
	When tap on byjus classes card
	Then verify the user is navigated to the PS screen
	And verify "Rate Now" button should be displayed
	And verify that See all option with down arrow present
	And tap on See all option
	And user should land on up next screen
	And verify "Rate Now" button should be displayed
	And tap on device back button
	And tap on "Completed" tab
	And verify "Rate Now" button should be displayed

@BVT 
Scenario: Verify that completed session tab should contain all the completed sessions.
	Given launch the application online
	When tap on byjus classes card
	Then verify the user is navigated to the PS screen
	And tap on "Completed" tab
	And verify completed session cards should be displayed

@BVT 
Scenario: Verify that session cards with details should be identical in both for you and up next screens.
	Given launch the application online
	When tap on byjus classes card
	Then verify the user is navigated to the PS screen
	And verify that session cards with details should be identical in both for you and up next screens.

@BVT 
Scenario: Verify that in session card if requisites are present in for you, session card should be identical in up next screen also.
	Given launch the application online
	And post-requisite "classnotes" should be tagged for the particular classroom session
	When tap on byjus classes card
	Then verify the user is navigated to the PS screen
	And get session details
	And verify "Join Now" button is not displayed
	And verify that See all option with down arrow present
	And tap on See all option
	And user should land on up next screen
	And verify that the session cards in upnext and for you should be identical with session details, requisites, requisites status

@BVT 
Scenario: Verify that user should be able to scroll the pagination screen
	Given launch the application online
	When tap on byjus classes card
	Then verify the user is navigated to the PS screen
	And verify that See all option with down arrow present
	And tap on See all option
	And verify that each page will load with 20 sessions cards in up next screen

@BVT 
Scenario: Verify that on scrolling on screen, 20 session cards should be loaded in each page in both up next and completed screens.
	Given launch the application online
	When tap on byjus classes card
	Then verify the user is navigated to the PS screen
	And verify that See all option with down arrow present
	And tap on See all option
	And verify that each page will load with 20 sessions cards in up next screen
	And tap on device back button
	And tap on "Completed" tab
	And verify that each page will load with 20 sessions cards in completed screen