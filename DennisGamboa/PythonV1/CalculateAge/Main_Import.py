from CalculateAge.Calculate_age import *
from CalculateAge.Print_Person import status_person

def main_test():
    users = int(input("insert amount of users:"))
    add_users = {}
    for p in range(users):
        print("What is your name user", str(p+1) + ": ", end="")
        us = input()
        print("What is tour age, ", us + ": ", end="")
        age = int(input())
        add_users[us] = age
    for names, age in add_users.items():
        if age > 0:
            print("------------------")
            print("Name:", names)
            print("Age:", age)
            print("Age in days", calculate_age_days(age), "days")
            print("Age in hrs", calculate_age_hrs(age), "hrs")
            print("Age in min", calculate_age_min(age), "min")
            print("and", status_person(age))
            print("------------------")

main_test()

