def verify_odd_even_number(value):
    """
    Method to define if the given value is odd or even

    :param value:   int     represent the number to be verified
    """
    print("Number is EVEN") if value % 2 == 0 else print("Number is ODD")

# Case when the user insert ODD number
verify_odd_even_number(33)
print("--------------------------")
# Case When the user insert EVEN number
verify_odd_even_number(20)


def generate_prime_number(min_range, max_range):
    """
    Method that generate a list of prime numbers given a range.

    :param min_range:   int     Represents the min number of the range
    :param max_range:   int     Represents the max number of the range
    """
    prime_list = []
    if min_range < max_range:
        for number in range(min_range, max_range+1):
            if is_prime(number): prime_list.append(number)

        if prime_list:
            print("Prime Number List into the given Range: {} - {}".format(min_range, max_range))
            for prime in prime_list: print(prime)
        else:
            print("There is any prime number into the given Range: {} - {}".format(min_range, max_range))
    else:
        print("Please insert valid range")


def is_prime(number):
    """
    Method to determine if a number is prime or not
    :param number:  int     The number to validate if is prime
    :return:        bool    True if the number is prime, False other way.
    """
    count = 0
    for i in range(1, abs(number) + 1):
        if number % i == 0:
            count += 1
    return True if count == 2 else False

# Case when there is prime number
generate_prime_number(1, 17)
print("--------------------------")
# Case when there is any prime in the range
generate_prime_number(54,58)
