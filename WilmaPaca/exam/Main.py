from Sales_emp import SalesEmployee
from Sales_emp import FactoryEmployee
from exam import Employee
import logging

class MainFactory(SalesEmployee,FactoryEmployee):
    global logger
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    handler = logging.FileHandler('Test_Log.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    def __init__(self):
        self.emp = {}
        self.index = 0
        self. discSales = 0.125

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

    def calSalary(self):
        self.salary = {}
        for key, value in self.emp.items():
            if value.getDepartment() == "sales":
                value = int(value.getPieceNumber())
#                print (value)
                salary_em = value * 2.5
                disc = salary_em * self.discSales
                self.salary[salary_em] = disc
            elif value.getDepartment() == "fatory":
                salary_em1 = (int(value.getEffectivePieceNumber()) * 10) - (value.getDefective()*1.3)
                disc1 = salary_em1 * self. discSales
                self.salary[salary_em1] = disc1
            return self.salary

    def printSalaryDisc(self):
#        print (self.calSalary())
        i = self.index
        for key, value in self.calSalary().items():
#            print (key)
            netSalary = key - self.salary[key]
            print ("Global Salary "," Total Discount", "Net Salary")
            print (key,"          ", self.salary[key],"           ",netSalary)
            i +=1

    def printSalary(self):
        for key , value in self.emp.items():
            print(key)
            print(value.getPieceNumber())
            print (value.getDepartment()," - ",value.getDepartment()," ")


number_employee = int(input("Enter employee's number to add: "))
newFactory = MainFactory()
if number_employee > 0:
    newFactory.addEmployee(number_employee)
else:
    print ("Value incorrect !!")

newFactory.printSalaryDisc()
#newFactory.printSalary()

