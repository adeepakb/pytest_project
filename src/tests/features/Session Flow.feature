Feature: Session Flow


Scenario: Verify that if tutor has not join the session yet, on tap of "join now" button student should be waiting in welcome screen
	Given launch the app and navigate to home screen
	reset student session if the session is incase completed
	And tap on Premium School card
	And navigate to one to mega homescreen
	When verify "Join Now" option is enabled for the current day session on your session has started card
	And tap on "Join Now" button
	Then verify byju's tutor icon
	verify text "Welcome" on welcome screen 
	verify text "{username}!" on welcome screen
	And verify loader 3 dots icon
	And verify text "Waiting for tutor to join the session" on welcome screen
	And verify subject name
	And verify chapter name


Scenario: Verify that on click of "join now" button student should land on session page successfully
	Given launch the app and navigate to home screen
	And ensure tutor has started the session
	And verify reset buffer time is completed
	And tap on Premium School card
	And navigate to one to mega homescreen
	When verify "Join Now" option is enabled for the current day session on your session has started card
	And tap on "Join Now" button
	Then verify user is landed on tutor videoplayer screen
	And close tutor session browser tab


Scenario: Verify that when clicking on the "X" icon the "Live Chat window", the pop-up should close
	Given launch the app and navigate to home screen
	And ensure tutor has started the session
	And tap on Premium School card
	And navigate to one to mega homescreen
	When verify "Join Now" option is enabled for the current day session on your session has started card
	And tap on "Join Now" button
	Then tap on tutor chat icon
	And switch "on" the tutor chat toggle button
	And verify that live chat is launched
	And tap on chat close icon
	And verify that chat window should be closed
	And close tutor session browser tab


Scenario: Verify that while clicking on outside of the "Live Chat window" pop-up, the pop-up should close.
	Given launch the app and navigate to home screen
	And ensure tutor has started the session
	And tap on Premium School card
	And navigate to one to mega homescreen
	When verify "Join Now" option is enabled for the current day session on your session has started card
	And tap on "Join Now" button
	Then tap on tutor chat icon
	And switch "on" the tutor chat toggle button
	And verify that live chat is launched
	And tap outside chat layout
	And verify that chat window should be closed
	And close tutor session browser tab


Scenario: Verify that tutor should be able to approve the messages send by the student and shown in the other students live chat window
	Given launch the app and navigate to home screen
	And ensure tutor has started the session
	And tap on Premium School card
	And navigate to one to mega homescreen
	When verify "Join Now" option is enabled for the current day session on your session has started card
	And tap on "Join Now" button
	Then send "test_approve" message
	And tap on tutor chat icon
	And tap on the tick mark (approve button) in the message
	And Verify that the tutor is able to approve the message "test_approve"
	And login as another student who attends same session
	And verify "Join Now" option is enabled for the current day session on your session has started card
	And tap on "Join Now" button
	And verify that live chat is launched
	And verify that approved message "test_approve" is shown in the other student chat window
	And close tutor session browser tab


Scenario: Verify that tutor should be able to reject the messages send by the student and messages should not shown to the other student
	Given launch the app and navigate to home screen
	And ensure tutor has started the session
	And tap on Premium School card
	And navigate to one to mega homescreen
	When verify "Join Now" option is enabled for the current day session on your session has started card
	And tap on "Join Now" button
	Then send "test_reject" message
	And tap on tutor chat icon
	And tap on "x" button(reject button) shown in the message
	And Verify that the tutor is able to reject the message "test_reject"
	And login as another student who attends same session
	And verify "Join Now" option is enabled for the current day session on your session has started card
	And tap on "Join Now" button
	And verify that live chat is launched
	And verify that rejected message "test_reject" is not shown in the other student chat window
	And close tutor session browser tab


Scenario: Verify that user should copy paste the text in live chat and send a message to teacher
	Given launch the app and navigate to home screen
	And ensure tutor has started the session
	And tap on Premium School card
	And navigate to one to mega homescreen
	When verify "Join Now" option is enabled for the current day session on your session has started card
	And tap on "Join Now" button
	Then verify that live chat is launched
	And tap on "Type something" text box
	And Paste the copied text "Hello" in the chat field
	And verify user is able to paste the text "Hello"
	And close tutor session browser tab


Scenario: Verify that if teacher disable live chat on student side text message stating  live chat disabled should be displayed
	Given launch the app and navigate to home screen
	And ensure tutor has started the session
	And tap on Premium School card
	And navigate to one to mega homescreen
	When verify "Join Now" option is enabled for the current day session on your session has started card
	And tap on "Join Now" button
	Then tap on tutor chat icon
	And switch "off" the tutor chat toggle button
	And verify user is landed on tutor videoplayer screen
	And verify Live chat is disabled
	And tap on live chat is disabled text box
	And verify chat dialog should not be displayed
	And switch "on" the tutor chat toggle button
	And close tutor session browser tab


Scenario: Verify that on tap of device back button,user should be able to view the "You are on ongoing session right now.Are you sure want to quit the session" pop up with cancel and quit button
	Given launch the app and navigate to home screen
	And ensure tutor has started the session
	And tap on Premium School card
	And navigate to one to mega homescreen
	When verify "Join Now" option is enabled for the current day session on your session has started card
	And tap on "Join Now" button
	Then verify user is landed on tutor videoplayer screen
	And tap on device back button
	And verify "You are on an ongoing session right now.\nAre you sure you want to quit?" bottom sheet dialog should be shown
	And verify "Cancel" should be displayed
	And verify "Quit" button should be displayed
	And close tutor session browser tab


Scenario: Verify that on click of "cancel" button student should stay in the session page and continue the session.
	Given launch the app and navigate to home screen
	And ensure tutor has started the session
	And tap on Premium School card
	And navigate to one to mega homescreen
	When verify "Join Now" option is enabled for the current day session on your session has started card
	And tap on "Join Now" button
	Then verify user is landed on tutor videoplayer screen
	And tap on device back button
	And verify "You are on an ongoing session right now.\nAre you sure you want to quit?" bottom sheet dialog should be shown
	And tap on "Cancel" text
	And verify ongoing session bottom sheet dialog should disappear
	And close tutor session browser tab


Scenario: Verify that on click of "Quit" button student should exit from the session page successfully.
	Given launch the app and navigate to home screen
	And ensure tutor has started the session
	And tap on Premium School card
	And navigate to one to mega homescreen
	When verify "Join Now" option is enabled for the current day session on your session has started card
	And tap on "Join Now" button
	Then verify user is landed on tutor videoplayer screen
	And tap on device back button
	verify "You are on an ongoing session right now.\nAre you sure you want to quit?" bottom sheet dialog should be shown
	And tap on "Quit" button
	verify user is landed on one to mega dashboard homescreen
	And close tutor session browser tab


Scenario: Verify that in between the session if network issues occurs,Looks like something went wrong pop should be displayed
	Given launch the app and navigate to home screen
	And ensure tutor has started the session
	And tap on Premium School card
	And navigate to one to mega homescreen
	When verify "Join Now" option is enabled for the current day session on your session has started card
	And tap on "Join Now" button
	Then verify user is landed on tutor videoplayer screen
	And switch "off" the device data
	And verify offline related bottom sheet dialog should be displayed
	verify "Oops! Looks like something went wrong. Please try again after some time." should be displayed
	And switch "on" the device data
	And close tutor session browser tab


Scenario: Verify that Looks like something went wrong pop up should disappear when network is good
	Given launch the app and navigate to home screen
	And ensure tutor has started the session
	And tap on Premium School card
	And navigate to one to mega homescreen
	When verify "Join Now" option is enabled for the current day session on your session has started card
	And tap on "Join Now" button
	Then verify user is landed on tutor videoplayer screen
	switch "off" the device data
	And verify offline related bottom sheet dialog should be displayed
	switch "on" the device data
	And verify offline related bottom sheet dialog should disappear
	And close tutor session browser tab


Scenario: Verify the elements in live chat window
	Given launch the app and navigate to home screen
	And ensure tutor has started the session
	And tap on Premium School card
	And navigate to one to mega homescreen
	When verify "Join Now" option is enabled for the current day session on your session has started card
	And tap on "Join Now" button
	Then verify that live chat is launched
	And verify the text Live chat as header
	And verify chat close button
	And tap on "Type something" text box
	And verify that cursor should point to the first place of the text field
	And verify smileys are disabled
	And close tutor session browser tab


Scenario: Verify that on tap of chat icon,live chat should be launched.
	Given launch the app and navigate to home screen
	And ensure tutor has started the session
	And tap on Premium School card
	And navigate to one to mega homescreen
	When verify "Join Now" option is enabled for the current day session on your session has started card
	And tap on "Join Now" button
	Then verify that live chat is launched
	And tap on "Type something" text box
	And Enter text "Testing" in chat dialog
	And tap on send button in the chat box
	And close tutor session browser tab


Scenario: Verify that user should be able chat in the livechat.
	Given launch the app and navigate to home screen
	And ensure tutor has started the session
	And tap on Premium School card
	And navigate to one to mega homescreen
	When verify "Join Now" option is enabled for the current day session on your session has started card
	And tap on "Join Now" button
	Then verify that live chat is launched
	And tap on "Type something" text box
	And verify chat dialog should be displayed
	And Enter text "Hello" in chat dialog
	And verify user is able to enter the chat text "Hello"
	And tap on send button in the chat box
	And verify student is able to send the typed text "Hello" to tutor
	And close tutor session browser tab


Scenario: Verify that Once joined, the session will start playing video with live chat connected to teacher.
	Given launch the app and navigate to home screen
	And ensure tutor has started the session
	And tap on Premium School card
	And navigate to one to mega homescreen
	When verify "Join Now" option is enabled for the current day session on your session has started card
	And tap on "Join Now" button
	Then verify user is landed on tutor videoplayer screen
	And verify that live chat is launched
	And tap on "Type something" text box
	And Enter text "Chat" in chat dialog
	And tap on send button in the chat box
	And tap on tutor chat icon
	And verify tutor received "Chat" message from student
	And close tutor session browser tab


Scenario: Verify that  students should be able to chat messages toTeacher Assistants
	Given launch the app and navigate to home screen
	And ensure tutor has started the session
	And tap on Premium School card
	And navigate to one to mega homescreen
	When verify "Join Now" option is enabled for the current day session on your session has started card
	And tap on "Join Now" button
	Then tap on tutor chat icon
	And teacher send message "Welcome students" in chat to students
	And verify user is landed on tutor videoplayer screen
	And verify student able to view teacher message "Welcome students"
	And send "Yes teacher" message
	And verify tutor received "Yes teacher" message from student
	And close tutor session browser tab


Scenario: Verify that while rejoining to the session the chat thread should be present
	Given launch the app and navigate to home screen
	And ensure tutor has started the session
	And tap on Premium School card
	And navigate to one to mega homescreen
	When verify "Join Now" option is enabled for the current day session on your session has started card
	And tap on "Join Now" button
	Then verify user is landed on tutor videoplayer screen
	And tap on "Type something" text box
	And verify chat dialog should be displayed
	And Enter text "Hi" in chat dialog
	And tap on send button in the chat box
	And verify user is landed on tutor videoplayer screen
	And tap on device back button
	And tap on "Quit" button present in the ongoing session bottom sheet dialog
	And verify "Join Now" option is enabled for the current day session on your session has started card
	And tap on "Join Now" button
	And verify that live chat is launched
	And verify old chat thread message "Hi" should be displayed in chat window
	And close tutor session browser tab


Scenario: Verify that Video player is going to play a recorded session with Live chat option
	Given launch the app and navigate to home screen
	And ensure tutor has started the session
	And tap on Premium School card
	And navigate to one to mega homescreen
	When verify "Join Now" option is enabled for the current day session on your session has started card
	And tap on "Join Now" button
	Then verify chat icon is displayed
	And tap on chat icon
	verify that live chat is launched
	And verify video elements are present
	And close tutor session browser tab


Scenario: Verify that Video player shouldn't have any controls to seek, pause, play.
	Given launch the app and navigate to home screen
	And ensure tutor has started the session
	And tap on Premium School card
	And navigate to one to mega homescreen
	When verify "Join Now" option is enabled for the current day session on your session has started card
	And tap on "Join Now" button
	Then verify user is landed on tutor videoplayer screen
	verify that videoplayer should not have any controls like seek bar,pause,play icons on the screen
	And close tutor session browser tab


Scenario: Verify the elements in Tutor's chat window when student send a message to tutor
	Given launch the app and navigate to home screen
	And ensure tutor has started the session
	When verify elements in Tutor's chat window
	Then Verify when student sends message student name is shown
	And Verify that Ban button , Approve button and Reject button is shown
	And close tutor session browser tab


Scenario: Verify that if a session was started late for any reason then the join now button should show up until the session ends.
	Given launch the app and navigate to home screen
	And ensure tutor has started the session
	And tap on Premium School card
	And navigate to one to mega homescreen
	When verify "Join Now" option is enabled for the current day session on your session has started card
	And tap on "Join Now" button
	Then verify user is landed on tutor videoplayer screen
	And close tutor session browser tab


Scenario: Verify that while clicking on Ban button "Ban Student" pop-up should be shown with the following details
	Given launch the app and navigate to home screen
	And ensure tutor has started the session
	When tap on tutor chat icon
	Then tap on Ban button
	And Verify that "Ban the student" pop-up should be shown with the options as "Inappropriate Content","Abusive Language","Content Sharing" and "Others" along with radio button and "Cancel" and "Ban" buttons
	And Verify that Inappropriate Content should be selected by default
	And Verify that while clicking on Cancel button the pop-up should go off
	And Verify the while clicking outside of the pop-up it should go off
	And Verify on clicking on Ban button user should be banned and banned student messages should not be shown
	And close tutor session browser tab


Scenario: Verify that if tutor end the session,student should be able to view the end session pop up stating "Your session has been ended" with okay button
	Given launch the app and navigate to home screen
	And ensure tutor has started the session
	And tap on Premium School card
	And navigate to one to mega homescreen
	When verify "Join Now" option is enabled for the current day session on your session has started card
	And tap on "Join Now" button
	Then verify user is landed on tutor videoplayer screen
	tutor ends session
	And verify "Your session has ended!" bottom sheet dialog should be shown
	And verify "Okay" button should be displayed
	And tap on "Okay" button
	And verify "Your session has ended!" bottom sheet dialog is not shown
	And close tutor session browser tab