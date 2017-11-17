# While loop
# while expression:
#     statements

count =0
while(count <9):
    print("the count is :" , count)
    count= count + 1
else:  # si la condicion no se cumple
    print("good bye")

#==========================================
flag =0
while (flag): print("it is true")
else: print("good bye else")
print("next good bye")
#==========================================
# For loop
# For iterating_var in sequence:
#     statements(s)

#example1
numbers=[6,7,8,9,3,4,5,6,73,2,4,]
sum=0
for val in numbers:
    sum = sum +val
print("te sum is :" ,sum)
#example2
def print_list():
    """ document print_list"""
    list1 = [1, 2, 3, 4, 5]
    a=""
    i= 1
    sum =0
    for i in list1:
        sum+= i
    return sum
print("function for is",print_list())
#example3
def print_list_integer():
    """ document print_list"""
    ranges = range(10)
    a=""
    i= 1
    sum =0
    for i in ranges:
        sum+= i
    return sum
print("function for is",print_list_integer())
#example4 with index ---> iterate over the list using index
def print_list_index():
    """ document print_list"""
    granges = ["pop","rock","jazz"]
    for i in range(len(granges)):
        print("I don't like", granges[i])
    return "End function"
print("function for is",print_list_index())
########### ########### ########### ########### ###########
########### TASK create script
#1 determinar si un par o impar entrada
# dentro un minimo y un rango, determinar si el numero es o no primo e imprimirlo
#range(10, 20)
#for y while  ---->
########### ########### ########### ########### ########### ###########
# break --- no es bueno utilizarlo porque crea codigo muerto
# continue  ---- es como un skip de las siguientes lineas y continua con la verificacion
for var in "string":
    if (val == "i"):
        continue
    print("break for",val)
print("end")
# ejample
val =20
while val > 0:
    print("current value", val, "break while")
    val -= 1
    if(val== 5):
        print("continue start")
        continue   # encontrar una condicional  para hacer
        print("continue")
print("good bye")

########### ########### ########### ########### ########### ###########
# pass statement similar TODO como un skip
sequence = {"p","a","s","f"}
for val in sequence:
    pass
print("past")
########### ########### ########### ########### ########### ###########
# Ejercicios
#1. write a fuction area_of_circle(r) which returns the area of a circle of radius R only
#the radius value is greater than 10
# a= pi*r2

def area_of_cicle(r):
    pi= 3.141516
    if (type(r)== int):
        if(r>10):
            value= pi*(r*r)
            print("The radius is", value)
        else:
            print("Radius is less than 10")
    else:
        print("Enter a integer")
area_of_cicle(8)
area_of_cicle(15)
# Ejercicios
#2. white a function sum_to(n) that returns the sum of all integer numbers up to and
# including only ntil any vaue lower than 35

def sum_to(n):
    sum =0
    start=1
#    while(sum ):
#sumar la cantidad de valore de acuerdo al imput de la funcion
#sumar hasta n
#sum de todos los numemeros hasta 35  como limite
#if n=40 , sumar de 1+2+3 ... +35 y no hasta 40

#takes the name of a month, and returnsthe

# Ejercicios
# 3. funcion day_in_month
#    entrada el mes
#day_in_month("february")==28
#day_in_month("december")==31
#if it is invalid argument return None
#use    range, elif
# Ejercicios
# 3.