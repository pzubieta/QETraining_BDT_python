# Constantes
meses = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]

# functions

"""Function to define if a given number is non"""
def function_par(value1):
    flag = False
    if value1 > 0 :
        if value1%2 == 0: flag = True
    return flag

"""Function to define if a given number is primo"""
def function_primo (value1):
    flag = True
    if value1 > 0:
        for i in range (2,value1):
            if value1%i == 0:
                flag = False
                i=value1
    return flag
"""Function to return the major between 2 numbers"""
def function_major(value1,value2):
    major = 0
    if (value1 != value2):
        if(value1 > value2):
            major = value1
        else:
            major=value2
        return major
    else:
        return major

"""Function task"""
def function_task(value1, value2):
    major = function_major(value1,value2)
    if major == 0 :
        print ("Both numbers are equals")
    else:
        flag_primo = function_primo (major)
        print ('Major is',major,' and is primus? ', flag_primo)
    print("Gracias")

print("======= SUMA DE NUMEROS MENOR A 35 ======")
def sum_to (n):
    sum = 0
    for i in range (n):
        sum = sum + i
        if (i > 36):
            break
    return sum
test_sum = sum_to(10)
print ('Suma ' , test_sum)


"""Function to return the days of a month"""
def function_months (month):
    days = 0
    if month == "enero" : days = 31
    elif month == "febrero": days = 28
    elif month == "Marzo": days = 31
    elif month == "Abril": days = 30
    elif month == "Mayo": days = 31
    elif month == "Junio": days = 30
    elif month == "Julio": days = 31
    elif month == "Agosto": days = 31
    elif month == "Septiembre": days = 30
    elif month == "Octubre": days = 31
    elif month == "Noviembre": days = 30
    elif month == "Diciembre": days = 31
    else: days = 0
    return days

#testing par
print("testing par")
par = input ("Ingrese un valor:")
if not par.isnumeric():
    print('No es un valor entero ', par)
else:
    result = function_par(int(par))
    print (par,' is par? ',result)

#testing major and primo
print ("testing major and primo")
num1 = input ("Ingrese un valor entero:")
num2 = input ("Ingrese un valor entero:")
if not num1.isnumeric() or not num2.isnumeric():
    print('Ambos valores deben ser numeros enteros ')
else:
    maj = function_major(int(num1),int(num2))
    prim = function_primo(int(maj))
    print (maj,' is primus? ',prim)

# testing function to return days of a month
print("testing function to return days of a month")
month = input ("Ingrese el nombre de un mes:")
if not month.isalpha():
    print('Nombre no valido :( ')
else:
    days = function_months(month)
    if days == 0 : print ("No valid month")
    else: print(month, ' has ',days, ' days ')



