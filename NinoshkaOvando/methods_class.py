#len(str) length of string
##str[i]
# string_a=ring
#ring[i]  --> rng
###############################################v
#str[i:j]
#    0:3  ---> sub string "a, b, c, d, e, f"  is "def"
#str[:5]  --> ini to the end
###################################################v
# index , encontrar un patron en una cadena
#a="anhwhere"
#str.find("wh") ---> return the index
#####################################################
def search_url(text_example):
    result=""
    index_aux= text_example.find("http://")
    print("index_aux find:  ", index_aux)
    if (index_aux == -1 ):
        index_aux = text_example.find("https://")
        print("index:  ",index_aux)
    if(index_aux!= 0):
        result =text_example[index_aux:len(text_example)]
        print("substring:  ", result)
    cont=0
    result_url=""
    while(cont <len(text_example)):
        if(result[cont] == " "):
            return result_url
        else:
             result_url+= result[cont]
        cont+=1
    return None

def main():
    text_example = " I am in https://github.com where it is a page"
    text_example2 = " It is other example http://www.codedrinks.com/sucesion-fibonacci-en-python/ with one http"
    print("Example 1: ", text_example)
    print(search_url(text_example))
    print("Example 2: ", text_example2)
    print(search_url(text_example2))
main()


###### append(n):::::add argument to the end
a={1,2, 3}
#Append(4) inserta dynamicamente
#{1,2,3,4}
###### insert(position, value):::::add argument to the end
a={1,2, 3}
#Append(1,4) inserta dynamicamente
#{4,1,2,3}
###### count(vaue):::::
###### extend(vaue):::::
#b=[a,b]
#a={1,2, 3}
#a.append(1,b) inserta dynamicamente
#{1,2,3, [a,b]}
#a.extend(1,b)
#{1,2,3, a, b}

###### reverse(vaue):::::
###### delete(vaue):::::
###### split(vaue):::::
#song_a="sdsfd dfd fsd sd df fgfg gfgff"
#words=song_a.split()
#print(words)
#words1=song_a.split("ai")  busca ai y cuerta antes y despues de este

# join  :::::::::::;;;;  vuelve una cadena donde a;adimos un parametro
#  determinado remplazado el scpacio

# practica, hacer un remplase TASK
#remplace (word, old, new)
# remplace(Misisipi, "i', I) == > MIsIssIppI
####################################################33
#dictionarios o hashes
#a=[1, 2, 3]  array ------elemento e indice------- extructura de datos
#diccionario
#a={value:1, code: 3434, deparment: "jhon"} --->  key es unico: value
#assigna un valor que va estar relacionado
dict={}
dict['one'] = "this is one"
dict[2]="this is two"
tinydict={'name':'john','code':34343,'dept':"sales" }
print(dict ['one'])
print(dict [2])
print(tinydict.keys())
print(tinydict.values())

########Task 2
# script que lear un string i que muestre las ocurrencuas de cada letra
# use list

#def occurences_of_word(word.lower()):
#    return None


