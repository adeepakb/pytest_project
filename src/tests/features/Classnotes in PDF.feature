Feature: Classnotes in PDF


Scenario: Verify that taping on app back navigation icon should land back on  home screen.
	Given launch the application and navigate to home screen
	When tap on byjus classes card
	Then tap on device back icon
	And verify that user navigates to home screen


Scenario: Verify that taping on "get Help", quick help chat screen will open.
	Given launch the application and navigate to home screen
	When tap on byjus classes card
	Then tap on "Get help" button
	And Verify that quick help bottom sheet opens


Scenario: Verify that user can switch between the tabs on taping on  it
	Given launch the application and navigate to home screen
	When tap on byjus classes card
	Then verify that user is able to switch between "For you" and "Completed" tabs


Scenario: Verify that on switching to tab, respective cards/content should be  load
	Given launch the application and navigate to home screen
	When tap on byjus classes card
	Then tap on "For you" tab
	And Verify that For you tab contents are loading
	And tap on "Completed" tab
	And Verify that Completed sessions tab contents are loading


Scenario: Verify that user should be able to attach pdf notes to the sessions as pre or post requisites
	Given launch the application and navigate to home screen
	And post-requisite "classnotes" should be tagged for the particular classroom session
	When tap on byjus classes card
	Then tap on "Completed" tab
	And verify that "REVISION MATERIAL" shown in the postrequisites card
	And verify that "classnotes" shown in the postrequisites card


Scenario: Verify the elements in classnotes Card
	Given launch the application and navigate to home screen
	When tap on byjus classes card
	Then tap on "Completed" tab
	And verify that "classnotes" shown in the postrequisites card
	And verify classnote icon beside class-note text is present
	And verify Download button is present


Scenario: Verify that class notes card available under Completed Classes and on session details screen once user completes the class.
	Given launch the application and navigate to home screen
	When tap on byjus classes card
	Then tap on "Completed" tab
	And tap on completed session card
	And verify that "classnotes" shown in the postrequisites card


Scenario: Verify that if the post requisite contain only 2 resource type, then "See more" should not be present on the  card
	Given post-requisite "class note requisite group1" should be tagged for the particular classroom session
	And launch the application and navigate to home screen
	When tap on byjus classes card
	Then tap on "Completed" tab
	And verify that in the Completed tab, post requisite card is present
	And verify "See more" option is not displayed if the post requisite contain only 2 resource type


Scenario: Verify that taping on "See more", should open in the new screen, where all the tagged resource types are  shown
	Given post-requisite "auto-post-classnotes-video" should be tagged for the particular classroom session
	And launch the application and navigate to home screen
	When tap on byjus classes card
	Then tap on "Completed" tab
	And verify that in the Completed tab, post requisite card is present
	And verify that "See more" shown in the postrequisites card
	And tap on "See more"
	And verify the user is navigated to the session details screen where all the tagged resource types are shown


Scenario: Verify that elements in the completed sessions tab when content team upload the class notes
	Given launch the application and navigate to home screen
	When tap on byjus classes card
	Then tap on "Completed" tab
	And Verify App back button on left hand side of the screen
	And Verify Get help button
	And Verify the text "Classes"
	And Verify that "Completed" tab is highlighted by default
	And Verify the completed session card along with Subject Name, topic Name and the text "Completed" with date and the session rating given by the user in stars followed by the numeric
	And Verify the text "REVISION MATERIAL"
	And Verify the Class Notes card is present and Pdf size displayed below the down Arrow Button
	And tap on "See more"
	And verify the user is navigated to the session details screen where all the tagged resource types are shown


Scenario: Verify that if Class note updation done from backend before the session start and verify it reflect same on app end
	Given post-requisite "auto-post-classnotes-video" classnote should be updated to "48" for the particular classroom session
	And launch the application and navigate to home screen
	When tap on byjus classes card
	Then tap on "Completed" tab
	And Verify the Class Notes card is present and Pdf size displayed below the down Arrow Button
	And verify that "NEW" shown in the postrequisites card


Scenario: Verify downloading should  Stop  when internet goes off
	Given launch the application and navigate to home screen
	When tap on byjus classes card
	Then tap on "Completed" tab
	And switch "off" the device data
	And verify that "REVISION MATERIAL" shown in the postrequisites card
	And tap on class notes download icon
	And verify "Download failed, please try again" toast message is displayed
	And switch "on" the device data


Scenario: Verify that When user tap on download button ,it should show download processing state
	Given launch the application and navigate to home screen
	When tap on byjus classes card
	Then tap on "Completed" tab
	And tap on class notes download icon
	And verify that loader keeps loading the file


Scenario: Verify that Taping on download button should download the PDF in the phone storage
	Given launch the application and navigate to home screen
	When tap on byjus classes card
	Then tap on "Completed" tab
	And verify while taping on the forward icon pdf file should open
	And click on More options-Download option
	And Verify that PDF download in the storage of the phone


Scenario: Verify that when user downloaded the pdf then it should show forward icon
	Given launch the application and navigate to home screen
	When tap on byjus classes card
	Then tap on "Completed" tab
	And verify class notes downloaded state along with forward icon


Scenario: Verify that if user have inbuilt pdf viewer  to open Pdf
	Given launch the application and navigate to home screen
	When tap on byjus classes card
	Then tap on "Completed" tab
	And verify class notes downloaded state along with forward icon
	And verify that user asked to select pdf viewer to open


Scenario: Verify while taping on the forward icon pdf file should open
	Given launch the application and navigate to home screen
	When tap on byjus classes card
	Then tap on "Completed" tab
	And verify class notes downloaded state along with forward icon
	And verify while taping on the forward icon pdf file should open


Scenario: Verify that downloaded  PDF in the  phone storage can be viewed in offline mode
	Given launch the application and navigate to home screen
	When tap on byjus classes card
	Then tap on "Completed" tab
	And switch "off" the device data
	And verify class notes downloaded state along with forward icon
	And verify while taping on the forward icon pdf file should open
	And switch "on" the device data


Scenario: Verify that after the pdf download, user able to share
	Given launch the application and navigate to home screen
	When tap on byjus classes card
	Then tap on "Completed" tab
	And verify class notes downloaded state along with forward icon
	And verify while taping on the forward icon pdf file should open
	And verify that after the pdf download and user able to share


Scenario: Verify that max allowed size for the PDFs should  be 15 MB
	Given login to tutor-plus-cms-staging
	When verify that user uploads classnotes pdf more than 15 MB size
	Then verify that an error message should be displayed


Scenario: Verify that user should not be able to upload class Notes in any other format (ex img or csv )
	Given login to tutor-plus-cms-staging
	When user try to upload class Notes in any other format (ex img or csv)
	Then upload was not successful