from Person import Person

class Employee(Person):
    def __init__(self,name,lastName,Age,CI,Employee_Id,Department):
        super().__init__(name,lastName,Age,CI)
        self.Employee_Id = Employee_Id
        self.Department = Department

    def getEmployee(self):
        return self.name+" "+ self.lastName+", Departamento: "+self.Department

    def infoEmployee(self):
        return "Tiene ",self.Age," años, CI: ",self.CI," EmployeeID:",self.Employee_Id




