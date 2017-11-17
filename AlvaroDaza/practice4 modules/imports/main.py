from package1 import calculate_age
from package2 import print_message

user_amount = int(input("insert the amount of users \n"))
users = {}
for i in range(user_amount):
    name = input("insert name \n")
    age = int(input("insert age \n"))
    users[name] = age

for key, value in users.items():
    print("========= name =====: {}".format(key))
    print(calculate_age.calculate_age_days(value), " DAYS")
    print(calculate_age.calculate_age_hours(value), " HOURS")
    print(calculate_age.calculate_age_minutes(value), "MINUTES")
    print_message.print_age_message(value)
