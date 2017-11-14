Feature: Google main page
  Scenario: Google search using  valid words
    Given a web browser is in Google home page
    When the user enters words to search into the search text field
	And the user clinks in 'Google Search'
    Then links related to word that user entered are shown on the results page
	
  Scenario: Google search using only special characters 
    Given a web browser is in Google home page
    When the user enters only special characters into the search text field
	And the user clinks in 'Google Search'
	And message about did not match any documents  is displayed
	And the user enters words to search into the search text field
	And the user clicks in 'Search' image icon
    Then links related to word that user entered are displayed on the results page
	
  Scenario: Google I'm Felling Lucky
    Given a web browser is at the Google home page
    When the user clinks in 'I'm Felling Lucky'
	And active google doodles 
	And the users selects a google doodle
    Then google doodle with the History is opened
	
  Scenario: Google offered
    Given a web browser is at the Google home page
	When the user Clicks in offered language
	And Google home page is refreshed 
    Then all Google home page is displayed in the prefered language 

  Scenario: Google Gmail without saved session
    Given a web browser is at the Google home page
	When the user Clicks in 'Gmail' link
	And there are no saved gmail accounts in the browser
	And page is redirected to gmail page
	Then gmail links and options are displayed on the gmail page

  Scenario: Google Gmail with saved session
    Given a web browser is at the Google home page
	When the user Clicks in 'Gmail' link
	And there are saved gmail accounts in the browser
	Then gmail email for saved account is displayed
	
  Scenario: Google Images with valid words to search the image
    Given a web browser is at the Google home page
	When the user Clicks in 'Images' link
	And Google images serach page is displayed
    And the user enters words to search images into the search text field
	And the user press 'Enter' key in the keyboard 
	Then images related to word that user entered are shown on the results page

  Scenario: Google Images search without pressing enter
    Given a web browser is at the Google home page
	When the user Clicks in 'Images' link
	And Google images serach page is displayed
    And the user enters words to search images into the search text field
	But the user doesn't press 'Enter' key in the keyboard 
	Then images related to word that user entered are not displayed
	
  Scenario: Google Apps using more option
    Given a web browser is at the Google home page
	When the user Clicks in Google Apps image icon
	And 'My Accpunt', 'Serach', 'Maps', 'Play', 'Gmail', 'Drive', 'Calendar', 'Google+', and  'Traslate' menu are displayed
	And the user cliks in 'More' option
	And 'Docs', 'Books', 'Blogger', 'Contacts', 'Hangouts', and 'Keep' menu are displayed
	Then all main google apps menu are displayed

  Scenario: Google Apps without more option
    Given a web browser is at the Google home page
	When the user Clicks in Google Apps image icon
	And 'My Accpunt', 'Serach', 'Maps', 'Play', 'Gmail', 'Drive', 'Calendar', 'Google+', and  'Traslate' menu are displayed
	But  the user doesn't clik in 'More' option
	Then not all main google apps menu are displayed

  Scenario: User Location Google
    Given a web browser is at the Google home page
	When the user see on the footer page
	Then user's  Country is inthe footer 

  Scenario: Google Sign In without saved session
    * I have a web browser is at the Google home page
	* the user Clicks in 'Sign In' button
	* there is not google session saved in the browser
    * Then 'Sign in' form to credentials is displayed
  
  Scenario: Google Sign In with one saved session
    Given a web browser is at the Google home page
	When the user Clicks in 'Sign In' button
	And there is google session saved in the browser
	And profile picture is displayed in the header
	And user clicks in profile picture
	And only one session is saved
	Then google mail information is displayed

  Scenario: Google Sign In with several sessions saved
    Given a web browser is at the Google home page
	When the user Clicks in 'Sign In' button
	And there is google session saved in the browser
	And profile picture is displayed in the header
	And user clicks in profile picture
	And There are more than one session saved
	Then google mail information for all sessions saved displayed
	
 Scenario: Google Footer links
    Given a web browser is at the Google home page
	When the user see on the footer page
	Then user see all footer links Privacy Terms, Settings, Advertising, Business, and About
	
  Scenario: Google Privacy Terms
    Given a web browser is at the Google home page
	When the user cliks in 'Privacy Terms' on the footer page
	Then user is redirected to 'Privacy Terms' page

  Scenario: Google Settings 
    Given a web browser is at the Google home page
	When the user cliks in 'Settings' on the footer page
	Then user is redirected to 'Settings' page
	
  Scenario: Google Advertising
    Given a web browser is at the Google home page
	When the user cliks in 'Advertising' on the footer page
	Then user is redirected to 'Privacy Terms' page

  Scenario: Google Business 
    Given a web browser is at the Google home page
	When the user cliks in 'Business' on the footer page
	Then user is redirected to 'Business' page
	
  Scenario: Google Business 
    Given a web browser is at the Google home page
	When the user cliks in 'About' on the footer page
	Then user is redirected to 'About' page
	



