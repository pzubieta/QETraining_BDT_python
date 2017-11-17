Feature: withdrawal
  Withdrawal

  Scenario: withdrawal if I have more than $100

    Given I have $100 in my Account
    When I enter 20 as the withdrawal amount
    And Confirm withdrawal

    Then My new balance will be 100 - 20

    Given I have $250 in my Account
    When I enter 20 as the withdrawal amount
    And Confirm withdrawal

    Then My new balance will be 100 - 20


