def replaceString_easy(strTest, strOld, strNew):
    #Replace an old string piece with a new in the given string strTest.
    print (strTest.replace(strOld, strNew))

def replaceString_hard(strTest, strOld, strNew):
    index = 0
    for ch in strTest:
        index = strTest.index(strOld)
        strTest.join(strNew)
        strTest.rstrip(strOld)

    print (strTest)

replaceString_easy("Easy Escuchar musica en casa es muy agradable", "ca", "que")
replaceString_hard("Hard Escuchar musica en casa es muy agradable", "ca", "que")