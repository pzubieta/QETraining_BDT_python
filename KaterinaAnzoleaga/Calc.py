def calc(a, b, operator):
    if operator == '+':
        return (a + b)
    elif operator == '-':
        return (a - b)
    elif operator == '*':
        return (a * b)
    elif operator == '/':
        if b != 0:
            return (a / b)
        else:
            return ('Canot divide by zero!!!')
    elif operator == '%':
        return (a % b)
    elif operator == '**':
        return (a ** b)
    elif operator == '//':
        return (a // b)
    else:
        return ('Operador no valido')


def operator(symbol):
    if symbol == '+':
        return ('suma')
    elif symbol == '-':
        return ('resta')
    elif symbol == '*':
        return ('multiplicacion')
    elif symbol == '/':
        return ('division')
    elif symbol == '%':
        return ('modulo')
    elif symbol == '**':
        return ('exponente')


try:
    num_a = float(input('Introduce el valor de a: '))
except:
    print
    "Ingresa un numero!"
    sys.exit(1)

try:
    num_b = float(input('Introduce el valor de B: '))
except:
    print
    "Ingresa un numero!"
    sys.exit(1)

symbol = input('Introduce el operador (+,-,*,/,%,//,**): ')

operator = operator(str(symbol))
print (operator)
if operator not in ('modulo', 'exponente'):
    print ("La ", operator, "de ", num_a, "y ", num_b, "es: ", calc(num_a, num_b, symbol))
else:
    print ("El ", operator, "de ", num_a, "y ", num_b, "es: ", calc(num_a, num_b, symbol))

