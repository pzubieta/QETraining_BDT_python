from Examen.Employee import Employee
from Examen.lib.log import Log

logger = Log()
listEmployee = []

limit = int(input("Limite users: "))
cont = 0
while cont <= limit:
    name = input("ingrese name: ")
    depa = input("ingrese departament: ")

    if depa == "Sales":
        posi = int(input("cantidad piesas efectivas: "))
        listEmployee.append(Employee(name, depa, posi))
    elif depa == "Factory":
        posi = int(input("cantidad piesas efectivas: "))
        nega = int(input("cantidad piesas defectuosas: "))
        listEmployee.append(Employee(name, depa, posi, nega))
    x = listEmployee[cont]
    logger.log_info(x)
    cont = cont+1

for i in range(len(listEmployee)):
    x = listEmployee[i]
    logger.log_info(x)
    if x.getDepartament() == "Sales":
        print(x.toStringSales())
    else:
        print(x.toStringFactory())