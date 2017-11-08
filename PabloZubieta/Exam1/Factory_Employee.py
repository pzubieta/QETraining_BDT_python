import logging
from Employee import Employee

class Factory_Employee(Employee):
    def __init__ (self, first, last, depa, globalsalary, totaldiscount, effpieces, defpieces):
        self.firstname = first
        self.lastname = last
        self.depa = depa
        self.globalsalary = globalsalary
        self.totaldiscount = totaldiscount
        self.effpieces = effpieces
        self.defpieces = defpieces

    def geteffpieces(self):
            return self.effpieces

    def getdefpieces(self):
            return self.defpieces