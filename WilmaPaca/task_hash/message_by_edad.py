
def message_by_age(age):
    if age > 0 and age <= 12:
        value = "You are a child"
    elif age > 12 and age < 18:
        value = "You are  teenager"
    elif age >= 18 and age <= 29 :
        value = "You are  young"
    elif age >= 30:
        value = "You are adult"
    else:
        value = None
    return value
