from AlejandroAlcocer.exam.Person import Person
class Employee(Person):


    def __init__(self, name, last_name, department):
        Person.__init__(self, name, last_name)
        self.department = department
        self.salary = {"Global Salary": 0,
                       "Total Discount": 0,
                       "Net Salary": 0}

    def get_employee(self):
        employee = (Person.get_person(self))
        employee.extend([self, self.department])
        return employee

    def set_salary(self, salary):
        self.salary["Global Salary"] = salary[0]
        self.salary["Total Discount"] = salary[1]
        self.salary["Net Salary"] = salary[2]

    def print_employees(self):
        employee_info = [self.name + " " + self.last_name, self.department, self.salary["Global Salary"],
                         self.salary["Total Discount"], self.salary["Net Salary"]]
        print(employee_info)