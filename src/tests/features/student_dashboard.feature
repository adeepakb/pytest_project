Feature: student_dashboard

#Scenario: Verify if student subscribed only to one to many then after login should land on one to many student dashboard
#Given Clean launch the tutor app online
#And "Allow" all the app permissions
#And Verify that user is landed on login screen
#When Enter registered mobile number in mobile number field
#And tap on "Next" button
#And verify auto verify bottom sheet dialog is displayed
#And enter a valid otp in the otp field
#Then verify user is landed on one to many student dashboard screen
#And minimize the app by tapping on device back button
#And Launch the app again
#And verify user is landed on one to many student dashboard

Scenario: Verify elements in one to many student dashboard.
Given Launch the tutor app online
When navigate to one to many student dashboard screen
Then verify user is landed on one to many student dashboard screen
And verify Byjus icon followed by "BYJU'S TUTOR | Classroom" text
And verify "Sessions in" Month 'YY text
And verify by default "UP NEXT" session card should be selected
And verify by default current month should be selected
And verify previous sessions cards are displayed
And verify Future session cards are displayed
And verify SESSION DETAILS card is displayed

Scenario: Verify elements in Session card
Given Launch the tutor app online
When navigate to one to many student dashboard screen
And verify user is landed on one to many student dashboard screen
Then verify subject icon in session card
And verify subject name in the session card is displayed
And verify topic name in the session card is displayed
And verify DD MMM, DAY,HH:MM AM/PM details are displayed
And verify Rate Session option is displayed

Scenario: Verify elements in SESSION DETAILS card
Given Launch the tutor app online
When navigate to one to many student dashboard screen
Then verify SESSION DETAILS card is displayed
And verify text "SESSION DETAILS"
And verify subject name is displayed
And verify topic name is displayed
And verify calender icon followed by date format DD MMM,Day is displayed
And verify time icon followed by HH:MM AM/PM details are displayed
And verify topic description
Then verify Change topic card is displayed if session starts in post 2 days
And verify Your session starts in with day is displayed if session starts within 2 days
And verify session starts timer is displayed if session starts within 24 hours

Scenario: verify offline related message is displayed when user taps on any session card
Given Launch the tutor app online
When navigate to one to many student dashboard screen
And switch off the device data
Then tap on any session card
And verify "Oops! something went wrong" text should be displayed on card
And verify "Please check internet connection and try again" text is displayed
And verify Retry button should be displayed
And switch on the device data
And tap on Retry button
And verify respective session details are loaded


