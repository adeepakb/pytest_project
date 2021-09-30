Feature: InClass


  Scenario: Verify the chat section "Class Forum" below the tutor's screen.
    Given Student launches in-class and navigate to home page
    And click on "JOIN" button in home page
    And tutor start the session
    When student join neo session
    #And tutor turns off his video
    #And tutor turns off his audio
    #And student scrolls right on students cards
    And student hover over the info button
    Then Verify the tutor's video section when video of the tutor is turned off
    Then Verify that tutor's video is not displayed when camera of the tutor is turned off
    Then Verify that Tutor's first name is displayed on the tutor's video thumbnail
    Then Verify that 'Tutor' text is displayed on the tutor's video thumbnail below tutor's name
    Then Verify that students cannot control tutor's camera/mic
    Then Verify that correct Subject name and Topic name followed by info icon is displayed on the top left corner of session window
    Then Verify that clicking on info icon should open Class info popup with correct information/details on the active session
    Then Verify that clicking on info icon or anywhere else on the screen, while Class Info pop up is open, should dismiss the pop-up
    Then Verify that students count who have joined session is <=6, previous (<) and next (>) icon should not appear below the student video thumbnails
    Then Verify that when more than 6 students have joined previous (<) and next (>) icon appear below the students video thumbnails
    Then Verify that when few students drop and total count drops below 7, previous (<) and next (>) icon disappears from below the students video thumbnails
    Then Verify that clicking on next (>) icon should scroll the students thumbnails towards the right and screen should update left most column moving out of the screen and new column appearing on the right
    Then Verify that next (>) icon is clickable until all thumbnails of students have been displayed
    Then Verify that previous (<) icon is clickable until the user reaches the first column of the thumbnails
    Then Verify that user should be able to use "Raise Hand" functionality anytime during the session
    Then Verify that "Raise Hand" button is present at the bottom of the screen next to camera and mic controls
    Then Verify that when student clicks on "Raise Hand" button, button should change to "Lower Hand" button. Also on the chat forum same should be notified as "You raised hand"
    Then Verify the "Lower Hand" button doesn't change if reconnection happens due to flaky network
    Then Verify the state of "Lower Hand" button if user leaves and then rejoins the session
    Then Verify that when student clicks on "Lower Hand" button, button should change to "Raise Hand" button. Also on the chat forum same should be notified as "You lowered hand"
    Then Verify that if other students in the class raises hand, a hand icon should be displayed beside the mic icon on the student's thumbnail
    Then Verify that if other students in the class lower hand, the hand icon should be removed from the student's thumbnail
    Then Verify the status of "Lower Hand" button if a student has raised hand and then drops from session, the tutor lowers the hand for that student and then the student rejoins the class
    Then Verify that "Thumbs Up" button is present at the bottom of the screen
    Then Verify that clicking on "Thumbs Up" icon expands the expression tab and list of expressions are displayed
    Then Verify that student is able to send expression during the session
    Then Verify that animation of the expressions on the session screen