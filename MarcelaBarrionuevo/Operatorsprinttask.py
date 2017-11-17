def perform_operation_asig(numone, numtwo):

    result = numone
    result += numtwo
    print("The sum between %d and %d is: " % (numone, numtwo), result)

    result = numone
    result -= numtwo
    print("The subtraction between %d and %d is: " % (numone, numtwo), result)

    result = numone
    result *= numtwo
    print("The multiplication between %d and %d is: " % (numone, numtwo), result)

    result = numone
    result /= numtwo
    print("The division between %d and %d is: " % (numone, numtwo), result)

    result = numone
    result %= numtwo
    print("The module between %d and %d is: " % (numone, numtwo), result)

perform_operation_asig(8, 2)