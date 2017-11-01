def replace (text, old, new):
    text_withoutOld = text.split (old)
    print (text_withoutOld)
    text_withNew = new.join (text_withoutOld)
    print (text_withNew)


def cuentaPalabras (text):
    lista_palabras = text.split ()
    print (len(lista_palabras))


replace ("Mississippi", "i", "I")
cuentaPalabras(input ("Ingrese el texto: "))