from Person import *
from CalculateSalary import *

class Employee(Person):
    def __init__(self, name, last, age, CI, employee_id, department):
        Person.__init__(self, name, last, age, CI)
        self.employee_id = employee_id
        self.department = department
    def getGlobalSalary (self):



    def getObject (self):
        tuple = (self.name, self.last, self.age, self.CI, self.employee_id, self.department)
        return (tuple)



