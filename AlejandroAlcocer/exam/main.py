from AlejandroAlcocer.exam.package.Calculations import *
from AlejandroAlcocer.exam.Employee import *
from AlejandroAlcocer.exam.Logger import *


def insert_employee(amount_of_employees):
    """
    This method insert employes into a list.
    :param amount_of_employees: The amount of employees.
    :return: List of employees.
    """
    list_of_employees = []
    while amount_of_employees > 0:
        name = input("insert name: ")
        logger.info("insert_employee: %s", "name was inserted {}".format(name))
        last_name = input("insert last name: ")
        logger.info("insert_employee: %s", "last name was inserted {}".format(last_name))
        department = input("insert department (sales/factory): ")
        logger.info("insert_employee: %s", "department was inserted {}".format(department))
        if department == "sales":
            amount_of_pieces_sold = int(input("insert the amount of pieces sold: "))
            logger.info("insert_employee: %s", "amount of pieces was inserted {}"
                        .format(amount_of_pieces_sold))
            salary = sales_employee(amount_of_pieces_sold)
        else:
            amount_of_effective_pieces = int(input("insert the amount of pieces produced: "))
            logger.info("insert_employee: %s", "amount of produced pieces was inserted {}"
                        .format(amount_of_effective_pieces))
            amount_of_defected_pieces = int(input("insert the amount of defective pieces: "))
            logger.info("insert_employee: %s", "amount of defected pieces was inserted {}"
                        .format(amount_of_defected_pieces))
            salary = factory_employee(amount_of_effective_pieces, amount_of_defected_pieces)
            logger.info("insert_employee: %s", "salary was calculated {}"
                        .format(salary))
        employee = Employee(name, last_name, department)
        employee.set_salary(salary)
        list_of_employees.append(employee)
        amount_of_employees = amount_of_employees - 1
    return list_of_employees

def print_exam_result():
    """
    this method run the exam
    :return: A printed list of the employees.
    """
    amount = ask_for_employee_amount()
    list_of_employees = insert_employee(amount)
    for employee in list_of_employees:
        employee.print_employees()



def ask_for_employee_amount():
    """
    This method ask for the amount of employees that will be evaluated.
    :return: None.
    """
    amount_of_employees = int(input("insert an amount of employees: "))
    if amount_of_employees >= 3 and amount_of_employees < 15:
        logger.info("amount_of_employees: %s", "valid amount of employees {}"
                    .format(amount_of_employees))
        return amount_of_employees
    else:
        print("invalid amount of employees next time try "
                "with more than three and less than fifteen ")
        logger.debug("amount_of_employees: %s", "invalid amount of employees {}"
                .format(amount_of_employees))
        return False


print_exam_result()
