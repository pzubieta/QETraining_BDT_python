# Tare de funciones con los operadores aritmeticos

def taskOperators(op,num1,num2):
    result = 0
    if op == "+":
        result = num1 + num2
    if op == "-":
        result = num1 - num2
    if op == "*":
        result = num1 * num2
    if op == "/":
        result = num1 / num2
    if op == "%":
        result = num1 % num2

    print(num1, "", op, "", num2, "=", result)

numero1 = int(input("Ingrese primer numero: "))
numero2 = int(input("Ingrese segundo numero: "))

taskOperators("+", numero1, numero2)
taskOperators("-", numero1, numero2)
taskOperators("*", numero1, numero2)
taskOperators("/", numero1, numero2)
taskOperators("%", numero1, numero2)