def minutes_age(age_m):
    return age_m*12*365*24*60
def hour_age(age_h):
    return age_h*12*365*24
def day_age(age_d):
    return age_d*12*365


def calculate_age(age):
    if age > 0:
        value= [day_age(age),hour_age(age),minutes_age(age)]
    else:
        value = None
    return value



