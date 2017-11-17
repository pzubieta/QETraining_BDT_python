class Person(object):

    def __init__(self, name, last, age, ci):
        self.name = name
        self.last = last
        self.age= age
        self.ci=ci

    def GetNamePerson(self):
        return self.firstname + " " + self.lastname+ " " + self.age + " " + self.ci
