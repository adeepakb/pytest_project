Feature:  In-Class

Scenario: Verify video session is being presented,full screen, default screen,student video/audio scenarios, stay back and exit class options in neo
	Given launch the application online as neo user and navigate to home screen
	And tutor start the session
	When click on "JOIN" button in home page
	And student join neo session
	Then Verify the alignment of student's thumbnail when only one student joins and enters the class
	And Verify that camera and mic controls are present at the bottom left side on the screen
	And Verify that camera and mic states are retained with the state they are set before joining the session
	And Verify the alignment of Tutor's video when student joins the class
	And Verify that the student can enable/disable their A/V during the session using the camera and mic buttons
	And Verify that audio/video state transition is smooth when user toggles the controls ON/OFF
	And Verify that video of student is not displayed when camera is turned off by the student
	And Verify that student is muted when mic is turned off by the student
	And Verify that camera and mic icons change when same are toggled On/Off
	And Verify that a translucent window encases the student's name on their thumbnail
	And Verify that if the student has turned off their camera and do not have their profile picture set, initials of their first name should be displayed on the thumbnail
	And Verify the tutor's video section when video of the tutor is turned off
	And Verify that tutor's audio is muted when mic of the tutor is turned off
	And Verify the default alignment of student's thumbnails when two students join and enter the class
	And Verify that the student's thumbnails update dynamically when any new student joins while session is in progress
	And Verify that audio/video state transition is smooth when many students toggle the controls ON/OFF at different times
	And Verify that audio/video state transition is maintained when students toggle the controls ON/OFF who are not present on active screen
	And Verify the browser's performance during In-class when one or more students have A/V enabled
	And Verify that there are no glitches when one or many students are casting A/V and the network is flaky
	And Verify the browser's performance during In-class when all students have A/V disabled
	And Verify that camera and mic button's states are retained with the state they are set when network is lost and then connection is established again
	And Verify that audio and video states are retained with the state they are set when network is lost and then connection is established again
	And Verify that current student's name is not displayed on the thumbnail, instead 'You' text is displayed at the bottom left corner of the thumbnail
	And Verify that, for current student, other student's name are displayed at the bottom left corner of the thumbnail
	And Verify the default alignment of student's thumbnails when three students join and enter the class
	And Verify the default alignment of student's thumbnails when four students join and enter the class
	And Verify the default alignment of student's thumbnails when five students join and enter the class
	And Verify the default alignment of student's thumbnails(six students) when they join and enter the class

Scenario: Verify the inclass feature in web
  Given Launch the application online
  And tutor start the session
  When join neo session
  And click on start class
  Then Verify the display of student count icon
  Then Verify the functionality of minimising window during session and reopening
  Then Verify the display of controls in fullscreen mode
  Then Verify the display of Focus mode icon
  Then Verify the display of mic and camera during Focus mode
  Then Verify the display of session video continues without fail
  Then Verify the display of video session in chrome
  Then Verify the display of screen in desktop during video session
  Then Verify that user should not able to pause or play video during session
  Then verify the tutor's video background when student rejoins the session
  Then Verify the tutor's video background when user refreshes the page
  Then Verify that when tutor has turned off mic and chat for all students, mic icon on the student thumbnails are greyed out and shown as disabled
  Then Verify that the if a student speaks for less than 2 seconds his thumbnail should not be moved to view port
  Then Verify that the if a student speaks for more than 2 seconds his thumbnail should be moved to view port
  Then Verify that if any student stays quite for 2 seconds should be removed from view port
  Then Verify the only <=3 students who are speaking should appear in view port in chronological manner
  Then Verify that if multiple students are speaking, the thumbnail should appear in the view port in order of speaking
  Then Verify the display of screens when Tutor changes the slides
  Then Verify the functionality when student rejoins after"Tutor want to discuss doubt with you" is triggered
  Then Verify the tutor's background video when network is flaky


Scenario: Verify the inclass feature in mobile
  Given Launch the application online in mobile
  And tutor start the session
  When join neo session
  And click on start class
  Then Verify the text Hand Raised in mobile browser
  Then Verify the class description in desktop/mobile browser
  Then Verify the display of student count icon in mobile view
  Then Verify the display of student cards in mobile view
  Then Verify display of subject/ Topicname/focus mode in mobile browser
  Then Verify the display of student count in mobile browser
  Then Verify the display of weak signal icon in mobile browser