Feature: Creation new gmail account
validation of form new gmail account

  Scenario: create new gmail account
    Given  I enter the first name: Daneiva
    And I enter last name: Gamboa
    And I enter username: degamboa
    And I enter pass: pass123.
  But I enter confirm_pass: pas123.
    And I enter birthday 02/02/1986
    And I enter gender: female
    And I enter email: daneiva@gmail.com
    Then The new Gmail Account should be created.