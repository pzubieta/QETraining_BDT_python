class Person:
    def __init__(self,name, last_name):
        self.name_p = name
        self.last_name_p = last_name
    def getData(self):
        return self.name_p+" "+self.last_name_p
