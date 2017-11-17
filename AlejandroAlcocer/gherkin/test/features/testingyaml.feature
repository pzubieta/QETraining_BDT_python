Feature: API

  Scenario:
    Given I have connection to "http://todo.ly"
    When I send GET
    Then I receive status code 200