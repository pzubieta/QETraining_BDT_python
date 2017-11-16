class Person:

    def __init__(self, first, last, age, ci):
        self.first_name = first
        self.last_name = last
        self.ages = age
        self.cis = ci

    def Name(self):
        return self.first_name + " " + self.last_name + " " + self.ages + " " + self.cis

class Employee(Person):

    def __init__(self, first, last, age, ci, employe_id, department):
        Person.__init__(self, first, last, age, ci)
        self.employee_id = employe_id
        self.department = department
    def GetEmployee(self):
        return self.Name() + ", " + self.employee_id + ", " + self.department

x = Person("Marge", "Simpson", "28", "405260")
y = Employee("Homer", "Simpson", "30", "457829", "1001", "Tester")

print(x.Name())
print(y.GetEmployee())