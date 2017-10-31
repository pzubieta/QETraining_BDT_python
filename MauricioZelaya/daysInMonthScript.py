def days_in_month(month):
    """returns the total days in a given month"""
    if(month == "January"):
        return 31
    elif(month == "February"):
        return 28
    elif (month == "March"):
        return 31
    elif (month == "April"):
        return 30
    elif (month == "May"):
        return 31
    elif (month == "June"):
        return 30
    elif (month == "July"):
        return 31
    elif (month == "August"):
        return 30
    elif (month == "September"):
        return 31
    elif (month == "October"):
        return 30
    elif (month == "November"):
        return 31
    elif (month == "December"):
        return 30
    else:
        return 0


months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December", "mauricio"]
for month in months:
    daysInMonth = days_in_month(month)
    if daysInMonth == 0:
        print("Invalid month name in the input => '%s'" % month)
        continue
    print("%s have %s days" % (month, daysInMonth))
