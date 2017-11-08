def total_salary_sales(number_of_pieces):
    return number_of_pieces*2.5

def total_salary_factory(sum_efective_pieces, sum_defective_pieces):
    return (sum_efective_pieces*10)- (sum_defective_pieces*1.3)

def total_discount(total_salary):
    return total_salary*0.125

def total_net_salary(total_salary,total_discount ):
    return total_salary-total_discount
