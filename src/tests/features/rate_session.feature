Feature: rate_session

Scenario: Verify Rate Session hyperlink shown on the completed session cards
Given navigate to home page and verify student profile
When Verify user has completed atleast a session
Then verify "Rate Session" hyperlink shown on the completed session cards

Scenario: Verify taping on Rate Session hyperlink should show session details card
Given navigate to home page and verify student profile
When Verify user has completed atleast a session
And tap on "Rate Session" hyperlink
Then verify session details card is shown
And verify the badge text "COMPLETED" should be shown
And verify the  text completed should be in green colour RGB value "(110, 226, 158)"

Scenario: Verify Rate Session card  should have all the required elements
Given navigate to home page and verify student profile
When Verify user has completed atleast a session
And tap on "Rate Session" hyperlink
Then verify session details card is shown
Then verify text "How was your experience?" on Rate Session card
And verify text "Tell us so that we can improve" on Rate Session card
And verify "Rate Session" button is displayed

Scenario: Verify taping on Rate Session button should display Rate your session card
Given navigate to home page and verify student profile
When Verify user has completed atleast a session
And tap on "Rate Session" hyperlink
Then verify session details card is shown
Then tap on Rate Session button
And verify all Rate your session card details are displayed
And tap on close button
And verify session details card is shown
And tap on Rate Session button
And verify all Rate your session card details are displayed
And tap on device back button
And verify session details card is shown

Scenario: Verify Rate  your Session card  should have all the required elements
Given navigate to home page and verify student profile
When Verify user has completed atleast a session
And tap on "Rate Session" hyperlink
Then verify session details card is shown
Then tap on Rate Session button
Then verify text "RATE YOUR SESSION" at the top
And Verify Cancel button
And verify all Rate your session card details are displayed

Scenario: Verify tapping on close button in Rate your session card should close the Rate your session card
Given navigate to home page and verify student profile
When Verify user has completed atleast a session
And tap on "Rate Session" hyperlink
Then verify session details card is shown
And tap on Rate Session button
And verify all Rate your session card details are displayed
And tap on close button
Then verify session details card is shown

Scenario: Verify selecting and deselecting stars on Rate your session card
Given navigate to home page and verify student profile
When Verify user has completed atleast a session
And tap on "Rate Session" hyperlink
Then verify session details card is shown
And tap on Rate Session button
And verify all Rate your session card details are displayed
And tap on each star and verify user is able to select the stars
And deselect the selected stars and verify user is able to deselect the selected stars

Scenario: Verify submitted rating should reflect on the session card
Given navigate to home page and verify student profile
When Verify user has completed atleast a session
When tap on "Rate Session" hyperlink
Then tap on Rate Session button
And verify "Submit" button should be disabled state before selecting any stars
And tap on a star
And verify "Submit" button is enabled
Then tap on Submit button
Then verify user rating "1.0" is reflected on Session details screen
And verify user given rating "1.0" should be reflecting on the session card
And verify Rate Session hyperlink  text should not be shown on the  rated  session card

Scenario: Verify tapping on Rate session hyperlink in offline mode should display offline related message
Given navigate to home page and verify student profile
When Verify user has completed atleast a session
When switch "off" the device data
And tap on "Rate Session" hyperlink
Then verify offline message "Oops! Something went wrong" text is shown
And tap on any previous session card
And verify offline message "Oops! Something went wrong" text is shown
And switch "on" the device data

Scenario: Verify elements in offline message card
Given navigate to home page and verify student profile
When Verify user has completed atleast a session
When switch "off" the device data
And tap on "Rate Session" hyperlink
Then verify text "Oops! Something went wrong" with icon
And verify text "Please check internet connection and try again"
And verify "Retry" button is displayed
And switch "on" the device data
