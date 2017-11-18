def askForArguments():
    """This function will ask three arguments two numbers and one operator"""
    number_1 = input("please enter first number"+'\n')
    number_2 = input("please enter second number"+'\n')
    operator = input("please enter the Operator"+'\n')
    allValues = [number_1, number_2, operator]
    return allValues

def task():
    """This function handle all the values entered by console and after review the condition execute it and show the results"""
    valuesEntered = askForArguments()
    if valuesEntered[2] == '+':
        result = int(valuesEntered[0]) + int(valuesEntered[1])
        print("%d + %d = %d" % (int(valuesEntered[0]), int(valuesEntered[1]), result))

    elif valuesEntered[2] == '-':
        result = int(valuesEntered[0]) - int(valuesEntered[1])
        print("%d - %d = %d" % (int(valuesEntered[0]), int(valuesEntered[1]), result))

    elif valuesEntered[2] == '*':
        result = int(valuesEntered[0]) * int(valuesEntered[1])
        print("%d * %d = %d" % (int(valuesEntered[0]), int(valuesEntered[1]), result))

    elif valuesEntered[2] == '/':
        result = int(valuesEntered[0]) / int(valuesEntered[1])
        print("%d / %d = %d" % (int(valuesEntered[0]), int(valuesEntered[1]), result))

    elif valuesEntered[2] == '%':
        result = int(valuesEntered[0]) % int(valuesEntered[1])
        print("%d module %d = %d" % (int(valuesEntered[0]), int(valuesEntered[1]), result))

    elif valuesEntered[2] == '**':
        result = int(valuesEntered[0]) ** int(valuesEntered[1])
        print("%d ** %d = %d" % (int(valuesEntered[0]), int(valuesEntered[1]), result))

    elif valuesEntered[2] == '//':
        result = int(valuesEntered[0]) - int(valuesEntered[1])
        print("%d // %d = %d" % (int(valuesEntered[0]), int(valuesEntered[1]), result))

    else:
        print("The operator entered doesn't exist please try again")


task()




