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
	And Verify that if the student has turned off their camera and have their profile picture set, profile picture should be displayed on the thumbnail
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
