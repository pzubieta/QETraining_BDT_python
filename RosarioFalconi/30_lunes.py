count = 0
while count < 5 :
    count +=1
    print ("imprime")
else :
    print("no imprime")
print("=============")
flag =1
while (flag) :
    print ('Given flag is really true')
    flag=0
else: print('nose')
print("Good ...")
print("=============")
list1 = [2,5,10,15,20,25,27]
print("Tamano lista ", len (list1))
for number in list1 :
    if (number%5 == 0):
        print ('Number %number es multiplo de 5')
    else:
        print('Number &number no es multiplo de 5 ', number)
print("=============")
print ('un\nombre')
print (r'un\nombre')
print("=============")
genre = ['a','b','z']
for i in range (len(genre)):
    print ('This is '+ genre[i])
    genre.append(' hola ')
print("=============")
for i in range (len(genre)):
    print ('This is '+ genre[i])
print("=============")
array = []
cadena = "Este es un texto de prueba"
array = cadena.split(" ",-1)
print("array ", len(array))
print(array)
print("=============")
for val in "string":
    if val == "i":
        break
    print("Val ", val)
print("====== BREAK =======")
val=20
while val > 0 :
    print("Value ",val)
    val -=1
    if val == 15 :
        print("Break")
        break
print("======= CONTINUE ======")
while val > 0 :
    print("Value ",val)
    val -=1
    if val < 15 :
        continue
        print("Continue")
print("======= PASS ======")
for val in array :
    pass
print("======= PASS ======")

print("======= AREA DE UN CIRCULO ======")
def area_of_circle (radio):
    if (radio > 10):
        area = (radio*3.14)**2
        print ("Area ",area)
    else:
        print ("Radio es menor a 10, radio = ",radio)
area_of_circle(50)
area_of_circle(5)
print("======= AREA DE UN CIRCULO ======")

print("======= SUMA DE NUMEROS MENOR A 35 ======")
def sum_to (n):
    sum = 0
    for i in range (n):
        sum += i
        print ('sum ',sum)
        if (i > 35):
            print ('i ', i)
            break
    return sum
test_sum = sum_to(10)
print ('Suma ' , test_sum)
