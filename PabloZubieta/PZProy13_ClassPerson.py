class Person

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
            return self.firstname + "" + self.lastname

class Employee(Person):
    def __init__ (self, first, last, staffnum):
        #Person.__init__(self,first,last)
        super().__init__(first,last) #otra alternativa pero no es necesario usar self
        self.staffnumber = staffnum

    def GetEmployee(selfself):
        return self.Name() + "," + self.staffnumber

x = Person("Marge", "Simpson")
y = Employee("Homer", "Simpson","1007")

print(x.Name())
print(y.GetEmployee())