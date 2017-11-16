def status_person(age):
    if age <= 12:
        return "he/she is a child"
    elif 13 <= age <= 17:
        return "he/ she is teenager"
    elif 18 <= age <= 29:
        return "he/she is young"
    elif age >= 30:
        return "he/she is adult"

#status_person(40)