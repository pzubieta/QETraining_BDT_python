import random

def generateNumberPrime(inicio, fin):
    list = []
    while inicio <= fin:
        list.append(random.randrange(100))
        for index in range(len(list)):
            verifyPrime(list[index])
        inicio = inicio + 1

def verifyPrime(number):
    count = 0
    for i in range(1, number + 1):
        if (number % i == 0):
            count = count + 1
    if (count != 2):
        print(" - No es primo", number)
    else:
        print("Si es primo", number)


generateNumberPrime(10, 90)