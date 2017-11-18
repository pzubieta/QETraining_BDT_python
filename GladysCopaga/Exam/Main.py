from Person import *
from Employee import *
import Calculate_globalSalaryS
import Calculate_globalSalaryF
import Calculate_discount
import Calculate_netSalary

class Main:
    def __init__(self):
        self.employees = []
        self.employee = Employee.getEmployee()

    #def addEmployeeSales(self, employee, piecesV):
    #    employeeSales = [piecesV]
    #    self.employee.append(employeeSales)

    #def addEmployeeFactory(self, employee, piecesP, piecesD):
    #    employeeFactory = [piecesP, piecesD]
    #    self.employee.append(employeeFactory)

    #def enterEmp(self):
    option = int(input("Please, enter the number of emp: "))
    list = []
    if (3<= option<=15):
        var = []
        dep = int(input("Do you want to register in the department Sales: press 1 = Yes, press 2 = No:"))
        for i in range(option):
            if dep == 1:
                name = input("Please enter a name: ")
                lastname = input("Please enter a lastname: ")
                departament = input("Please enter a department: ")
                piecesV = int(input("Please enter the number of pieces sold: "))
                var = [name+ " " +lastname +"- "+departament,piecesV]
                list.append(var)
                print(list)
            #inbox[index][0] == False:
            #return list
            for index in range(len(list)):
                print(name,lastname)
                totalS = Calculate_globalSalaryS.calculateGlobalSales(list[index][1])
                #disc = Calculate_discount.calculateDiscount(3)
                #disc = Calculate_discount.calculateDiscount(totalS)
                #netSal = Calculate_netSalary(sal,disc)

            else:
                name = input("Please enter a name: ")
                lastname = input("Please enter a lastname: ")
                departament = input("Please enter a department: ")
                piecesP = int(input("Please enter the number of pieces produced: "))
                piecesD = int(input("Please enter the number of pieces defecttive: "))
                var = [name + "-" +lastname + departament,piecesP,piecesD]
                list.append(var)
                print(list)
            #else:
             #   print("enter only the two options mentioned")

    else:
        print("Enter a valid number between 3 - 15")

   # enterEmp()
        #print(list)

employee1 = Employee("T","a","b")
#employee1.enterEmp("Test","12","123","1")
