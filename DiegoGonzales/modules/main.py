from lib.module_calcular import calulate_ege_days, calculate_ege_hours, calculate_ege_minutes
from lib.module_print import show_ege

totalUsers = int(input("Ingrese total users: "))
listUser = {}
for i in range(totalUsers):
    name = input("Ingrese name: ")
    ege  = int(input("Ingrese ege: "))
    listUser[name] = ege

for x,j in listUser.items():
    ege = calulate_ege_days(listUser.get(x))
    hour = calculate_ege_hours(listUser.get(x))
    minute = calculate_ege_minutes(listUser.get(x))
    show_ege(listUser.get(x), x, ege, hour, minute)