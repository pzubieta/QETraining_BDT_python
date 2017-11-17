Feature: Search by Google

This is a page that allows search by phrases or words introduced inside text field, as standard user 

Scenario: Go to Google page

Given  Internet connection and URL as 'https://www.google.com/'
When  A user introduce URL in address bar and press enter
Then  A google page should be displayed and search field should be editable

Scenario: Search  topic

Given  Google page active and a topic chosen
When  A user introduce the topic in words inside search field 
            and press the search button
Then  A list of pages that contains the words should be displayed 
           and the list should be sorted by priority

Scenario: Choose search category

Given A list of search in Google
          and labels with categories
When A user click on selected category

Then A new list or result should be displayed