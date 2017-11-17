import logging
from Person import Person

class Employee(Person):
    def __init__ (self, first, last, depa, globalsalary, totaldiscount):
        self.firstname = first
        self.lastname = last
        self.depa = depa
        self.globalsalary = globalsalary
        self.totaldiscount = totaldiscount

    def getdepartament(self):
        return self.depa

    def getglobalsalary(self):
        return self.globalsalary

    def gettotaldiscount(self):
        return self.totaldiscount
