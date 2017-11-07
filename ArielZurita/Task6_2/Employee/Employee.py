from Task6_2.Person.Person import Person

class Employee(Person):
    def __init__(self, employeeId, department):
        self.employeeId = employeeId
        self.department = department