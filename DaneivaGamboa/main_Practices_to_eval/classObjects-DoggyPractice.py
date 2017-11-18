class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'


def __init__(self):
    self.data = []

#def self.method_name(self,argument):
#print("asd")

#def self.method_name(self,arg1=0,arg2=1):
#print("asd")


class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)                # unexpectedly shared by all dogs
['roll over', 'play dead']
