def ageMessage(ageInYears):
    if (type(ageInYears) is str):
        message = "I don't know what you are"
        return message
    else:
        if (ageInYears < 12):
            message = "You are a child"
            return message
        elif (ageInYears > 13 and ageInYears < 17):
            message = "You are a teenager"
            return message
        elif (ageInYears > 18 and ageInYears < 29):
            message = "You are a young"
            return message
        elif (ageInYears > 30):
            message = "You are adult"
            return message

