def total_salary_sales(num_pieces):
    return num_pieces * 2.5


def total_salary_factory(num_effective_pieces, num_defective_pieces):
    return (num_effective_pieces * 10) - (num_defective_pieces * 1.3)


def total_discount(total_salary):
    return total_salary * 0.125


def net_salary(total_salary, discount):
    return total_salary - discount

