Feature: Ask Question


  Scenario: Verify the chat section "Class Forum" below the tutor's screen.
    Given launch the application online as neo user and navigate to home screen
    And click on "JOIN" button in home page
    And tutor start the session
    When student join neo session
    Then verify raise hand is present in the screen
    Then Verify that when the user click on the 'raise hand' the hand icon be displayed on the student’s screen
    Then Verify that the left and right navigation(< >) is displayed below the student's screen
    Then Verify that the student who is asking the question, his video should be enlarged compared to other students.
    Then Verify when user hover on the info popup on the top of the screen
    Then Verify when user hover on the video button
    Then Verify when user hover on the audio button
    Then Verify the default reactions when user hover on the reaction (thumbs up)
    Then Verify the Tutor's video should display right side of the screen
    And Verify the student whom the tutor select those students can ask questions
    Then Verify the Tutor name should display on the screen
    Then Verify the functionality of the live chat
    Then Verify that student's count and live chat should be displayed below the Tutor video
    Then Verify that student should able to ask doubt when the Tutor allow the student to come on the screen
    Then Verify that alignment of the thumbnail when tutor allow student to ask question
    Then Verify that other students should able to hear when a student asks doubts to Tutor
    Then Verify that when the Tutor remove a student from ask question , the thumbnail should be realigned
    Then Verify that alignment of the thumbnail when tutor allow student to ask question
