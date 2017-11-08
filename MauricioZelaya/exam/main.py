from exam.logger import login_msg
from exam.employee import employee
from exam.salary_calculation import total_salary_sales
from exam.salary_calculation import total_salary_factory

employee_list = []
count = 0
login_msg("info", "Starting process............")
total_employees = int(input("please insert the total employees of the company:\n"))
login_msg("debug", "inserting %s employees" % total_employees)
if total_employees >= 3 and total_employees <= 15:
    while count < total_employees:
        login_msg("info", "insert employee # %s" % count)
        employee_name = input("Employee Name:\n")
        employee_lname = input("Employee Last Name:\n")
        employee_department = input("Employee department:\n")
        login_msg("debug", "employee: %s" % employee_name + " " + employee_lname + " - " + employee_department)
        login_msg("info", "calculating total salary")
        if employee_department == "factory":
            num_effective_pieces = int(input("insert effective pieces for the employee\n"))
            num_defective_pieces = int(input("insert defective pieces for the employee\n"))
            total_salary = total_salary_factory(num_effective_pieces, num_defective_pieces)
            login_msg("debug", "total salary for factory employee %s" % total_salary)
        else:
            num_sold_pieces = int(input("insert sold pieces for the employee\n"))
            total_salary = total_salary_sales(num_sold_pieces)
            login_msg("debug", "total salary for sales employee %s" % total_salary)
        employee_list.append(employee(employee_name, employee_lname, employee_department, total_salary))
        count += 1
    print("NAME | Department | Global Salary | Total Discount | Net Salary")
    for employee in employee_list:
        print(employee.get_full_name() + " | " + employee.get_employee_department()
              + " | " + str(employee.get_total_salary()) + " | " + str(employee.get_total_discount())
              + " | " + str(employee.get_net_salary()))
else:
    print("You are not able to input less than 3 employees or more than 15. Please try again")
