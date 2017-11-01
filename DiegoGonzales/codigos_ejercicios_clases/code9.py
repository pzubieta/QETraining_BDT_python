
url = 'I am in the https://www.google.com/fotos/logo.png'
#url = 'I am in the web site demo'

ini = url.find('https')
fin = url.find('.com')

cadena = ""

for x in range(ini, fin+4):
    cadena += url[x]

print(cadena)

