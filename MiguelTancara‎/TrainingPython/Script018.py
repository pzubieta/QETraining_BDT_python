# Inheritance
# class BaseClass:
#    body     of     baseclass

# class DerivedClass(BaseClass)
#    body    of    derivedclass

#    attributes and methods    are    shared


class Person:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def name(self):
        return self.firstname + " " + self.lastname


class Employee(Person):
    def __init__(self, first, last, staffnum):
        Person.__init__(self, first, last)
        #super().__init__(first, last)
        self.staffnumber = staffnum

    def getEmployee(self):
        return self.name() + "," + self.staffnumber


x = Person("Marge", "Simpsons")
y = Employee("Homer", "Simpsons", "1007")

print(x.name())
print(y.getEmployee())