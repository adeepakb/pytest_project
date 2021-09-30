Feature: Celebrations


Scenario: Verify the celebrations feature in web
  Given Launch the application online
  And tutor start the session
  When join neo session
  And click on start class
  Then click on thumb icon
  Then Verify that student should be able to click celebrations option in website
  Then Verify that student should be able to see all 4 celebrations in website
  Then Verify the emoji clicking once
  Then Verify that when student tap on celebrations icon in website, same emoji's reaction keeps coming
  Then Verify the emoji clicking multiple times
  Then Verify the interval time after sending 5 emojis
  Then Verify that student should be able to send celebrations in flaky network
  Then Verify that a student is able to send celebration 5 times
  Then Verify that the celebrations send by students should not reach Tutor side
  Then Verify that user should  be able to send multiple celebrations when refresh
  Then Verify that when a student send celebration, other students should be able to see the same
  Then Verify user should not be able to send emojis in interval while switching multiple tabs

Scenario: Verify the celebrations feature in mobile
  Given Launch the application online in mobile
  And tutor start the session
  When join neo session
  And click on start class
  Then click on thumb icon
  Then Verify that the celebrations icon is present in mobile browser
  Then Verify that the celebrations icon is tappable in mobile browser
  Then Verify that 4 celebrations icon appear when student tap on celebration icon when logged in from mobile browser
  Then Verify that when student tap on celebrations icon in mobile browser, same emoji's reaction keeps coming
  Then Verify that student should be able to tap all the 4 celebrations icon
  Then Verify that same celebration icons are seen when student tap any specific celebration icon multiple times
  Then Verify that set of 4 celebrations should close when student tap outside in mobile browser
