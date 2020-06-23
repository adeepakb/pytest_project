Feature: month_selector
  Scenario: Verify month selector icon with dropdown shown on student dashboard
  Given Launch the tutor app online
  And navigate to one to many student dashboard screen
  When Verify month selector icon with dropdown icon shown on student dashboard
  And verify by default current month should be highlighted
  And tap on month dropdown icon
  Then verify month list should be shown
  And verify month list should be in sorted order
  And verify on taping on other month name respective month should get highlighted
  And verify on taping on outside any where in the screen dropdown should disappear

  Scenario: Verify after selecting any month from the month selector respective details of that month should be displayed
  Given Launch the tutor app online
  And navigate to one to many student dashboard screen
  When Verify month selector icon with dropdown icon shown on student dashboard
  And tap on month dropdown icon
  Then tap on any month from the dropdown and verify respective details of that month should be displayed

  Scenario: Verify user is able to switch the months in month dropdown in offline mode
  Given Launch the tutor app online
  And navigate to one to many student dashboard screen
  When Verify month selector icon with dropdown icon shown on student dashboard
  Then tap on month dropdown icon
  And switch "off" the device data
  And tap on any month from the dropdown and verify respective details of that month should be displayed
  And switch "on" the device data
