#age=int(input("Please, enter the age in years:"))

#CREATE THE METHOD TO CALCULATE THE AGE
def cal_age(age_to_calculate):
    #CALCULATE THE AGE IN MINUTES
    age_in_minutes = age_to_calculate*525960

    # CALCULATE THE AGE IN HOURS
    age_in_hours = age_to_calculate*8766

    # CALCULATE THE AGE IN DAYS
    age_in_days = age_to_calculate*365

    #PRINT THE RESULTS
    print("The age in minutes is: ", age_in_minutes)
    print("The age in hours is: ", age_in_hours)
    print("The age in days is: ", age_in_days)
