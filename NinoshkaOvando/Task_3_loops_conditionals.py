########### TASK create script
#1 determinar si un par o impar entrada
# dentro un minimo y un rango, determinar si el numero es o no primo e imprimirlo
#range(10, 20)
#for y while  ---->
#Task 1#########################################################################
def  is_pair(number):
    if(type(number)==int):
        if(int(number)%2 ==0):
            print('The number {} is pair '.format(str(number)))
        else:
            print('The number {} is not pair '.format(str(number)))
    else:
        return None
#Task 2#########################################################################
def is_prime(number):
    if (type(number) == int):
        num= int(number)
        range_b = range(2, num)
        for i in range_b:
            if (num % i) == 0:
                # es divisible
                return False
        return True
# Task 3#########################################################################
#3. write a fuction area_of_circle(r) which returns the area of a circle of radius R only
#the radius value is greater than 10
# a= pi*r2
def area_of_cicle(r):
    pi= 3.141516
    if (type(r)== int):
        if(r>10):
            value= pi*(r*r)
            print("The area is", value)
            print('Radio is {} and its Area is {} '.format( r, value))
        else:
            print('Radius {} is less than 10'.format(r))
    else:
        print("Enter a integer")
# Task 4#########################################################################
#4. white a function sum_to(n) that returns the sum of all integer numbers up to and
# including only until any vaue lower than 35
def sum_to(n):
    sum_a =0
    if (type(n)== int):
        number=int(n)
        range_x = (1, number)
        for val in range_x:
            if (n > 35):
                sum_a += val
                if(val>35):
                    break
            else:
                sum_a+= val
        if(number>35):
            print('Sum until 35 is {} of range 1 until {} '.format( sum_a, number))
        else:
            print('Sum is {} of range 1 until {} '.format(sum_a, number))
    else:
        print("Enter a integer")
# Task 5#########################################################################
# 5. function day_in_month



def main():
    print("#Task 1#########################################################################")
    range_a= range(0, 10)
    for val in range_a:
        is_pair(val)
    print("#Task 2#########################################################################")
    range_b = range(7,33)
    for val in range_b:
        if(is_prime(val)):
            print('The number {} is prime '.format(val))
        else:
            print('The number {} is not prime '.format(val))
    print("#Task 3#########################################################################")
    range_c = range(0, 63, 7)
    for val in range_c:
        area_of_cicle(val)
    print("#Task 4#########################################################################")
    range_d = range(30, 45, 5)
    for val in range_d:
        sum_to(val)

main()
