Feature: MasterClass


Scenario: Verify the display of masterclass card in For you section
	Given launch the app and navigate to home screen
	And navigate to one to mega home screen
	When verify for you sessions tab is highlighted
	And verify master class are scheduled
	Then verify the display of master class in "Recommended Classes" section


Scenario: Verify the display of elements present in the masterclass
	Given launch the app and navigate to home screen
	And navigate to one to mega home screen
	When verify for you sessions tab is highlighted
	And verify master class are scheduled
	Then verify details of master class session card


Scenario: Verify the display of masterclass if masterclass not booked
	Given launch the app and navigate to home screen
	And navigate to one to mega home screen
	When verify for you sessions tab is highlighted
	And verify master class are scheduled
	Then verify that "Recommended Classes" section should display below three cards with see all CTA


Scenario: Verify the display of Up next and Recommended classes when master class not booked
	Given launch the app and navigate to home screen
	And navigate to one to mega home screen
	When verify for you sessions tab is highlighted
	And verify the display of regular class in "Up Next" section
	And verify that master classes are not booked
	And verify master class are scheduled
	Then verify the display of master class in "Recommended Classes" section


Scenario: Verify the display of workshop tag for masterclass cards
	Given launch the app and navigate to home screen
	And navigate to one to mega home screen
	When verify for you sessions tab is highlighted
	And verify master class are scheduled
	Then verify workshop tag is displayed on the available masterclasses


Scenario: Verify when user taps on see all navigated to full view of up next screen
	Given launch the app and navigate to home screen
	And navigate to one to mega home screen
	When verify for you sessions tab is highlighted
	And verify master class are scheduled
	And user taps on see all option
	Then verify the display of regular class in "Up Next" section
	And verify user is able to scroll


Scenario: Verify the display of Detailed screen when user taps on masterclass card
	Given launch the app and navigate to home screen
	And navigate to one to mega home screen
	When verify for you sessions tab is highlighted
	And verify master class are scheduled
	And tap on master class session card
	Then verify text "Class Details"
	And verify text "Workshop"
	And verify the display of topic name
	And verify display of slots
	And verify the display Book button


Scenario: Verify the display of FillingFast tag for masterclass cards
	Given verify profile for booking masterclass and validation
	When verify for you sessions tab is highlighted
	And verify and add slot for master class booking
	And verify master class are scheduled
	Then verify filling fast label is displayed


Scenario: Verify that when user taps on Book on master card successfully Booked pop up should be displayed
	Given verify profile for booking masterclass and validation
	When verify for you sessions tab is highlighted
	And verify master class are scheduled
	And verify and add slot for master class booking
	Then book master class and verify details in booking and booked successful screen
	And verify masterclass it is listed in session list as per schedule date and time
	And verify filling fast label should not be displayed on the booked masterclass session


Scenario: Verify the display of for you session  when one master class booked and more than one master class available for that grade
	Given verify profile for masterclass booking
	When verify for you sessions tab is highlighted
	And verify the display of regular class in "Up Next" section
	And verify master class are scheduled
	And verify more than one master classes are available
	And verify one masterclass is booked
	Then verify the display of master class in "Recommended Classes" section
	And verify "See all" or "See less" option is displayed


Scenario: Verify that  user should  be able to successfully  join master class session
	Given verify profile for booking masterclass and validation
	And verify master class is booked for the current day and is not completed
	When "Join Now" button is enabled before 30 minutes of the session
	Then verify that user is able to join the session


Scenario: Verify that  user should be able to join session from the card or from the session detail page page
	Given verify profile for booking masterclass and validation
	And verify master class is booked for the current day and is not completed
	When "Join Now" button is enabled before 30 minutes of the session
	Then verify that user is able to join the session from session details screen


Scenario: Verify the booking the master class when device wifi/data is turned Off
	Given launch the app and navigate to home screen
	And navigate to one to mega home screen
	When verify for you sessions tab is highlighted
	And verify master class are scheduled
	And switch off the device wifi
	Then try to book a master class session
	And verify the error toast message is displayed


Scenario: Verify the error message when user tries to Book the masterclass after the 30 min of the session start time
	Given verify profile for booking masterclass and validation
	When verify for you sessions tab is highlighted
	And add slot for master class booking post booking time
	And verify master class are scheduled
	And verify that the session has crossed the booking time
	Then verify error message is displayed when user tries to book a session


Scenario: Verify that session completed mastercard should be displayed in completed tab
	Given verify profile for booking masterclass and validation
	When verify for you sessions tab is highlighted
	And verify last master class session is ended but not rated
	Then verify completed master class should be displayed in "Completed" tab


Scenario: Verify that post,pre and in requisites can be attached to masterclass
	Given verify profile for booking masterclass and validation
	When verify for you sessions tab is highlighted
	And verify last master class session is ended but not rated
	And all requisites are attached to booked masterclass session
	Then verify that for completed session both pre and post requisite are displayed


Scenario: Verify that post completion of the masterclass session, should be shown in both under for you and completed sessions tabs.
	Given verify profile for booking masterclass and validation
	When verify for you sessions tab is highlighted
	And verify last master class session is ended but not rated
	Then verify completed masterclass session is displayed under both "For you" and "Completed" tab


Scenario: Verify that taping on back navigation icon or device back navigation from "Up next" see all screen, user should land on home page
	Given launch the app and navigate to home screen
	And navigate to one to mega home screen
	When verify for you sessions tab is highlighted
	And verify master class are scheduled
	And user taps on see all option
	Then tap on device back or app back button
	And verify user navigated to home screen


Scenario: Verify that taping on back navigation icon or device back navigation from masterclass session details screen, user should come back to classes screen in up next tab.
	Given launch the app and navigate to home screen
	And navigate to one to mega home screen
	When verify for you sessions tab is highlighted
	And verify master class are scheduled
	And tap on master class session card
	Then tap on device back or app back button
	And verify user landed on student dashboard screen
	And verify for you sessions tab is highlighted


Scenario: Verify that "See less" should collapse expanded session list screen.
	Given launch the app and navigate to home screen
	And navigate to one to mega home screen
	When verify for you sessions tab is highlighted
	And user taps on see all option
	And verify hidden upcoming sessions are displayed
	And user taps on see less option
	Then verify that session list should collapse and shows fewer session


Scenario: Verify that session list scrolling should be enabled when session list is in view all state.
	Given launch the app and navigate to home screen
	And navigate to one to mega home screen
	When verify for you sessions tab is highlighted
	And verify master class are scheduled
	And user taps on see all option
	Then verify user should be able scroll to view all upcoming sessions