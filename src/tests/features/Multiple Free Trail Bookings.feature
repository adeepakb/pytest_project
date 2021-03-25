Feature: Multiple Free Trail Bookings


Scenario: Verify that Users who attend the booked free trial class still able to book the free trial classes
	Given user launch the app and navigate to home screen
	When Verify  that user attended  free trail session
	And Verify  that multiple free booking session is enabled from back-end
	Then Verify  that user should get book option for free trial sesions in recommended  section


Scenario: Verify the if the user has not booked the free trail , free trail sessions should be shown in the recommended session
	Given user launch the app and navigate to home screen
	When Verify  that user had not booked free Trial session 
	And Verify  that user had booked master sessions
	Then Verify  that free trial sessions should be displayed in recommended section


Scenario: Verify that the user should be able to  only book free trial sessions one at a particular time
	Given user launch the app and navigate to home screen
	When Verify  that user lands on booking  screen
	Then Verify  that user should  be able to book only one free trail session at a time
	And verify  that user should  not be able to book multiple  free trail session at a time


Scenario: Verify that user should not be able to book multiple sessions at same time
	Given user launch the app and navigate to home screen
	Verify that multiple free booking should  be enabled from backend
	When Verify  that user booked one session
	And verify  that booked session has not started/completed
	Then Verify  that user cannot book multiple  free trail session 
	And verify  that Free trial  sessions should  not be displayed  in recommended  section


Scenario: Verify that Once the user books the free trial class, user can't book another free trial class until he/she has attended or missed the existing booking
	Given user launch the app and navigate to home screen
	When Verify that user booked the session 
	And multiple  free trail classes enabled from backend
	Then Verify  that until user completes session
	free trail classes should not  be displayed in completed tab


Scenario: Verify that user should be able to book and attend multiple free trail classes when master class is available
	Given user launch the app and navigate to home screen
	When Verify  that user had attended one free trail
	And verify  that user had booked masteclass
	Then Verify  that user can book and attended multiple  free trial  And Verify  that user can book multiple  mastercalss sessions


Scenario: Verify that if the user miss the booked class , the session should get auto booked for the user with Swap option
	Given user launch the app and navigate to home screen
	When Verify  that user misses booked session
	Then Verify  that user should  get autobooked/rebook option


Scenario: Verify that if the user miss the auto booked class, user should get rebook button
	Given user launch the app and navigate to home screen
	When Verify  that If  user misses autobooked session
	And same topics are not available  from backend
	Then Verify that user should get Rebook option