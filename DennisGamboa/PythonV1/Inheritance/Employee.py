from Inheritance.Person import *
class Employee(Person):

    def __init__(self, first, last, age, ci, employe_id, department):
        Person.__init__(self, first, last, age, ci)
        self.employee_id = employe_id
        self.department = department
    def GetEmployee(self):
        return self.Name() + ", " + self.employee_id + ", " + self.department