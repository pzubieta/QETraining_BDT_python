import logging
from RosarioFalconi.Examen.Employee import Employee

list_employees=[]

def main_test():
    global list_employees

    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    handler = logging.FileHandler('application.log')

    nro_employees = input("Nr employees:")
    while not nro_employees.isnumeric():
        nro_employees = input("Nr employees:")
    nro_emp=int(nro_employees)
    i=0
    if nro_emp >= 3 and nro_emp <= 15:
        for i in range (nro_emp):
            i+=1
            print(i, "===================================")
            name=input("Employee's name:")
            last=input("Employee's lastname:")
            etype=input("Employee's type:")
            defect=0
            if(etype is "S"):
                pieces=int(input("Sold pieces:"))
                etype="Sales"
            else:
                etype="Factory"
                pieces=int(input("Effective pieces:"))
                defect=int(input("Defective pieces:"))
            emp = Employee(name, last, pieces, defect, etype)
            list_employees.append(emp)
        logger.info('Registered employees %s... ',len(list_employees))
    else:
        print("No valid number. Number employees must be between 3 and 15")
        main_test()

    i=0
    name = ""
    department = ""
    globalSalary = 0
    discount = 0
    netSalary = 0
    print ('Name | Department | Global Salary | Total Discount | Net Salary')

    for i in range (len(list_employees)):
        aux_emps = list_employees
        aux_emp=aux_emps.pop()
        name = aux_emp.Name()
        department = aux_emp.getType()
        globalSalary = aux_emp.getGlobal()
        discount = aux_emp.getDiscount()
        netSalary = globalSalary-discount
        print (name,' | ', department, ' | ', globalSalary,' | ', discount,' | ', netSalary)
        #handler.setFormatter(formatter)
        #logger.addHandler(handler)
    logger.info('Finish updating records')

main_test()