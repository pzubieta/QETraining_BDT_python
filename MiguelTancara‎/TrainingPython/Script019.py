userInput = input("Type a number: ")

try:
    userInputASNumber = float(userInput)
except ValueError:
    print("You did not enter a number")
else:
    print("", userInputASNumber**2)
finally:
    print("Thank you")
