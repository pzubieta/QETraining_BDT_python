import random

def verParImpar(cantidad):
    list = []
    for index in range(cantidad):
        list.append(random.randrange(100))

    for i in range(len(list)):
        if list[i]%2 == 0:
            print("Es Par: ", list[i])
        else:
            print("Es Impar: ", list[i])


verParImpar(100)
