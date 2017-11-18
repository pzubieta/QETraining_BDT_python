def isPrime (n):
    n=int(n)
    if n==1 or n==0: return (False)
    else:
        for i in range (2,n-1):
            if n%i==0:
                return (False)
                break
        else: return (True)

a=int(input("Ingrese el primer número del rango: "))
b=int(input("Ingrese el último número del rango: "))
lista = []
for i in range (a, b+1):
    if (isPrime(i)): lista.append(i)
print (lista)
