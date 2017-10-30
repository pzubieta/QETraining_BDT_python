# odd or even
def oddOrEven (number):
    """determine if a given number is odd or even"""
    if number % 2 == 0: print("number %s is an EVEN number" % number)
    else: print("number %s is an ODD number" % number)


listOfNumbers = [1, 2, 50, 45, 56, 1234, 3253, 12354]
for val in listOfNumbers: oddOrEven(val)

