def area_of_circle (radius):
    #calculates the circle area for given radius in a list when radius are greater than 10
    res = 0

    for r in radius:
        if r > 10 : print ("Area = ", 3.14159265 * (r ** 2))


def sum_to (n):
    count = 0
    sum = 0

    if n > 35 : n = 35

    while count <= n:
        sum = sum + n
        count = count + 1

    print("Sum to ", n," is: ", sum)

area_of_circle([15,3,7,12,17])
sum_to (44)