from Person import Person
class Employee(Person):
    def __init__(self, first,last,department):
        Person.__init__(self,first,last)
        self.department_emp =department

    def get_Employee(self):
        return self.get_dataPerson()+","+self.department_emp

    def getDepartment(self):
        return self.department_emp

    def setDepartment(self, dep):
        self.department_emp = dep


