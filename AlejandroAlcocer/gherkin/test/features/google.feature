
Feature: Testing search engine for google.com

  @smoke
  Scenario: Verify that endpoint is available
    Given I want to know if google is up
    When I send a message to a google method
    Then I should get a 2xx response

  @acceptance
  Scenario: Search for "x" information
    Given I want to search for the word
    When I write the word: "tesla"
    Then I get by default 20 results that include the word "tesla"
      And I get the response of 2xx

  @negative
  Scenario: Search for invalid information
    Given I want google execute some html tags
    When I send the html code tags
    Then The browser should not execute the code
      And the response should be results with the code tag
      And a 2xx response for the API

  @smoke @negative
  Scenario: Verify that is possible to sign in
    Given A user name and a password
      But invalid credentials
    When I attempt to login with the credentials
    Then I get an exception

  @negative @functional
  Scenario: Verify that is possible to sign in
    Given Valid user name and a password
    When I attempt to login with the credentials
    Then I get a success message

#  Scenario: Verify that is possible search by images
#    Given A word to search
#      And a by image criteria
#    When I attempt to search for that image
#    Then I get a success message
#      And A list of images that match
#      And a 2xx response for the API
#
#  Scenario: Verify that is possible search by videos
#    Given A word to search
#      And a by videos criteria
#    When I attempt to search for that video
#    Then I get a success message
#      And A list of videos that match
#      And a 2xx response for the API
#
#  Scenario: Verify that is possible search by news
#    Given A word to search
#      And a by news criteria
#    When I attempt to search for that news
#    Then I get a success message
#      And A list of news that match
#      And a 2xx response for the API
#
#  Scenario: Verify that is possible search by maps
#    Given A word to search
#      And a by maps criteria
#    When I attempt to search for that map
#    Then I get a success message
#      And A list of maps that match
#      And a 2xx response for the API
#
#  Scenario: Verify that is possible obtain second page of results
#    Given A word to search
#    When I attempt to obtain results from the page 2
#    Then I get a success message
#      And A list of search that match
#      And a 2xx response for the API
#
#  Scenario: Verify that is possible set the language
#  * That I want to change the language of the app
#  * I attempt to set the language
#  * I get a success message
#  * a 2xx response for the API
#
