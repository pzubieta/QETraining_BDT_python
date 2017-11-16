@customer_search
Feature: customer search
  Scenario Outline: getting the total priced for a given user
    Given a <Customer_ID>
    When I request the <total_amount> of a purchase
    Then I get the <Customer_ID> information



    Examples:
    | Customer_ID | Customer_Name | total_amount |
    |1            |Mauricio       |1500          |
    |2            |Diego          |2000          |
    |3            |Noelia         |2000          |
    |4            |Maria_Esther   |3000          |
    |5            |Carmela        |1300          |
    |6            |Dana           |1000          |
    |7            |Katya          |1150          |
    |8            |Lizeth         |1800          |
    |9            |Maria_Rene     |1745          |
    |10           |Ariel          |1325          |