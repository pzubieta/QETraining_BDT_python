#print("****************calcular edad en dias minutos y segundo*****************")
from datetime import datetime, date, time, timedelta

def CalculoEdad(anio, mes, dia):
    #anio = int(input('insertar Año:\n'))
    #mes = int(input('insertar Mes:\n'))
    #dia = int(input('insertar Dia:\n'))

    # Asigna datetime de la fecha actual
    fechaActual = datetime.today()
    # Asigna datetime específica
    fechaNacimineto = datetime(anio, mes, dia)
    diferencia = fechaActual - fechaNacimineto
    EdadAnios = diferencia.days // 365
    #print("fechaActual:", fechaActual)
    #print("fechaNacimineto:", fechaNacimineto)
    #print("Hay una diferencia de:", diferencia)
    #print("Tienes", EdadAnios, " años")
    return (EdadAnios)

#print(CalculoEdad(2005,9,9))


#print("*********************MensajesReferencialesDeEdad*******************")

def MensajesReferencialesDeEdad(edad: object) -> object:

    if edad<=12:
        print("He is a child")
    elif edad<=17:
        print("He is a teenager")
    elif edad<=29:
        print("He is a young")
    else:
        print("He is an adult")


#MensajesReferencialesDeEdad(30)
