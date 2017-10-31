# Constantes
meses = {1:"enero",2:"febrero",3:"marzo",4:"abril",5:"mayo",6:"junio",7:"julio",8:"agosto",9:"septiembre",10:"octubre",11:"noviembre",12:"diciembre"}

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


value = input ("Por favor ingrese un valor: ")
if not value.isnumeric():
    print("No es un valor numerico")
else:
    par = function_par(float(value))
    print ('Es Par ?', par)

value = input ("Por favor ingrese un valor: ")
if not value.isnumeric():
    print("No es un valor numerico")
else:
    primo = function_primo(float(value))
    print ('Es Primo ', primo)

