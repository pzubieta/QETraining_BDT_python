# Constantes
meses = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]

# functions

print("\n=============Function to define if a given number is non=========")
def function_par(value1):
    flag = False
    value1 = int(value1)
    if value1 > 0 :
        if value1%2 == 0:
            flag = True
    print (value1,'  is par? ',flag)

function_par(101)
function_par(220)

print ("\n===========Function to return the days of a month============")
def function_months (month):
    days = 0
    if not month.isalpha():
        print('Nombre no valido :( ')
    else:

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
    if days > 0 : print ('Month ',month, ' has ',days, ' days')
    else: print('No valid month ', month)
function_months("enero")
function_months("mio")

print("======= SUMA DE NUMEROS MENOR A 35 ======")
def sum_to (n):
    sum = 0
    i = 0
    for i in range (n):
        i +=1
        sum = sum + i
        if (i < 36):
            continue
    return sum
test_sum = sum_to(10)
print ('Suma ' , test_sum)

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

print("\n=============== Function to define the major and if it is primus ===============")
def function_task(value1, value2):
    major = function_major(value1,value2)
    flag_primo = True
    if major is 0 :
        print ("Both numbers are equals")
    else:
        flag_primo = function_primo (major)
        print ('Major is',major,' and is primus? ', flag_primo)

function_task(55,101)
function_task(11,11)
function_task(50,23)



