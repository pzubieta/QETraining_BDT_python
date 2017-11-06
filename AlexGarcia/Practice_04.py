print("************************encontrarURL*************************")
# Suppose any line of text can contain at most one url that starts with “http://” and ends at the next space in the line. Write a  fragment of code to extract and print the full url if it is present.
def encontrarURL():
    cadena = input("Introduce una cadena de texto:\n")
    # cadena="I am in https://www.youtube.com/watch?v=eUY4YMtSVYQ hello teacher"
    # print(cadena)

    encontrarHTTP = cadena.find("http")
    if encontrarHTTP == -1:
        print("NO hay URL")
    else:
        # print(encontrarHTTP)

        extraer1 = cadena[encontrarHTTP:]
        # print(extraer1)

        encontrarEspacio = extraer1.find(" ")
        # print(encontrarEspacio)

        URLes = extraer1[:encontrarEspacio]
        print("La URL es:\n", URLes)

encontrarURL()

print("*************************Remplazar***************************")
# Write a function replace(s, old, new) that replaces all occurrences of old with new in a string s:

cadena = input("Introduce una cadena de texto:\n")
# cadena="I am in https://www.youtube.com/watch?v=eUY4YMtSVYQ hello teacher"
old = input("Introduce el string que quiere cambiar:\n")
# old='e'
new = input("Introduce el string que replazara al amterior\n")


# new='E'

def remplazo(cadena, old, new):
    buscar = cadena.find(old)
    if buscar == -1:
        print('NO existe', old, 'en', cadena)
    else:
        print(cadena)
        nuevaCadena = cadena.replace(old, new)
        print(nuevaCadena)


remplazo(cadena, old, new)

print("************************Diccionarios********************************")

import operator


def LetraSolamente(s):
    global cadena
    soloLetras = "+-*/!@#$%^&*()_ +=-0987654321`~:[]}{'?><,./"
    s_sin_vocales = ""
    for letra in s:
        if letra not in soloLetras:
            s_sin_vocales += letra
    # print(s_sin_vocales)
    cadena = s_sin_vocales
    return cadena


# Write a program that reads a string and returns a table of the letters of the alphabet in alphabetical order which occur in the string together with the number of times each letter occurs.
cadena = input("Introduce una cadena de texto:\n")
# cadena="I am in https://www.youtube.com/watch?v=eUY4YMtSVYQ hello teacher"
# cadena="Banana"
cadena = LetraSolamente(cadena)  # remueve los caracteres que no son letras
longitud = len(cadena)
contadorDeCadena = 0
dict = {}

for i in cadena:
    contadorDos = 0
    # contadorDeCadena = 0

    for j in cadena:
        contadorDeCadena = contadorDeCadena + 1
        if i == j:
            contadorDos = contadorDos + 1
        if contadorDeCadena == longitud:
            print(i, ' = ', contadorDos)
            dict[i] = contadorDos
            contadorDeCadena = 0
            print('ya dio una ciclo')
            print(i)

resultado = sorted(dict.items(), key=operator.itemgetter(0))
print(resultado)

resultado = sorted(dict.items(), key=operator.itemgetter(1))
print(resultado)