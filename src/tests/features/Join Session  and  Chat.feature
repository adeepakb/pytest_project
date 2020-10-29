Feature: Join Session  and  Chat


Scenario: verify that on click of "join now" button student should land on session page successfully
	Given launch the app and navigate to home screen
	Given ensure tutor has started the session
	And tap on Premium School card
	And navigate to one to mega homescreen
	When verify "Join Now" option is enabled for the current day session on your session has started card
	And tap on "Join Now" button
	Then verify user is landed on tutor videoplayer screen


Scenario: verify that when clicking on the close"X" icon the "Live Chat window", the pop-up should close
	Given launch the app and navigate to home screen
	And ensure tutor has started the session
	And tap on Premium School card
	And navigate to one to mega homescreen
	When verify "Join Now" option is enabled for the current day session on your session has started card
	And tap on "Join Now" button
	Then tap on chat icon
	verify Live chat is enabled
	And tap on chat close icon
	And verify that chat window should be closed


Scenario: verify that while clicking on outside of the "Live Chat window" pop-up, the pop-up should close.
	Given launch the app and navigate to home screen
	And ensure tutor has started the session
	And tap on Premium School card
	And navigate to one to mega homescreen
	When verify "Join Now" option is enabled for the current day session on your session has started card
	And tap on "Join Now" button
	Then tap on chat icon
	verify Live chat is enabled
	And tap outside chat layout
	And verify that chat window should be closed


Scenario: verify that student should be able to copy paste the text and send a message to tutor
	Given launch the app and navigate to home screen
	And ensure tutor has started the session
	And tap on Premium School card
	And navigate to one to mega homescreen
	When verify "Join Now" option is enabled for the current day session on your session has started card
	And tap on "Join Now" button
	Then tap on chat icon
	And verify Live chat is enabled
	And tap on "Type something" text box
	Paste the copied text "Hello" in the chat field
	And verify user is able to paste the text "Hello"
	And close tutor session browser tab


Scenario: verify that if tutor disables the chat,student should be able to view live chat disabled text
	Given launch the app and navigate to home screen
	And ensure tutor has started the session
	And tap on Premium School card
	And navigate to one to mega homescreen
	When verify "Join Now" option is enabled for the current day session on your session has started card
	And tap on "Join Now" button
	Then verify user is landed on tutor videoplayer screen
	And switch "off" the tutor chat toggle button
	And tap on chat icon
	And verify Live chat is disabled
	And tap on live chat is disabled text box
	And verify chat dialog should not be displayed
	And switch "on" the tutor chat toggle button
	And close tutor session browser tab


Scenario: verify that on tap of device back button,user should be able to view the "You are on ongoing session right now.Are you sure want to quit the session" pop up with cancel and quit button
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


Scenario: verify that student should be able to "Cancel" ongoing session bottom sheet dialog
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


Scenario: verify that student should be able to "Quit" ongoing session
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


Scenario: verify that in between the session if network issues occurs,Looks like something went wrong pop should be displayed
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


Scenario: verify that Looks like something went wrong pop up should disappear when network is good
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


Scenario: verify that if tutor end the session,student should be able to view the end session pop up stating "Your session has been ended" with okay button
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