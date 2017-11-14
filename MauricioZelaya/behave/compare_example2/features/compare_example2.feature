Feature:
  Scenario:
    Given I have $500 in my account
    When I choose withdraw the fixed amount of $50
    Then I should receive $50 cash
      And the balance of my account should be $450

  Scenario:
    Given I have $500 in my account
    When I choose withdraw the fixed amount of $100
    Then I should receive $100 cash
      And the balance of my account should be $400

  Scenario:
    Given I have $500 in my account
    When I choose withdraw the fixed amount of $200
    Then I should receive $200 cash
      And the balance of my account should be $300

  Scenario:
    Given I have $500 in my account
    When I choose withdraw the fixed amount of $350
    Then I should receive $350 cash
      And the balance of my account should be $150