import logging
import salary_calc
from Factory_Employee import Factory_Employee
from Sales_Employee import Sales_Employee

logging.basicConfig(filename='employeeManagemt.log', level=logging.INFO)

nroemp = int(input("Insert the nubmer of empoyees: "))
count = 1
saleflag = 0
f_employeelist = []
s_employeelist = []
logging.info('Filling the employees')
while count <= nroemp:
    count = count + 1
    first = input("First name: ")
    last = input("Last name: ")
    dep = input("Department: ")
    glo = input("Global Salary: ")

    if int(input("Is it a sales employee? 1->yes 0->no: ")):
        psold = int(input("Num of Pieces sold: "))
        saleflag = 1
    else:
        peff = int(input("Num of Effective Pieces: "))
        pdef = int(input("Num of Defective Pieces: "))

    if saleflag:
        employee = Sales_Employee(first,last,dep,glo,psold,12.5)
        s_employeelist.append(employee)
    else:
        employee = Factory_Employee(first, last, dep, glo,12.5, peff, pdef)
        f_employeelist.append(employee)
    print("---------Enter next employee data-----")
    logging.info('Employee has been filled out, asking for next employee')

logging.info('Calculating salaries and printing table')
print ("Name     !        Departament     !  Global Sal  ! Total Disc  ! Net Salary!")
for employee in s_employeelist:
    glosal = employee.getglobalsalary()
    totsal = salary_calc.total_salary_calc_sales(employee)
    netsal = salary_calc.net_salary_calc_sales(employee)
    print(employee.getname(),"   !   ", employee.getdepartament(),"   !   ",glosal,"   !   ",totsal,"   !   ",netsal)

for employee in f_employeelist:
    glosal = employee.getglobalsalary()
    totsal = salary_calc.total_salary_calc_factory(employee)
    netsal = salary_calc.net_salary_calc_factory(employee)
    print(employee.getname(),"   !   ", employee.getdepartament(),"   !   ",glosal,"   !   ",totsal,"   !   ",netsal)
