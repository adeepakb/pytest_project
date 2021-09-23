Feature: Rate Session screen - Post session end


Scenario: Verify that after session ended rate session screen should be displayed
	Given launch the application online and navigate to home screen
	And reset student session and start session
	When tap on premium school card
	Then click on session card
	And tap on "Join Now" button
	And tutor should end the session
	And tap on Okay button
	And verify text "Rate this session" on Rate Session card


Scenario: Verify that rate session consist of following elements
	Given launch the application online and navigate to home screen
	When tap on premium school card
	Then verify user is in premium school-home screen
	And verify "Rate Now" button is displayed
	And tap on "Rate Now" button
	And verify text "Rate this session" on Rate Session card
	And verify text "Rate Your Session" on Rate Session card
	And verify text "Share your experience with us!" on Rate Session card


Scenario: Verify that when user provide a rating between 1-3 following elements should be displayed
	Given launch the application online and navigate to home screen
	When tap on premium school card
	Then verify user is in premium school-home screen
	And verify "Rate Now" button is displayed
	And tap on "Rate Now" button
	And verify text "Rate this session" on Rate Session card
	And tap of rating option "1"
	And verify text "What went Wrong?" on Rate Session card
	And verify text "Sorry about this! Write to us on how we can better this session/experience for you" on Rate Session card
	And verify feedback option "1"- "Technical Issues" with a checkbox is present
	And verify feedback option "2"- "Teaching Quality" with a checkbox is present
	And verify feedback option "3"- "Pace of teaching was fast" with a checkbox is present
	And verify feedback option "4"- "Pace of teaching was slow" with a checkbox is present
	And verify "Submit" button is displayed


Scenario: Verify that when user provide a rating between 4-5 following elements should be displayed
	Given launch the application online and navigate to home screen
	When tap on premium school card
	Then verify user is in premium school-home screen
	And verify "Rate Now" button is displayed
	And tap on "Rate Now" button
	And verify text "Rate this session" on Rate Session card
	And tap of rating option "4"
	And verify text "We are glad you had a great session." on Rate Session card
	And verify "Submit" button is displayed


Scenario: Verify that user is able to select and deselect the option on rate session screen
	Given launch the application online and navigate to home screen
	When tap on premium school card
	Then verify user is in premium school-home screen
	Then verify "Rate Now" button is displayed
	And tap on "Rate Now" button
	And verify text "Rate this session" on Rate Session card
	And tap on each star and verify user is able to select the stars
	And deselect the selected stars and verify user is able to deselect the selected stars
	And verify "Submit" button is displayed


Scenario: Verify that on tap of back icon user should be navigated to premium school home screen
	Given launch the application online and navigate to home screen
	When tap on premium school card
	Then verify user is in premium school-home screen
	And verify "Rate Now" button is displayed
	And tap on "Rate Now" button
	And verify text "Rate this session" on Rate Session card
	And tap on back navigation icon
	And verify user is in premium school-home screen


Scenario: Verify that in session   details screen rate session option is present
	Given launch the application online and navigate to home screen
	When tap on premium school card
	Then verify user is in premium school-home screen
	And tap on session card
	And verify "Rate Now" button is displayed
	And verify text "How was your experience ?" on Rate Session card
	And verify text "Tell us so that we can improve" on Rate Session card


Scenario: Verify that If Last Session has Post Requisites && Last Session is Not Rated in For you tab rate session option should be present
	Given launch the application online and navigate to home screen
	And post-requisite "auto-post-assessment-video" should be tagged for the particular classroom session
	When tap on premium school card
	Then verify user is in premium school-home screen
	And verify text "Rate Your Session" is present
	And verify text "Let us know your experience" is present
	And verify "Rate Now" button is displayed
	And tap on "Rate Now" button
	And verify text "Rate this session" on Rate Session card


Scenario: Verify If Last Session has no Post Requisites && Last Session is Not Rated) should Show Last completed session card in "For you" screen with "Ratings Star" Options
	Given launch the application online and navigate to home screen
	#And detach post requisite for latest session
	When tap on premium school card
	Then verify user is in premium school-home screen
	And verify "Rate Now" button is displayed
	And tap on "Rate Now" button
	And verify text "Rate this session" on Rate Session card
	And tap of rating option "4"
	And tap on Submit button


Scenario: Verify If Last Session has Post Requisites && Last Session is Rated)    in "For You" Screen with Post requisites should show rating provided by the user on the card
	Given launch the application online and navigate to home screen
	And post-requisite "auto-post-assessment-video" should be tagged for the particular classroom session
	When tap on premium school card
	Then verify user is in premium school-home screen
	And verify in For you tab rated count "4" is displayed


Scenario: Verify that in session  details screen rating should be present
	Given launch the application online and navigate to home screen
	#And detach post requisite for latest session
	When tap on premium school card
	Then verify user is in premium school-home screen
	And tap on "Completed" tab
	And tap on session card
	And verify user rating "4" is reflected on Session details screen