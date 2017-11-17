Feature: Add a video to the playlist
  As a registered youtube user I can add a video from youtube to my personal playlist.

  The video that I added should appear in the list every time I open my playlist.

  Scenario: Adding a video to user's playlist
    Given A user logged to youtube
      And the user has a playlist
     When the user is watching the recommended videos list
      And expands options of a video from the list
      And select "Add to playlist"
     Then the video is added to the list
      And the playlist shows the video appended to the end
