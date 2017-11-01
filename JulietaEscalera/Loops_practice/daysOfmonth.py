import calendar
#Create a plain text calendar
def days_in_month(month):
    testlist = ["January","February","March","April","May","June","July","August","September", "October", "November", "December"]

    if month.isdigit() is False:
     for position, item in enumerate(testlist):
        if item == month:
            print (position)
            amountOfDays = calendar.monthrange(2017, position+1)#+1 because my list start in 0 (1,31)
            print("Days in the " + month + " month:", amountOfDays[1])
            break

    else:
        print (None)




days_in_month("5")
