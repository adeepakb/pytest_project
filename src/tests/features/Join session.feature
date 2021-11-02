Feature: Join session

Scenario: Verify the join session feature
  Given Launch the application online
  And tutor start the session
  When join neo session
#  Then Verify that the student is visible clearly or not when the camera is enabled.
#  Then Verify the student's audio when the mic is enabled
#  Then Verify the functionality of the Audio and video settings
#  Then Verify the functionality of the mic and the camera on the student's screen
#  Then Verify the class joining screen before the class starts
#  Then Verify the student video and audio in poor network
#  Then Verify that user is able to join neo class
#  Then session started X minute back message should be displayed when user joins after the session starts time.
  Then Verify that confirmation popup should be displayed when user click on leave the session
  Then Verify that the student should join and leave the class multiple times
  And verify that validation should be displayed when user try join the class with out internet connection








