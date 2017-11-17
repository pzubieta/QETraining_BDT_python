Feature: Searching in google
  Search information about a specific text o image in jpg,png , file, video

Scenario: Load a google page
  Given the conexion to Internet does exist
  When  Url: <www.google.com> is put in browser
  Then  Google home page is loaded
    And Search image, search text link are added

Scenario: Attempt to load a google page
  Given the conexion to Internet does not exist
  When  Url: <www.google.com> is put in browser
  Then Google page does not load
    And  An exception is returned to check the conexion

Scenario: Search a text
  Given Google home page is loaded in browser
    And I have to find a file  related to <text>
  When I enter <text> into the search bar
  Then All links related to <text> are displayed on ´result´ page

Scenario: Search a specific image
  Given Google home page is loaded in browser
    And I have to find an image related to <image name>
  When I enter <image name> into the search bar
    And I click on ´Images´ link at the top of the results page
  Then images related to <image name> are displayed on ´result´ page

Scenario: Search a specific video
  Given Google home page is loaded in browser
    And I have to find a video related to <video name>
  When I enter <video name> into the search bar
    And I click on ´Video´ link at the top of the results page
  Then videos related to <video name> are displayed on ´result´ page
