import AlejandroAlcocer.practices.person as person

class Employee(person):

    def __init__(self, name, last_name, age, ci, employee_id, department):
        person.Person.__init__(self, name, last_name, age, ci)
        self.employee_id = employee_id
        self.department = department

