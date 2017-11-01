nz =2
def h2 ():
    global nz
    #tess.turn(42)
    #tess.forw
    nz += 2

str = "Hola mundo enfermo"
size = len(str)
subscript = str[5]
extracted = str[2:7]
found = str.find("la ")
print ('Size', size)
print ('subscript', subscript)
print ('extracted', extracted)
print ('found', found)


# Practice
str = "Go to https://internal.softlayer.com and my"
str2 = "Go to print everything"

def searching ():
    global str
    targ="http"
    ini = 0
    fin = 0
    endurl=".com"
    if str.find(targ)>0 :
        ini = str.find(targ)
    if str.find(endurl):
        fin = str.find(endurl)+ len(endurl)
    if ini >0 and fin > 0 :
        print ('There is a url in text ', str[ini:fin])
    else:
        print ("There is not a url in text")

#searching()

def searching2(str):
    #global str
    targ="http"
    ini = 0
    fin = 0
    if str.find(targ)>0 :
        ini = str.find(targ)
        new_str = str[ini:len(str)]
        fin = new_str.find(' ')
        print('There is a url in text ', new_str[0:fin])
    else:
        print ("There is not a url in text")

#searching2(str)

def list_append(str): #terminar
    names = str.split(";",-1)
    print ('Array ', names)

#names = input("Ingreso los nombres:")
#list_append(names)

def list_join(str): #terminar
    names = str.split(";",-1)
    print ('Array ', names)
    new_names = names.join()
    print(names)

#names = input("Ingreso los nombres:")

def str_replacing(str): #terminar sin replace
    print('OLD text: \n', str)
    str.replace("np","mp")
    print('NEW text: \n', str)

names = input("Ingrese un texto:")
str_replacing(names)

