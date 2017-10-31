#VARIABLES DE TEXTO CON Y SIN URL
text1 = "I am in https://google.com page in my browser"
text2 = "I am in google.com page in my browser"
text3 = "Yesterday I was browsing in many pages, like example the URL http://www.hotmail.es "

#FUNCION QUE IDENTIFICA 1 URL DE TIPO .COM
def find_url(text):
    position1=text.find("http")
    position2 = text.find(".com")
    url=text[position1:position2+4]

    if url:
        print("Existe una URL en el texto.")
        print("La URL es: ",url)
    else:
        print("No existe una URL en el texto.")


#FUNCION QUE IDENTIFICA 1 URL DE CUALQUIER EXTENSION
def find_url2(text):
    position1=text.find("http")
    partial_url = text[position1:]
    position2 = partial_url.find(" ")
    url=partial_url[:position2]

    if url:
        print("Existe una URL en el texto.")
        print("La URL es: ",url)
    else:
        print("No existe una URL en el texto.")

print("FUNCION 1 (Solo .COM):")
find_url(text3)
print("\n")
print("FUNCION 2 (Cualquier extension):")
find_url2(text3)
