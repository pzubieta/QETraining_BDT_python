def ComparisonOperators ():
    age = (input ("Please, enter the year of your birth from 1900s to 2000s: " ))
    if (type(age) != type(20)):
        print (age, " is not a valid number, please a valid year using 4 digits: ")
    elif (type(age) == type(20)):
        if (1900 <=age <  2000):
            age -=1900
            if (age < 15):
                print ("Your date of birth is less than 1915, then you belong to the Interbellum generation :)")
            elif (14 < age <= 24):
                print ("Your date of birth is greater than 1914 and less or equal than 1924, then you belong to the 'Grandiosa' generation :)")
            elif (24 < age <=45):
                print ("Your date of birth is greater than 1924 and less or equal than 1945, then you belong to the 'Sileciosa' generation :)")
            elif (45 < age <=64):
                print ("Your date of birth is greater than 1945 and less or equal than 1964, then you belong to the 'Baby Boomer' generation :)")
            elif (64 < age <=81):
                print ("Your date of birth is greater than 1964 and less or equal than 1981, then you belong to the 'X' generation :)")
            elif (81 < age <=94):
                print ("Your date of birth is greater than 1981 and less or equal than 1994, then you belong to the 'Y' generation :)")
            elif (94 < age <=99):
                print ("Your date of birth is greater than 1994 and less or equal than 1999, then you belong to the 'Z' generation :)")
        elif (age >= 2000):
            age -=2000
            if (age >=0 and age <= 17):
                print ("Your date of birth is greater or equal than 2000 and less or equal than 2017, then you belong to the 'Z' generation :)")
            else:
                print("You were not born yet")
        else:
            print("Please enter the year of your birth from 1900s to 2000s")
ComparisonOperators()