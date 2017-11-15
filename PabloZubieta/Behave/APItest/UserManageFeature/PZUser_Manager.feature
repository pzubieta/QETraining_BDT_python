Feature: User management
  Background: Go to My profile
    Given I login appication
    When I click on User icon
    Then I see My profile

  Scenario: Change user picture
    Given I select change picture
    When I select a new image from my pc
    Then I see new picture

  Scenario: Change user password
    Given I select change password
    When I save my new password
    Then I should see confirmation message
