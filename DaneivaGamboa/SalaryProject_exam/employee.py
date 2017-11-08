from person import Person

class Employee(Person):
    def __init__(self, name, last, age, departament, emp_type):
        super().__init__(name, last, age, departament,emp_type)
        self.emp_type = emp_type

    def get_name_employee(self):
        return self.name + " " + self.last

    def get_departament(self):
        return self.name + " " + self.last

    def calc_type_of_employe(self):
        if  self.emp_typeemp_type != "Sales" or self.emp_type != "Factory":
            if  self.emp_typeemp_type == "Sales":
                a = '2,5'
                porcen = '12,5'
                num_pieces_sold = input('Insert number of pieces sold?')
                total_salary = (num_pieces_sold * a)
                total_discount = ((total_salary * porcen) / 100)
                net_salary = (total_salary - total_discount)
                res = total_salary, "|", total_discount, "|", net_salary
            elif  self.emp_type == "Factory":
                pocen2= '1,3'
                num_pieces_produced = input('Insert number of pieces produced?')
                num_pieces_defect = input('Insert number of defective pieces ?')
                total_salary = ((num_pieces_produced * 10) - (num_pieces_defect *1,3 ))
                total_discount = ((total_salary * 1,3) / 100)
                net_salary = (total_salary - total_discount)
                res= total_salary,"|", total_discount,"|", net_salary
            return (res)
        print("error value!, bye")
        pass

def add_employe():
    amount_employee = int(input("nro employee to register: "))
    list_employee = []
    count = 0
    if ((amount_employee > 0) and (amount_employee < 15)):
        while (count < amount_employee):
            name = input('Name of Employee')
            last = input('Lastname of Employee')
            age = input('Age')
            departament = input('Departament')
            emp_type = input('Sales or Factory?')
            calc_type_of_employe(emp_type)
            Employee(name, last, age, departament, emp_type)
            list_employee.append(Employee(name, last, age, departament, emp_type))
            count += 1
        print("Name       |", "Departament |", "Global Salary |", "Total Discount |", "Net Salary")
        for employee in list_employee:
            print(employee.get_name_employee(),"|",employee.get_departament(),"|", "\n")

    #else: print(" please enter a new value, no less 3 and no more 15. Bye!")

add_employe()

