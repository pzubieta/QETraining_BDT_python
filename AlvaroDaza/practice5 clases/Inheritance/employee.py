from person import Person


class Employee(Person):
    def __init__(self, first, last, staff_num):
        Person.__init__(self, first, last)
        # super().__init__(first,last)
        self.staff_number = staff_num

    def get_employee(self):
        return self.name() + "," + self.staff_number


x = Person("Marge", "Simpson")
y = Employee("Homer", "Simpson", "1007")

print(x.name())
print(y.get_employee())