def showMultipleDistintoPares(cantidad, multiple):
    cont = 0
    lista = []
    while cont <= cantidad:
        if (cont % multiple) == 0:
            if cont % 2 != 0:
                print(cont)
        cont = cont + 1

showMultipleDistintoPares(100, 3)