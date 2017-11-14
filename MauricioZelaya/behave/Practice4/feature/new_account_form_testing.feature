Feature: Validating fields of create account form
  Scenario: Validating form fields
    Given user first name is Mauricio
      And user last name is Zelaya
      And desired username is maurizel
      And password is Control1234_
      And confirm password contains Control1234_
      And birthday month is 3
      And birthday day is 11
      And birthday year is 1980
      And gender is Male
      And Mobile phone is 70720612
      But has not current email address