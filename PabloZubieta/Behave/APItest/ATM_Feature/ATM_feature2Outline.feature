Feature: Withdraw Fixed Amount
  The "Withdraw Cash" menu contains several fixed amounts to speed uo transactions for users.

  Scenario Outline: Withdraw fixed amount
    Given I have <Balance> in my account
    When I choose withdraw the fixed amount of <Withdraw>
    Then I should receive <Cash> cash
      And the balance of my account should be <New_balance>

    Examples:
    |Balance|Withdraw|Cash|New_balance|
    |$500   |$50     |$50 |$450       |
    |$600   |$100    |$100|$500       |
    |$300   |$70     |$70 |$230       |
    |$200   |$10     |$10 |$190       |

