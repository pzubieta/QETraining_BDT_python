def prime(number):
    count = 0
    for i in range(1, (number+1)):
         if number % i == 0:
             count += 1
    if count > 2:
        print (number, "is not a prime number")
    else:
        print (number, "is a prime number")

def list_prime(min, max):
	for i in range(min, max):
		prime(i)
list_prime(2,9)