# Function
# scope: Sum, Subtraction, Multiplication, Division

def validation_number(number):
    if (type(number) == str):
        print("string")
        return -1
    elif(type(number) == int):
        if ( number>=0):
            return int(number)
        else:
            return -1
    else:
        return -1

def valitation_operator(operator_aux):
    if(type(operator_aux)==  str):
        if (operator_aux == "+" or operator_aux == "1"): return 1
        elif(operator_aux == "-" or operator_aux == "2"): return 2
        elif (operator_aux == "*" or operator_aux == "3"): return 3
        elif (operator_aux == "/"or operator_aux == "4"): return 4
        else: return 0
    elif(type(operator_aux)==  int):
        if (operator_aux == 1): return 1
        elif(operator_aux == 2): return 2
        elif (operator_aux == 3): return 3
        elif (operator_aux == 4): return 4
        else: return 0
    else: return 0

def test_valitation_operator():
    test_str = valitation_operator("+")
    print(test_str)
    test_str = valitation_operator("-")
    print(test_str)
    test_str = valitation_operator("*")
    print(test_str)
    test_str = valitation_operator("/")
    print(test_str)




def run_operation( operation_t, a, b):
    # Validation
    operator_function = valitation_operator(operation_t)
    num_b = validation_number(b)
    num_a = validation_number(a)
    if (operator_function == 0):
        print("Operator is not supported or it is incorrect: ")
    elif (num_a == -1):
        print("Invalid input. Enter an integer: ", num_a)
    elif (num_b == -1):
        print("Invalid input. Enter an integer: ", num_b)
    else:
        result=0
        operation_str = ""
        if(operator_function == 1):
            result=num_a+num_b
            operation_str = "Sum"
        elif(operator_function == 2):
            result = num_a-num_b
            operation_str = "Subtraction"
        elif (operator_function == 3):
            result = num_a*num_b
            operation_str = "Multiplication"
        elif (operator_function == 4):
            if(b != 0):
                result = num_a/num_b
                operation_str = "Division"
            else:
                operation_str = "Division"
                print('There is an error on {} of {} and {} .'.format(operation_str,num_a, num_b), "Second number should not be zero when a division is executed")
        else:
            print("It is not possible to run your operation. Please, start again.")
    sentence = 'The {} of {} and {} is {}.'.format(operation_str,num_a, num_b, result)
    print(sentence)


def test_run_operation():
    a=3
    b=4
    run_operation("+", a, b)
    run_operation("-", a, b)
    run_operation("*", a, b)
    run_operation("/", a, b)
    run_operation("/", 5, 0)

def main():
    # Input
    print("Welcome to Run Operation")
    test_run_operation()
    print("To start, you can input an operator:")
    print("Sum: Enter 1 or +")
    print("Subtraction: Enter 2  or -")
    print("Multiplication: Enter 3 or *")
    print("Division: Enter 4 or /")
    operator = input("Enter an operator: ")
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))
    run_operation(operator, a, b)

main()
