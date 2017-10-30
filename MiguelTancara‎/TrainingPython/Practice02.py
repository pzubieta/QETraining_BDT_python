#Create python script applying at least one time each one of the operators learned.
#Print the values and the condition that give you the result obtained.

def logicalOperator(operator, number1, number2):
    print("Operator is: ", operator)
    if operator == "==":
        if number1 == number2:
            print(number1, " is equal to ", number2)
        else:
            print(number1, " is different to ", number2)
    elif operator == "!=":
        if number1 != number2:
            print(number1, " is different to ", number2)
        else:
            print(number1, " is equal to ", number2)

    elif operator == ">":
        if number1 > number2:
            print(number1, " is greater than ", number2)
        else:
            print(number1, " is equal o minor than ", number2)
    elif operator == "<":
        if number1 < number2:
            print(number1, " is minor than ", number2)
        else:
            print(number1, " is equal o greather than ", number2)
    elif operator == ">=":
        if number1 >= number2:
            print(number1, " is greater than or equal to", number2)
        else:
            print(number1, " is minor than ", number2)
    elif operator == "<=":
        if number1 <= number2:
            print(number1, " is minor than or equal to ", number2)
        else:
            print(number1, " is greather than ", number2)
    else:
        print("Comparison operator is a non-valid one")


#Positive cases
logicalOperator("==", 100, 100)
logicalOperator("!=", 100, 102)
logicalOperator(">", 103, 102)
logicalOperator("<", 10, 102)
logicalOperator(">=", 125, 85)
logicalOperator("<=", 16, 945)

#Negative cases
logicalOperator("*", 100, 100)
logicalOperator("equal", 100, 100)