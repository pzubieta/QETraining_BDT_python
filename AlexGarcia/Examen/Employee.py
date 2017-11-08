from Person import Person

class Employee(Person):
    def __init__(self, name, lastName, Department, piecesSold, piecesGood, piecesBad):
        super().__init__(name,lastName)
        self.Department = Department
        self.piecesSold = piecesSold
        self.piecesGood = piecesGood
        self.piecesBad = piecesBad

    def getEmployee(self):
        return self.name+" "+ self.lastName

    def SalaryGlobal_sale_Employee(self, piecesSold):
        return piecesSold * 2.5

    def SalaryGlobal_fatory_Employee(self,piecesGood, piecesBad):
        return (piecesGood * 10)-(piecesBad * 1.3)

    def descuento(self, SalaryGlobal):
        return (SalaryGlobal * 0.125)

    def Salario_Neto(self, SalaryGlobal, Descuento):
        return SalaryGlobal - Descuento





