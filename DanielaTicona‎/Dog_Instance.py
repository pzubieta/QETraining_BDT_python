class Dog:


    def __init__(self, name):
        self.name = name
        self.tricks=[]
        self.roars=[]

    def add_trick(self,trick):
        self.tricks.append(trick)

    def add_roar(self,roar):
         self.roars.append(roar)

d=Dog('Fido')
e=Dog('Buddy')
d.add_roar('miau')
e.add_roar('guau')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.name,d.tricks,d.roars)
print(e.name,e.tricks, e.roars)