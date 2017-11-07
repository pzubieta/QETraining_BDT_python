from personScript.person import person

class employee(person):
    def __init__(self, fname, lname, age, ci, employee_id, department):
        super().__init__(fname, lname, age, ci)
        self.employee_id = employee_id
        self.department = department

    def get_employee_name(self):
        return super().get_full_name()

    def get_employee_department(self):
        return self.department

    def get_employee_id(self):
        return self.employee_id

