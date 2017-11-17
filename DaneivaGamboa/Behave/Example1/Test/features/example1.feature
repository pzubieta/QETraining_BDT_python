Feature: Example class

  Scenario: first case
    Given I have a $a
    When I select "asd
    Then My result should be "a"

  Scenario: second case
    Given Login as "Ana"
    And Pass is "log"
    When I click onm log
    Then Message "Welcome Ana"