# Calculate ages in minutes module

def minsAge(timeAge):    # write Fibonacci series up to n
    timeAgeDays = timeAge * 365
    timeAgeHours = timeAge * 24
    timeAgeminutes = timeAge * 60

    return timeAgeDays*timeAgeHours*timeAgeminutes

print (minsAge(0.1))