
def total_salary_calc_sales(employee):
    return (employee.getpiecessold()*2.5)

def total_salary_calc_factory(employee):
    return (employee.getpiecessold()*10 - employee.getdefpieces()*1.3)

def net_salary_calc_factory(employee):
    totalsal = total_salary_calc_factory(employee)
    disc = employee.getdiscount()
    netsal = totalsal-(totalsal*disc/100)
    return netsal

def net_salary_calc_sales(employee):
    totalsal = total_salary_calc_sales(employee)
    disc = employee.gettotaldiscount()
    netsal = totalsal-(totalsal*disc/100)
    return netsal