from RosarioFalconi.Person import Person
class Employee(Person):
    def __init__(self, first, last, staffnum, department):
        Person.__init__(self,first,last)
        self.staffNumber=staffnum
        self.department=department

    def getEmployee(self):
        return 'Employee: '+self.Name()+", has ID "+self.staffNumber

    def getDepartment(self):
        return "Employee's department: "+self.department


##################
x=Person("Marge","Simpson")
y=Employee("Homero","Simpson","107", "Sales")
print (x.Name())
print (y.getEmployee())
print (y.getDepartment())