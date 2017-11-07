from person_package.person import Person

class Employee(Person):
    def __init__(self, name, last, age, ci, emp_id, departament):
        super().__init__(name, last, age, ci)
        self.emp_id = emp_id
        self.departament = departament

    def get_employee(self):
        return self.name + " " + self.departament + " " + self.emp_id
x = Employee("Marge", "Simpson", "11", "2558", "01", "cb")
print(x.get_employee())


def add_employe():
    amount_employee = int(input("nro employee: "))
    list_employee = []
    count=0

    while (amount_employee > 0) and (count < amount_employee):
        name = input('name')
        last = input('last')
        age = input('age')
        ci = input('ci')
        emp_id = input('emp_id')
        departament = input('departament')

        Employee(name, last, age, ci, emp_id, departament)
        list_employee.append(Employee(name, last, age, ci, emp_id, departament))
        count+= 1
    var=1
    for employee in list_employee:

        print ("employe #", var, employee.get_employee(),"\n")
        var=var +1

add_employe()



