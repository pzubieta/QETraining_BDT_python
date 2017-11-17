
def age_message (edad):
    msg=""
    if edad >= 1 and edad < 13:
        msg="You are a child"
    elif edad >=13 and edad < 18 :
        msg="You are teenager"
    elif edad >=18 and edad < 29 :
        msg = "You are young"
    elif edad >=30 :
        msg = "You are adult"
    else:
        msg = "You are a baby"
    print (msg)