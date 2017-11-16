#© Copyright 2017 by Dennis G.
#This is my Dennis G.
#This is my Dennis G.
  Feature: Google Searching
  User should be able to search articles, files and images from web

  Scenario: Simple Google search
    Given User navigates to the Google home page
    When user enters "Jalasoft" at the search bar
    Then links related to "Jalasoft" will be shown on the results page

  Scenario: Sign in into Google
    Given User navigates to the Google home page
    When User does a click on "Sign in"
      And login with an account invalid
      And login with a valid account
    Then account is displayed in the home page
      And Message error is displayed if an account is invalid

    Scenario: Search by voice
    Given User navigates to the Google home page
    When User does a click on "Microphone icon"
    Then New page is displayed listening what do you need to search

    Scenario: Gmail home page
    Given User navigates to the Google home page
    When User does a click on "Gmail" link
    Then New page is displayed with gmail home page

    Scenario: Books search
    Given User navigates to the Google home page
    When User enters "Jalasoft" into the search bar
      And User does a click on search option
      And User does a click on More link option
      And User does a click on Books link option
    Then Books related to "Jalasoft" are shown in the results page