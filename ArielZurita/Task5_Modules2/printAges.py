from ArielZurita.Task5_Modules import calculateAge
def printAges(age):
    if age < 12: return "You are a child"
    elif age >= 13 and age <= 17: return "Your are teenager"
    elif age >= 18 and age <= 29: return "You are a young"
    elif age > 30: return "Your are adult"
    else: return "Invalid value entered"
