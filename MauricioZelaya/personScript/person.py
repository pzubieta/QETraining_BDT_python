class person:
    def __init__(self, fname, lname, age, ci):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.ci = ci

    def get_full_name(self):
        return self.fname + " " + self.lname


# x = person("mau", "zel", 37, 1234)
# print(x.get_full_name())
