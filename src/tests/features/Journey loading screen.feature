Feature: Journey loading screen


Scenario: Verify the elements in journey loading screen
	Given Launch the app online
	When User is in journey loading Screen
	Then Verify "Back arrow" on top left corner of the screen
	And Verify <Chapter name>
	And Verify image
	And Verify "Hi <Username>! Analysing your learning profile to find the best path for you" text


Scenario: Verify that tapping on back button in journey loading screen should redirect the user to personalised chapter list screen
	Given Launch the app online
	And user is in journey loading screen
	When User taps on back button
	Then Verify that user should be redirected to <PersonalisedChapterListScreen>


Scenario: Verify that after loading animation(3sec) user should navigate to journey map screen and formation of map should start and the nodes appear with node names followed by node arrangement
	Given Launch the app online
	And User opens the journey for the first time
	When User is in journey loading screen
	Then Verify that user should navigate to <JourneyMapScreen> after the loading screen
	And Verify formation of map should start
	And Verify the nodes appear with node names followed by node arrangement


Scenario: Verify that user should navigate to Journey map screen after the loading screen and journey path animation should be shown and auto load the node which user need to continue to proceed the journey.
	Given Launch the app online
	And User opens already downloaded journey
	When User is in journey loading screen
	Then Verify that user should navigate to <JourneyMapScreen> after the loading screen
	And Verify formation of map should start
	And Verify auto load the node which user need to continue to proceed the journey


#Scenario: Verify that few mandatory nodes will also be hidden in some cases, these nodes will be marked as hidden in the backend and they shouldn't show up at the time of map loading
#	Given Launch the app
#	And a journey has hidden node
#	And user is in journey map screen
#	When Journey path animation is formed
#	Then Verify that hidden nodes are not shown in journey map screen