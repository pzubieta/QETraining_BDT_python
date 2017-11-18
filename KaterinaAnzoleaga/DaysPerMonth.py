month = "Diciembre"
while (month in ("Enero", "Marzo", "Mayo", "Julio", "Agosto", "Octubre", "Diciembre","Abril", "Junio", "Septiembre", "Noviembre", "Febrero")):
    month = input("Ingrese un mes del año: ")
    if month in ("Enero", "Marzo", "Mayo", "Julio", "Agosto", "Octubre", "Diciembre"):
        print ("El mes de ", month, "tine 31 dias")
    elif month in ("Abril", "Junio", "Septiembre", "Noviembre"):
        print ("El mes de ", month, "tine 30 dias")
    elif month in ("Febrero"):
        print ("El mes de ", month, "tine 28 dias")
else: print ("Mes no valido, intente este formato: 'Febrero'!")