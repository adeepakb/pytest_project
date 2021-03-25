Feature: Get Help


Scenario: Verify that taping on  a bottom sheet will come up with cancel icon on it.
	Given Launch the app online
	When Click on the Premium school card in the home page
	And navigate to one to mega homescreen
	Then Verify that in landing screen get help link is present
	And tap on "Get help" button
	And verify cancel icon is present on chat box


Scenario: Verify that in byjus landing screen get help icon is present
	Given Launch the app online
	When Click on the Premium school card in the home page
	And navigate to one to mega homescreen
	Then Verify that in landing screen get help link is present


Scenario: Verify that Premium School Homepage  have a "Get Help" button
	Given Launch the app online
	When Click on the Premium school card in the home page
	And navigate to one to mega homescreen
	Then Verify that in landing screen get help link is present
	And verify get help button is responsive


Scenario: Verify that taping on cancel icon, bottom sheet should go off.
	Given Launch the app online
	When Click on the Premium school card in the home page
	And navigate to one to mega homescreen
	Then Verify that in landing screen get help link is present
	And tap on "Get help" button
	And Tap on Cancel button
	And Verify that quick help bottom sheet goes off