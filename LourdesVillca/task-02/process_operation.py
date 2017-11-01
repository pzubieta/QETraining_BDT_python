def process_arithmetic_op(operator, number1, number2):
    """
    Method to process the given arithmetic operation.

    :param operator:    string  represents the operator to be calculated
    :param number1:     int     number to be used in the operation
    :param number2:     int     number to be used in the operation
    """
    string_to_eval = '{} {} {}'.format(str(number1),operator,str(number2))
    operators_options = ['+', '-', '*', '/', '%']
    if operator in operators_options:
        print("{} = {}".format(string_to_eval,eval(string_to_eval)))
    else:
        print("Operator is not defined")

process_arithmetic_op("*", 9, 10)
