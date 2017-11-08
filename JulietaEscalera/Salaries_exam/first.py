from Employee import *
from Persona import *


nombre= input("Escribe el nombre: ")
apellido= input("Escribe el apellido: ")

x= Person(nombre, apellido)
y= Employee("Juan", "Perez", "Sales")
z= Employee("Jhon", "Adreus", "Factory")
print(x.Name())
print(y.getEmployee())