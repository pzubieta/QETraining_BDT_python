Feature: search google
	When I Google search an item, I expect to see the result of the item in the result summary.

Scenario: search "music rock "
	Given that I have gone to the Google page
	When I add "Metalica" to the search box
	And click the Search Button
	Then "Metalica" should be displayed in the results

Scenario: search box empty
	Given that I have gone to the Google page
	When I not add any item in the search box
	And click the Search Button
	Then not should be displayed any result. 