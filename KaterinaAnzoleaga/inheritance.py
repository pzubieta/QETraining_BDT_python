class Person:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last
    def Name (self):
        return self.firstname+" "+self.lastname

class Employee(Person):
    '''
        Alternative init method:
        def __init__(self, first, last, staffnum):
        Person.__init__(self, first, last)
        self.staffnumber = staffnum
    '''
    def __init__(self, first, last, staffnum):
        super().__init__(first, last)
        self.staffnumber = staffnum

    def GetEmployee (self):
        return self.Name()+" "+self.staffnumber

x = Person ("Marge", "Simpson")
y = Employee ("Homer", "Simpson", "1008")

print (x.Name())
print(y.GetEmployee())

