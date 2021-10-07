Feature: Chat Forum


  Scenario: Verify the chat section "Class Forum" below the tutor's screen.
    Given Student launches in-class and navigate to home page
    And click on "JOIN" button in home page
    And tutor start the session
    When student join neo session
    Then Verify the chat section Class Forum below the tutor's screen.
    And Verify that "students count" in chat Forum.
    And Verify that "Type Something" in chat Forum.
    Then Verify messages when users typed  any combination of alphanumeric & special characters in the chat box.
    And Verify that text wrapping should happen without truncation or spill over the window when texts include multiple lines.
    Then Verify when more than one students sent messages in chat box at the same time.
    Then Verify that stickers option when user clicked on expand (upward arrow) beside emojis in chat forum & then selects sticker option.
    Then Verify stickers in chat when user selects any sticker from the list.
    And Verify that raised hands option  in chat forum when logged in user raised hand.
    And Verify that "You lowered hand" message when logged in student lowers hand.
    And Verify the state of "Lower Hand" button if user leaves and then rejoins the session .
    Then Verify that chat forum when multiple users sent stickers at the same time.
    Then Verify that if a student has raised hand and the tutor lowers the hand for that student, text Lower Hand button should again change to Raise Hand and button goes to default state
    And Verify that when student clicks on Lower Hand button, button should change to Raise Hand button. Also on the chat forum same should be notified as You lowered hand
    #Reshma
    #Then Verify that messages should not get posted while user is typing and network goes off.
    #And Verify that messages is showing in the chat when user sent & then network goes off.
    Then Verify that by default 2 rows of stickers are showing in sticker menu with a scroll option.
    #And Verify typing messages when the network is flaky.
    Then Verify that all the messages from tutor side is left aligned.
    And Verify that all the messages from other students side is left aligned.
    And Verify that logged user messages is right aligned.
    And Verify that tutor's name & tutor tag with time is showing in the chat forum.
    And Verify tutor's thumbnail in the chat forum.
    #Reshma
#    And Verify message count in Class Forum when tutor send messages
    Then Verify the message count in tutor's reply  when tutor replies to students message.
    And Verify that "Text input is temporarily disabled for all " shows when tutor disables the chat option.
    And Verify that students cant type when message is disabled from the tutor's end.
    And Verify that students chat is disabled and network goes off when he/she rejoin chat must be in disabled state.
    And Verify that students chat is enabled and network goes off when he/she rejoin chat must be in the same state.
    Then Verify that sticker sent in chat shouldn't be distorted.
    Then Verify that logged in user message shows first then tutor's reply when tutor responds to any doubts.
    And Verify the Class Forum when student throttles network to Offline





