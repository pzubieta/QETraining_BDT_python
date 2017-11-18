from persontask.Person import Person

class Employee(Person):
    def __init__(self, name, lastName, age, ci, emp_id, departament):
        super().__init__(name, lastName, age, ci)
        self.emp_id = emp_id
        self.departament = departament


    def EmployeeId(self):
        return self.emp_id

    def Departament(self):
        return self.departament

    def toEmployeeString(self):
        return Person.PersonRecord() + " " + self.EmployeeId() + " " + self.Departament()


person = Person("Marce", "Ines", "16", "1234698")
employee = Employee("Irina", "Ines", "16", "8512364", "01", "Ventas")

print(person.PersonRecord())
print(employee.EmployeeRecord())



