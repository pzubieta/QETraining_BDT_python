def area_of_circle (radius):
    res = 0

    for r in radius:
        if r>10: print ("Area = ",3.14159265 * (r ** 2))

def sum_to (n):
    count = 0
    sum = 0
    while count < n:
        sum = sum + n
        count += count

    print("Sum to ", n," is: ", sum)

area_of_circle([15,3,7,12,17])
sum_to (44)