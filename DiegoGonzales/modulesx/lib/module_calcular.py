
def calulate_ege_days(ege):
    days_ege = ege * 365
    return days_ege

def calculate_ege_hours(ege):
    aux = calulate_ege_days(ege)
    hours_ege = aux * 24
    return hours_ege

def calculate_ege_minutes(ege):
    aux = calculate_ege_hours(ege)
    minutes_ege = aux * 60
    return minutes_ege