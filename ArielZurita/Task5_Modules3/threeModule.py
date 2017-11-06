from Task5_Modules import *
from Task5_Modules2 import *

def askAmountUsers():
    numberUsers = int(input("Enter the number of users"))
    return  numberUsers

def saveUsersAndAges(numberUsers):
    user = {}
    for i in range(numberUsers):
        username = str(input("Enter username\n"))
        age = int(input("Enter the user age\n"))
        user[username] = age
    print(user)

saveUsersAndAges(2)