def number_prime():
    """This method is to identify if a number is prime or not"""
    number = int(input("Please enter a number\n"))
    counter = 0
    for i in range(1, number+1):
        if (number % i == 0): counter = counter+1
    if counter == 2: print("The number %d is prime" %number)
    else: print("The number %d is not prime" %number)

number_prime()
