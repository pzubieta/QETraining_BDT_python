def isEven (n):
    if n%2: return (False)
    else: return (True)

number = int(input ("Enter an integer number (0 to finish): "))
while  number:
    if isEven(number): print ("The number ", number, "is even")
    else:  print ("The number ", number, "is odd")
    number = int(input("Enter an integer number (0 to finish): "))
else:
    print ("Good bye!")