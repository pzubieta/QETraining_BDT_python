import logging
class Person:
    def __init__(self, name, lastName):
        self.name = name
        self.lastName = lastName


class SalesEmployee(Person):

    def __init__(self, firstName, lastName, piecesSold):
        Person.__init__(self, firstName, lastName)
        self.piecesSold = piecesSold
        self.totalSalary = self.calculateTotalSalary()
        self.discount = self.calculateDiscount()
        self.netSalary = self.calculateNetSalary()

    def calculateTotalSalary(self):
        value = self.totalSalary = self.piecesSold * 2.5
        return value

    def calculateDiscount(self):
        value = self.discount = (self.totalSalary * 12.5) / 100
        return value

    def calculateNetSalary(self):
        value = self.netSalary = self.totalSalary - self.discount
        return value



class FactoryEmployee(Person):
    def __init__(self, firstName, lastName, producedPieces, defectivePieces):
        Person.__init__(self, firstName, lastName)
        self.producedPieces = producedPieces
        self.defectivePieces = defectivePieces
        self.effectivePieces = producedPieces - defectivePieces
        self.totalSalary = self.calculateTotalSalary()
        self.discount = self.calculateDiscount()
        self.netSalary = self.calculateNetSalary()

    def calculateTotalSalary(self):
        value = self.totalSalary = (self.effectivePieces * 10) - (self.defectivePieces * 1.3)
        return value

    def calculateDiscount(self):
        value = self.discount = (self.totalSalary * 12.5) / 100
        return value

    def calculateNetSalary(self):
        value =self.netSalary = self.totalSalary - self.discount
        return value


class Test:
    logging.basicConfig(filename="application.log", level=logging.INFO)
    logging.info("Program started")
    def __init__(self):
        logging.info("Initializing varaibles")
        self.employeeList = []
        self.deptoEmployee = {}
        self.totalSalary = {}
        self.discount = {}
        self.netSalary = {}

    def registerEmployees(self):
        logging.info("getting hte number of users")
        numberEmployees = int(input("How many employees do you wan to enter: "))
        if numberEmployees > 2 and numberEmployees < 16:
            for num in range(0, numberEmployees):
                logging.info("getting the type of user sales or factory")
                typeOfEmployee = str(input("The employee to be registered is sales or factory? : "))
                nameEmployee = str(input("Please enter the name of the employee: "))
                logging.info("getting the name of the employee")
                lastNameEmployee = str(input("Please enter the lastname of the employee: "))
                logging.info("getting the lastname of the employee")
                employee = nameEmployee+" "+lastNameEmployee
                if typeOfEmployee == "sales":
                    logging.info("getting the number of pieces for the sales employee")
                    piecesSold = int(input("Please enter the number of pieces sold: "))
                    salesemp = SalesEmployee(nameEmployee, lastNameEmployee, piecesSold)
                    logging.info("Adding the employee to the list")
                    self.employeeList.append(employee)
                    logging.info("calculating total salary")
                    self.deptoEmployee[employee] = "Sales"
                    self.totalSalary[employee] = salesemp.totalSalary
                    logging.info("calculating discount")
                    self.discount[employee] = salesemp.discount
                    logging.info("calculating net salary")
                    self.netSalary[employee] = salesemp.netSalary
                elif typeOfEmployee == "factory":
                    logging.info("getting the number of produced pieces for the factory employee")
                    piecesProduced = int(input("Please enter the number of pieces produced: "))
                    logging.info("getting the number of defective pieces for the factory employee")
                    piecesDefective = int(input("Please enter the number of pieces defective: "))
                    empFactory = FactoryEmployee(nameEmployee, lastNameEmployee, piecesProduced, piecesDefective)
                    logging.info("Adding the employee to the list")
                    self.employeeList.append(employee)
                    self.deptoEmployee[employee] = "Factory"
                    logging.info("calculating total salary")
                    self.totalSalary[employee] = empFactory.totalSalary
                    logging.info("calculating discount salary")
                    self.discount[employee] = empFactory.discount
                    logging.info("calculating net salary")
                    self.netSalary[employee] = empFactory.netSalary
                else:
                    print("The employee that you are trying to register should be 'sales' or 'factory'")
        else:
            print("The number of employees to be registered should be between 3 and 15")

    def printEmployees(self):
        print("Name  |  Depto   |   Total   |   Discount    |   Net Salary")
        print("")
        for i in range(len(self.employeeList)):
            print(self.employeeList[i]+" | "+self.deptoEmployee[self.employeeList[i]]+" | "+str(self.totalSalary[self.employeeList[i]])+" | "+str(self.discount[self.employeeList[i]])+" | "+str(self.netSalary[self.employeeList[i]]))
            #print(self.employeeList[i]+" | "+self.deptoEmployee[self.employeeList[i]]+" | "+str(self.totalSalary[self.employeeList[i]]))






myTest = Test()
myTest.registerEmployees()
myTest.printEmployees()
