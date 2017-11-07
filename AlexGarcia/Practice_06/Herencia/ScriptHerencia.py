from Person import Person
from Employee import Employee

primeraPersona = Person('Bob','Esponja',10,66656232)
segundaPersona = Person('Cumbiero','Terry',35,9638254)
terceraPersona = Employee('Ruber','Cuellar',29,62656135, 98745312,'BQE',)

print("*******************Persona******************************")
print(primeraPersona.mostrarInfo(),'persona con CI: ',primeraPersona.CI,' y ',primeraPersona.Age,'años de edad' )
print("*******************Employee******************************")
print(terceraPersona.getEmployee())
print(terceraPersona.infoEmployee())