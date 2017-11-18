@try @pz
Feature: Withdraw Fixed Amount
  The "Withdraw Cash" menu contains several fixed amounts to speed uo transactions for users.

  Scenario: Withdraw fixed amount of $50
    @tags_scenario
    Given I have $500 in my account
    When I choose withdraw the fixed amount of $50
    Then I should receive $50 cash
      And the balance of my account should be $450

  Scenario: Withdraw fixed amount of $100
    Given I have $600 in my account
    When I choose withdraw the fixed amount of $100
    Then I should receive $100 cash
      And the balance of my account should be $500

  Scenario: Test Withdraw fixed amount of $100
    Given I have $600 in my account
    When I choose withdraw the fixed amount of $100
    Then I should receive $100 cash
      And the balance of my account should be $500