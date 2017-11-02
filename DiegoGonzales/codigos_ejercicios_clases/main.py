from module_calcular import calulate_ege_days, calculate_ege_hours, calculate_ege_minutes
from module_print import show_ege

totalUsers = int(input("Ingrese total users: "))
listUser = {}
for i in range(totalUsers):
    name = input("Ingrese name: ")
    ege  = int(input("Ingrese ege: "))
    listUser[name] = ege

edad = 0
for x,j in listUser.items():
    edad = calulate_ege_days(listUser.get(x))
    show_ege(edad)