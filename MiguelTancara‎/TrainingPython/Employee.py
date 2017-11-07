import /Person/Person

class Employee(/Person/Person):
    def __init__(self, name, lname, age, ci, empId, depto):
        Person.__init__(self, name, lname, age, ci)
        self.employeeID = empId
        self.department = depto
SystemError
    def getDepto(self):
        return self.department
