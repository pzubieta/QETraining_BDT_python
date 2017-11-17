from exam.Employee import *
import logging

logging.basicConfig(filename='example.log', level=logging.DEBUG)
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


class Person(Employee):
   def __init__(self, name, department, numberofpieces, pieces_produced, pices_defect):
      super().__init__(name, department)
      self.name = name
      self.department = department
      self.numberofpiecessold = numberofpieces
      self.num_pieces_produced = pieces_produced
      self.num_pieces_defect = pices_defect

   def get_employee(self):
      return self.Name()

   def global_salary(self,):
      return self.numberofpiecessold*2.5

   def factory_employee(self):
      return (self.num_pieces_produced * 10) - (self.num_pieces_defect * 1.3)

   def discount(self, band):
      if band == 1:
         return (self.global_salary() * 12.5) / 100
      else:
         return (self.factory_employee() * 12.5) / 100

   def Next_Salary(self, band):
      if band == 1:
         return self.global_salary() - self.discount(band)
      else:
         return self.factory_employee() - self.discount(band)



logger.info("add employes")
print("Number of Employees")
ne = int(input("Please add the number of employees: "))
logger.info("number of employees")
salesEmployee = 0
factoryEmployee = 0
number_pieces_sold = 0
number_pieces_produced = 0
number_defective_pieces = 0
employee = {}

for e in range(ne):
   print("SALES EMPLOYEE?")
   y = int(input("insert yes =1/no =0 "))
   if y == 1:
      nameemployee = input("Name employee: ")
      department = input("department: ")
      number_pieces_sold = int(input("number of pieces sold: "))
      employee[nameemployee] = Employee(nameemployee, department,)
      xx = Person(nameemployee, department, number_pieces_sold, 0, 0)
      salesEmployee += 1
   else:
      nameemployee = input("Name employee: ")
      department = input("department: ")
      number_pieces_produced = int(input("number of pieces produced: "))
      number_defective_pieces = int(input("number of defective pieces: "))
      employee[nameemployee] = Employee(nameemployee, department)
      yy = Person(nameemployee, department, 0, number_pieces_produced, number_defective_pieces)
      factoryEmployee += 1

print("NAME | Department | Global Salary | Total Discount | Next Salary")
print(xx.get_employee(), "    ", xx.global_salary(), "    ", xx.discount(1), "    ", xx.Next_Salary(1))
print(yy.get_employee(), "    ", yy.factory_employee(), "    ", yy.discount(0), "    ", yy.Next_Salary(0))
