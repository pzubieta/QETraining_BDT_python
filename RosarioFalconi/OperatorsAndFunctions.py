var1=100
var2=50
var3="Texto prueba"
var4=""
var5=[0,10,20,30,40,50,60,70,80,90]
var6=["a","b","c","d","e","f"]

"""Perform operation function"""
def task1(action, value1,value2):
    result = 0
    if action == "+": result = value1 + value2
    elif action == "-": result = value1 - value2
    elif action == "*": result = value1 * value2
    elif action == "/": result = value1 / value2
    elif action == "%": result = value1 % value2
    elif action == "//": result = value1 // value2
    elif action == "**": result = value1 ** value2
    else: result = "No valid action. Please enter a valid arithmetic operator"
    return result

test_task1 = task1 ("+", var1,var2)
print ("Addition: ",test_task1)
test_task1 = task1 ("-", var1,var2)
print ("Substraction ", test_task1)
test_task1 = task1 ("*", var1,var2)
print ("Multiplication ", test_task1)
test_task1 = task1 ("/", var1,var2)
print ("Division ", test_task1)
test_task1 = task1 ("%", var1,var2)
print ("Module ", test_task1)
test_task1 = task1 ("**", var1,var2)
print ("Power ", test_task1)

"""Fucntin using assignments, membership and identity operators"""
def square():
    multiplos = []
    for i in range (5):
        multiplos.append(i**2)
    print ("Multiplos de 2 ", multiplos)
    return multiplos

def task2 (lista):
    lista2= []
    result=0
    for valor in lista:
        if valor == 0 :
            print ("Nothing to do on first if valor == 0, NEXT")
        elif valor >  50 :
            print ("elif valor > 51")
            result += 3
            if "a" in var6 :
                var6.remove("a")
                print ("if a in var6 remove a from var6")
        else:
            print ("else")
            result -= 10
            print("result -=10")
            lista2 = square()
        print("Valor ", valor)
    print("Hola")
task2(var5)