@test @test1
Feature: User Managment

  Background: Go to My Profile
    Given I login application
    When I click User icon 2
    Then I see My profile

  @functional @test2

  Scenario: Change user picture
    Given I selec change pic
    When I select a new image from my PC
    Then I see new picture loaded

    @smoke
      Scenario: Change user password
      Given I selec change pass
      When I save my new pass
      Then I should see confirmation message



