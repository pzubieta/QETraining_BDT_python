from oop.Person import Person
from oop.Employee import Employee

person1 = Person("Diego","Gonzales", "28", "6552890")
employ1 = Employee("Bilma", "Balderrama", "29", "6521231", "emp0001", "Administracion")

print(person1.toString())
print(employ1.toEmployeeString())