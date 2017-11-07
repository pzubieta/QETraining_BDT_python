from AlejandroAlcocer.practices.person import Person

class Employee(Person):


    def __init__(self, name, last_name, age, ci, employee_id, department):
        Person.__init__(self, name, last_name, age, ci)
        self.employee_id = employee_id
        self.department = department

    def get_employee(self):
        employee = (Person.get_person(self))
        employee.extend([self.employee_id, self.department])
        return employee


####################  TEST    ####################

e = Employee("name", "las_name", 30, 45, 123, "dev")
print(e.get_person())
print(e.get_employee())
