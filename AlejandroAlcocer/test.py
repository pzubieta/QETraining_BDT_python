# flag = 1
# while (flag): print('Given flag is really true!')
# print('Goodbye')

# determineif a value is odd or even
# list of values determine if a number is prime or not
# write a function area_of_circle(r) which returns the area of a circle of raidious r only if
# the radios value is greater of 10


import random
import math

def area_of_circle(r):
    return math.pi*r**2 >= 10

def sum_to(list_numbers):
    value_to_return = 0
    for number in list_numbers:
        if value_to_return + number <= 35:
            value_to_return += number
        else: return value_to_return
    return value_to_return

print(sum_to([1,50,7,9]))

def odd_or_even(number):
    if number % 2 == 0:
        return 'the number {} is even'.format(number)
    else:
        return 'the number {} is odd'.format(number)


def prime_or_not(list):
    for number in list:
        cont = 2
        divisions = 1
        while cont >= number:
            if number / cont == 1 and divisions < 2:
                divisions += 1
                return 'prime'




# val = 20
# while val > 0:
#     print('current value: ', val)
#     val -= 1
#     if val == 5:
#         print('in the break')
#         break
#     print('in the loop')
# print('Good bye')
# print(odd_or_even(random.randrange(0, 1000)))
