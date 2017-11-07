class Person:
    def __init__(self,name, last_name,age,ci):
        self.name_p = name
        self.last_name_p = last_name
        self.age_p = age
        self.ci_p = ci
    def get_dataPerson(self):
        return self.name_p+" "+self.last_name_p+" "+self.age_p+" "+self.ci_p
    def get_ci(self):
        return self.ci_p
    def get_age(self):
        return self.age_p