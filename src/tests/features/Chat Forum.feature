Feature: Chat Forum


  Scenario: Verify the chat section "Class Forum" below the tutor's screen.
    Given Student launches in-class and navigate to home page
    And click on "JOIN" button in home page
    And tutor start the session
    When student join neo session
    Then Verify the chat section Class Forum below the tutor's screen.
    And Verify that "students count" in chat Forum.
    And Verify that "Type Something" in chat Forum.
    And Verify messages when users typed any combination of alphanumeric & special characters in the chat box.
    Then Verify when more than one students sent messages in chat box at the same time.
    And Verify that stickers option when user clicked on expand (upward arrow) beside emojis in chat forum & then selects sticker option.
    And Verify stickers in chat when user selects any sticker from the list.
    And Verify that raised hands option in chat forum when logged in user raised hand.
    And Verify that "You lowered hand" message when logged in student lowers hand.
    And Verify the state of "Lower Hand" button if user leaves and then rejoins the session .
    And Verify that if a student has raised hand and the tutor lowers the hand for that student, text "Lower Hand" button proper message is shown
    And Verify that when student clicks on "Lower Hand" button, button should change to "Raise Hand" button. Also on the chat forum same should be notified as "You lowered hand"
    And Verify that messages should not get posted while user is typing and network goes off.
    And Verify that messages is showing in the chat when user sent & then network goes off.
    And Verify typing messages when the network is flaky.
    And Verify that all the messages from tutor side is left aligned.
    And Verify that all the messages from other students side is left aligned.
    And Verify that logged user messages is right aligned.
    And Verify that tutor's name & tutor tag with time is showing in the chat forum.
    And Verify tutor's thumbnail in the chat forum.
    And Verify message count in Class Forum when tutor send messages
    Then Verify the message count in tutor's reply when tutor replies to students message.
    Then Verify that "Text input is temporarily disabled for all " shows when tutor disables the chat option.
    Then Verify that students cant type when message is disabled from the tutor's end.
    Then Verify that students chat is disabled and network goes off when he/she rejoin chat must be in disabled state.
    Then Verify that students chat is enabled and network goes off when he/she rejoin chat must be in the same state.
    Then Verify that sticker sent in chat shouldn't be distorted.
    Then Verify that logged in user message shows first then tutor's reply when tutor responds to any doubts.
    Then Verify the Class Forum when student throttles network to Offline

    #When Student sends sticker
    #And Verify that text wrapping should happen without truncation or spill over the window when texts include multiple lines.
    #Then Verify sticker is shown in chat
    #And student raises hand
    #And student lower hand
    #Then verify student hand is raised
    #Then  verify lower hand message is displayed
    #When student rejoins the session
    #Then  verify lower hand message is displayed
    #And tutor unraises hand for student
    #Then student's hand is unraised
    #And  wifi is turned off
    #And students types random chat message
    #Then verify no message is sent in the chat
    #And click on sticker icon
    #Then two rows of stickers are shown in the chat
    #And tutor types the chat
    #Then verify tutor messages are left alligned
    #And another student joins the session
    #And another student sends a chat
    #Then verify other student chats are left alligned
    #And student sends chat message
    #Then verify student chat is right alligned
#    Then verify tutor name is shown in tutor box
#    And Verify that "Tutor thumbnail" in chat Forum.








