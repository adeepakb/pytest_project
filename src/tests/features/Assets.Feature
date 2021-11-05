Feature: Assets

Scenario: Verify neo-tute assets testcases
Given launch the application online as neo user and navigate to home screen
When tutor start the session
And click on "JOIN" button in home page
And student join neo session
Then Verify that the volume slider is displayed when Tutor keeps cursor on the volume icon of Video
And Verify that User should be able to increase or decrease volume accordingly
And Verify that Audio Mute icon should be displayed when User mutes the audio
And Verify that Video Mute icon should display when User mutes the video
And Verify that Video and Audio Mute icon should display when tutor mutes the video and audio
And Verify that the first letter of the Student will be displayed as profile picture incase the Student haven't uploaded any photo
And Verify that if the Student have uploaded a profile photo, then same should be displayed as Profile Thumbnail
And Verify that raise hand icon should appear in the profile thumbnail when Student clicks Raise Hand
And Verify that question mark icon should appear in the profile thumbnail when Tute asks question

