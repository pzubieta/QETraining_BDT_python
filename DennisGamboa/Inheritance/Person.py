class Person:

    def __init__(self, first, last, age, ci):
        self.first_name = first
        self.last_name = last
        self.ages = age
        self.cis = ci

    def Name(self):
        return self.first_name + " " + self.last_name + " " + self.ages + " " + self.cis