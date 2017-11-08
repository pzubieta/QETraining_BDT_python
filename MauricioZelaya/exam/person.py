class person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def get_full_name(self):
        return self.fname + " " + self.lname


# x = person("mau", "zel", 37, 1234)
# print(x.get_full_name())
