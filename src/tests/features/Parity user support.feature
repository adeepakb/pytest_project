Feature: Parity user support


Scenario: Verify that for Parity with PS user for future paid cohort can access Free trial and master class
	Given PS subscribed user launch the app and navigate to home screen
	And new user's book history is deleted from backend
	When Verify that user selects the future subscribed grade
	And navigate to byju's classes home screen
	Then Verify that Free trail and master classes should be displayed in recommended section
	And verify that user should be able to book free trail and masterclasses


Scenario: Verify that Parity user with Expired PS can access Free trail and masterclass in future paid cohort
	Given Parity user with Expired PS user launch the app and navigate to home screen
	And new user's book history is deleted from backend
	When Verify that user switches to future paid cohort
	And navigate to byju's classes home screen
	Then Parity user with Expired PS can access Free trail and masterclass in future paid cohort