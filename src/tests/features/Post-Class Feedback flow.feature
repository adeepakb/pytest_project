Feature: Post-Class Feedback flow

Scenario: verify postclass feedback flow
  Given Launch the application online
  When join neo session
  And click on start class
  And Exit the class
  And click on exit class button in exit popup
  Then Verify the post the session Feedback popup should display on top of the video screen
  Then Verify that the rating should include the class rating and tutor rating
  Then Verify the class rating feedback screen should display with 'How was your class' (with 5 smiley options)
  Then Verify that close icon should present on the feedback popup and it is clickable
  Then Verify that feed-back popup should close when user clicks on the close icon
  Then Verify that continue button should be enabled when user selects any emoji
  Then Verify that the next screen should be display the selected emoji with other emojis and 'What did you like the most'
  Then Verify that the emoji which is selected in the previous screen should be highlighted in the next screen
  Then Verify that submitted button should be enabled when user selects any option from what did you like the most? and clicking on the submit button feedback3 should display
  Then Verify that the Feedback3 screen should be displayed with 'How was your experience with our tutor'( with five smileys)
  Then Verify that tutor's name, profile picture and number of sessions assisted should be displayed in Feedback3 screen
  Then Verify that user can't select multiple emojis
  Then verify that the details of feedback4 should be displayed with 'what can be improved?' with different options in feedback5 popup.
  Then Verify that the user should able to select multiple options from 'What can be improved?'
  Then Verify that when user selects others option from 'What can be improved?' , an additional comments textbox should display with the text' Add your comment here"
  Then Verify submit button after adding comments in the feedback section
  Then Verify that when user submit the ratings 'thank you' popup should be displayed
  Then Verify that the students can skip the ratings at any point
  Then Verify that the rating popup should display whether the student leaves the session or the session ends
  Then Verify that feedback popup should display when user rejoins the class who has already submitted the feedback
  Then Verify that student should able to rejoin the class after submitting the ratings
  Then Verify that rating popup should display when user close the ratings and rejoins the session again
  Then Verify the colour's of the emojis