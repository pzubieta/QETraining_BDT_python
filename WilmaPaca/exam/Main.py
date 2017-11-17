from Sales_emp import SalesEmployee
from Sales_emp import FactoryEmployee
from Employee import Employee
from Person import Person

import logging

class MainFactory(SalesEmployee,FactoryEmployee,Employee,Person):
    global logger
    global index

    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    handler = logging.FileHandler('application.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    def __init__(self):
        self.emp = {}
        self. discSales = 0.125
        self.salary = {}
        self.dataSalary = {}
        self.index = 0

    def addEmployee(self,num):
            logger.info('Start adding employees....')
            while self.index < num:
                name = input("Enter the name: ")
                last = input ("Enter last name: ")
                depart = input ("Enter department:")
                if depart == 'SALES' or depart == 'Sales' or depart == 'sales':
                    piece = int(input("Enter piece number: "))
                    s_add = SalesEmployee(name,last,depart,piece)
                    self.emp[self.index] = s_add
                elif depart == 'FACTORY' or depart == 'factory' or depart == 'Factory':
                    piece = int(input("Enter effective piece number: "))
                    pieceDef = int(input("Enter defective piece number: "))
                    f_add = FactoryEmployee(name, last, depart, piece,pieceDef)
                    self.emp[self.index]= f_add
                self.index += 1
            self.calSalary(self.emp)

    def calculateSalaryF(self,effec,defect):
        a = int(effec)
        b = (a*10)-(defect*1.3)
        return b

    def calculateSalaryS(self, numP):
        return numP*2.5

    def discountF(self,salaryF):
        a = salaryF*self.discSales
        return a

    def calSalary(self,dictio):
        self.index = 0
        logger.debug('Start calculating salaries....')
        while self.index < len(dictio.items()):
            for key, value in dictio.items():
                v = value.getDepartment()
#                print (v,"++++++")
                if v == "sales":
                    salary_em = self.calculateSalaryS(value.getPieceNumber())
                    self.salary[salary_em] = self.discountF(salary_em)
                elif v == "fatory":
                    salary_em1 = self.calculateSalaryF(int(value.getEffectivePieceNumber()),value.getDefective())
                    self.salary[salary_em1] = self.discountF(salary_m1)
            self.index += 1
#        self.printSalaryDisc(self.salary)
        return self.salary

    def printSalaryDisc(self):
        i = 0
        for key, value in self.salary.items():
             netSalary = key - self.salary[key]
             self.dataSalary[i] =[key,self.salary[key],netSalary]
             i+=1
        return self.dataSalary
#        print("---",self.dataSalary)

    def printSalary(self):
        i = 0
        print("Name   ", "Department", "Global Salary ", " Total Discount", "Net Salary")
        print("-----------------------------------------------------------------------------")
        for key, value in self.emp.items():
            value_s = self.dataSalary[i]
#            print (self.dataSalary,"---+----")
            print (value.getData()," | ",value.getDepartment()," | ",value_s[0]," | ",value_s[1]," | ",value_s[2])
            i += 1



number_employee = int(input("Enter employee's number to add: "))
newFactory = MainFactory()
if number_employee > 0:
    newFactory.addEmployee(number_employee)
else:
    print ("Value incorrect !!")

newFactory.printSalaryDisc()
newFactory.printSalary()

