# Write a function days_in_month which takes the name of a month,
#  and returns the number of days in the month.
#  Ignore leap years:
# 		days_in_month("February") == 28
#       days_in_month("December") == 31
# If the function is given invalid arguments,
# it should return None.


print("------------Months ---------------")

def days_in_month(name_month):
    months_31=['January','March','May','July','September','December']
    months_30=['February','April','June','Audgust','October','November']

    if name_month == 'February':
        print(name_month, "have 28 days")
    else:
        if name_month in  months_31:
            print( name_month,"have 31 days")
        elif name_month in months_30:
            print( name_month,"have 30 days")
        elif name_month not in months_31 and name_month not in months_31:
            print(name_month, ": NONE")

days_in_month('January')
days_in_month('February')
days_in_month('June')
