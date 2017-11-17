from CalcularEImprimir import CalculoEdad, MensajesReferencialesDeEdad
import datetime

Users = dict()

Users = {
    "Casillas":"1990-09-05",
    "Ramos":"1995-09-05",
    "Pique":"2000-09-05",
    "Puyol":"2005-09-05",
    "Capdevila":"2010-09-05",
    "Xabi Alonso":"2015-09-05",
    "Busquets":"1985-09-05",
    "Xavi Hernandez":"1980-09-05",
    "Pedrito":"1975-09-05",
    "Iniesta":"1970-09-05",
    "Villa":"1965-09-05"
}


for k,v in Users.items():
    newFormat = datetime.datetime.strptime(v, '%Y-%m-%d').date()
    anios = int(newFormat.strftime("%Y"))
    mes = int(newFormat.strftime("%m"))
    dia = int(newFormat.strftime("%d"))
    Edad= CalculoEdad(anios,mes,dia)
    print(k,'tiene:',Edad,'años')
    print(k, 'tiene:', Edad * 365, 'dias')
    print(k, 'tiene:', Edad * 365 * 24, 'horas')
    print(k, 'tiene:', Edad * 365 * 24 * 60, 'segundos')
    MensajesReferencialesDeEdad(Edad)
    print("**************************")

print(Users)