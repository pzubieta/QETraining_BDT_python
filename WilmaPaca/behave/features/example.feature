Feature:
Scenario:
  Given I have ${amount:d} in my Account
  Given I have $abc in my Account
  When I request ${amount1:d} of my account
  Then My account is {amount:d} substraction {amount1:d}
    And I have happy