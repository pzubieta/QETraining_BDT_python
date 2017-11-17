def area_of_circle():
    radius = (input("Enter the radius of your circle: "))
    if (type(radius) !=  type(20) or type(radius) !=  type(20.3)):
        pi = 3.1416
        if (radius > 10):
            area = pi*radius**2
            print ("the area of your circle is: ", area)
        else:
            print ("The are given is less than 10")
    else:
        print ("Please, enter an integer or float number value ")
area_of_circle()

