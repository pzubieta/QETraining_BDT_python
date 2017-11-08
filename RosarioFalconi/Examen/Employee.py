from Examen.Person import Person
from Examen.Module import *


class Employee(Person):

    def __init__(self, first, last, pieces, defect, type):
        Person.__init__(self, first,last)
        self.pieces=pieces
        self.defect=defect
        self.type=type

    def getEmployee(self):
        return 'Name: '+self.last+' '+self.first+', Type '+self.type

    def getFullName(self):
        return + self.Name()

    def getType(self):
        return self.type

    def getPieces(self):
        return self.pieces

    def getDefectives(self):
        return self.defect

    def getGlobal(self):
        if self.type is "S":
            return getSalesSalary(self.pieces)
        else:
            return getFactorySalary(self.defect, self.pieces)

    def getDiscount(self):
        gSalary = self.getGlobal()
        discount = getDiscount(gSalary)
        return discount
