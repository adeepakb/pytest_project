Feature: Profile Screen

Scenario: Verify the fields in profile for logged In user
	Given Launch the app online
	And User is Logged In user with some data.
	And User taps on profile card on hamburger menu
	When User is in profile screen
	Then Verify that back arrow on the top left corner
	And Profile Image beside Profile name (Default Avatar) with Edit option
	And Profile Name below the profile image.
	And My badges below that profile name with badges name.
	And Course Selection drop down below the profile name
	And Profile Completeness Progression in Percentage

Scenario: Verify that tapping on edit option on Profile image should display a pop up with list of avatars
	Given Launch the app
	And User is in profile screen
	When User taps on profile image
	Then Verify that User should be displayed popup with list of avatars


Scenario: Verify in pop up that it should have a label avatar followed by list of Avatar images
	Given Launch the app
	When User is in Avatar popup
	Then Verify that avatar label and list avatar should be displayed

@Sanity
Scenario: Verify that user should be able to select an Avatar
	Given Launch the app
	And User is in Avatar popup
	When User selects the profile image
	Then Verify that user navigate back to profile screen and profile image should be changed


Scenario: Verify that tapping on device back button should dismiss the pop up
	Given Launch the app
	And User is in Avatar popup
	When User taps on device back button
	Then Verify that popup should be dismissed

@Sanity
Scenario: Verify that without selecting any avatar when user dismiss the avatar  bottom sheet dialog, old image should be retained.
	Given Launch the app
	And User is in Avatar popup
	When User comes out of popup without selecting an avatar
	Then Verify that Old image should be retained in profile screen

@Sanity
Scenario: Verify that tapping on course selection drop down in profile screen should display a bottom sheet dialog with list of all Courses.
	Given Launch the app
	And User is in profile screen
	When User taps on course selection drop down
	Then Verify that user should taken to bottom sheet dialog with list of all courses

Scenario: Verify that tick mark should be shown next to course for which user is enrolled
	Given Launch the app
	And User taps on course selection drop down
	When User is in course selection sheet
	Then Verify that tick mark should be shown for enrolled user
#
@Sanity
Scenario: Verify that radio button option should be selected for the current course
	Given Launch the app
	And User taps on course selection drop down
	When User is in course selection sheet
	Then Verify that radio button is selected for current course


Scenario: Verify that user should able to dismiss the dialog by tapping the device back button
	Given Launch the app
	And User taps on course selection drop down
	When User is in course selection sheet
	And tap on device back button
	Then Verify that course selection dialog should be dismissed


#Scenario: Verify that my badges in profile screen should be shown message and should have earn your first badge button
#	Given Launch the app
#	And User enroll course for first time
#	When User is in profile screen
#	Then Verify that message should be shown "You don�t have any badges."
#	And should have "Earn Your First Badge" button
#
#
#Scenario: Verify that all badges and see all forward arrow under my badges
#	Given Launch the app
#	And User earned few badges
#	When User is in profile screen
#	Then Verify that all badges and see all forward arrow should be displayed
#
#
#Scenario: Verify that only three badges under my badges
#	Given Launch the app
#	And User earned three badges
#	When User is in profile screen
#	Then Verify that only three badges should be displayed
#
#
#Scenario: Verify that tapping on see all button under my badges should navigate user to badges screen
#	Given Launch the app
#	And User is in profile screen
#	When User taps on see all button under my badges
#	Then Verify that user should be navigate to "Earned Badges Screen"
#
#
#Scenario: Verify that updating profile details(both Gender and Date of birth) for a new user updates profile completeness to 100% in profile screen.
#	Given Launch the app
#	And User is in profile screen
#	When User updates both date of birth and gender in profile details
#	Then Verify that profile completion section updates to "100%"
#
#
#Scenario: Verify that account details section has mobile number field
#	Given Launch the app online
#	When user is in profile screen
#	Then Verify that mobile number field should be displayed
#
#
#Scenario: Verify that mobile number has a phone icon to the left and a edit icon to the right
#	Given Launch the app online
#	When user is in profile screen
#	Then Verify that mobile number has a phone icon to the left and a <Edit> icon to the right should be displayed
#
#
#Scenario: Verify that tapping on edit icon should displays a pop-up with options to switch country code and  mobile number with submit button
#	Given Launch the app online
#	And user is in profile screen
#	When User taps on edit of mobile number field
#	Then Verify that Edit icon should displays a pop-up "Please enter your phone number" with options to switch country code and enter mobile number with submit button
#
#
#Scenario: Verify that tapping on submit button in the pop-up without entering a number displays error message
#	Given Launch the app online
#	And user is in profile screen
#	When Remove the existing mobile number
#	And User taps on submit button
#	Then Verify that "Please enter your mobile number" error message should be displayed
#
#
#Scenario: Verify that tapping submit button in pop-up by entering an invalid number (lesser or greater than 10 digits) displays valid error message
#	Given Launch the app online
#	And user is in profile screen
#	When User enter invalid mobile number
#	Then Verify that "Please enter your mobile number" error message should be displayed
#
#
#Scenario: Verify that tapping device back button or anywhere outside the pop-up dismiss the pop-up
#	Given Launch the app online
#	And user is in profile screen
#	When User taps on device back button /anywhere outside that popup
#	Then Verify that change number popup should be displayed
#
#
#Scenario: Verify that tapping on submit with an existing number displays an error
#	Given Launch the app online
#	And user is in profile screen
#	When User taps on submit button with existing mobile number
#	Then Verify that "You entered same number" error message should be displayed
#
#@Sanity
#Scenario: Verify that changing mobile number and tapping submit button should redirect user to OTP screen
#	Given Launch the app online
#	And user is in profile screen
#	When User changes the mobile number
#	Then Verify that user should be navigate to OTP screen
#
#
#Scenario: Verify that tapping on cancel button on popup should dismiss the popup
#	Given Launch the app online
#	And user is in profile screen
#	When User taps on cancel button on popup
#	Then Verify that popup should be dismissed
#
#@Sanity
#Scenario: Verify the fields in profile details
#	Given Launch the App online
#	When user is in profile screen
#	Then Verify that Profile Details has all fields <Name>
#	And <Email>
#	And <Gender>
#	And <Location>
#	And <Birthday>
#	And <SignOut>
#
#
#
#Scenario: Verify that tapping on edit button of  add your gender redirects to edit profile screen.
#	Given Launch the app online
#	And user is in profile screen
#	When User taps on edit button of gender in edit profile screen
#	Then Verify that user redirects to edit gender profile screen.
#
#
#Scenario: Verify that tapping on edit button of add your birthday redirects to edit profile screen
#	Given Launch the app online
#	And user is in profile screen
#	When User taps on edit button of birthday in edit profile screen
#	Then Verify that user redirects to edit birthday profile screen.
#
#
#Scenario: Verify that tapping on edit button redirects to edit profile screen
#	Given Launch the app online
#	And user is in profile screen
#	When User taps on edit button of profile details
#	Then Verify that user redirects to edit profile screen.
#
#
#Scenario: Verify that tapping on back arrow at the top in edit profile page discards any changes made and returns to profile screen.
#	Given Launch the app online
#	And User is in edit profile screen
#	When User taps on back arrow
#	Then Verify that user redirects to profile screen
#
#
#Scenario: Verify the fields in edit profile screen
#	Given Launch the app online
#	When User is in edit profile screen
#	Then Verify that back arrow on the top left corner
#	And A text "Edit Profile" below the app back arrow
#	And Name field with icon
#	And Email field with icon
#	And Gender field with icon
#	And Location field with icon
#	And Birthday field with icon
#	And "Save" button bottom of the page
#
#
#Scenario: Verify that tapping on name field displays the text keypad and the field becomes editable.
#	Given Launch the app online
#	And User is in edit profile screen
#	When User taps on name field
#	Then Verify that name field should be editable
#
#
#Scenario: Verify that tapping on email field displays the text keypad and the field becomes editable
#	Given Launch the app online
#	And User is in edit profile screen
#	When User taps on email field
#	Then Verify that email field should be editable
#
#
#Scenario: Verify that tapping on select gender field displays a drop down list and has options Male/Female and any one is selectable at a time
#	Given Launch the app online
#	And User is in edit profile screen
#	When User taps on gender field
#	Then Verify that gender drop down displayed and any one should be selectable
#
#
#Scenario: Verify that tapping on location field displays the text field and enter a characters
#	Given Launch the app online
#	And User is in edit profile screen
#	When User taps on location field
#	Then Verify that location field should be editable
#
#
#Scenario: Verify that tapping on location field auto detect should display the message auto detecting location  and it should detect current location
#	Given Launch the app online
#	And User is in edit profile screen
#	When User taps on auto detect
#	Then Verify that it should detect current location
#
#
#Scenario: Verify that tapping on set button in calendar popup should update the date
#	Given Launch the app online
#	And User is in edit profile screen
#	When User taps on set button in calendar popup
#	Then Verify that calendar popup should update the date
#
#
#Scenario: Verify that tapping on cancel button in calendar popup should dismiss popup
#	Given Launch the app online
#	And User is in edit profile screen
#	When User taps on cancel button in calendar popup
#	Then Verify that calendar popup should be dismissed
#
#
#Scenario: Verify that tapping on save button deleting name should display error message
#	Given Launch the app online
#	And User is in edit profile screen
#	When User delete the name
#	And taps on save button
#	Then Verify that error message "Please enter your name." should be displayed
#
#
#Scenario: Verify that tapping on save button after deleting email should display error message
#	Given Launch the app online
#	And User is in edit profile screen
#	When User delete the email address
#	And taps on save button
#	Then Verify that error message "Please enter your email address" should be displayed.
##
##
#Scenario: Verify that tapping on save button after deleting location data should display error message
#	Given Launch the app online
#	And User is in edit profile screen
#	When User deletes the location data
#	And taps on save button
#	Then Verify that error message "Please enter your city" should be displayed.
##
##@Sanity
#Scenario: Verify that tapping on save after entering valid data redirects to profile page and displays toaster message
#	Given Launch the app online
#	And User is in edit profile screen
#	When User enter all profile details
#	And taps on save button
#	Then Verify that user should be redirects to profile screen with toast message <profile have been updated>
#
#@Sanity
#Scenario: Verify that tapping on sign out button in profile screen should display sign out bottom sheet dialog
#	Given Launch the app online
#	And user is in profile screen
#	When User taps on sign out button
#	Then Verify that bottom sheet dialog displayed
#
#
#Scenario: Verify the fields in sign out dialog popup
#	Given Launch the app online
#	And user is in profile screen
#	When User is in sign out bottom sheet dialog
#	Then Verify that Label <Sign out> should be displayed
#	And Text "Are you sure you want to sign out?" message
#	And CTA <Yes> and <Cancel>
#
#
#Scenario: Verify that yes button should be highlighted and redirect the user to login screen.
#	Given Launch the app online
#	And user is in profile screen
#	When User is in sign out bottom sheet dialog
#	And User taps on yes button
#	Then Verify that user redirects to login screen
#
#
#Scenario: Verify that tapping on cancel button should dismiss the bottom sheet dialog
#	Given Launch the app online
#	And user is in profile screen
#	When User taps on cancel button
#	Then Verify that bottom sheet dialog should be dismissed
#
#
#Scenario: Verify that if user tries to logout of the application it should display a toast message
#	Given Launch the app online
#	And user is in profile screen
#	When User is in sign out bottom sheet dialog
#	And User is on offline
#	And User taps on yes button in sign out dialog sheet
#	Then Verify that toast message "Please connect to internet and try again" should be displayed.
#
#
#Scenario: Verify the Account Details field in profile for logged In user
#	Given Launch the App online
#	And User is Logged In user with some data.
#	And user taps on profile card on hamburger menu
#	When User is in profile screen
#	Then verify Phone Number field with icon in Account details
#	And An Edit icon should be shown next to this field click on edit icon
#	And Phone number field should accept only numeric values.
#
#
#Scenario: Verify the Profile Details field in profile for logged In user
#	Given Launch the App online
#	And User is Logged In user with some data.
#	And user taps on profile card on hamburger menu
#	When User is in profile screen
#	Then verify Profile Name with icon and should be Pre Filled
#	And verify Email with icon and should be Pre Filled
#	And verify Location with icon and should be Pre Filled
#	And verify gender with icon with "Add your gender" text
#	And verify birthday with icon with "Add your Birthday" text
#	And Sign out button with icon