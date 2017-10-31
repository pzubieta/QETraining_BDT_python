#Write a function days_in_month which takes the name of a month, and returns the number of days in the month. Ignore leap years:
#		days_in_month("February") == 28 				    days_in_month("December") == 31
#If the function is given invalid arguments, it should return None

def days_in_month (month):
    monthsWith31Days= ["January", "March", "May", "July", "August", "October", "December"]
    monthsWith30Days = ["April", "June", "September", "November"]
    if month in monthsWith31Days:
        return 31
    elif month in monthsWith30Days:
        return 30
    elif month == "February":
        return 28
    else:
        return None


print(days_in_month("February"))
print(days_in_month("April"))
print(days_in_month("August"))