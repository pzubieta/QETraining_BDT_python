
var_sales = 2.5
var_factory1=10
var_factory2=1.3

def getSalesSalary(pieces):
    global  var_sales
    sales_salary=pieces*var_sales
    return sales_salary

def getFactorySalary(defect, effect):
    global var_factory1
    global var_factory2
    factory_salary = (effect*var_factory1)-(defect*var_factory2)
    return factory_salary

def getDiscount(salary):
    discount = salary*(12.5/100)
    return discount

def getSalary(salary, discount):
    return salary-discount
'''
salario= getSalesSalary(1500)
print(salario)

desc= getDiscount(salario)
print(desc)

sal= getSalary(salario, desc)
print(sal)
'''