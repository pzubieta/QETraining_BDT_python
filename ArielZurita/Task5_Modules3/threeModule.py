from ArielZurita.Task5_Modules.calculateAge import calculateAge
from ArielZurita.Task5_Modules2.printAges import printAges

def insertUsers():
    numberUsers = int(input("Enter the number of users \n"))
    users = {}
    for i in range(numberUsers):
        username = str(input("Enter the username \n"))
        age = int(input("Enter the age \n"))
        users[username] = age

    for username, age in users.items():
        message = printAges(age)
        ages = calculateAge(age)
        print("%s You have %d years, %d days, %d hours. %d minutes" %(username, ages[0], ages[1], ages[2], ages[3]))
        print("Dear %s" %username, message)
insertUsers()