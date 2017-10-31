# primes in range
def isPrime (number):
    flag = True
    if number > 1:
        for val in range(2, number):
            if number % val == 0:
                flag = False
                break
            else:
                flag = True
    return flag


listOfNumbers = [9, 3, 7, 35, 21, 7, 3, 1, 2, 94537]
for number in listOfNumbers:
    if isPrime(number):
        print("%s is prime " % number)
    else:
        print("%s is not prime " % number)
