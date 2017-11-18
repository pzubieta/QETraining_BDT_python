# Write a function area_of_circle(r) which returns the area of a circle of radius r only if the radius value is greater of 10

def area_of_circle(r):
    if r>=10:
        result = 3.1416 * r**2
        print("The area of circle is: {:.2f} ".format(result))
    else:
        print("The provided radio is minor than 10")

area_of_circle(3)
area_of_circle(10)
area_of_circle(20)



# Write a function sum_to(n) that returns the sum of all integer numbers up to and including only until any value lower than 35.
# So sum_to(10)wouldbe1+2+3...+10which would return the value 55, but if n=40 only until sum to 35 need to be returned

def sum_to(n):
    sum = 0
    for num in range(0, n+1):
        if num <= 35:
            sum = sum + num
        else:
            break
    print("The result of the sum is: ", sum)

sum_to(10)
sum_to(20)
sum_to(36)
sum_to(40)