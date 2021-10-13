Feature: Pre_Class


  Scenario: Verify pre class scenarios
    Given launch the application online as neo user and navigate to home screen
    When student join neo session for next day
    Then Verify the Student's greeting message on the landing screen.
    And Verify the list of students bubble on the screen before the class starts.