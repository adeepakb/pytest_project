Feature: In-Class


Scenario: Verify the celebrations feature in web
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