Feature: User Login
    Scenario: Successful login with valid credentials
        Given the user is on the login page
        When the user enters valid credentials
        And the user submits the login forms
        Then the user should be redirected to the dashboard
    