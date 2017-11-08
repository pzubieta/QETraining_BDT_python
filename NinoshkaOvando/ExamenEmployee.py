import logging
#import ExamenPerson
from ExamenPerson import ExamenPerson


class ExamenEmployee(ExamenPerson):

    def __init__(self, name,last_name,age,ci,employee_id,department ):
        ExamenPerson.__init__(self, name,last_name,age,ci)   #----super().__init__(self, name,last_name,age,ci)
        self.employee_id=employee_id
        self.department= department
        self.global_salary_employee=0
        self.total_discount_employee=0
        self.net_salary_employee = 0
        self.number_of_pieces_sold=0
        self.number_of_efective_piece = 0
        self.number_of_defective_piece = 0
        self.create_logger()

    def getEmployee(self):
        self.logger.info('getEmployee Action')
        return "Employee is ", self.employee_id,": ",  self.Name() + ", Department: " + self.department

    def print_employee(self):
        self.logger.info('print_employee Action')
        print("|	 Name	|	Department	 |	 Global Salary	 |	 	Total Discount 	 |	 Net Salary 	 |")
        print("|	 {}	|	{}	 |	 {}	 |	 	{} 	 |	 {} 	 |".format(self.name, self.department, self.global_salary_employee, self.total_discount_employee, self.net_salary_employee))

    def set_global_salary_employee(self,global_salary_employee ):
        self.global_salary_employee = global_salary_employee
    def get_global_salary_employee(self):
        return self.global_salary_employee

    def set_total_discount_employee(self,total_discount_employee ):
        self.total_discount_employee = total_discount_employee
    def get_total_discount_employee(self):
        return self.total_discount_employee

    def set_net_salary_employee(self,net_salary_employee ):
        self.net_salary_employee = net_salary_employee
    def get_net_salary_employee(self):
        return self.net_salary_employee

    def set_number_of_pieces_sold(self,number_of_pieces_sold):
        self.number_of_pieces_sold= number_of_pieces_sold
    def get_number_of_pieces_sold(self):
        return self.number_of_pieces_sold

    def set_number_of_efective_piece(self,number_of_efective_piece):
        self.number_of_efective_piece= number_of_efective_piece
    def get_number_of_efective_piece(self):
        return self.number_of_efective_piece

    def set_number_of_defective_piece(self,number_of_defective_piece):
        self.number_of_defective_piece= number_of_defective_piece
    def get_number_of_defective_piece(self):
        return self.number_of_defective_piece

    def create_logger(self):
        self.logging = logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)
        self.handler = logging.FileHandler('Log_Employee.log')
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)