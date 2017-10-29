def numeroEsParImpar(numero):
    if(numero%2 == 0):
        result = "Numero es par: ", numero
    else:
        result = "Numero es impar: ", numero
    return result

num = int(input("Ingrese numero: "))

print(numeroEsParImpar(num))