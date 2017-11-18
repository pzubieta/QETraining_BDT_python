from Persona import *

class Employee(Person):

   def __init__(self,first,last,staffnum):
     Person.__init__(self,first,last)
     self.staffnumber=staffnum

   def getEmployee(self):
      return self.Name()+" "+ self.staffnumber