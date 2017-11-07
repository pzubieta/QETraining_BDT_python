import calcular_edad
import you_are

def users1(num):
    usuarios={}
    nu=int(num)
    while(nu != 0):
        nombre =str(input("Ingrese su nombre:" ))
        edad =int(input("Ingrese su edad:"))
        usuarios[nombre]= edad
        calcular_edad.calcular_edad(edad)
        you_are.you_are(edad)
        nu -= nu


n = int(input("Ingrese el la cantidad de usuarios:"))
users1(n)