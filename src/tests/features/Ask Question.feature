Feature: Ask Question


  Scenario: Verify the chat section "Class Forum" below the tutor's screen.
    Given launch the application online as neo user and navigate to home screen
    And click on "JOIN" button in home page
    And tutor start the session
    When student join neo session
    #Then verify raise hand is present in the screen
    #Then verify user is able to raise hand and ask question
    #When another student joins the session
    #And another second student joins the session
    #And tutor start the session
    #And tutor allows student to ask question
    #Then verify user asking question has enlarged video
    #And student hover over the info button
    #Then verify info pop_up is shown
    #And student turn "off" camera
    #And student hover over video button
    #Then verify tool tip message "Turn on Camera" is being displayed
    #When student turn "on" camera
    #And student hover over video button
    #Then verify tool tip message "Turn off Camera" is being displayed
    #When student turn "off" mic
    #And student hover over mic button
    #Then verify tool tip message "Turn on Microphone" is being displayed
    #When student turn "on" mic
    #And student hover over mic button
    #Then verify tool tip message "Turn off Microphone" is being displayed
    #And student hover over reaction button
    #Then default reactions are shown
    And tutor turns on his video
    #Then tutor videos should be displayed
    #And tutor allows student to ask question
    #Then ask question pop up is displayed
    #Then verify tutor name is shown in tutor box
    #Then Verify that students count besides chat Forum.
    When tutor types the chat
    And student sends chat message
    Then verify live chat by tutor and student
    Then Verify that other students should able to hear when a student asks doubts to Tutor