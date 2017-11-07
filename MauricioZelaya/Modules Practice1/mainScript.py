from agesMessages import messageForAge
from agesConversor import *

numberOfUsers = int(input("please set a number of users: "))
usersDictionary = {}

for val in range(numberOfUsers):
    aName = raw_input("name: ")
    anAge = raw_input("age: ")
    usersDictionary[aName] = anAge
#print(usersDictionary)

# print(usersDictionary[1])
for dictKey in usersDictionary:
    print("Hi %s" % dictKey)
    print("your Age in Months: %s" % ageToMonths(int(usersDictionary[dictKey])))
    print("your Age in days: %s" % ageToDays(int(usersDictionary[dictKey])))
    print("your Age in Minutes: %s" % ageToMinutes(int(usersDictionary[dictKey])))
    print("your Age in seconds: %s" % ageToSeconds(int(usersDictionary[dictKey])))
    messageForAge(int(usersDictionary[dictKey]))


