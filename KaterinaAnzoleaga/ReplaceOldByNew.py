def replace (text, old, new):
    """This function replaces in text all occurrence of 'old' by 'new'"""
    text_withoutOld = text.split (old)
    text_withNew = new.join (text_withoutOld)
    return (text_withNew)

def cuentaPalabras (text):
    lista_palabras = text.split ()
    return (len(lista_palabras))

text = input ("Ingrese un texto: ")
old = input ("Ingrese la parte que quiere remplazar: ")
new = input ("Ingrese el valor nuevo: ")
newText = replace (text, old, new)
print  ("The result replacing ", old,"by ", "new, is: ", newText)
print ("El numero de palabras en el texto es :", cuentaPalabras(text))
