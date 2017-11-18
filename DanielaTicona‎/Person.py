class Person(object):

    def __init__(self, first, last, age, ci):
        self.firstname=first
        self.lastname=last
        self.Edad=age
        self.carnet=ci

    def Name(self):
         return self.firstname+" "+self.lastname+" "+ self.Edad+" "+self.carnet

class Employee(Person):

    def __init__ (self,first, last, age, ci, EmployeeId, Departament):

        Person.__init__(self,first,last,age,ci)
        self.EmpId=EmployeeId
        self.Dep=Departament

    def GetEmployee(self):
        return self.Name()+", "+self.EmpId +", "+self.Dep



x= Employee("Juan","Perez","23","2432543656 LP","132423432","Marketing")
y=Person("Manuel","Martinez","45","4344656 LP")

z=Employee("Jorge","Lopez","32","11111656 LP","24444444","Ingenieria")

print (x.GetEmployee())
print (y.Name())
print (z.GetEmployee())

#dfgjdflgxcvb