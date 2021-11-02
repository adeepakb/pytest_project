Feature: Chat Forum


  Scenario: Verify the chat section "Class Forum" below the tutor's screen.
    Given Student launches in-class and navigate to home page
    And tutor start the session
    And click on "JOIN" button in home page
    When student join neo session
    Then Verify the chat section Class Forum below the tutor's screen.
    And Verify that "students count" in chat Forum.
    And Verify that "Type Something" in chat Forum.
    And Verify messages when users typed  any combination of alphanumeric & special characters in the chat box.
    And Verify that text wrapping should happen without truncation or spill over the window when texts include multiple lines.
    And Verify when more than one students sent messages in chat box at the same time.
    And Verify that stickers option when user clicked on expand (upward arrow) beside emojis in chat forum & then selects sticker option.
    And Verify stickers in chat when user selects any sticker from the list.
    And Verify that raised hands option  in chat forum when logged in user raised hand.
    And Verify that "You lowered hand" message when logged in student lowers hand.
    And Verify the state of "Lower Hand" button if user leaves and then rejoins the session .
    And Verify that chat forum when multiple users sent stickers at the same time.
    And Verify that if a student has raised hand and the tutor lowers the hand for that student, text Lower Hand button should again change to Raise Hand and button goes to default state
    And Verify that when student clicks on Lower Hand button, button should change to Raise Hand button. Also on the chat forum same should be notified as You lowered hand
    And Verify that by default 2 rows of stickers are showing in sticker menu with a scroll option.
    And Verify that all the messages from tutor side is left aligned.
    And Verify that all the messages from other students side is left aligned.
    And Verify that logged user messages is right aligned.
    And Verify that tutor's name & tutor tag with time is showing in the chat forum.
    And Verify tutor's thumbnail in the chat forum.
    And Verify typing messages when the network is flaky.
    And Verify that "Text input is temporarily disabled for all " shows when tutor disables the chat option.
    And Verify that students cant type when message is disabled from the tutor's end.
    And Verify that students chat is disabled and network goes off when he/she rejoin chat must be in disabled state.
    And Verify that students chat is enabled and network goes off when he/she rejoin chat must be in the same state.
    And Verify that sticker sent in chat shouldn't be distorted.
    And Verify the Class Forum when student throttles network to Offline


Scenario: Verify class forum scenarios at neo tutor end
Given Student launches in-class and navigate to home page
And tutor start the session
And click on "JOIN" button in home page
When student join neo session
Then Verify that messages sent by student is present in Tutor side
And Verify that latest message is displayed to the Tutor
And Verify that Reply option present against each message should be clickable
And Verify that chat box should appear on clicking 'Reply' option
And Verify that text wrapping in Tutor's message bubble when they reply
And Verify  that the selected message should be displayed when User click 'Reply' option
And Verify that Tutor should be able to reply to student messages
And Verify that 'Close' option should be present and is clickable
And Verify that the 'Send' option should be enabled
And Verify the elements present in Class Forum
And Verify that 'Stickers' should be present in the chat box
And Verify that a list of Stickers should be displayed when User click 'Stickers' option
And Verify that Chat forum when student enables full screen mode
And Verify that Chat forum when tutor enables focus mode.
And Verify that the toast message "Live Chat is disabled" when Tutor turn off chat
And Verify that students name are shown correctly in Class Forum
And Verify that Tutor is able to disable chat
And Verify that Tutor is able to enable chat
And Verify that Class Forum on student side is disabled when Focus Mode is ON
And Verify that message tiles as per zeplin screen.
And Verify that after Tutor refresh the page also, messages in Class Forum should be intact
And Verify that the messages sent by the students should be present in Tutor's Class Forum if Tutor joins the session late
And Verify that messages & stickers on mobile web.
And Verify message count in Class Forum when tutor send messages
And Verify the message count in tutor's reply  when tutor replies to students message.
And Verify that logged in user message shows first then tutor's reply when tutor responds to any doubts.
