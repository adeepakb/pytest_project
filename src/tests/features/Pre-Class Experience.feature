Feature: Pre-Class Experience


Scenario: Verify profile photo upload, approval and reject photo scenarios
Given launch the application online as neo user and navigate to home screen
And tutor start the session
When click on "JOIN" button in home page
Then Verify hovering over student's name bubble when uploaded photo approval is pending.
And Verify the profile photo edit functionality when user clicks on edit icon
And Verify the "Change profile photo" pop up when user selects "Use Camera" option.
And Verify that student able to close, change profile photo pop up by tapping on close icon
And Verify adjusting image by drag image option in Adjust Photo pop up.
And Verify that student able to close, Adjust photo pop up by tapping on close icon
And Verify that student able to change photo by tapping on change icon
And Verify that student able to save photo by tapping on Save icon
And Verify the student's name bubble when photo approval is pending.
And Verify that till the time photo is in review state, student will see own photo with overlay text shown as per zeplin
And Verify the approval pending flash message when user uploads a photo for user profile.
And Verify that once tutor approves photo will be visible to student only if student refresh screen
And Verify the congratulations flash message when uploaded photo gets approved.
And Verify the edit button in bubble before & after photo gets approved
And Verify the rejected flash message upon when user uploads a photo for user profile.
And Verify the bubble when uploaded photo gets rejected for the logged in user.
And Verify the error message when internet connection is lost while uploading an image
And Verify that student can upload photo only in JPEG,JPG,PNG format
And Verify that maximum size allowed for photo should be upto 3MB
And Verify uploading photos with different resolutions and sizes in the change profile photo pop up.
