#import Person
from Person import Person


class Employee(Person):

    def __init__(self, name,last_name,age,ci,employee_id,department ):
        Person.__init__(self, name,last_name,age,ci)   #----super().__init__(self, name,last_name,age,ci)
        self.employee_id=employee_id
        self.department= department

    def getEmployee(self):
        return "Employee is ", self.employee_id,": ",  self.Name() + ", Department: " + self.department