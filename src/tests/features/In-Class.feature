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
	#deepak
	Then student hover over the info button
    And Verify the tutor's video section when video of the tutor is turned off
    And Verify that tutor's video is not displayed when camera of the tutor is turned off
    And Verify that Tutor's first name is displayed on the tutor's video thumbnail
    And Verify that 'Tutor' text is displayed on the tutor's video thumbnail below tutor's name
    And Verify that students cannot control tutor's camera/mic
    And Verify that correct Subject name and Topic name followed by info icon is displayed on the top left corner of session window
    And Verify that clicking on info icon should open Class info popup with correct information/details on the active session
    And Verify that clicking on info icon or anywhere else on the screen, while Class Info pop up is open, should dismiss the pop-up
    And Verify that students count who have joined session is <=6, previous (<) and next (>) icon should not appear below the student video thumbnails
    And Verify that when more than 6 students have joined previous (<) and next (>) icon appear below the students video thumbnails
    And Verify that when few students drop and total count drops below 7, previous (<) and next (>) icon disappears from below the students video thumbnails
    And Verify that clicking on next (>) icon should scroll the students thumbnails towards the right and screen should update left most column moving out of the screen and new column appearing on the right
    And Verify that next (>) icon is clickable until all thumbnails of students have been displayed
    And Verify that previous (<) icon is clickable until the user reaches the first column of the thumbnails
    And Verify that user should be able to use "Raise Hand" functionality anytime during the session
    And Verify that "Raise Hand" button is present at the bottom of the screen next to camera and mic controls
    And Verify that when student clicks on "Raise Hand" button, button should change to "Lower Hand" button. Also on the chat forum same should be notified as "You raised hand"
    And Verify the "Lower Hand" button doesn't change if reconnection happens due to flaky network
    And Verify the state of "Lower Hand" button if user leaves and then rejoins the session
    And Verify that when student clicks on "Lower Hand" button, button should change to "Raise Hand" button. Also on the chat forum same should be notified as "You lowered hand"
    And Verify that if other students in the class raises hand, a hand icon should be displayed beside the mic icon on the student's thumbnail
    And Verify that if other students in the class lower hand, the hand icon should be removed from the student's thumbnail
    And Verify the status of "Lower Hand" button if a student has raised hand and then drops from session, the tutor lowers the hand for that student and then the student rejoins the class
    And Verify that "Thumbs Up" button is present at the bottom of the screen
    And Verify that clicking on "Thumbs Up" icon expands the expression tab and list of expressions are displayed
    And Verify that student is able to send expression during the session
    And Verify that animation of the expressions on the session screen
