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
logging.info('Filling1 the employees')

while count <= nroemp:
    count = count + 1
    first = input("First name: ")
    last = input("Last name: ")
    dep = input("Department: ")
    glo = input("Global Salary: ")

    if int(input("Is it a sales employee? 1->yes 0->no: ")) == 1:
        psold = int(input("Num of Pieces sold: "))
        saleflag = 1
    else:
        peff = int(input("Num of Effective Pieces: "))
        pdef = int(input("Num of Defective Pieces: "))
        saleflag = 0

    if saleflag == 1:
        employee = Sales_Employee(first,last,dep,glo,psold,12.5)
        s_employeelist.append(employee)
    else:
        employee = Factory_Employee(first, last, dep, glo,12.5, peff, pdef)
        f_employeelist.append(employee)
    print("---------Enter next employee data-----")
    logging.info('Employee has been filled out, asking for next employee')
'''
# testing data
logging.info('Calculating salaries and printing table')
employee1 = Factory_Employee("Pablo", "Zubieta", "Dep1", 100,12.5, 10, 1)
employee2 = Factory_Employee("Pablo2", "Zubieta2", "Dep2", 200,12.5, 20, 2)
employee3 = Sales_Employee("Pablo3", "Zubieta3", "Dep3", 300, 30, 12.5)

f_employeelist.append(employee1)
f_employeelist.append(employee2)
s_employeelist.append(employee3)
'''

print ("Name     !        Departament     !  Global Sal  ! Total Disc  ! Net Salary!")
for employee_s in s_employeelist:
    glosal = employee_s.getglobalsalary()
    totsal = salary_calc.total_salary_calc_sales(employee_s)
    netsal = salary_calc.net_salary_calc_sales(employee_s)
    print(employee_s.getname(),"   !   ", employee_s.getdepartament(),"   !   ",glosal,"   !   ",totsal,"   !   ",netsal)

for employee_f in f_employeelist:
    glosal = employee_f.getglobalsalary()
    totsal = salary_calc.total_salary_calc_factory(employee_f)
    netsal = salary_calc.net_salary_calc_factory(employee_f)
    print(employee_f.getname(),"   !   ", employee_f.getdepartament(),"   !   ",glosal,"   !   ",totsal,"   !   ",netsal)
