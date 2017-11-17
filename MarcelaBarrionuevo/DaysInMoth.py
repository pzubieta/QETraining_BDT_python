def days_of_month(month):
    if month == "January":
        print("Days in %s are: 31 " % month)
    elif month == "February":
        print("Days in %s are: 28 " % month)
    elif month == "March":
        print("Days in %s are: 31 " % month)
    elif month == "April":
        print("Days in %s are: 30 " % month)
    elif month == "May":
        print("Days in %s are: 31 " % month)
    elif month == "June":
        print("Days in %s are: 30" % month)
    elif month == "July":
        print("Days in %s are: 31 " % month)
    elif month == "August":
        print("Days in %s are: 31 " % month)
    elif month == "September":
        print("Days in %s are: 31 " % month)
    elif month == "October":
        print("Days in %s are: 31 " % month)
    elif month == "November":
        print("Days in %s are: 30 " % month)
    elif month == "December":
        print("Days in %s are: 31 " % month)
    else:
        print("Invalid Month")


days_of_month("January")


# Second solution

def days_of_month_two(month):
    if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "September" or month == "October" or month == "December":
        print("Days in %s are: 31 " % month)
    elif month == "April" or month == "June" or month == "November":
        print("Days in %s are: 30 " % month)
    elif month == "February":
        print("Days in %s are: 28 " % month)
    else:
        print("Invalid Month")


days_of_month_two("February")

# third solution

def days_of_month_three(month):
    dayswiththirtyone = ['January','March', 'May', 'July', 'August', 'September', 'October', 'December']
    dayswiththirty = ['April', 'June', 'November']
    dayfebruary = "February"

    foundmonth = False
    for val in dayswiththirtyone:
        if val == month:
            print("Days in %s are: 31 " % month)
            foundmonth = True

    if foundmonth == False:
        for valtwo in dayswiththirty:
            if valtwo == month:
                print("Days in %s are: 30 " % month)
                foundmonth = True

    if dayfebruary == month:
        print("Days in %s are: 28 " % month)
        foundmonth == True

    if foundmonth == False:
        print("Invalid Month")

days_of_month_three("June")