Feature:  Whiteboard

  Scenario: Verify whiteboard screen, texts, handwritten shapes, markers on Whiteboard presentation
    Given launch the application online as neo user and navigate to home screen
    And tutor start the session
    When click on "JOIN" button in home page
    And student join neo session
    Then Verify the elements in default whiteboard screen when user lands on.
    And Verify the full screen mode option in whiteboard.
    And Verify the whiteboard screen when user selects full screen mode.
    And Verify the whiteboard when focused mode is turned on.
    And Verify the tutor's video section when video of the tutor is turned off in the right side.
    And Verify the tutor's audio/video quality when network is flaky.
    And Verify the "Lower Hand" button doesnt change if reconnection happens due to flaky network.
    And Verify the like emoji "thumbs up" below the whiteboard.
    And Verify that student can select like emoji.
    And Verify that like emoji should be highlighted when student clicks on thumbs up icon.
    And Verify that student cant control other student's camera & mic.
    And Verify that if student joins the session during Whiteboard presentation, already entered texts, shapes, markers are also visible to the students
    And Verify that alignment of texts, handwritten shapes, markers on Whiteboard presentation in different browser window sizes
    And Verify that contents presented on Whiteboard is available if user refreshes/rejoins the session
    And Verify that contents presented on Whiteboard is available if reconnection happens

    #deepak
    And Verify that if other students in the class raises hand, a hand icon should be displayed beside the mic icon on the student's thumbnail.
    And Verify that if other students in the class lower hand, the hand icon should be removed from the student's thumbnail.
    And Verify that user should be able to use "Raise Hand" functionality anytime during the session.
    And Verify that user should be able to use "Lower Hand" functionality anytime during the session.
    Then Verify that students thumbnail is not displayed when the focused mode is turned on for full screen.
    And Verify that mic/camera icon is displayed when the focused mode is turned on for full screen.
    And Verify that raise hand option is available when whiteboard is in focused mode for full screen.
    And Verify the message when tutor send request to student to turn on video / discuss doubt.
    And Verify the flash message text “Tutor wants to discuss your doubt with you.Please turn on your mic and camera" when tutor sends request to turn on mic/camera.
    And Verify the students video when students accepts tutor's request to turn on the camera.
    And Verify that like emoji & minimize screen option is displayed at the bottom of whiteboard when its in full screen mode.
    And Verify the video screen when user turns on camera while discussing doubts .
    And Verify student is audible when students accepts tutor's request to turn on the mic.
    And Verify that logged in student can turn off their mic/camera when they are discussing doubts with tutor.
    And Verify the other student's video when they also start discussing doubts.
    And Verify the whiteboard screen size when users clicks on minimise screen icon.




