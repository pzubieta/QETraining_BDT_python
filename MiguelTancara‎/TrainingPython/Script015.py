import calculateAge
import whatYouAre

############################
numberOfUsers = int(input("How many users? "))
users = {}

for num in range(0, numberOfUsers):
    name = input("enter the name of the user: ")
    age = int(input("enter the age of the user: "))
    users[name] = age

print(users)
for key,value in users.items():
    myAgeInMinutes = calculateAge.calculateAgeInMinutes(value)
    myAgeInHours = calculateAge.calculateAgeInHours(value)
    myAgeInDays = calculateAge.calculateAgeIndays(value)
    print("The age of: ", key, "in minutes is: ", myAgeInMinutes)
    print("The age of: ", key, "in hours is: ", myAgeInHours)
    print("The age of: ", key, "in days is: ", myAgeInDays)

    message = whatYouAre.ageMessage(value)
    print(key, message)
    print("")





############################

############################
#myAge = Script013.calculateAgeInMinutes(10)
#print ("My age in minutes is:", myAge)

#myAge = Script013.calculateAgeInHours(10)
#print ("My age in hours is:", myAge)

#myAge = Script013.calculateAgeIndays(10)
#print ("My age in days is:", myAge)


#############################
#message = Script014.ageMessage(10)
#print(message)

#message = Script014.ageMessage(15)
#print(message)

#message = Script014.ageMessage(20)
#print(message)

#message = Script014.ageMessage(40)
#print(message)

#message = Script014.ageMessage("cuarenta")
#print(message)