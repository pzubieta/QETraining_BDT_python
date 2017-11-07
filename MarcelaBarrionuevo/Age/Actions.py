import Age.Messages as m
import Age.CalculateAge as a

u = int(input("Input the user number : "))



if u > 0:
    count = 0
    dic = {}
    while (count < u):

        name = input("What's your name?:  ")
        age = int(input("What's your age?:  "))
        count = count + 1
        dic[name]= age
    print(dic)

    for key in dic:
        age = int(dic[key])
        message = m.messages(age)
        days = a.age_days(age)
        hours = a.age_hours(age)
        mins = a.age_min(age)

        print("Age in years: %d" % dic[key])
        print ("Age in days: %d" % days)
        print ("Age in hours: %d" % hours)
        print("Age in minutes: %d" % mins)


else:
    print("There is no users in the list")