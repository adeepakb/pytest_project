Feature:  Video Session

Scenario: Verify video session is being presented,full screen, default screen,student video/audio scenarios, stay back and exit class options in neo
	Given launch the application online as neo user and navigate to home screen
	And tutor start the session
	When click on "JOIN" button in home page
	Then student join neo session
	And tutor play video in the session and turn off focus mode
	And Verify that default layout of the screen when session video is playing (not Focused)
	And Verify that aspect ratio of the session video window is 16:9 through out the session
	And Verify that the student is able to "Raise Hand" any time during the video session
	And Verify that the student is able to "Lower Hand" after raising hand, any time during the video session
	And Verify that smaller thumbnails of the students are displayed below the video window
	And Verify that during video session the student's name is not displayed on the thumbnails except for the current student where 'You' is displayed at the bottom left corner of the thumbnail
	And Verify that mic's status is displayed for other students on their thumbnail
	And Verify that student video/audio is playing if they have turned their camera/mic ON during the session
	And Verify that current student's camera and mic controls are displayed with correct status at the bottom of the session screen
	And Verify that if students have turned off their camera, only the initials of their name is displayed on the thumbnail
	And Verify that when control is not on the video window, full screen icon is not displayed at the bottom right corner of video window
	And Verify that hovering/clicking over the video window(not during focused mode) should show full screen icon at the bottom right corner of video window
	And Verify that clicking on full screen icon should enlarge the video window to full screen
	And Verify that when full screen mode is active the full screen icon should transition to shrink/windowed mode button
	And Verify that clicking on shrink/windowed mode button should shrink the video to default windowed mode
	And Verify that video plays without any issue during full screen or windowed mode, video should not be stretched, shrinked or cropped
	And Verify that aspect ratio of video is maintained in full screen mode
	And Verify that on hovering/clicking over the video screen while playback is happening in full screen mode, should show all controls; camera, mic, Raise/Lower hand and thumbs up icons
	And Verify that all above buttons function as intended even when video is playing in full screen mode
	And Verify the animation of the reactions when students send reactions while on full screen mode, verify that these should not cover the content video or distort the A/V of the on going session
	And Verify that Subject and Topic name is displayed at the top left corner of the video window, also verify that click in 'i' icon should display the class details
	And Verify that clicking on info icon or anywhere else on the screen, while Class Info pop up is open, should dismiss the pop-up
	And Verify that there is a kebab menu at the bottom corner of the session window beside the thumbs up icon which is clickable
	And Verify that clicking on kebab menu should show "Facing Issue" and "Exit Class" options
	And Verify that clicking on "Exit Class" option should open confirmation popup
	And Verify the content of "Exit Class" confirmation popup
	And Verify that clicking on "Stay Back" option on "Exit Class" confirmation popup, should take the user back to session
	And Verify that clicking on 'Exit Class' option on 'Exit Class' confirmation popup, should exit the session to Byju's classes page
	And Verify that user is able to rejoin the session after exiting the session


Scenario: Verify hand raise,focus mode,network issues in neo
	Given launch the application online as neo user and navigate to home screen
	And tutor start the session
	When click on "JOIN" button in home page
	Then student join neo session
	And Verify that when focus mode is enabled by tutor the transition of screen from windowed to full screen mode is smooth
	And Verify that student should not be able to exit focus mode
	And Verify that aspect ratio of video is maintained in focused mode
	And Verify that if reconnection happens due to network issue, focus mode is retained when student is back in the session
	And Verify that if reconnection happens due to network issue while focus mode is on, mic state of students are still turned off after the student is back in the session
	And Verify that mic control is disabled for the students while focus mode is on
	And Verify that mic is turned off for the students while focus mode is on
	And Verify that focus mode icon is displayed on the top left corner of the screen when same is turned on and controls are not active on screen
	And Verify that on click/hover on the screen indication is present on the screen while focus mode is on, "Focus Mode" text is added after the session name on top left corner of the screen
	And Verify that all controls are displayed when the student hovers/clicks in the screen while focus mode is on
	And Verify that Camera, "Raise/Lower Hand", "Thumbs Up" and Kebab Menu are the only controls that is accessible while focus mode is on
	And Verify the animation of the reactions when students send reactions while focus mode is on, verify that these should not cover the content video or distort the A/V of the on going session
	And Verify student's video thumbnail not visible while focus mode is on
	And Verify the transition of student video is smooth when same dismisses from screen
	And Verify the state of the session if the user exits and joins the session again while focus mode is on
	And Verify the transition of session is smooth when focus mode is turned off by the tutor
	And Verify that mic controls of the students become enabled after focus mode is turned off, but the state of button should be off
	And Verify that camera status of students is retained as it was before focus mode was on after focus mode is turned off