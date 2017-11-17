import random



def verParImpar(limite):
    listNumbers = []
    for i in range(limite):
        listNumbers[i] = random.randrange(100)

    for j in listNumbers:
        if listNumbers[j]%2 == 0:
            print("Es par ", listNumbers[j])
        else:
            print("Es Impar ", listNumbers[j])

verParImpar(100)