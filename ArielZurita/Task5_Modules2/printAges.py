from Task5_Modules import calculateAge
def printAges():
    age = int(input("Enter your age \n"))
    ages = calculateAge.calculateAge(age)
    if ages[0] < 12: print("You are a child")
    elif ages[0] in (13, 17): print("Your are teenager")
    elif ages[0] in (18, 29): print("Your are young")
    elif ages[0] > 30: print("Your are adult")
    else: print("Invalid value entered")


printAges()