
def findURL (text):
    i = text.find("http://")
    if i != -1:
        url = text[i:] # por ahora la URL se copia hasta el final
        j = url.find (" ") # la nueva url sera solo hasta el siguiente espacio
        url = url [:j]
        print (url)
    else: print("No hay una URL valida en el texto")


text = input("Ingrese el texto: ")
findURL (text)