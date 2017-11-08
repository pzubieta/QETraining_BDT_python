from Persona import *
import Calculate.discount
import Calculate.netSalary
import Calculate.Salary

class Employee(Person):

   def __init__(self,first,last,department):
     Person.__init__(self,first,last)
     self.department=department

   def getEmployee(self):
      return self.Name()+" "+ self.department

   def salary(self):
     if self.department=='Sales':
       numSold = int(input("Insert number of pieces sold :"))
       sal=Calculate.Salary.salary1(numSold)
       dis = Calculate.discount.discount1(numSold)
       net = Calculate.netSalary.netSalary1(numSold)
       return sal,dis,net
     elif (self.department == 'Factory'):
         numProd = int(input("Insert number of pieces Produced :"))
         numDefect = int(input("Insert number of pieces Defective :"))
         sal = Calculate.Salary.salary2(numProd,numDefect)
         dis = Calculate.discount.discount2(numProd,numDefect)
         net = Calculate.netSalary.netSalary2(numProd,numDefect)
         return sal,dis,net
     else:
         return print("Invalid value inserted in num of pieces")

