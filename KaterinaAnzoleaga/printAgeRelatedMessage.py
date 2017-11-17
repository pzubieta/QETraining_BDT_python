# Module that prints a message related to your age range

def saySomethingAboutAge (age):
    if age in range (0, 12):
        return "You are a child"
    elif age in range (13, 17):
        return "You are a teenager"
    elif age in range (18, 29):
        return "You are yung"
    elif age > 30:
        return "You are an adult"


print (saySomethingAboutAge(12))
