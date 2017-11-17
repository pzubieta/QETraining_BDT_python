
class Employee(Person):
    def __init__(self, name, lname, age, ci, empId, depto):
        Person.__init__(self, name, lname, age, ci)
        self.employeeID = empId
        self.department = depto

    def getDepto(self):
        return self.department
