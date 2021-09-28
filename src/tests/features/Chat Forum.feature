Feature: Chat Forum


  Scenario: Verify the chat section "Class Forum" below the tutor's screen.
    Given Student launches in-class and navigate to home page
    And click on "JOIN" button in home page
   #And tutor start the session
    When student join neo session
    Then Verify the chat section Class Forum below the tutor's screen.
    And Verify that "students count" in chat Forum.
    And Verify that "Type Something" in chat Forum.
    And Verify messages when users typed any combination of alphanumeric & special characters in the chat box.
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
    Then verify tutor name is shown in tutor box
    And Verify that "Tutor thumbnail" in chat Forum.








