from package1 import calculate_age
from package2 import print_message

user_amount = int(input("Insert the amount of users \n"))
users = {}
for i in range(user_amount):
    name = input("Insert the username: \n")
    age = int(input("Insert age: \n"))
    users[name] = age

for key, value in users.items():
    print("Information Detail  -- Username: {}".format(key))
    print("Age in DAYS: ", calculate_age.calculate_age_days(value))
    print("Age in HOURS: ", calculate_age.calculate_age_hours(value))
    print("Age in MINUTES:", calculate_age.calculate_age_minutes(value))
    print_message.print_age_message(value)
