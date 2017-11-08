import log

logger = log.setup_custom_logger(__name__)


def calculate_total_salary(employee):
    logger.info('Verifying the departament ')
    if employee.get_departament() == 'Sales':
        employee.set_total_salary(employee.get_effective_pieces() * 2.5)
    elif employee.get_departament() == 'Factory':
        employee.set_total_salary((employee.get_effective_pieces() * 10) - (employee.get_defective_pieces() * 1.3))
    else:
        employee.set_total_salary = employee.salary
    return employee


def calculate_descount(total_salary):
    logger.info('calculating the descount')
    return total_salary * 0.125
