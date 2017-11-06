def calculateAge(age):
    ageInDays = age*365
    ageInHours = ageInDays*24
    ageInMinutes = ageInHours*60
    ages = [age, ageInDays, ageInHours, ageInMinutes]
    return ages

calculateAge(1)