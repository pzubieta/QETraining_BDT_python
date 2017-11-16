#@try
#Feature: Withdraw fixed amount

#  @tag
#  Scenario Outline: Withdraw fixed amount of $50
#    Given I have $<amount> in my account
#    When I choose to withdraw the fixed amount of $<amount_to_withdraw>
#    Then I should receive $<withdraw> cash
#    And the balance of my account should be $<balance>
#
#  Scenario Outline: Withdraw fixed amount of $50
#    Given I have $<amount> in my account
#    When I choose to withdraw the fixed amount of $<amount_to_withdraw>
#    Then I should receive $<withdraw> cash
#    And the balance of my account should be $<balance>

#    this is outline JIC, different values for different steps
#    Examples: account
#      | amount  | amount_to_withdraw | withdraw | balance |
#      | 5000.00 | 1000.00            | 1000.00  | 4000.00 |
#      | 358.21  | 58.11              | 58.11    | 300.10  |
#      | 250.00  | 300.00             | 300.00   | -50.00  |