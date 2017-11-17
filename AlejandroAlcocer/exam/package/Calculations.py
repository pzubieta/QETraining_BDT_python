
def sales_employee(pieces_sold):
    """
    This method calculate the salary of a sales employee.
    :param pieces_sold:  The amount of items sold by a employee.
    :return: The salary of the employee.
    """
    salary = pieces_sold * 2.5
    discount_v = discount(salary)
    net_salary = salary - discount_v
    return [salary, discount_v, net_salary]


def discount(salary):
    """
    This method return the discount of a salary
    :param salary: The salary
    :return: A discounted salary
    """
    return salary * 0.125

def factory_employee(amount_of_pieces, defected_pieces):
    """
    This method calculate the salary of a factory employee
    :param amount_of_pieces: The amount of pieces that the employee fabricate
    :param defected_pieces: The amount of pieces that are defected
    :return:
    """
    salary = (amount_of_pieces * 10) - (defected_pieces * 1.3)
    discount_v = discount(salary)
    net_salary = salary - discount_v
    return [salary, discount_v, net_salary]