import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
# create a file handler
handler = logging.FileHandler('application.log')
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(handler)

from QuizArielZurita.Person.Employee import *
from QuizArielZurita.performCalculations.calculateSalesSalary import salesSalary
from QuizArielZurita.performCalculations.calculateFactorySalary import calculateFactorySalary
from QuizArielZurita.performCalculations.discount import discount
from QuizArielZurita.performCalculations.netSalary import netSalary

class Principal:
    def __init__(self):
        self.salaries = []

    def askNumberEmployees(self):
        logger.info('Asking number employees')
        numberEmployees = int(input("Enter number employees \n"))
        salesEmployees = ()
        totalSales = []
        factoryEmployees = ()
        totalFactory = []
        employeeWithSalaries = ()
        toPrint = [("Name", "Department", "Global Salary", "Total Discount", "Net Salary")]

        logger.info('Asking if the value entered %d meets condition greter than 3 and lower than 15')
        if numberEmployees >= 3 and numberEmployees <= 15:
            for i in range(numberEmployees):
                logger.debug('creating employess')
                empFirstName = str(input("Employee first name: \n"))
                empLastName = str(input("Employee last name: \n"))
                employeeType = str(input("Employee Type: \n")).lower()
                if employeeType == "sales":
                    logger.debug('Create employee with type sales')
                    numberPiecesSold = int(input("Enter Number Pieces Sold: \n"))
                    e = Employee(empFirstName, empLastName, employeeType)
                    salesEmployees = (e.getNameAndDepartment(), numberPiecesSold)
                    totalSales.append(salesEmployees)
                    logger.debug('Sales employee created')
                elif employeeType == "factory":
                    logger.debug('Create employee with type factory')
                    numberPiecesEffective = int(input("Number of pieces effective: \n"))
                    numberPiecesDefective = int(input("Number of pieces defective: \n"))
                    e = Employee(empFirstName, empLastName, employeeType)
                    factoryEmployees = (e.getNameAndDepartment(), numberPiecesEffective, numberPiecesDefective)
                    totalFactory.append(factoryEmployees)
                    logger.debug('Factory employee created')

            for item in totalSales:
                logger.info('calculating salary')
                salary = salesSalary(item[1])
                logger.info('calculating discount')
                dis = discount(salary)
                logger.info('calculating net salary')
                fullSalary = netSalary(salary, dis)
                employeeWithSalaries = (item[0], salary, dis, fullSalary)
                logger.debug('adding employee with all its salaries')
                toPrint.append(employeeWithSalaries)

            for item in totalFactory:
                salary = calculateFactorySalary(item[1], item[2])
                dis = discount(salary)
                fullSalary = netSalary(salary, dis)
                employeeWithSalaries = (item[0], salary, dis, fullSalary)
                logger.debug('adding employee with all its salaries')
                toPrint.append(employeeWithSalaries)

            for item in toPrint:
                logger.debug('printing employees')
                print(item)

        else: print("Incorrect Value")

p = Principal
p.askNumberEmployees(p)



