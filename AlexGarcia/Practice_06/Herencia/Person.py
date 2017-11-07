class Person:
    def __init__(self, name,lastName,Age, CI):
        self.name = name
        self.lastName = lastName
        self.Age = Age
        self.CI = CI
    def mostrarInfo(self):
        return self.name +" "+ self.lastName