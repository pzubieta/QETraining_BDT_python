#Create a function that receive 3 arguments :
#	2 numbers
#	1 operations
#According the operation defined the expected result need to be printed.
# For example :  operator “*” , numbers: “5” “6”
#perform_operation(“*”,”5”,”6”) => 30

def perform_operation(op,first_number,second_number):
      if (first_number > second_number):
                 if op == "+":
                 #  + Addition
                     result = first_number + second_number
                     print(first_number, op, second_number, "=>", result),
                 elif op == "-":
                    #  - Subtraction
                     result = first_number-second_number
                     print(first_number, op, second_number, "=>", result),
                 elif op=="*":
                    #  * Multiplication
                     result = first_number * second_number
                     print(first_number, op, second_number, "=>", result),
                 elif op == "/":
                    #  Division
                     result = first_number/second_number
                     print(first_number, op, second_number, "=>", result)
                 elif op == "%":
                    #  % Modulus
                     result = first_number % second_number
                     print(first_number, op, second_number, "=>", result)
                 elif op == "^":
                    #  ** Exponent
                     result = second_number ** first_number
                     print(first_number, op, second_number, "=>", result)
                 elif op == "//":
                    #
                     result = first_number//second_number
                     print(first_number, op, second_number, "=>", result)
      else:
            print("the first value should be mayor")


perform_operation("+",8,4)
perform_operation("-", 8,4)
perform_operation("*", 8,4)
perform_operation("/", 8,4)
perform_operation("%", 8,4)
perform_operation("^", 8,4)
perform_operation("//", 8,4)

def perform_operation_option2(first_value, second_value):
    if (first_value>=second_value):
        op_list = ['add', 'sub', 'mult', 'div']
        for i in range(len(op_list)):
          if op_list[i] == 'add':
                result=(first_value+second_value)
                print(first_value,op_list[i],second_value,result)
          elif op_list[i] == 'sub':
                result = (second_value-first_value)
                print(first_value, op_list[i], second_value, result)
          elif op_list[i] == 'mult':
                result = (first_value * second_value)
                print(first_value, op_list[i], second_value, result)
          elif op_list[i] == 'div':
                result = (first_value / second_value)
                print(first_value, op_list[i], second_value, result)

perform_operation_option2(9,3)







