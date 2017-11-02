
def days_in_month(mes):
    listMes = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    listDias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for indice in range(len(listMes)):
        if listMes[indice] == mes:
            print("El mes: ", listMes[indice], " tiene total dias: ", listDias[indice])

days_in_month("Marzo")