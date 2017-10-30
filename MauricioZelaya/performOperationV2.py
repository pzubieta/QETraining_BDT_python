def perform_operation(operator, firstNumber, secondNumber):
    """function to perform the math operation according the symbols sent in the first argument of the function"""
    if operator == '+':
        return firstNumber + secondNumber
    elif operator == '-':
        return firstNumber - secondNumber
    elif operator == '*':
        return firstNumber * secondNumber
    elif operator == '/':
        return firstNumber / secondNumber
    elif operator == '%':
        return firstNumber % secondNumber
    elif operator == '**':
        return firstNumber ** secondNumber
    elif operator == '//':
        return firstNumber // secondNumber
    return "operator not recognized"

operatorsList = ['+', '-', '*', '/', '%', '**', '//']
firstNumber = input("write the first Number: ")
secondNumber = input("write the second Number: ")

for operator in operatorsList:
        result = perform_operation(operator, firstNumber, secondNumber)
        print("result of %s %s %s = %s" % (firstNumber, operator, secondNumber, result))

