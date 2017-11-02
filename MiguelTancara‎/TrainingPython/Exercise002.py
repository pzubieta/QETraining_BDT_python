# Create 1 script to determine is a number is odd or even (use single line statement if applies)

def isOddOrEvenNumber(value):
    if value%2 == 0: print("The provided number is even")
    else: print("The provide number is odd")


isOddOrEvenNumber(3)
isOddOrEvenNumber(10)
isOddOrEvenNumber(5000)

# According a list of values between a Min and Max range, identify if the number is prime or not.

def listOfNumbersPrime(minorValue, majorValue):
    for num in range(minorValue, majorValue):
        for i in range(2,num):
            if num%i == 0:
                break
            else:
                print(num, 'is a prime number')
                break

listOfNumbersPrime(1, 10)
listOfNumbersPrime(10, 20)
#listOfNumbersPrime(1, 100)