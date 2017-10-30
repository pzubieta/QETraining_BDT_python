# primes in range
def isPrime (number):
    for val in range(2, number):
        if(number % val == 0): return True
        else: return False

print("%s is prime " % number)