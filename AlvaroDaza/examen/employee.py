from person import Person


class Employee(Person):
    def __init__(self, first_name, last_name, departament, effective_pieces, defective_pieces, salary):
        Person.__init__(self, first_name, last_name)
        self.employee_departament = departament
        self.effective_pieces = effective_pieces
        self.defective_pieces = defective_pieces
        self.total_salary = salary
        self.salary = 1500

    def get_departament(self):
        return self.employee_departament

    def get_global_salary(self):
        return self.salary

    def get_effective_pieces(self):
        return self.effective_pieces

    def get_defective_pieces(self):
        return self.defective_pieces

    def set_total_salary(self, salary):
        self.total_salary = salary
