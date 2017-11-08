def calculate_sale_employee(pieces_sold):
    return pieces_sold * 2.5


def calculate_factory_employee(number_pieces_prod, defective_pieces):
    return number_pieces_prod * 10 - defective_pieces * 1.3


def discount(total_salary):
    return total_salary * 0.125


def calculate_net_salary(total_salary, discount):
    return total_salary - discount
