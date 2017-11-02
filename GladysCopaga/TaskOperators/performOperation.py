# First version to perform operations
def performOperation (operator,number1,number2):
    number3 = 0
    if (operator == "+"):
        number3 = (number1 + number2)
    elif (operator == "-"):
        number3 = (number1 - number2)
    elif (operator == "*"):
        number3 = (number1 * number2)
    elif (operator == "/"):
        number3 = (number1 / number2)
    elif (operator == "%"):
        number3 = (number1 % number2)
    elif (operator == "**"):
        number3 = (number1 ** number2)
    elif (operator == "//"):
        number3 = (number1 // number2)
    print("(' %s" %(operator), "' , '", (number1), "' , '", (number2), "') The result is: ", (number3))
performOperation("+",1,2)


# Second version to perform operations with input
def ArithmeticOperations():
    num1 = eval(input("Introduzca un numero1: "))
    num2 = eval(input("Introduzca un numero2: "))
    oper = input("Introduzca un operador: ")
    num3 = 0
    if (oper == "+"):
        num3 = (num1 + num2)
    elif (oper == "-"):
        num3 = (num1 - num2)
    elif (oper == "*"):
        num3 = (num1 * num2)
    elif (oper == "/"):
        num3 = (num2 / num1)
    elif (oper == "%"):
        num3 = (num2 % num1)
    elif (oper == "**"):
        num3 = (num1 ** num2)
    elif (oper == "//"):
        num3 = (num1 // num2)
    else:
        print("introduzca un operador aritmetico como: +, -, *, /, %, ** o //")
        exit()
    print ("Operador:", oper, ", numero1:", num2, ", numero2:", num2)
    print ("La suma es: ", num3)
ArithmeticOperations()