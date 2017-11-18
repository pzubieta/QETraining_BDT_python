def isPrime(min, max):
    for numbers in range(min, max+1):
        counter = 0
        for index in range(1, numbers+1):
            if numbers % index == 0: counter = counter + 1
        if counter == 2: print("Number %d is prime" % numbers)

isPrime(1,100)