def print10numbers():
    number = 0
    while number < 10:
        number += 1
        print(number)


def print10numbersSubtraction():
    number = 10
    while number > 0:
        number -= 1
        print(number+1)

def print10numbersMultiply():
    number_1 = 2
    number_2 = 3
    number_2 *= number_1
    print("Multiply Operator", number_2)

def print10numbersDivide():
    number_1 = 2
    number_2 = 3
    number_2 /= number_1
    print("Divide Operator", number_2)

def print10numbersModulus():
    number_1 = 2
    number_2 = 3
    number_2 %= number_1
    print("Mudulus Operator", number_2)


print10numbers()
print10numbersSubtraction()
print10numbersMultiply()
print10numbersDivide()
print10numbersModulus()