import log
from employee import Employee
from salary import calculate_salary

logger = log.setup_custom_logger(__name__)

total_employees = []
defective_pieces = 0
effective_pieces = 0
salary = 0.0
employees_number = int(input('how many employees do you want register?'))
for index in range(employees_number):
    logger.info('Set the employee')
    name = raw_input('introduce the name')
    last_name = raw_input('introduce the last name')
    departament = raw_input('introduce the departament')
    if departament == 'Sales':
        effective_pieces = int(input('how many effective pieces he sold'))
        print('============== O ===============')
    elif departament == 'Factory':
        effective_pieces = int(input('how many Effective pieces he produced'))
        defective_pieces = int(input('how many Defective pieces he produced'))

    employee = Employee(name, last_name, departament, effective_pieces, defective_pieces, salary)
    total_employees.append(employee)


def print_all_employees(total_employees):
    for employee_in_list in total_employees:
        logger.info('calculating the salary')
        calculate_salary.calculate_total_salary(employee_in_list)
        total = employee.get_global_salary() - calculate_salary.calculate_descount(employee.get_global_salary())
        print (
            str(employee_in_list.get_name()) + '    ' + str(employee_in_list.get_departament()) + '   ' + str(
                employee_in_list.get_global_salary()) + '    ' + str(
                calculate_salary.calculate_descount(employee_in_list.get_global_salary())) + '    ' + str(total))


print_all_employees(total_employees)
