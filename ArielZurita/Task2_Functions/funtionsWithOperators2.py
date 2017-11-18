def askForArguments():
    """This function will ask two values"""
    value_1 = input("please enter first value"+'\n')
    value_2 = input("please enter second value"+'\n')
    allValues = [value_1, value_2]
    return allValues

def comparisonOperatorsCharacters():
    dataEntered = askForArguments()
    if dataEntered[0] == dataEntered[1]:
        print("Values entered are equal")

    elif dataEntered[0] != dataEntered[1]:
        print("Values entered are not equal")

def comparisonOperatorsNumbers():
    print("Please enter numbers")
    dataEntered = askForArguments()
    value1 = int(dataEntered[0])
    value2 = int(dataEntered[1])
    if (value1 > value2):
        print("%d is greater than %d" % (value1, value2))
    elif (value1 < value2):
        print("%d is lower than %d" % (value1, value2))
    else:
        print("Values entered are not numbers please try again with other numbers")

def comparisonOperatorsLengtgOfCharacters():
    dataEntered = askForArguments()
    if len(dataEntered[0]) >= len(dataEntered[1]):
        print("length of ", dataEntered[0], " is greater or equal than ", dataEntered[1])

    else:
        print("length of ", dataEntered[0], " is lower or equal than ", dataEntered[1])

#comparisonOperatorsCharacters()
#comparisonOperatorsNumbers()
comparisonOperatorsLengtgOfCharacters()

