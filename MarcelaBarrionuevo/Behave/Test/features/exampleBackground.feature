Feature: User Management
test background 
  Background: Go to my profile
    Given I login application
	When I click on the user Icon
    Then I see my profile	

  Scenario: Change User Picture
    Given I select change picture
	When I select a new image
    Then I see the pictore loaded	

  Scenario: Change User Password
    Given I select change password
	When I save my new password
    Then I should see confirmation message	
	