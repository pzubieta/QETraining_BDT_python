class Dog:
    #tricks = [] ==> variable de clase public

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog("Fido")
e = Dog("Buddy")

d.add_trick("rolll over")
e.add_trick("play dead")

print(d.tricks)
print(e.tricks)

#variables
# * locales: Alcance mas corto
# * Instancia; Vive dentro de una clase y se puede compartir entre los metodos self.myvariable
# * Clase: pemrite comparar la variable entra clases
# * Global:

# SOLID ---> leer