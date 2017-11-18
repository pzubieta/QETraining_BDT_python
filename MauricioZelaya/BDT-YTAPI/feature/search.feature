@search
Feature: This will test the search method feature for the API in youtube

  @smoke_test
  Scenario Outline: I would like to make a regression and obtain the response on the search method
    When I need to test the response in the <method> method
    Then I get a <code> response

    Examples:
      | method  | code |
      | /search | 200  |