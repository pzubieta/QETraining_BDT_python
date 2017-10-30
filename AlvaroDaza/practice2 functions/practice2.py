number1 = 10
number2 = 4
operator = '+'


def operations(number1, number2, operator):
    if operator == '+':
        print ('the addition is:' + str(number1 + number2))
    elif operator == '-':
        print ('the subtraction is:' + str(number1 - number2))
    elif operator == '*':
        print ('the multiplication is:' + str(number1 * number2))
    elif operator == '/':
        print ('the division is:' + str(number1 / number2))
    else:
        print ('the operator is not recognized')


operations(number1, number2, operator)
