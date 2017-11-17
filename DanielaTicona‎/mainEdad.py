from Age import agetype
from calcularEdad import Edad_days
Int_numUsr= int(input("introduzca la cantidad de usuarios:"))
tip=Int_numUsr
count=0

print("\n")
listUsr={}
#INTRODUCE USUARIOS
while count< Int_numUsr:
    print count
    name=raw_input("introduzca el nombre usario:")
    listUsr[count] = name
    age=int(input("introduzca la edad de usuario:"))
    listUsr[name]= age
    count=count+1
print("\n")

#print (listUsr.keys(),listUsr.values())

for i in listUsr:
  print "Calculando la edad del usario: ",i
  Edad_days(listUsr[i])
  agetype(listUsr[i])
  print "sdasfsf",listUsr[i]
print("\n")







