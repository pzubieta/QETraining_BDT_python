import logging
import logging.config


class Person:
    def __init__(self,nameP,departamentP):
        self.name = nameP
        self.departament = departamentP

        def nam(self):
            return self.name

        def depart(self):
            return self.departament

class Employee(Person):
    def __init__(self,nameP,departamentP,globalSalaryP,totalDiscountP,netSalaryP):
        Person.__init__(self,nameP,departamentP)
        self.globalSalary = globalSalaryP
        self.totalDiscount = totalDiscountP
        self.netSalary = netSalaryP

    def GetEmployee(self):
        return self.nam()+" "+self.depart()+" "+self.globalSalary+" "+self.totalDiscount+" "+self.netSalary
