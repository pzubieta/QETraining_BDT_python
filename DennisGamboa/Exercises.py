# -----------------------------------------------------------------------------------------------
# Create 1 script to determine is a number is odd or even (use single line statement if applies)
# -----------------------------------------------------------------------------------------------
num = [10, 3, 1, 8, 4, 15, 0]
for val in num:
    if val == 1:
        print("is odd:", val)
    elif val == 0:
        print("is even:", val)
    elif val % 2 == 0:
        print("is even:", val)
    else:
        print("is odd:", val)

# -----------------------------------------------------------------------------------------------
# According a list of values between a Min and Max range, identify if the number is prime or not.
# -----------------------------------------------------------------------------------------------
def Prime_Numbers(lower, upper):
    for numbers in range(lower, upper + 1):
        #print("value num", num)
        if numbers > 1:
            for i in range(2, numbers):
                #print("value i", i)
                if numbers % i == 0:
                    #print("mod 0")
                    break
            else:
                print("prime number:", numbers)

Prime_Numbers(1, 10)

# ---------------------------------------------------------------------------------------------------------------------------
#Write a function area_of_circle(r) which returns the area of a circle of radius r only if the radius value is greater of 10.
# ---------------------------------------------------------------------------------------------------------------------------
def area_of_circle(r):
    a = 3.1416 * (r * r)
    if r >= 10:
        return a

print("radio", area_of_circle(10))

# -------------------------------------------------------------------------------------------------------------------------------
# Write a function sum_to(n) that returns the sum of all integer numbers up to and including only until any value lower than 35.
# So sum_to(10)wouldbe1+2+3...+10which would return the value 55, but if n=40 only until sum to 35 need to be returned.
# -------------------------------------------------------------------------------------------------------------------------------
def sum_to(n):
    sum = 0
    if n <= 35:
        for numb in range(n+1):
            sum += numb
        print("The sum for", n, "is:", sum)
    else:
        for numb in range(n+1):
            #print("number", numb)
            if numb <= 35:
                sum += numb
        print("The sum for", n, "is:", sum)

sum_to(40)

# -------------------------------------------------------------------------------------------------------------------------------
# Write a function days_in_month which takes the name of a month, and returns the number of days in the month. Ignore leap years:
# days_in_month("February") == 28 				    days_in_month("December") == 31
# If the function is given invalid arguments, it should return None.
# -------------------------------------------------------------------------------------------------------------------------------
def days_in_month(year, month):
    if year % 4 == 0 or (year % 100 == 0 and year % 400 == 0):
        if month in ['September', 'April', 'June', 'November']:
            print(month, "=", 30, "days")
        elif month in ['January', 'March', 'May', 'July', 'August', 'October', 'December']:
            print(month, "=", 31, "days")
        elif month == 'February':
            print(month, "=", 29, "days")
        print("The year is leap year")
    else:
        if month in ['September', 'April', 'June', 'November']:
            print(month, "=", 30, "days")
        elif month in ['January', 'March', 'May', 'July', 'August','October','December']:
            print(month, "=", 31, "days")
        elif month == 'February':
            print(month, "=", 28, "days")
        print("The year is not leap year")

days_in_month(2020, "February")