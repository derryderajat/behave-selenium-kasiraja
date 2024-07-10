Feature: User Logout

  Scenario: Successful logout
    Given the user is logged in
    When the user clicks the logout button
    Then the user should be redirected to the login page