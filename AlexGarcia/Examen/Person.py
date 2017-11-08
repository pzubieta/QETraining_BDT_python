class Person:
    def __init__(self, name,lastName):
        self.name = name
        self.lastName = lastName

    def mostrarInfo(self):
        return self.name +" "+ self.lastName