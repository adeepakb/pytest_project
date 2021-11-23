Feature: Class View


  Scenario: Verify the chat section "Class Forum" below the tutor's screen.
    Given Student launches in-class and navigate to home page
    And tutor start the session
    And click on "JOIN" button in home page
    When student join neo session
    Then Verify the screen when the class starts
    And Verify that thumbnail controller for student's image/video view should display right side of the screen
    And Verify that Tute should able to large and small the thumbnails clicking on the thumbnail controller
    And Verify that the tutor video should display on the top right side of the screen
    And Verify the tutor internet connection should display on the top of the screen
    And  Verify that audio/video/chat button should display on the top middle of the screen
    And Verify that tutor should be able to turn off the student's camera clicking on camera icon
    And Verify that tutor should be able to mute the students clicking the mic
    And Verify that tutor should able to disable the chat clicking on the chat icon
    And Verify that the End class button should display top right side of the screen
    And Verify that the End class button is clickable and tutor can end the class clicking on End class
    And Verify that the class should end when user click on exit class
    And Verify that when tute click on end class confirmation popup should display with Exit and stay back options
    And Verify that class should continue clicking on stay back
    And Verify the timer beside the End class button
    And Verify that when focus mode is ON the text "Focus Mode :ON" along with icon
    And Verify that global icon of audio and chat should be disabled state
    And Verify that in Focus mode all students mike should be muted by default