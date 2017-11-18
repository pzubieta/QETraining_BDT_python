#Copyright (C) 2017 Miquilin - All Rights Reserved. You may use, distribute and modify this code under the terms of the XYZ license, which unfortunately won't be written for another century.
#You should have received a copy of the XYZ license with this file. If not, please write to: mixmeil@gmail.com, or visit: https://miquilin.wordpress.com/

Feature: Google Searching
  User should be able to search articles, files and images from web

  Scenario: Simple Google search
    Given User navigates to the Google home page
    When user enters "Jalasoft" at the search bar
    Then links related to "Jalasoft" will be shown on the results page

  Scenario: Search from the search bar
    Given a web browser in the Google home page
    When User enters "Jalasoft" into the search bar
    Then links related to "Jalasoft" are shown on the results page

  Scenario: Image search
    Given Google search results for "Jalasoft" are shown
    When User does a click on Images link option
    Then images related to "Jalasoft" are shown on the results page

    Scenario: location search
    Given User navigates to the Google home page
    When User enters "Jalasoft" into the search bar
      And User does a click on search option
      And User does a click on Maps link option
    Then A map with the Jalasoft's location is displayed

    Scenario: Books search
    Given User navigates to the Google home page
    When User enters "Jalasoft" into the search bar
      And User does a click on search option
      And User does a click on More link option
      And User does a click on Books link option
    Then Books related to "Jalasoft" are shown in the results page


    Scenario: Pesonal search
    Given Google search results for "Jalasoft" are shown
    When User does a click on More link option
      And User does a click on Personal link option
    Then Personal links related to "Jalasoft" are shown on the results page