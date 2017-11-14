Feature: Google search main window
  Scenario: Basic Search

  Scenario: I'm feeling lucky search
    When 'I'm Feeling lucky' button is pressed to perform a search
    Then the page of the first result of the result is opened directly


  Scenario: searching using '@' search operator for social media results
    Given a search text
    When '@' + some social media page (e.g @twitter) is used before the string
    Then all the results are displayed from the social media used in the string


  Scenario: login with a google account
    Given I press Log in button
      And enter valid credentials of a google account
    When I press Following button after write the account password
    Then account is logged in
      And profile picture is displayed
      And notifications icon is added


  Scenario: Pressing profile picture button
    Given a user is loged with a gmail account
    When click on the profile picture
    Then a modal window is displayed with profile information
      And button to access to the account settins is displayed
      And button to add a new account is displayed
      And button to sign out is displayed