# Create a function that receive 3 arguments :
#	2 numbers
#	1 operations
# According the operation defined the expected result need to be printed. For example :  operator “*” , numbers: “5” “6”
# perform_operation(“*”,”5”,”6”) => 30

def perform_operation(operation, number1, number2):
    if operation == "+":
        print("The operation is ADD")
        print ("The result of this operation is:", number1 + number2, "\n")
    elif operation == "-":
        print("The operation is SUBSTRACTION")
        print("The result of this operation is:", number1 - number2, "\n")
    elif operation == "*":
        print("The operation is MULTIPLICATION")
        print("The result of this operation is:", number1 * number2, "\n")
    elif operation == "/":
        print("The operation is DIVISION")
        print("The result of this operation is:", number1 / number2, "\n")
    elif operation == "%":
        print("The operation is MODULUS")
        print("The result of this operation is:", number1 % number2, "\n")
    elif operation == "**":
        print("The operation is EXPONENT")
        print("The result of this operation is:", number1 ** number2, "\n")
    elif operation == "//":
        print("The operation is FLOOR DIVISION")
        print("The result of this operation is:", number1 // number2, "\n")
    else:
        print ("The operation is not allowed")


#valid cases
perform_operation("+", 2, 3)
perform_operation("-", 9, 3)
perform_operation("*", 3, 5)
perform_operation("/", 10, 3)
perform_operation("%", 10, 3)
perform_operation("**", 2, 4)
perform_operation("//", 10, 3)

#Non-valid cases
perform_operation("?", 3, 6)
perform_operation("++", 4, 5)
