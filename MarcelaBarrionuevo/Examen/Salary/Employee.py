from Salary.Person import Person
import math

class Employee(Person):

    def __init__(self, name, lastName, globalSal =0, totalDiscount =0 , netSal =0):
        super().__init__(name, lastName)
        self.globalSal = globalSal
        self.totalDiscount = totalDiscount
        self.netSal = netSal

    def globalSal(self):
        return self.globalSal

    def getGlobalSal(self, i):
        globalSal = i
        return  globalSal



    def totalDiscount(self):
        return self.totalDiscount

    def netSal(self):
        return self.netSal

    def setglobalSal(self, totalsal):
        self.globalSal = totalsal

    def settotalDiscount(self, newtotalDiscount):
        self.totalDiscount = newtotalDiscount

    def setnetSal(self, newnetSal):
        self.netSal = newnetSal

    def salarySales(self, pieces):
        pieces2 = math.floor(pieces)
        salarySales = pieces2 * 2.5
        return salarySales

    def salaryFacoryPositive(self, piecesPostive,piecesNegative):
        piecesPostive2 = math.floor(piecesPostive)
        piecesNegative2 = math.floor(piecesNegative)
        salaryFacoryPositive = piecesPostive2 * 10
        salaryFacorynegative = piecesNegative2 * 1.3
        total = salaryFacoryPositive - salaryFacorynegative
        return total


    def Discount(self, salarySales3):
        discSales2 = math.floor(salarySales3)
        DiscountSales = (discSales2 * 12.5) / 100
        return DiscountSales

    def netSalaryFactory(self, salaryGlobal01, salarydiscount):
        netsal = salaryGlobal01 - salarydiscount
        return netsal
