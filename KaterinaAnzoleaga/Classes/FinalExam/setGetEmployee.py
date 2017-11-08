from Employee import *
from LoginModule import *

anEmplo = Employee ('Juan', 'Perez', 'Sales')
anEmplo.setPiecesSold(45)
anEmplo.calcSalary()
anEmplo.calcTotalDiscount()
anEmplo.calcNetSalary()
print (anEmplo.getObject())

number = int (input("Ingrese el numero de empleados: "))

list = []
for i in range (number):
    name = input ("Name: ")
    last = input("Lastname: ")
    deparment = input("Department: ")
    anEmplo = Employee name, last, deparment)
    if deparment == 'Factory':
        effective = int (input('Effective pieces: '))
        anEmplo.setEfectivePieces (effective)
        defective = int (input('Defective pieces: '))
        anEmplo.setDefectivePieces(defective)
    elif deparment == 'Sales':
        sold = int (input('Pieces sold: '))
        anEmplo.setPiecesSold (sold)
    anEmplo.calcSalary ()
    anEmplo.calcTotalDiscount()
    anEmplo.calcNetSalary ()
    list.append(anEmplo.getObject())

for i in list:
    print(i)