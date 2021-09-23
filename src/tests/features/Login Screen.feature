Feature: Login Screen


Scenario: Verify the elements in Login screen
	Given Launch the app online
	When Navigate to Login screen
	Then Verify the "Premium Login" text
	And Mobile Number field with auto filled country code
	And Verify the "We will send a 4 digit OTP to verify" text
	And Verify the "Next" Button
	And Verify the "Not a premium user?" text
	And Verify the "Start Free Trial of" text
	And Verify the "Byjus the learning app" app icon.


Scenario: Verify the elements on the Login screen
	Given Launch the app online
	When Navigate to Login screen
	Then Verify the "Premium Login" text is shown.
	And verify the text "Mobile Number".
	And verify that auto-filled country code drop-down field is shown.
	And verify that the Mobile Number text field is shown.
	And Verify the text "We will send a 4 digit OTP to verify" is shown.
	And Verify the "Next" button is shown.


Scenario: Verify that Country Code should be a drop down menu. By default India(+91) should be selected in the drop down menu.
	Given User is new to the app and device ID is not saved in the server
	And Launch the app online and navigate to Login screen
	When User taps on Country Code menu
	Then Verify Country Code should be a drop down menu
	And By default "India(+91)" should be selected in the drop down menu.


Scenario: Verify that User should be able to select any Country Code and respective Country name from the drop down
	Given Launch the app online and Navigate to Login screen
	When User taps on Country Code menu
	And select any  from the drop down
	Then Verify selected  should be shown in country code field
	Examples:
		|countryCode|code|
		|Cook Islands (+682)|+682|


Scenario: Verify that GCC Countries should be on the top in the Country code drop down followed by other countries in Alphabetical order.
	Given Launch the app online
	And Navigate to Login screen
	When On Login screen tap on country code drop down
	Then Verify GCC countries mentioned below should be displayed first
	And verify these listed countries are displayed first and in the same order as mentioned "India(+91),UAE(+971),Bahrain(+973),Kuwait(+965),Oman(+968),Qatar(+974),Saudi Arabia(+966),United Arab Emirates (+971)"
	And verify all the  other countries apart from 8 are displayed in Alphabetical order


Scenario: Verify that tapping on Mobile Number field numeric keypad gets activated and should accept only Numeric values
	Given Launch the app online and Navigate to Login screen
	When User taps on Mobile Number field
	Then Verify numeric keypad gets activated
	And should accept only Numeric values


Scenario: Verify that when users enter mobile number below 7 digits for all Countries including India mobile Number field should be validated with error message 'Please enter valid mobile number'
	Given Launch the app online and Navigate to Login screen
	When User taps on Mobile Number field
	And Enters  Mobile Number field
	And taps on Next Button
	Then Verify error message "Please enter valid mobile number" is displayed below mobile number field
	Examples:
	|DigitsBelow7|
	|123456|


Scenario: Verify that when users enter mobile number above 15 digits for all Countries including India mobile Number field should be validated with error message 'Please enter valid mobile number'
	Given Launch the app online and Navigate to Login screen
	When User taps on Mobile Number field
	And enters  in Mobile Number field
	And taps on Next Button
	Then Verify error message "Please enter valid mobile number" is displayed below mobile number field
	Examples:
	|DigitsAbove15|
	|1234567891234567|


Scenario: Verify that for the new users mobile number field should be empty on Login Screen
	Given Device id is not saved in server
	And launch the app online.
	When User Navigate to Login screen
	Then Verify for the new users mobile number Field should be empty on Login Screen.


Scenario: Verify that for the existing users mobile number should be prefilled on Login Screen.
	Given Device id is saved in server
	And Launch the app online
	When User navigates to Login screen
	Then Previously logged in user  should be prefilled on Login Screen


Scenario: Verify that tapping on Next button after entering the valid Mobile number should redirect the user to OTP verification Screen
	Given Launch the app online and Navigate to Login screen
	When User enters valid
	And taps on Next Button
	Then User should navigate to LoginOTPVerificationScreen
	Examples:
	|MobileNumber|
	|9871234|


Scenario: Verify that tapping on back button in Login screen should close the app
	Given Launch the app online and Navigate to Login screen
	When taps on Device back button
	Then Verify  should be closed
	Examples:
	|App|
	|com.byjus.thelearningapp|


Scenario: Verify that tapping outside the bottom sheet dialog having "This phone number is not registered with a premium account", should dismiss the bottom sheet dialog.
	Given Launch the app online and Navigate to Login screen
	When User enters  in Mobile Number Field
	And taps on Next Button
	Then Verify the "This phone number is not registered with a premium account." text
	And tap outside the dialog
	And Verify "Phone number is not registered with a premium account." bottom sheet dialog dismissed
	Examples:
	|UnregisteredNnumber|
	|9875643245|


Scenario: Verify that tapping on  option "Try Again" should empty the user mobile number field on Premium Login screen.
	Given Launch the app online and Navigate to Login screen
	And User enters  in Mobile Number Field
	And taps on Next Button
	When The bottom sheet is displayed.
	And tap on "Try Again" button
	Then Verify user is redirected to Premium Login screen with empty user mobile number field.


Scenario: Verify that tapping on option "Contact Us" should redirect the user to Phone dialer with Phone number prefilled(+91-9241333666)
	Given Launch the app online and Navigate to Login screen
	When User enters  in Mobile Number Field
	And taps on Next Button
	Then Verify the "This phone number is not registered with a premium account." text
	And tap on 'Contact Us' button
	And Verify user is redirected to Phone dialer with Phone number prefilled(+91-9241333666)
	Examples:
	|UnregisteredNnumber|
	|9875643245|


Scenario: Verify that tapping on option "Contact Us" should redirect the user to Phone dialer and device back button, navigate back to Premium app.
	Given Launch the app online and Navigate to Premium Login screen.
	And User enters  in Mobile Number Field
	And taps on Next Button
	When The bottom sheet appears.
	And tap on 'Contact Us' link
	Examples:
	|UnregisteredNnumber|
	|9875643245|
	Then Verify user is redirected to Phone dialer with Phone number prefilled(+91-9241333666)


Scenario: Verify that tapping on  'Byjus the Learning App' app icon, navigates the user to Play store ''Byju's The Learning App.''
	Given Launch the app online and Navigate to Premium Login screen.
	When Tap on 'Byjus the Learning App' icon .
	Then Verify that tapping on 'Byjus the Learning App' app icon, navigates the user to Play store 'Byju's The Learning App.'


Scenario: Verify that User having sibling navigates to Sibling page
	Given Launch the app online
	And Navigate to Premium Login screen
	When User enters valid  having multiple accounts
	And taps on Next Button
	And enter valid otp in Verify OTP Screen
	Then Verify that User navigates to Sibling screen which list multiple accounts


Scenario: Verify that User lands to Sibling screen, text  "We found multiple accounts registered to the number you provided. Select the correct one." is shown.
	Given Launch the app online
	And Navigate to Premium Login screen
	When User enters valid  having multiple accounts
	And taps on Next Button
	And enter valid otp in Verify OTP Screen.
	Then Verify that User navigates to Sibling page having below mentioned text.


Scenario: Verify that User lands to Sibling page having list of accounts with name and grade
	Given Launch the app online
	And Navigate to Premium Login screen
	When User enters valid  having multiple accounts
	And taps on Next Button
	And enter valid otp in Verify OTP Screen
	Then Verify that User navigates to Sibling page having list of accounts with name and grade


Scenario: Verify that the radio button is present for users having  multiple accounts in sibling screen.
	Given Launch the app online
	And Navigate to Premium Login screen
	When User enters valid  having multiple accounts
	And taps on Next Button
	And enter valid otp in Verify OTP Screen
	And navigates to sibling page.
	Then Verify that the radio button is present for users having multiple accounts in the sibling screen.


Scenario: Verify that user clicks on 'Continue' button without selecting the account, it will display error toast message as 'Please select account to Login'.
	Given Launch the app online
	And Navigate to Premium Login screen
	When User enters valid  having multiple accounts
	And taps on Next Button
	And enter valid otp in Verify OTP Screen
	And navigates to Siblings screen.
	Then Verify that user clicks on 'Continue' button without selecting the account, it will display error toast message as 'Please select account to Login'.


Scenario: Verify the user navigates to Welcome Screen after selection of siblings account and tapping on Continue button.
	Given Launch the app online
	And Navigate to Premium Login screen
	When User enters valid  having multiple accounts
	And taps on Next Button
	And enter valid otp in Verify OTP Screen
	And navigates to a sibling screen.
	And Select the account from the list of multiple accounts.
	And Click on 'Continue' button
	Then Verify the user navigates Welcome Screen


Scenario: Verify that after selection of siblings account tapping on Continue button on Welcome screen should navigate to Home Screen.
	Given Launch the app online
	And Navigate to Premium Login screen
	When User enters valid  having multiple accounts
	And taps on Next Button
	And enter valid otp in Verify OTP Screen
	And navigates to a sibling screen.
	And Select the account from the list of multiple accounts.
	And tap on the 'Continue' button
	And navigates Welcome Screen
	And tap on the 'Continue' button
	Then Verify the user should be navigating to Home Screen


Scenario: Verify that tapping on device back button should dismiss the 'Phone number is not registered with a premium account' bottom sheet dialog
	Given Launch the app online and Navigate to Login screen
	When User enters  in Mobile Number Field
	And taps on Next Button
	Then Verify the "This phone number is not registered with a premium account." bottom sheet dialog.
	And taps on Device back button
	And Verify "Phone number is not registered with a premium account." bottom sheet dialog dismissed
	Examples:
	|UnregisteredNnumber|
	|9875643245|


Scenario: Verify that if user tries to Login with an unregistered number then it should show a bottom sheet dialog with message "This phone number is not registered. Please register to continue" along with "Register" button.
	Given Launch the app online and Navigate to Login screen
	When User enters  in Mobile Number Field
	And taps on Next Button
	Then Verify the "This phone number is not registered with a premium account." text
	And Verify "Try again" button
	And Verify "Contact Us" link
	Examples:
	|UnregisteredNnumber|
	|9875643245|


Scenario: Verify that tapping on option "Try Again" should redirect the user to Premium Login screen
	Given Launch the app online and Navigate to Login screen
	And User enters  in Mobile Number Field
	And taps on Next Button
	When The bottom sheet is displayed.
	And tap on "Try again" button
	Then Verify that the bottom sheet is dismissed.
	And login screen should be displayed.


Scenario: Verify that if user tries to Login with an unregistered number then it should show a bottom sheet dialog with message "This phone number is not registered with a premium account" along with "Try again" & "Contact Us" button.
	Given Launch the app online and Navigate to Login screen
	When User enters  in Mobile Number Field
	And taps on Next Button
	Then Verify the text "This phone number is not registered with a premium account.",
	And "Try again" button,
	And "Contact Us" button.
