Feature: BYJUS CLASSES - Know More option in left navigation


Scenario: Verify that in Left Nav Byjus classes know more option is present
	Given New user launch the app and navigate to home screen
	And new user's book history is deleted from backend
	When Tap on the Hamburger menu at the left corner on the home screen
	And verify that the Left nav is displayed
	Then Verify that in the left nav "Byjus classes-Know more" option is present
	And tap on the "Byjus classes-Know more" option in the left nav
	And verify  "Byjus classes-Know more" option is responsive


Scenario: Verify that on tap of Byjus classes  will lead the user to a web page opened through webview
	Given New user launch the app and navigate to home screen
	When Tap on the Hamburger menu at the left corner on the home screen
	And verify that the Left nav is displayed
	Then Tap on "Byjus classes-Know more" option on the left nav
	And verify that web page opened through webview which should show all the information wrt "BYJU’S CLASSES"


Scenario: Verify that Web view  should show all the information wrt BYJU’S CLASSES
	Given New user launch the app and navigate to home screen
	When Tap on "Byjus classes" option on left navigation
	Then verify that web page opened through webview which should show all the information wrt "BYJU’S CLASSES"


Scenario: Verify that If user has not booked the free trial class on webview when user navigates it should display Book a free session CTA
	Given New user launch the app and navigate to home screen
	When Tap on the "Byjus classes" option on the left nav
		And verify that the web page opened through webview which should show all the information wrt "BYJU’S CLASSES"
	Then Verify that "BYJUS CLASSES" web view consist of "Book a free class" card
	And tap of "Book a free class" card
	And verify "Book a free class" card is responsive


Scenario: Verify that when PS subscribed user tap on left nav Byjus classes "Book a free class" CTA is shown
	Given New user launch the app and navigate to home screen
	When Tap on the "Byjus classes" option on the left nav
	And verify that the web page opened through webview which should show all the information wrt "BYJU’S CLASSES"
	Then Verify that the "BYJUS CLASSES" web view consist of the "Book a free class" card


Scenario: Verify that when user tap on Book a free class CTA on web view user should be navigated to book a free class screen
	Given New user launch the app and navigate to home screen
	When Tap on the "Byjus classes" option on the left nav
	And verify that the web page opened through webview which should show all the information wrt "BYJU’S CLASSES"
	Then Verify that the "BYJUS CLASSES" web view consist of the "Book a free class" card
	And tap of "Book a free class" card
	And verify that user is navigated to "Book a free class" screen


Scenario: Verify that through web view user is able to "Book a free class" successfully
	Given New user launch the app and navigate to home screen
	When Tap on the "Byjus classes" option on the left nav
	And verify that the web page opened through webview which should show all the information wrt "BYJU’S CLASSES"
	Then Verify that the "BYJUS CLASSES" web view consist of the "Book a free class" card
	And tap of "Book a free class" card
	And verify that the user is navigated to the "Book a free class" screen
	And tap on "Book" button
	And verify user is able to book a session


Scenario: Verify that If user has  booked the free trial class on webview when user navigates it should display View Class details CTA
	Given New user launch the app and navigate to home screen
	When Tap on the "Byjus classes" option on the left nav
	And verify that the web page opened through webview which should show all the information wrt "BYJU’S CLASSES"
	Then Verify that "BYJUS CLASSES" consist of "View Class details" card
	And tap of "View Class details" card
	And verify "View Class details" card is responsive


Scenario: Verify that when user taps on View Class details CTA on webview user should be navigated  to PS classroom screen
	Given New user launch the app and navigate to home screen
	When Tap on the "Byjus classes" option on the left nav
	And verify that the web page opened through webview which should show all the information wrt "BYJU’S CLASSES"
	Then Verify that the "BYJUS CLASSES" web view consist of "view details" card
	And tap of "view Class details" card
	And verify that user is navigated to Premium school classroom session screen


Scenario: Verify that when trial class completed  on tap of left nav Byjus classes view details is shown
	Given New user launch the app and navigate to home screen
	When Tap on the "Byjus classes" option on the left nav
	And verify that the web page opened through webview which should show all the information wrt "BYJU’S CLASSES"
	Then Verify that "BYJUS CLASSES" web view consist of "view details" card


Scenario: Verify that when user is in Web view if user tap on back icon user is navigated to home screen successfully
	Given New user launch the app and navigate to home screen
	When Tap on the "Byjus classes" option on the left nav
	And verify that the web page opened through webview which should show all the information wrt "BYJU’S CLASSES"
	Then Tap on the back icon on the web view
	Verify that the user is navigated to the home screen successfully