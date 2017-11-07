#Write a function area_of_circle(r) which returns the area of a circle
# of radius r only if the radius value is greater of 10.
#A=pi*r*r
print("------------Area of Circle exercise ---------------")
def area_of_circle(r):

    pi= 3.1416
    if r!=0:
        area= pi *(r^2)
        print("the area of circle is:", area )
    else:print("please enter valid value")


var = int(input("the circle radius is: "))
area_of_circle(var)
print("-----------------------------------")


# Write a function sum_to(n) that returns the sum of all integer numbers
#  up to and including only until any value lower than 35.
# So sum_to(10)wouldbe1+2+3...+10which would return the value 55,
# but if n=40 only until sum to 35 need to be returned.
print("------------Function SUM---------------")
def sum_to(n):
    total = 0

    for i in range(1,n+1):
        total = total +i
        if i == 35:
           break
    print("The total is",total)

sum_to(10)
print("-----------------------------------")











