
def days_in_month(month_day):
    month = ['January','March','May','July','August','October','December']
    month_2 = ['April', 'June', 'September', 'November']
    day =0
    print (month_day)
    if month_day == "February":
        day = 28
    elif month_day in month:
        day = 31
    elif month_day in month_2:
        day = 30
    else:
        day = None
    return day

month_days = input("Enter the month e.g. February: ")
day_printt = days_in_month(month_days)
#print (day_print)
if day_printt == None:
    print("This month does not exist ->", day_printt, " day")
else:
    print(month_days, "has", day_printt, "days")
