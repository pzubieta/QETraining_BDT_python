class Person:

    def __init__(self, first, last, age, ci):
        self.first = first
        self.last = last
        self.age = age
        self.ci = ci

    def first(self):
        return self.first


    def last(self):
        return self.last

    def ciEmp(self):
        return self.ci

    def Age(self):
        return self.age


    def PersonRecord(self):
        return self.first() + " " + self.last() + " " + self.ciEmp() + " " + self.Age()