from QuizArielZurita.Person.Person import *

class Employee(Person):
    def __init__(self, firstName, lastName, department):
        Person.__init__(self, firstName, lastName)
        self.department = department

    def getNameAndDepartment(self):
        name = self.getName()
        departmentAndName = name, self.department
        return departmentAndName





