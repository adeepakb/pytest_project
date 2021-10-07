Feature: Ask Question


  Scenario: Verify the chat section "Class Forum" below the tutor's screen.
    Given launch the application online as neo user and navigate to home screen
    And click on "JOIN" button in home page
    And tutor start the session
    When student join neo session
    Then Verify the raise hand option should present in the screen
    And Verify that student should able to ask doubt clicking on the 'Raise hand' option
    And Verify that when the user click on the 'raise hand' the hand icon be displayed on the student’s screen
    And Verify that the student who is asking the question, his  video should be enlarged compared to other students.
    And Verify when user hover on the info popup on the top of the screen
    And Verify when user hover on the video button
    And Verify when user hover on the audio button
    And Verify the default reactions when user hover on the reaction (thumbs up)
    And Verify the Tutor's video should display right side of the screen
    And Verify the student whom the tutor select those students can ask questions
    And Verify the Tutor name should display on the screen
    And Verify the functionality of the live chat
    And Verify that a student should not be able to answer other student's questions in the chat
    And Verify that student's count and live chat should be displayed below the Tutor video
    And Verify that student should able to ask doubt when the Tutor allow the student to come on the screen
    And Verify that other students should able to hear when a student asks doubts to Tutor
    And Verify that when the Tutor remove a student from ask question , the thumbnail should be realigned
    And Verify that student can't control other student's video & mic when they ask questions
    And Verify that alignment of the thumbnail when tutor allow student to ask question

