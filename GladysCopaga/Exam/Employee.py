from Person import *

class Employee(Person):
    def __init__(self, name, lastname, department):
        super().__init__(name, lastname)
        self.department = department

    def getEmployee(self):
        return self.Name() + " - " + self.department

    #def addEmployee(self):
    #    list = []
    #    self.employee.append(list)


#person = Person("Camila", "Cortes",)
#employee1 = Employee("Dara", "Cortes", "Ventas")
#print(person.Name())
#print(employee1.getEmployee())