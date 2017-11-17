import logging
import logging.config

from exam_calculate_salary_employee_PACKAGE_CALCS import calc_total_sales_salary, calc_total_factory_salary, calc_discount_salary
import exam_calculate_salary_employee_PACKAGE_PERSON

number_employees = input("Please enter the number of employees to be registered: ")

while int(number_employees)<3 or int(number_employees)>15:
    print("\n")
    print("Please enter again the total number of employees to be registered: ")
    number_employees = input("No less than 3 and no more than 15 please.")
    print("\n")

#CREATE A LIST FOR OBJECTS PERSON
list_employees=[]

#ACCORDING THE NUMBER OF EMPLOYEE ENTERED, ASK FOR EACH EMPLOYEE DATA
for i in range(0,int(number_employees)):
    #Ask for the type of Employee
    print("Please enter the type of Employee:")
    print("1 - Sales")
    print("2 - Factory")
    typeEmployee = input(":")
    print("\n")

    #Ask for the name of the Employee
    if int(typeEmployee)==1:
        nameEmployee = input("Please enter the name of the Sales Employe:")

        # Ask for the departament of the employee
        departamentEmployee = input("Please enter the departament of the Sales Employee "+nameEmployee+":")

        # Ask for the number of sold pieces
        soldPieces = input("Please enter the number of sold pieces for Sales Employee "+nameEmployee+":")
        int(soldPieces)
        print("\n")

        #Calculate the Total Salary using the "calc_total_sales_salary" method from imported Package
        totalSalesSalary = calc_total_sales_salary(soldPieces)
        print("Total Salary for " + nameEmployee + " is:", totalSalesSalary)

        # Calculate the Discount to Salary using the "calc_discount_salary" method from imported Package
        discountSalary = calc_discount_salary(totalSalesSalary)
        print("Discount to Salary is: ", discountSalary)

        #Calculate the Net Salary having "totalSalesSalary" and "discountSalary"
        netSalary = totalSalesSalary - discountSalary
        print("Net Salary is: ", netSalary)
        print("\n")

        #With all gathered data we add the employee to our list
        list_employees.append(exam_calculate_salary_employee_PACKAGE_PERSON.Employee(nameEmployee,departamentEmployee,totalSalesSalary,discountSalary,netSalary))

    if int(typeEmployee)==2:
        nameEmployee = input("Please enter the name of the Factory Employee:")

        # Ask for the departament of the employee
        departamentEmployee = input("Please enter the departament of the Factory Employee " + nameEmployee + ":")

        # Ask for the number of total pieces
        totalPieces= input("Please enter the number of total pieces for Factory Employee " + nameEmployee + ":")
        int(totalPieces)

        # Ask for the number of defectie pieces
        defectivePieces = input("Please enter the number of defective pieces for Factory Employee " + nameEmployee + ":")
        int(defectivePieces)
        print("\n")

        # Calculate the Total Salary using the "calc_total_factory_salary" method from imported Package
        totalFactorySalary = calc_total_factory_salary(totalPieces,defectivePieces)
        print("Total Salary for "+nameEmployee+" is:", totalFactorySalary)

        # Calculate the Discount to Salary using the "calc_discount_salary" method from imported Package
        discountSalary = calc_discount_salary(totalFactorySalary)
        print("Discount to Salary is: ", discountSalary)

        # Calculate the Net Salary having "totalSalesSalary" and "discountSalary"
        netSalary = totalFactorySalary - discountSalary
        print("Net Salary is: ",netSalary)
        print("\n")

        # With all gathered data we add the employee to our list
        list_employees.append(exam_calculate_salary_employee_PACKAGE_PERSON.Employee(nameEmployee,departamentEmployee,totalSalesSalary,discountSalary,netSalary))

print("This is all the information of entered employes and their data:")
print("        NAME          |      DEPARTMENT      | TOTAL SALARY | TOTAL DISCOUNT | NET SALARY")
for i in list_employees:
    print(list_employees)

