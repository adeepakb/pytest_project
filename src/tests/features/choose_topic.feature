Feature: choose_topic

Scenario: Verify elements in session details section
Given Launch the tutor app online
And navigate to one to many student dashboard screen
When tap on any future scheduled session card
Then verify session details card is loaded
And verify text "SESSION DETAILS" should be displayed
And verify subject name should be displayed
And verify topic name should be displayed
And verify date,month,day details should be displayed
And verify time details should be displayed
And verify topic description details should be displayed
And verify choose a topic to learn card should be displayed
And verify text Learn what you want text should be displayed in choose a topic to learn card
And verify Choose Topic button is displayed
And verify text you can choose a topic till 4 days prior to the session below the choose a topic to learn card


Scenario: Verify taping on Choose topic button should shown a list of topics associated to the respective subject and grade
Given Launch the tutor app online
And navigate to one to many student dashboard screen
When tap on any future scheduled session card
And tap on choose topic button
Then verify change topic section is displayed
And verify topics are displayed under change topic section
And verify "Done" button is displayed
And verify close button is displayed
And tap on any topic which is displayed under change topic section
And verify selected topic button is highlighted
And tap on Done button
###
####
Scenario: Verify tapping on Cancel icon in choose topic card should land back on session details card.
Given Launch the tutor app online
And navigate to one to many student dashboard screen
When tap on any future scheduled session card
And tap on choose topic button
Then verify change topic section is displayed
And tap on close button
And verify user is on session details card
##
##
##
Scenario: Verify tapping on "Choose Topic" button in offline mode, should show network validation card
Given Launch the tutor app online
And navigate to one to many student dashboard screen
When tap on any future scheduled session card
And switch off the device data
Then tap on choose topic button
And verify text "Oops! Something went wrong" with icon
And verify text "Please check internet connection and try again".
And verify Retry button should be displayed
And switch on the device data
And tap on Retry button
And tap on close button
And verify session details card is loaded with all the required elements


Scenario: Verify Choose topic card should be shown only if the session scheduled post 2 days
Given Launch the tutor app online
And navigate to one to many student dashboard screen
When verify by default "UP NEXT" session card should be selected
Then verify if next session countdown timer reaches the session start time, then "JOIN NOW" button should be shown
And verify if next session is scheduled post 2 days, then "Choose topic" card should be shown.
And verify if next session is scheduled with in 2 days, then session starts cards shown with days remaining count
And Verify if next session starts with in 1 day then session countdown timer will be shown.

Scenario: Verify able to switch session card on taping on other card
Given Launch the tutor app online
And navigate to one to many student dashboard screen
When verify by default "UP NEXT" session card should be selected
And tap on any session card
Then verify respective session details card should be loaded
#
Scenario: Verify text You can choose a topic till 2 days prior to the session should not be shown under session starts card.
Given Launch the tutor app online
And navigate to one to many student dashboard screen
When Verify by default up next session card get highlighted.
Then Verify if next session is in prior to 2 days the session starts card should be shown
Then verify  text "You can choose a topic till 2 days prior to the session" should not be shown under session starts card.



#
##--------------------------------------------------------------------------------------------------------------------------#
#
Scenario: Verify "Up Next" badge on the next session card.
Given Launch the tutor app online
And navigate to one to many student dashboard screen
When Verify by default next session card should be highlighted.
Then Verify "Up Next" badge should be present on the next session card.

Scenario: Verify that in choose topic user is able to scroll the screen.
Given Launch the tutor app online
And navigate to one to many student dashboard screen
When Select a session card which is post 2 days from current date.
And Session details card with <Choose Topics> card loads.
And Tap on <Choose topic> button.
And verify CHANGE TOPIC card is displayed
And verify list of topics are shown with radio button
Then Verify user should be able to scroll the <Choose Topic> list on both upwards and downwards.
#
Scenario: Verify that after selecting the topic from the "CHOOSE TOPIC" respective topic should be updated in both 'SESSION DETAILS' and 'SCHEDULED SESSION' card
Given Launch the tutor app online
And navigate to one to many student dashboard screen
And Select a session card which is post 2 days from current date.
And Session details card with <Choose Topics> card loads.
And Tap on <Choose topic> button.
And verify CHANGE TOPIC card is displayed
And verify list of topics are shown with radio button
When tap on radio button
And verify user is able to select the particular topic on taping on radio button.
And verify subtopics are displayed for the selected topic
And select another topic by tapping on radio button
And verify only one topic should be selected at a time with associated subtopics
And Tap on <DONE> button
Then Verify that selected topic should be updated in both 'SESSION DETAILS' and 'SCHEDULED SESSION' card

Scenario: Verify that choose topic card color should be displayed based on subject
Given Launch the tutor app online
And navigate to one to many student dashboard screen
When Select a session card which is post 2 days from current date.
And Session details card with <Choose Topics> card loads.
Then Verify that choose topic card color should be displayed based on subject.
