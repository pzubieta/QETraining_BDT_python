class Person(object):
#dfs
    def __init__(self, nombre):
        self.Name=nombre


    def Name(self):
         return self.Name

class Employee(Person):

    def __init__ (self,name, DepartamentS, globalS, totalD, netSal ):

        Person.__init__(self,name)
        self.DepS=DepartamentS
        self.gloSal=globalS
        self.discTotal=totalD
        self.NetS=netSal

    def GetEmployeeS(self,countUsr):
        for i in countUsr:
         return self.Name()+" | "+self.DepS+" | "+self.gloSal+" | "+self.discTotal+" | "+self.NetS



