def findUrl(pathUrl):
    #Finds a URL in a string and extracts it printing it.

    inicio = pathUrl.find("http")
    urlString = pathUrl[inicio:]

    fin = urlString.find(" ")

    urlString = urlString[:fin]

    print (urlString)

findUrl("La pagina es http://pythontest.com fedrtgherth")