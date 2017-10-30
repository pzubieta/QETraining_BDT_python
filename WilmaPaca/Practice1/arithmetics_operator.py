
# practice_related to function with arithmetic operators

def perform_addition(a,b):
    return a + b
def perfom_multiplication(a,b):
    return a * b
def perform_division(a,b):
    return a/b
def perform_modulus(a,b):
    return a%b
def perform_substraction(a,b):
    return a-b
def perform_exponent(a,b):
    return a**b
def perform_floor_division(a,b):
    return a//b

def perform_operation(arithm_operator,number_one,number_two):
    if arithm_operator == '+':
        result=perform_addition(number_one,number_two)
    elif arithm_operator == '-':
        result = perform_substraction(number_one,number_two)
    elif arithm_operator == '*':
        result = perfom_multiplication(number_one,number_two)
    elif arithm_operator == '/':
        result = perform_division(number_one,number_two)
    elif arithm_operator == '%':
        result = perform_modulus(number_one,number_two)
    elif arithm_operator == '**':
        result = perform_exponent(number_one,number_two)
    elif arithm_operator == '//':
        result = perform_floor_division(number_one,number_two)
    else:
        result = None
        print("Operator is not correct!!")

    if result != None:
        print()
        print("---------- Arithmetic Operation -------------")
        print ("Operator: \"", arithm_operator, "\", numbers: \"%d\"  \"%d\"" %(number_one,number_two) )
        print (" %d %s %d = " %(number_one,arithm_operator,number_two), result)


arithmtic_operator = input('Enter operator: ')
number_one = float(input ("Enter the first number: "))
number_two = float(input ("Enter the second number: "))

perform_operation(arithmtic_operator,number_one,number_two)
