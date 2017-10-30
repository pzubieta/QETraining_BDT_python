def comparisionOperators(firstNumber, secondNumber, operator):
    """return type is void"""
    if operator == '==':
        if(firstNumber==secondNumber):
            print("%s is exactly equal to %s and operator used was %s" % (firstNumber, secondNumber, operator))
        else:
            print("%s is not equal to %s and operator used was %s" % (firstNumber, secondNumber, operator))
    elif operator == '!=':
        if (firstNumber != secondNumber):
            print("%s is not equal to %s and operator used was %s" % (firstNumber, secondNumber, operator))
        else:
            print("%s is equal to %s and operator used was %s" % (firstNumber, secondNumber, operator))
    elif operator == '>':
        if (firstNumber > secondNumber):
            print("%s is greater than to %s and operator used was %s" % (firstNumber, secondNumber, operator))
        else:
            print("%s is not greater than to %s and operator used was %s" % (firstNumber, secondNumber, operator))
    elif operator == '<':
        if (firstNumber < secondNumber):
            print("%s is less than to %s and operator used was %s" % (firstNumber, secondNumber, operator))
        else:
            print("%s is not less than to %s and operator used was %s" % (firstNumber, secondNumber, operator))
    elif operator == '<=':
        if (firstNumber <= secondNumber):
            print("%s is less than or equal to %s and operator used was %s" % (firstNumber, secondNumber, operator))
        else:
            print("%s is not less than or equal to %s and operator used was %s" % (firstNumber, secondNumber, operator))


def assignmentOperators(firstNumber, secondNumber, operator):
    """"return type is void"""
    # print("Original value of newNumber is %s" % (newNumber))
    newNumber = secondNumber
    if operator == '=':
        print("%s was assigned to secondNumber var due to operator used is %s" % (firstNumber, operator))
    elif operator == '+=':
        secondNumber += firstNumber
        print("original value of the second number was %s, after apply %s operator the new value assigned is %s " % (newNumber, operator, secondNumber))
    elif operator == '-=':
        secondNumber -= firstNumber
        print("original value of the second number was %s, after apply %s operator the new value assigned is %s " % (newNumber, operator, secondNumber))
    elif operator == '*=':
        secondNumber *= firstNumber
        print("original value of the second number was %s, after apply %s operator the new value assigned is %s " % (newNumber, operator, secondNumber))
    elif operator == '/=':
        secondNumber /= firstNumber
        print("original value of the second number was %s, after apply %s operator the new value assigned is %s " % (newNumber, operator, secondNumber))
    elif operator == '%=':
        secondNumber %= firstNumber
        print("original value of the second number was %s, after apply %s operator the new value assigned is %s " % (newNumber, operator, secondNumber))
    elif operator == '**=':
        secondNumber **= firstNumber
        print("original value of the second number was %s, after apply %s operator the new value assigned is %s " % (newNumber, operator, secondNumber))
    elif operator == '//=':
        secondNumber //= firstNumber
        print("original value of the second number was %s, after apply %s operator the new value assigned is %s " % (newNumber, operator, secondNumber))


def membershipAndIdentityOperators(aNumber, operator):
    numericList = [1, 2, 3, 4, 5]
    if operator == 'in':
        if(aNumber in numericList):
            print("%s is in numeric list using the operator: %s" % (aNumber, operator))
        else:
            print("%s is not in numeric list using the operator: %s" % (aNumber, operator))
    if operator == 'not in':
        if(aNumber not in numericList):
            print("%s is not in numeric list using the operator: %s" % (aNumber, operator))
        else:
            print("%s is in numeric list using the operator: %s" % (aNumber, operator))
    if operator == 'is':
        if(aNumber is numericList):
            print("%s has an id in numeric list using the operator: %s" % (aNumber, operator))
        else:
            print("%s has not an id in numeric list using the operator: %s" % (aNumber, operator))
    if operator == 'is not':
        if(aNumber is not numericList):
            print("%s has not an id in numeric list using the operator: %s" % (aNumber, operator))
        else:
            print("%s has an id in numeric list using the operator: %s" % (aNumber, operator))


comparisionOperatorList = ['==', '!=', '>', '<', '<', '>=', '<=']
assignmentOperatorList = ['=', '+=', '-=', '*=', '/=', '%=', '**=', '//=']
membershipAndIdentityOperatorList = ['in', 'not in', 'is', 'is not']
number1 = 2
number2 = 3

for operator in comparisionOperatorList:
    comparisionOperators(number1, number2, operator)
for operator in assignmentOperatorList:
    assignmentOperators(number1, number2, operator)
print("numeric list is: 1, 2 ,3, 4, 5")
for operator in membershipAndIdentityOperatorList:
    membershipAndIdentityOperators(number1, operator)
