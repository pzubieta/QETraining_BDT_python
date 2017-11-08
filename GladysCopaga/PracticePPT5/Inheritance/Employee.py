from Person import *

class Employee(Person):
    def __init__(self, name, lastname, age, ci, employee_id, department):
        #Person.__init__(self, name, lastname, age, ci)
        super().__init__(name, lastname, age, ci)
        self.employee_id = employee_id
        self.department = department

    def getEmployee(self):
        return self.Identity() + " - " + self.employee_id +" - "+ self.department

person1 = Person("Camila", "Cortes", "18", "263265")
person2 = Employee("Dara", "Cortes", "15", "263265","001","Ventas")

print(person1.Identity())
print(person2.getEmployee())