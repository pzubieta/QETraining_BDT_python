def area_of_cicle(r):
    if r>10:
        area = 3.1416 * (r * r)
        print("The area of circle is:",area)
        print("----------------------------")
    else:
        print("Wrong value")
        print("----------------------------")
area_of_cicle(5)


#Write a function sum_to(n) that returns the sum of all integer numbers up to and including only until any value
#lower than 35. So sum_to(10)wouldbe1+2+3...+10which would return the value 55,
# but if n=40 only until sum to 35 need to be returned.
def sum_to(n):
    total = 0
    if n<=35:
        for i in range(1,n+1):
            total = total +i
        print(total)
        print("----------------------------")
    else:

        print("35")
sum_to(10)
