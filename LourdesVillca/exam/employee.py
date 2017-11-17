from exam.person import Person

class Employee(Person):
    def __init__(self, name, department, global_salary, total_discount, net_salary, type):
        super().__init__(name)
        self.department = department
        self.global_salary = global_salary
        self.total_discount = total_discount
        self.net_salary = net_salary
        self.type = type
