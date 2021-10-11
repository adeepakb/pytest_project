Feature: In class-Notifications

Scenario: Verify the inclass-notifications feature
  Given Launch the application online
  And tutor start the session
  When join neo session
  And click on start class
  Then Verify that when mic and chat is disabled by tutor, hovering over mic icon should show a toast message that mic and text options is disabled by tutor
  Then Verify that the toast message is dismissed when hover is moved away from mic icon; verify that there is no distortion on the toast message when same appears and disappears
  Then Verify that the in-class notifications toast message should have tutor's image and indication that the message is from tutor
  Then Verify that when the student lowers hand a toast message is displayed prompting that student has lowered hand
  Then Verify that if network error happens, same is displayed as in-class notification toast message with "Retry" button
  Then Verify that there is a close button on the in-class notifications toast message which should allow students to close/dismiss the message
  Then Verify that when focus mode is about to start the student is notified for same as in-class notification toast message, also verify the content of the message
  Then Verify that in-class notification toast message for focus mode should not have close icon and same should get dismissed automatically after xx seconds
  Then Verify that the in-class notifications do not cover the video/content when full screen is not active
  Then Verify that the in-class notifications stay on the screen for xx seconds before disappearing from the screen
  Then Verify that there is no distortion on the in-class notifications toast message or the session content when they appear or disappear from the screen
