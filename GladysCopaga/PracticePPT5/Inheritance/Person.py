class Person:
    def __init__(self, name, lastname, age, ci):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.ci = ci

    def Identity(self):
        return self.name + " - " + self.lastname + " - " + self.age + " - " + self.ci