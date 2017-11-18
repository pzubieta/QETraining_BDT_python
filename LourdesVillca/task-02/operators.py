def comparison_operators(number1, number2):
    """
    Method to apply comparison operators.

    :param number1:     int     Number to make operations
    :param number2:     int     Number to make operations
    """
    if number1 == number2:
        print("Result for operator '==' is:", number1 == number2)
    if number1 != number2:
        print("Result for operator '!=' is:", number1 != number2)
    if number1 >= 0 and number1 <= 100:
        print("{} is between the range: 1-100".format(number1))
    if number2 > 50 and number2 < 300:
        print("{} is between the range: 50-300".format(number2))


def assignment_operators(value1, value2):
    """
    Method to apply assignment operators.

    :param value1:     int     Number to make operations
    :param value2:     int     Number to make operations
    """
    print("Initial Values - value1 = {}, value2 = {}".format(value1,value2))
    value1 += 10
    print("value1 after apply Assignment operator '+=' is {}".format(value1))
    value1 -= 10
    print("value1 after apply Assignment operator '-=' id {}".format(value1))
    value2 *= 10
    print("value2 after apply Assignment operator '*=' is {}".format(value2))
    value2 /= 10
    print("value2 after apply Assignment operator '/=' is {}".format(value2))


def membership_operators(value):
    """
    Method to apply membership operators.
    :param value:   int     number to make operations.
    """
    result = value
    if result is value:
        print("Result is Value")


def identity_operators(value):
    """
    Method to where to apply identity operators.

    :param value:   string     string to make operations.
    """
    if value is not None:
        if "Python" in value:
            print("string 'python' is in {}".format(value))
        else:
            print("string 'python' is not in {}".format(value))
    else:
        print("Invalid String")

comparison_operators(34,70)
assignment_operators(23, 89)
membership_operators([4,3])
identity_operators("Hello Python!!")