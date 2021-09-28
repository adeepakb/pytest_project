Feature: Technical Issues during Session


Scenario: Verify Technical Issues during Session functionality
	Given launch the application online as neo user and navigate to home screen
	And tutor start the session
	When click on "JOIN" button in home page
	And student join neo session
	Then Verify that kebab menu icon is present below the video screen
	And Verify that kebab icon is clickable and clicking on the this different options should be displayed
	And Verify the different issue types present in the popup when user clicks on 'Facing issues?' in the kebab menu
	And Verify that the pop up should display on the top of the video screen  clicking the kebab menu
	And Verify that by-default 'Report Now' button should be disabled
	And Verify that once user selects any option the button should be enabled
	And Verify that user should able to select multiple options
	And Verify that the selected option toggle should display in sky colour
	And Verify that once select any option the "Suggested tips" should be displayed below the issue
	And Verify that once user select any option , that option should be highlighted with bold text
	And Verify the alignment of the suggested  tips.
	And Verify that close icon is present the popup and its clickable
	And Verify that popup should close when user clicks on the close icon
	And Verify the popup when user refresh the page
	And Verify the pop should be scrollable
	And Verify that "Issue still Persists?" text should be displayed
	And Verify when user selects the issue type as "Others" one text box should be appear with ghost text "Type your issue here..."
	And Verify the alignment of the email icon on the popup after user writes "technical issue" in the text box and clicks on "Report Now" button
	And Verify that when the user clicks on report now button,"Our team is looking into this on priority. You will recieve a call from us soon. Sorry for this :(" popup should be displayed
	And Verify the popup should be disappeared automatically in 5 secs
	And Verify the popup should be disappeared if user refresh the page