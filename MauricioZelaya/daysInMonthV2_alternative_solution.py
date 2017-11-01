import calendar

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for month in range(len(months)):
    daysInMonth = calendar.monthrange(2017, month+1)
    if daysInMonth == 0:
        print("Invalid month name in the input => '%s'" % months[month])
        continue
    print("%s have %s days" % (months[month], daysInMonth[1]))

