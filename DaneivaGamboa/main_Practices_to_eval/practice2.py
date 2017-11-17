# Create 1 script to determine is a number is odd or even
# (use single line statement if applies)

number = 3

if number % 2 == 0:
    print("Number is ood")
else:
    print("Number is par")

print("------------------------------")

# According a list of values between a Min and Max range,
# identify if the number is prime or not.

number_min = 0
number_max = 100
total_prime_found = 0

if number_min>=0:
    number_min=2;
    for i in range(number_min, number_max):
        verif_prime = True
        for divisor in range(2, i):
            if i % divisor == 0:
                verif_prime = False
        if verif_prime:
            print ( " -", i, "is prime")
            total_prime_found =total_prime_found+1
        else:
            print ( " -", i, "is not prime")
    print("We find",total_prime_found,"prime numbers ")


