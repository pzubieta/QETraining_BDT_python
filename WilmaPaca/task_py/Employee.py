from Person import Person
class Employee(Person):
    def __init__(self, first,last,age,ci,employee_id,department):
        Person.__init__(self,first,last,age,ci)
        self.employee_id_emp =employee_id
        self.department_emp =department
    def get_Employee(self):
        return self.get_dataPerson()+","+self.employee_id_emp+","+self.department_emp

emp = Employee("Locky","Pat","23","568977","67","Finanzas")
print (emp.get_Employee())