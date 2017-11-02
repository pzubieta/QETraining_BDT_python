def replace_text(text, oldText, newText):
    newString = ""
    for i in range(len(text)):
        if text[i] == oldText:
            newString += newText
        else:
            newString += text[i]
    return newString

cadena = "La programacion es muy bonito pero si no jala lo rompes el teclado y la PC gooooooool"
oldText = "o"
newText = "X"
print(replace_text(cadena, oldText, newText))
print(cadena.replace("o","@")) # Ejemplo del uso del metodo replace.