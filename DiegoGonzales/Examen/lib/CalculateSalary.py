class CalculateSalary:
    def __init__(self):
        self.totalSaleEmp = 0
        self.totalFactEmp = 0
        self.discount     = 12.5
        self.nextSalary   = 0

    def cal_SalarySalesEmployee(self, cantidadVendidos):
        self.totalSaleEmp = cantidadVendidos * 2.5
        return self.totalSaleEmp

    def cal_SalaryFactEmployee(self, cantidadProducidos, cantidadDefectuoso):
        self.totalFactEmp = (cantidadProducidos * 10) - (cantidadDefectuoso * 1.3)
        return self.totalFactEmp

    def setDiscountSalary(self, salarioEmployee):
        self.discount = 100 + (salarioEmployee - 1000) * 12.5

    def getDiscountSalary(self):
        return self.discount

    def getNextSalary(self, totalSalary):
        self.nextSalary = totalSalary - self.discount

    def getDatox(self):
        print(self.discount)