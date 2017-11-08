import logging
from Perform_Calculations.SalaryCalculation import *
from ExamenEmployee import *

# Logger Definition
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
handler = logging.FileHandler('application.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Main program
def main():
    employee_list = []
    logger.info('Action: Start main program')
    #Ask for the number of employees, it should be >3 and <15
    number_employee = int(input("Enter number of employees more than 3 and less than 15:"))
    if(number_employee<=15 and number_employee >=3):
        logger.debug('Action: Start to store {} employee(s)'.format(number_employee))
        cont_employee=0
        while(cont_employee<number_employee):
            #name, last_name, age, ci, employee_id, department

            department_aux_id=input("Enter 1 if the employee belongs to the Sales department, and 2 if the employee belongs to the Factory department:")

            if(department_aux_id =="1"):
                logger.info('Action: Employee stored is from Sales department')
                name_aux = input("Enter employee name: ")
                last_name_aux = input("Enter employee last name: ")
                age_aux = int(input("Enter employee age: "))
                ci_aux = input("Enter employee ci: ")
                id_emp_aux = "SALES-{}".format(cont_employee)
                department_aux ="SALES"
                number_of_pieces_sold_aux=int(input("Enter number of pieces sold: "))
                employee_aux = ExamenEmployee(name_aux, last_name_aux, age_aux, ci_aux, id_emp_aux, department_aux)
                employee_aux.set_number_of_pieces_sold(number_of_pieces_sold_aux)
                employee_aux.set_global_salary_employee(total_salary_sales(number_of_pieces_sold_aux))
                employee_aux.set_total_discount_employee(total_discount(employee_aux.get_global_salary_employee()))
                employee_aux.set_net_salary_employee(total_net_salary(employee_aux.get_global_salary_employee(),employee_aux.get_total_discount_employee() ))
                employee_list.append(employee_aux)
                cont_employee += 1
            elif(department_aux_id =="2"):
                logger.info('Action: Employee stored is from Factory department')
                name_aux = input("Enter employee name: ")
                last_name_aux = input("Enter employee last name: ")
                age_aux = int(input("Enter employee age: "))
                ci_aux = input("Enter employee ci: ")
                id_emp_aux = "Factory-{}".format(cont_employee)
                department_aux = "Factory"
                number_of_efective_piece_aux = int(input("Enter number of efective pieces: "))
                number_of_defective_piece_aux = int(input("Enter number of defective pieces: "))
                employee_aux = ExamenEmployee(name_aux, last_name_aux, age_aux, ci_aux, id_emp_aux, department_aux)
                employee_aux.set_number_of_efective_piece(number_of_efective_piece_aux)
                employee_aux.set_number_of_defective_piece(number_of_defective_piece_aux)
                employee_aux.set_global_salary_employee(total_salary_factory(number_of_efective_piece_aux,number_of_defective_piece_aux))
                employee_aux.set_total_discount_employee(total_discount(employee_aux.get_global_salary_employee()))
                employee_aux.set_net_salary_employee(total_net_salary(employee_aux.get_global_salary_employee(),
                                                                      employee_aux.get_total_discount_employee()))
                employee_list.append(employee_aux)
                cont_employee += 1
            else:
                logger.info('Action: Employee stored is from None department')
                print("Your input id department is not correct")

        for val in employee_list:
            val.print_employee()

    else:
        print("Number of employees is incorrect: {}".format(number_employee))

    Person_a = ExamenEmployee("Adrian", "Marcos", 34, "3345566 bn", 3435, "Sales")


main()