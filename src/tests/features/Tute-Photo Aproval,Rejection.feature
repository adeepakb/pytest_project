Feature: Tute-Photo Aproval,Rejection


Scenario: Verify Tute-Photo Approval and Rejection scenarios
Given launch the application online as neo user and navigate to home screen
And tutor start the session
When click on "JOIN" button in home page
Then Verify the element present in student detail screen as per zeplin
And Verify that batch students details  are present in student detail screen
And Verify the name and student first letter is present in the case when user not uploaded any image
And Verify that Approve ,Reject and Review is present on the card
And Verify that review option shown below the image
And Verify that newly updated image along with  'x' updated the profile. Please approve and review text shown on the card
And Verify that tapping on review "x" "new profile picture text"  along with image and Reject, Approve btn should be present
And Verify the close btn fuctionality on review screen
And Verify the text "You have approved x profile picture" toast message appears when tute approves along with close icon
And Verify the text "You have rejected x profile picture" toast message appears when tute reject along with close icon
And Verify the approve request card when user change image for second time
And Verify validation message is displayed when Tute approves/rejects photo approval request while internet connection is interrupted
And Verify that tute able to approve or reject pending profiles only on next session