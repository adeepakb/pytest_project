Feature: Parity user support


Scenario: Verify that Free user cannot  Access free trial  and master class on App2
	Given launch the app and navigate to home screen
	When Verify the free user enters mobile number 
	And verify that user taps on Next button
	Then Verify that text message" this phone number is not registered with a premium account " displayed
	And verify button "Try Again"
	And Verify "Contact Us"Link


Scenario: Verify that for Parity  with PS user for paid cohort can access only master class
	Given PS subscribed user launch the app and navigate to home screen
	When Verify that user  selects the current subscribed grade
	Then Verify that in recommended section only masterclasses are displayed


Scenario: Verify that for Parity  with PS user for paid cohort should not access Free trial Classes
	Given PS subscribed user launch the app and navigate to home screen
	When Verify that user selects the current subscribed grade
	Then Verify that Free trail sessions should not be displayed in Recommended section


Scenario: Verify that for Parity  with PS user for future paid cohort can access Free trial and  master class
	Given PS subscribed user launch the app and navigate to home screen
	When Verify that user selects the future subscribed grade
	Then Verify that Free trail and master classes should be displayed in recommended section
	And verify that user should be able to book free trail and masterclasses