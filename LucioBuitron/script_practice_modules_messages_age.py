#age=int(input("Please, enter the age in years:"))

#CREATE THE METHOD TO DISPLAY MESSAGES
def category_age(age_to_calculate):
    #DETERMINE THE RANGE TO ASSIGN A MESSAGE
    if age_to_calculate <= 12:
        print("-It is a child-")
    elif age_to_calculate >=13 and age_to_calculate<=17:
        print("-It is a teenager-")
    elif age_to_calculate >=18 and age_to_calculate<=29:
        print("-It is a young-")
    elif age_to_calculate >=30:
        print("-It is an adult-")

