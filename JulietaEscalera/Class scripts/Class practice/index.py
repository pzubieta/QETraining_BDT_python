from Employee import *
from Persona import *


nombre= input("Escribe el nombre: ")
apellido= input("Escribe el apellido: ")

x= Person(nombre, apellido)
y= Employee("Homer", "Simson", "1007")
print(x.Name())
print(y.getEmployee())