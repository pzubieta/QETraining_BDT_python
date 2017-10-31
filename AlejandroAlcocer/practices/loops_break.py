import math

def area_of_circle(list_of_radius):
    '''
    Determine the area of a circle and return the value if it' higher than 10.
    :param list_of_radius: The radius
    :return: The area of the circle if it' higher than 10
    '''
    list_to_return = []
    for radius in list_of_radius:
        area = math.pi * radius ** 2
        if area >= 10: list_to_return.append('the area is: {}'.format(area))
        else: list_to_return.append('is not higher than 10')
    return list_to_return

def sum_to(list_of_numbers):
    '''
    Return the sum of the number from a list.
    :param number: A list of numbers.
    :return: The sum of all the numbers in the list.
    '''
    value_to_return = []
    for number in list_of_numbers:
        value_to_return.append(add_numbers(number))
    return value_to_return

def add_numbers(number):
    '''
    This method sum only one number.
    :param number: A number.
    :return: The sum of all previous numbers.
    '''
    if number <= 35:
        i = number
        sum_to_return = 0
        while i > 0:
            sum_to_return += i
            i -= 1
        return sum_to_return
    else: return 'the value is to big'

def odd_or_even(number):
    '''
    Return a string with a message if the number is even or odd.
    :param number: The number that will be tested
    :return: A string.
    '''
    if number % 2 == 0:
        return 'the number {} is even'.format(number)
    else:
        return 'the number {} is odd'.format(number)


def prime_or_not(list):
    '''
    This method determine prime numbers in a list.
    :param list: A list of numbers.
    :return: A list with false and true for each of the number in the list.
    '''
    list_to_return = []
    for number in list:
        list_to_return.append(is_number_prime(number))
    return list_to_return

def is_number_prime(number):
    '''
    This method determine if a number is prime or not.
    :param number: The number that will be tested.
    :return: True if it' prime and false if it's not prime
    '''
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False



def days_in_month(list_of_months):
    months = {'January': 31, 'February': 28, 'March': 31, 'April': 30,
              'May': 31, 'June': 30, 'July': 31, 'August': 31,
              'September': 30, 'October': 31, 'November': 30, 'December': 31}
    list_of_days = []
    for month in list_of_months:
        if month in months:
            list_of_days.append(months[month])
        else:list_of_days.append('is not in the dictionary')
    return list_of_days


#### TESTS#####


test_month = ['January', 'February', 'November']
print(days_in_month(test_month))

test_sum = [10,20,30,35,40]
print(sum_to(test_sum))

test_radius = [-1,0,2,3,4,5,100]
print(area_of_circle(test_radius))

test_numbers = [-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,15]
print(prime_or_not(test_numbers))

