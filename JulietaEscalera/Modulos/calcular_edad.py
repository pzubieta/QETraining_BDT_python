import math

def calcular_edad(edad):
    if int(edad != 0):
        edad_minutos=edad*365*60*24
        edad_horas=edad*365*24
        edad_dias=edad*365

        print("Tu edad en minutos es:",edad_minutos )
        print("Tu edad en horas es:", edad_horas)
        print("Tu edad en dias es:", edad_dias)
