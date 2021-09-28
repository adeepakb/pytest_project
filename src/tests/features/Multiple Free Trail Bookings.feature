Feature: Multiple Free Trail Bookings


Scenario: Verify the booking screen UI and Layout for Free Trial user
	Given launch the application online
	And reset completed free trial and masterclass sessions
	When click on the hamburger menu
	And tap on byjus classes card
	And User in booking screen page
	Then verify that Free class subject name, title name , time ,date, duration , day should display.
	And Verify that book option should display for free trial session


Scenario: Verift that free trial classes are availabe under Regular Classes section under booking screen
	Given launch the application online
	When click on the hamburger menu
	And tap on byjus classes card
	And User in booking screen page
	Then Verift that free trial classes are availabe under Regular Classes section under booking screen


Scenario: Verift that master classes are availabe under Master Classes section under booking screen
	Given launch the application online
	When click on the hamburger menu
	And tap on byjus classes card
	And User in booking screen page
	Then Verift that master classes are availabe under Master Classes section under booking screen


Scenario: Verify the UI and layout of free regular class tile
	Given launch the application online
	When click on the hamburger menu
	And tap on byjus classes card
	And User in booking screen page
	Then Verify that subject name and subject title should display in free regular class title


Scenario: Verify the UI and layout of free master class tile
	Given launch the application online
	When click on the hamburger menu
	And tap on byjus classes card
	And User in booking screen page
	Then Verify that subject name and subject title should display in Master class title


Scenario: Verify that for each distinct subject/topic there is only one tile in the booking screen
	Given launch the application online
	When click on the hamburger menu
	And tap on byjus classes card
	And User in booking screen page
	Then All unique sessions should have only one session card listed and should not be any duplicate session cards with same session name


Scenario: Verify that all availabe slots for subject/topic are listed on the tile as per zeplin UI
	Given launch the application online
	When click on the hamburger menu
	And tap on byjus classes card
	And User in booking screen page
	Then Verify that all availabe slots for subject/topic are listed on the tile as per zeplin UI


Scenario: Verify the book button functionality for regular class
	Given launch the application online
	When click on the hamburger menu
	And tap on byjus classes card
	And User in booking screen page
	And Click on Book option for a regular class
	Then verify that class date and time selection popup should display when user click on book option.


Scenario: Verify the UI of regular class date and time selection pop-up
	Given launch the application online
	When click on the hamburger menu
	And tap on byjus classes card
	And User in booking screen page
	And Click on Book option for a regular class
	Then verify that class date and time selection popup should display when user click on book option.
	And verify that 'confirm & book' and cancel option should display in the selection popup


Scenario: Verify that user is able to book from available slots
	Given launch the application online
	When click on the hamburger menu
	And tap on byjus classes card
	And User in booking screen page
	And Click on Book option for a regular class
	And click on 'Confirm & Book' button in the selection popup
	Then Verify that user is able to book from available slots


Scenario: Verify that correct slots are displayed on regular class date and time selection pop-up
	Given launch the application online
	And get current slot details from backend
	When click on the hamburger menu
	And tap on byjus classes card
	Then verify the user is navigated to the PS screen
	And Verify that correct slot is displayed on regular class date and time selection pop-up


Scenario: Verify that class is not booked and user lands back on booking page if cancel button is selected
	Given reset completed free trial and masterclass sessions
	And launch the application online
	When click on the hamburger menu
	And tap on byjus classes card
	And User in booking screen page
	And Click on Book option for a regular class
	And click on 'Cancel' button
	Then Verify that class is not booked and user lands back on booking page if cancel button is selected


Scenario: Verify that class is booked and user lands back on schedule/session page if booking is successful
	Given launch the application online
	When click on the hamburger menu
	And tap on byjus classes card
	And User in booking screen page
	And Click on Book option for a regular class
	And click on 'Confirm & Book' button in the selection popup
	Then Verify that class is booked and user lands back on schedule/session page if booking is successful


Scenario: Verify if user doesn't book and navigates away from booking screen and comes back to book
	Given reset completed free trial and masterclass sessions
	And launch the application online
	When click on the hamburger menu
	And tap on byjus classes card
	And User in booking screen page
	And tap on back navigation icon
	And tap on byjus classes card
	And User in booking screen page
	And Click on Book option for a regular class
	And click on 'Confirm & Book' button in the selection popup
	Then Verify that user is able to book from available slots


Scenario: Verify if user doesn't book closes the application and relogin and tries to book
	Given reset completed free trial and masterclass sessions
	And launch the application online
	When click on the hamburger menu
	And tap on byjus classes card
	And User in booking screen page
	And close the application
	And re-login to application
	And dismiss byjus classes book a free trail bottom sheet
	And click on the hamburger menu
	And tap on byjus classes card
	And User in booking screen page
	And Click on Book option for a regular class
	And click on 'Confirm & Book' button in the selection popup
	Then Verify that user is able to book from available slots


Scenario: Verify when user tries to book class anywhere between 30 mins before the session start time
	Given reset completed free trial and masterclass sessions
	And launch the application online
	When click on the hamburger menu
	And tap on byjus classes card
	And User in booking screen page
	And try to book the session 30 mins before the session starts
	And click on 'Confirm & Book' button in the selection popup
	Then Verify that user is able to book the session 30 mins before the session starts


Scenario: Verify the UI and layout of Regular Class booking confirmation page
	Given reset completed free trial and masterclass sessions
	And launch the application online
	When click on the hamburger menu
	And tap on byjus classes card
	And User in booking screen page
	And book regular trial session
	Then Verify that confirmation message should display when user book a session
	And Verify that session title , date , day , time should display.
	And Verify that session starts in time should display
	And Verify that okay button should display


Scenario: Verify the timer on the Regular Class booking confirmation page
	Given reset completed free trial and masterclass sessions
	And launch the application online
	When click on the hamburger menu
	And tap on byjus classes card
	And User in booking screen page
	And book regular trial session
	Then Verify that timer should display in confirmation page , when user book a session.
	And verify that the the timer should display in HH.MM.SS format


Scenario: Verify that user is unable to book the session less than 30 mins before the session starts
	Given launch the application online
	And add slot in backend which starts in less than 30 mins
	When click on the hamburger menu
	And tap on byjus classes card
	And User in booking screen page
	Then Verify that user is unable to book the session less than 30 mins before the session starts


Scenario: Verify that Users who attend the booked free trial class still able to book the free trial classes
	Given launch the application online
	And reset completed free trial and masterclass sessions
	When click on the hamburger menu
	Then tap on byjus classes card
	book special master class
	And tap on back navigation icon
	And tap on byjus classes card
	verify the user is navigated to the PS screen
	And verify "Recommended Classes" section is present
	And verify that user should get book option for free trial sessions in recommended section


Scenario: Verify the if the user has not booked the free trail , free trail sessions should be shown in the recommended session
	Given launch the application online
	When click on the hamburger menu
	And tap on byjus classes card
	Then book masterclass session
	And verify "Recommended Classes" section is present
	And verify that user should get book option for free trial sessions in recommended section


Scenario: Verify that if user has booked only master class, then free trail classes should be shown in the recommended session
	Given launch the application online
	When click on the hamburger menu
	And tap on byjus classes card
	Then verify the user is navigated to the PS screen
	Verify that user can book multiple masterclass sessions
	And verify "Recommended Classes" section is present
	And verify that user should get book option for free trial sessions in recommended section


Scenario: Verify that the user should be able to  only book free trial sessions one at a particular time
	Given launch the application online
	When click on the hamburger menu
	And tap on byjus classes card
	Then verify the user is navigated to the PS screen
	verify "Recommended Classes" section is present
	And user book one trial class
	And verify that user should not be able to book multiple free trail session at same time


Scenario: Verify that user should not be able to book multiple sessions at same time
	Given launch the application online
	When click on the hamburger menu
	And tap on byjus classes card
	Then verify the user is navigated to the PS screen
	verify that user booked the trial session
	And verify that user should not be able to book multiple free trail session at same time


Scenario: Verify that Once the user books the free trial class, user can't book another free trial class until he/she has attended or missed the existing booking
	Given launch the application online
	When click on the hamburger menu
	And tap on byjus classes card
	Then verify the user is navigated to the PS screen
	And verify that user booked the trial session
	And verify free trail class should not be displayed in completed tab


Scenario: Verify that user should be able to book master classes if the free trail class is expired
	Given launch the application online
	And expire free trail subscriptions for user
	When click on the hamburger menu
	And tap on byjus classes card
	Then verify the user is navigated to the PS screen
	And verify "Recommended Classes" section is present
	And verify that free trail completed card should displayed in For you section
	And verify that masterclasses are scheduled should be displayed in recommended section


Scenario: Verify that when the student reaches the maximum free trail class limit, empty state message like "Hope you enjoyed your free trail class" message should be shown
	Given launch the application online and login as expired user
	When click on the hamburger menu
	And tap on byjus classes card
	Then verify the user is navigated to the PS screen
	And verify that no master card available to book
	And verify expected message is shown once user reaches maximum free trail class limit


Scenario: Verify that user with paid Byju's Classes subscription should not be allowed to book trial class for their paid grade
	Given Launch the application online as paid user
	When click on the hamburger menu
	And tap on byjus classes card
	Then No trial classes should be displayed on their paid grade