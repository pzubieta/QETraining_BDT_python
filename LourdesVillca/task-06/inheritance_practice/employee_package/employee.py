from person_package.person import Person


class Employee(Person):
    def __init__(self, name, last_name, age, ci, employee_id, department):
        super().__init__(name, last_name, age, ci)
        self.employee_id = employee_id
        self.department = department
