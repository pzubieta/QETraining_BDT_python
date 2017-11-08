from exam.logger import login_msg
from exam.person import person
from exam.salary_calculation import total_discount
from exam.salary_calculation import net_salary


class employee(person):
    def __init__(self, fname, lname, department, total_salary):
        super().__init__(fname, lname)
        self.department = department
        self.total_salary = total_salary
        login_msg("info", "calculating discount")
        self.total_discount = total_discount(self.total_salary)
        login_msg("debug", "discount %s" % self.total_discount)
        login_msg("info", "calculating net salary")
        self.net_salary = net_salary(self.total_salary, self.total_discount)
        login_msg("debug", "net salary %s" % self.net_salary)

    def get_employee_name(self):
        return super().get_full_name()

    def get_employee_department(self):
        return self.department

    def get_total_salary(self):
        return self.total_salary

    def get_total_discount(self):
        return self.total_discount

    def get_net_salary(self):
        return self.net_salary
