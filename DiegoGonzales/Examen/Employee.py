from Examen.Person import Person
from Examen.lib.CalculateSalary import CalculateSalary

class Employee(Person):

    def __init__(self, name, departament, cantidadProducido=0, cantidadDefectuoso=0):
        # super().__init__(name)
        self.per = Person(name)
        self.cal = CalculateSalary()
        self.departament   = departament
        self.cantidadProducido = cantidadProducido
        self.cantidadDefectuoso = cantidadDefectuoso

    def getName(self):
        return self.per.getName()

    def getDepartament(self):
        return self.departament

    def getCantidadProd(self):
        return self.cantidadProducido

    def setCantidadProd(self, cantidad):
        self.cantidadProducido = cantidad

    def getCantidadDefect(self):
        return self.cantidadDefectuoso

    def setCantidadDefect(self, cantidad):
        self.cantidadDefectuoso = cantidad

    def getTotalSalarioSales(self):
        return self.cal.cal_SalarySalesEmployee(self.cantidadProducido)

    def getTotalSalaryFactory(self):
        total = self.cal.cal_SalaryFactEmployee(self.getCantidadProd(), self.getCantidadDefect())
        return total

    def getDiscount(self, salaryEmployee):
        self.cal.setDiscountSalary(salaryEmployee)
        total = self.cal.getDiscountSalary()
        return total

    def getNextSalary(self, salaryEmployee):
        total = salaryEmployee - self.getDiscount(salaryEmployee)
        return total

    def toStringSales(self):
        return self.per.getName(), self.getDepartament(), self.getTotalSalarioSales(), self.getDiscount(self.getTotalSalarioSales()), self.getNextSalary(self.getTotalSalarioSales())

    def toStringFactory(self):
        return self.per.getName(), self.getDepartament(), self.getTotalSalaryFactory(), self.getDiscount(self.getTotalSalaryFactory()), self.getNextSalary(self.getTotalSalaryFactory())
