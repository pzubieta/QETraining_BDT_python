from Person import *
from calculateSalary.discount import *
from calculateSalary.globalSalary import *



class Employee(Person):
    def __init__(self, name, last, department):
        Person.__init__(self, name, last)
        self.Name = self.Name()
        self.department = department
        self.global_salary = 0
        self.total_discount = 0
        self.net_salary = 0
        self.pieces_sold = 0
        self.efective_pieces = 0
        self.defective_pieces = 0

    def calcSalary (self):
        if self.department == 'Factory':
            self.global_salary = totalSalaryForFactory (self.efective_pieces, self.defective_pieces)
            totalSalaryForSales(self.pieces_sold)
        elif self.department == 'Sales':
            self.global_salary = totalSalaryForSales(self.pieces_sold)
            print (totalSalaryForSales(self.pieces_sold))

    def calcTotalDiscount (self):
        self.total_discount = discount(self.global_salary)
        print (discount(self.global_salary))

    def calcNetSalary (self):
        self.net_salary = self.global_salary-self.total_discount

    def setPiecesSold (self, num):
        self.pieces_sold = num

    def setEfectivePieces (self, num):
        self.efective_pieces = num

    def setDefectivePieces (self, num):
        self.defective_pieces = num

    def getObject (self):
        tuple = (self.Name, self.department, self.global_salary, self.total_discount, self.net_salary)
        return (tuple)






