Feature: Withdraw fixed amount
The 'Withdraw cash' menu contains several fixed amounts to
speed up a transaction for user
  
  Scenario Outline: Withdraw fixed amount
    Given I have <Balance> in my Account
	When I choose to withdraw the fixed amount of <Withdrawl>
	Then I should receive <Received> cash
	And the balance of my account should be <Remaining>

 Examples:
 |Balance|Withdrawl|Received|Remaining|
 |$500	 |$50	   |$50		|$450	  |
 |$500	 |$100	   |$100	|$400	  |
 |$500	 |$200	   |$200	|$300	  |
 |$500	 |$300	   |$300	|$200	  |
