def calcule_age_hours(age):
    return age*365*24

def calcule_age_days(age):
    return age*365

def calcule_age_minutes(age):
    return age*365*24*60

def test_calcule_age():
    print(calcule_age_hours(12))
    print(calcule_age_days(12))
    print(calcule_age_minutes(12))

