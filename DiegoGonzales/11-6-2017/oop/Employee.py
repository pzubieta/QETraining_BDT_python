from oop.Person import Person

class Employee(Person):

    def __init__(self, name, lastName, ege, ci, id, departament):
        super().__init__(name, lastName, ege, ci)
        self.id = id
        self.departament = departament

    def getID(self):
        return self.id

    def setID(self, newID):
        self.id = newID

    def getDepartament(self):
        return self.departament

    def setDepartament(self, newDepartament):
        self.departament = newDepartament

    def toEmployeeString(self):
        return self.getName() +" "+ self.getLastName() +" "+ self.getEge() +" "+ self.getCI() +" "+ self.getID() +" "+ self.getDepartament()

    def toEmpString(self):
        return self.getID() +" "+ self.getDepartament()