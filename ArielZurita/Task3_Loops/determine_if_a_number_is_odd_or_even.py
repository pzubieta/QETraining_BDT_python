def determine_number():
    while True:
        number = int(input("Please enter a number \n"))
        if (number%2 == 0): print("The number %d is even" %number)
        else: print("The number entered %d is odd" %number)

determine_number()