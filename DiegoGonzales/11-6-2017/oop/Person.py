class Person:

    def __init__(self, name, lastName, ege, ci):
        self.name     = name
        self.lastName = lastName
        self.ege      = ege
        self.ci       = ci

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getLastName(self):
        return self.lastName

    def setLastName(self, newLastName):
        self.lastName = newLastName

    def getEge(self):
        return self.ege

    def setEge(self, newEge):
        self.ege = newEge

    def getCI(self):
        return self.ci

    def setCI(self, newCI):
        self.ci = newCI

    def toString(self):
        return self.getName() +" "+ self.getLastName() +" "+ self.getEge() +" "+ self.getCI()