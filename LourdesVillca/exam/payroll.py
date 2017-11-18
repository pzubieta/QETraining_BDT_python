from prettytable import PrettyTable
from exam.logs import employee_log
from exam.salary_calculation import calculation
from exam.employee import Employee


class Payroll:
    def __init__(self):
        self.employee_list = []

    def insert_employee(self):
        name = input("Name: ")
        department = input("Department: ")
        type_employee = input("Type (Sales/Factory): ")
        employee_log.LOG.debug("Inserted Employee type is: {}".format(type_employee))
        if type_employee == "Sales":
            employee_log.LOG.info("Calculating the total Salary for: '{}' Employee type".format(type_employee))

            number_of_pieces_sold = int(input("Number of pieces sold: "))
            total_salary = calculation.calculate_sale_employee(number_of_pieces_sold)

            employee_log.LOG.debug("Total Salary: '{}'".format(total_salary))
        else:
            employee_log.LOG.info("Calculating the total Salary for: '{}' Employee type".format(type_employee))

            number_of_pieces_produced = int(input("Number of pieces produced: "))
            number_of_defective_pieces = int(input("Number of defective pieces: "))
            total_salary = calculation.calculate_factory_employee(number_of_pieces_produced,
                                                                  number_of_defective_pieces)

            employee_log.LOG.debug("Total Salary: '{}'".format(total_salary))

        total_discount = calculation.discount(total_salary)
        employee_log.LOG.debug("Total discount: {}".format(total_discount))

        net_salary = calculation.calculate_net_salary(total_salary, total_discount)
        employee_log.LOG.debug("Net Salary: {}".format(net_salary))

        self.employee_list.append(
            Employee(name, department, total_salary, total_discount, net_salary, type_employee))

    def print_payroll(self):
        employee_log.LOG.info("Print detail of calculated payroll")

        table = PrettyTable(['Name', 'Department', 'Global Salary', 'Discount', 'Net Salary'])
        for employee in self.employee_list:
            table.add_row([employee.name, employee.department, employee.global_salary, employee.total_discount,
                           employee.net_salary])
        print(table)


def register_payroll():
    payroll = Payroll()
    number = int(input("Insert the number of employee to be registered :"))
    employee_log.LOG.info("Number of employee to be registered is {} ".format(number))
    if number > 0 and number <= 15:
        count = 0
        while count < number:
            payroll.insert_employee()
            count += 1
        payroll.print_payroll()
    else:
        employee_log.LOG.debug("Employee Number is not into the range 3-15")


register_payroll()