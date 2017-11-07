class Dog:

       #tricks = []     #Variable de clase, trabaja sobre todas las insancias de la clase
        genTricks = []  #Variable de clase, trabaja sobre todas las insancias de la clase
        def __init__(self, name):
            self.name = name
            self.tricks = [] # This line turns a variable from Class Var to Instance Var

        def add_trick(self, trick):
            self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')

d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
print(e.tricks)

e.genTricks.append('playDead')
d.genTricks.append('rollOver')
print(e.genTricks)
print(d.genTricks)