Feature: Create a gmail account

Scenario:
  Given I want to create an gmail account in: 'www.gmail.com'
  Given My name is: Wilma Paca
  Given username: patytest
  Given password: P4ssw0rd!
  Given Cofirm to password: P4ssw0rd!
  Given Birthday: 23 septiembre 1985
  Given Gender: Female
  Given My current email: 'florpaty@gmail.com'
  Then I have a new email

