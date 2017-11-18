from printAgeRelatedMessage import saySomethingAboutAge
import ageInDaysHoursAndMinutes

number = int (input ("Enter the  number of users: "))
people = []
for i in range (number):
    name = input ("Enter the name of the user number ")
    age = int(input("Enter the age of the user nubmer "))
    people.append({'name': name, 'age': age})


for i in range (number):
    print (people[i])


for p in people :
    print ("The age of ", p['name'], "is ", p['age'])
    print (p['name'], saySomethingAboutAge(p['age']))





