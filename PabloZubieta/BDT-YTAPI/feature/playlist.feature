@playlist
  Feature: This feature is to review the playlist feature
    @smoke
    Scenario: Review if a user can get a collection of playlist
      Given an authenticated user
      When I send a GET playlist
      Then I get a status code 200

    @CRUD
    Scenario Outline: Create new playlist
      Given I as an authenticated user
      When I send a <title>
        And I send a <description>
      Then I get a <code> response

      Examples:
        | title          |  description  | code|
        | TestPlaylist1  |This is a PL1  | 201 |
        | TestPlaylist2  |This is a PL2  | 201 |

   @CRUD
    Scenario: update a playlist
      Given I as an authenticated user
      When I send a new newTitle
        And I send a new newDescription
      Then I get a response with the playlist with newTitle as title
        And newDescription as description

   @CRUD
    Scenario: Delete a playlist
      Given I as an authenticated user
      When I send the ID of a playlist to be Delete
      Then I get a response with the playlist resource