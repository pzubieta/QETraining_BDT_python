class Person:

    def __init__(self, name, lastName):
        self.name = name
        self.lastName = lastName

    def getName(self):
        return self.name

    def getLastname(self):
        return self.lastName

    def getPersonName(self):
        return self.getName() + " " + self.getLastname()
