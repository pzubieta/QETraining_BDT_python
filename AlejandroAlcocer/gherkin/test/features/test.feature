Feature: First feature

  Scenario Outline: Scenario: Testing in class
    Given I have $<value> in my account

    Examples:
      | value |
      | 100   |
      | 200   |
      | 300   |

  Scenario: filling form
    Given I fill the zip code field with 2500
    And I fill the country field with Bolivia
    And I fill the number with thousands with 1594.9

