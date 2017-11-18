def are_of_circle(r):
    pi = 3.14
    if r > 10:
        r2 = r ** 2
        area = r2 * pi
        print("Area is %d" % area)
    else:
        print("Invalid input the radio should be greater than 10")


are_of_circle(5)