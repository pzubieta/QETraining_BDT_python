from Salary.Person import Person
from Salary.Employee import Employee
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# create a file handler
handler = logging.FileHandler('Test_Log.log')

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)
u = int(input("Input the user number : "))
logger.info('Updating records ...')


if u > 0 and u < 15:
    count = 0
    listSales = []
    listFactory = []
    listOther = []
    dic = {"Sales": listSales, "Factory": listFactory, "Other": listOther}
    dic2 = {}
    while (count < u):
        departament = input("What's your Department?: ")
        if departament == "Sales":
            name = input("What's your Name?: ")
            lastname = input("What's your Last Name?: ")
            piecesSold = int(input("Please enter the pieces sold?: "))
            person = Person(name, lastname)
            employee = Employee(name, lastname)
            globalSal = employee.salarySales(piecesSold)
            personName = person.getPersonName()
            discountSal = employee.Discount(globalSal)
            netSal = employee.netSalaryFactory(globalSal, discountSal)
            dic2[personName] = globalSal
            print("your Discount is:",discountSal)
            print("your Net sal is:", discountSal)
            dic["Sales"].append(employee)


        elif departament == "Factory":
            name = input("What's your Name?: ")
            lastname = input("What's your Last Name?: ")
            efectiveSold = int(input("Please enter the Efective pieces ?: "))
            defectiveSold = int(input("Please enter the Defective pieces ?: "))
            person = Person(name, lastname)
            employee = Employee(name, lastname)
            globalSal = employee.salaryFacoryPositive(efectiveSold,defectiveSold)
            personName = person.getPersonName()
            discountSal = employee.Discount(globalSal)
            netSal = employee.netSalaryFactory(globalSal,discountSal)
            dic2[personName] = globalSal
            print("your Discount is:",discountSal)
            print("your netSalary is:", discountSal)
            dic2[personName] = globalSal
            dic["Factory"].append(employee)

        else:
            print("Invalid Departament")
        count = count + 1

        print(dic2)


else:
    print("Please enter users no less than 3 and no more than 15")
    logger.info('Finish updating records')