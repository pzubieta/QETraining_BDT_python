from Employee import *
from LoginModule import *

anEmplo = Employee ('Juan', 'Perez', 'Sales')
anEmplo.setPiecesSold(45)
anEmplo.calcSalary()
anEmplo.calcTotalDiscount()
anEmplo.calcNetSalary()
print (anEmplo.getObject())

number = int (input("Ingrese el numero de empleados: "))

for i in range (number):
    name = input ("Name: ")
    last = input("Lastname: ")
    deparment = input("Department: ")
    anEmplo = Employee (name, last, deparment)
    if deparment == 'Factory':
        effective = input('Effective pieces: ')
        anEmplo.setEfectivePieces (effective)
        defective = input('Defective pieces: ')
        anEmplo.setdefective_pieces(defective)
    elif deparment == 'Sales':
        sold = input('Pieces sold: ')
        anEmplo.setPiecesSold (sold)
