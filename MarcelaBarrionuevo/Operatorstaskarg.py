def perform_operation(numone, numtwo, operator):

    if operator == "+":
        sum = numone + numtwo
        print("The sum between %d and %d is: " % (numone, numtwo), sum)
    elif operator == "-":
        sub = numone - numtwo
        print("The subtraction between %d and %d is: " % (numone, numtwo), sub)
    elif operator == "*":
        mul = numone * numtwo
        print("The multiplication between %d and %d is: " % (numone, numtwo), mul)
    elif operator == "/":
        div = numone / numtwo
        print("The division between %d and %d is: " % (numone, numtwo), div)
    elif operator == "%":
        mod = numone % numtwo
        print("The module between %d and %d is: " % (numone, numtwo), mod)
    elif operator == "**":
        exp = numone ** numtwo
        print("The exponent between %d and %d is: " % (numone, numtwo), exp)
    elif operator == "//":
        flo = numone // numtwo
        print("The floor between %d and %d is: " % (numone, numtwo), flo)
    else:
        print("Invalid operator")

perform_operation(4, 5, "/")


