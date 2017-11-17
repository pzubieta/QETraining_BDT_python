class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def getname(self):
            return self.firstname + " " + self.lastname
