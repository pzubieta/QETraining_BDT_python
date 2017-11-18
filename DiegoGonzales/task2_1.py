def mayorNumero(num1, num2, num3):
    if num1 >= num2 and num2 >= num3:
        print('El mayor de {0}, {1}, {2}'.format(num1, num2, num3),' es: ', num1)
    elif num2 >= num1 and num2 >= num3:
        print('El mayor de {0}, {1}, {2}'.format(num1, num2, num3), ' es: ', num2)
    else:
        print('El mayor de {0}, {1}, {2}'.format(num1, num2, num3), ' es: ', num3)


def menorNumero(num1, num2, num3):
    if num1 <= num2 and num2 <= num3:
        print('El menor de {0}, {1}, {2}'.format(num1, num2, num3),' es: ', num1)
    elif num2 <= num1 and num2 <= num3:
        print('El menor de {0}, {1}, {2}'.format(num1, num2, num3), ' es: ', num2)
    else:
        print('El menor de {0}, {1}, {2}'.format(num1, num2, num3), ' es: ', num3)


numero1 = int(input("Introducir numero1: "))
numero2 = int(input("Introducir numero1: "))
numero3 = int(input("Introducir numero1: "))

mayorNumero(numero1, numero2, numero3)
menorNumero(numero1, numero2, numero3)