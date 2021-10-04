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
And Verify that alignment of texts, handwritten shapes, markers on Whiteboard presentation in different browser window sizes
And Verify that contents presented on Whiteboard is available if user refreshes/rejoins the session
And Verify that contents presented on Whiteboard is available if reconnection happens
And Verify that if student joins the session during Whiteboard presentation, already entered texts, shapes, markers are also visible to the students


