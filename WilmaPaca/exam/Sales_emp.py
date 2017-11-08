from Employee import Employee
from Person import Person

class SalesEmployee(Employee):

    def __init__(self,name, last,department,n_piece ):
        Employee.__init__(self,name,last, department)
        self.n_pieces = n_piece

    def getPieceNumber(self):
        return self.n_pieces

    def getNameEmpS(self, value):
        return Person.getData
    def getDepartS(self):
        return Employee.getDepartment


class FactoryEmployee(Employee):
    def __init__(self, name, last, department, effectivePiece, defect):
        Employee.__init__(self, name, last, department)
        self.effectivePieceF = effectivePiece
        self.defective = defect

    def getEffectivePieceNumber(self):
        return self.effectivePieceF

    def getNameEmpF(self):
        return Person.getData()

    def getDepartF(self):
        return Employee.getDepartment()

    def getDefective(self):
        return self.defective
