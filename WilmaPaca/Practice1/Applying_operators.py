# Defining the triangule type
import math
def isosceles(a,b,c):
    if a != 0 and b != 0 and c != 0:
        if a == b:
            text = print("a: %d = b: %d  and c: %d is not equal" %(a,b,c))
        elif a == c:
            text = print("a: %d = c: %d  and b: %d is not equal" % (a, c, b))
        elif b == c:
            text = print("b: %d = c: %d  and a: %d is not equal" % (b, c, a))
        elif a == b:
            text = print("a: %d = b: %d  and c: %d is not equal" %(a,b,c))
        else:
            text = ''
    else:
        text = ''
    return text

def perimeter_triangle(a,b,c):
    return (a + b + c) / 2

def area_triangle(a,b,c):
    s = perimeter_triangle(a,b,c)
    area_t = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area_t

def triangule_type(a,b,c):

    if a < b and b < c:
       print("if %d < %d < %d then is : " %(a,b,c),"Righ triangle")
    elif a == b and b == c and c == a:
        print("if %d = %d = %d then is : " % (a, b, c), "Equilateral triangle")
    elif isosceles(a,b,c) != '':
        print_t=isosceles(a,b,c)
        print(print_t,"Triangle isosceles")
    else:
        print("Undefined triangle")

    print("If you want to know the permiter -> option: 1\n If you want to know the area -> option: 2 \n Exit -> option: 0 ")
    option = int(input("option -> "))
    if option is 1:
        print("Perimeter : %d " % (perimeter_triangle(a,b,c)))
    elif option is 2:
        print("Area : %d " %(area_triangle(a,b,c)))
    else:
        print("Thanks a lot, :) ")

print("----------- Determining the triangule and perimeter or area ----------")
side_one =  int(input("Enter the first side: "))
side_two = int(input("Enter the second side: "))
side_three = int(input("Enter the third side: "))

triangule_type(side_one,side_two,side_three)



