from Employee import *
from LoginModule import *

def listEmployees (list):
    for i in list:
        print (i)


login_msg ('info', "Starting with a sample")
anEmplo = Employee ('Juan', 'Perez', 'Sales')
anEmplo.setPiecesSold(45)
anEmplo.calcSalary()
anEmplo.calcTotalDiscount()
anEmplo.calcNetSalary()
print (anEmplo.getObject())

login_msg ('info', "Starting asking the number of employees")
number = int (input("Ingrese el numero de empleados: "))
if number >= 3 and number <= 15:
    message = 'A valid number of employees was entered :'+str (number)
    login_msg('info', message)
    list = []
    for i in range (number):
        name = input ("Name: ")
        last = input("Lastname: ")
        deparment = input("Department: ")
        anEmplo = Employee (name, last, deparment)
        if deparment == 'Factory':
            message = 'Factory employee being entered. Getting efective and defective prices'
            login_msg('debug', message)
            effective = int (input('Effective pieces: '))
            anEmplo.setEfectivePieces (effective)
            defective = int (input('Defective pieces: '))
            anEmplo.setDefec3tivePieces(defective)
        elif deparment == 'Sales':
            message = 'Sales employee being entered. Getting number of pieces sold'
            login_msg('debug', message)
            sold = int (input('Pieces sold: '))
            anEmplo.setPiecesSold (sold)
        message = 'Calculating Global Salary, Discount and NetSalay based on the department of the employee'
        login_msg('debug', message)
        anEmplo.calcSalary ()
        anEmplo.calcTotalDiscount()
        anEmplo.calcNetSalary ()
        message = 'Entering the full record to the list of employees: '+str(anEmplo.getObject())
        login_msg('debug', message)
        list.append(anEmplo.getObject())
    listEmployees(list)

else:
    print ("Ingrese un valor entre 3 y 15")
    exit (1)
