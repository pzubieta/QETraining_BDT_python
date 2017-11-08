import logging
from Employee import Employee

class Sales_Employee(Employee):

    def __init__(self, first, last, depa, globalsalary, piecessold, totaldiscount = 12.5):
        self.firstname = first
        self.lastname = last
        self.depa = depa
        self.globalsalary = globalsalary
        self.totaldiscount = totaldiscount
        self.piecessold = piecessold

    def getpiecessold(self):
            return self.piecessold

    def getdiscont(self):
            return self.totaldiscount
