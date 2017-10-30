def print_type(value_1):
    """ This function is to print all operations and recognizes if the data type of the given variable"""

    if type(value_1) is int:
        print("Variable value_1 is a: Integer")
    elif type(value_1) is str:
        print("Variable value_1 is a: String")
    elif type(value_1) is list:
        print("Variable value_1 is a: List")

def do_operations(value_1, value_2, strValue_3,  value_4):

    #This is de function to perform and print aritmethic operations from a given value, a list, an operator and a position on the list.

    print("Var1: ", value_1, strValue_3)

    for val_in in value_2:
        print("Var2 Values: ", val_in)

    print("Operations results:")
    print("Sum: ",value_1, " + ", val_in," = ",  value_1 + value_2[0])
    print("Sub: ",value_1, " + ", val_in," = ", value_1 - value_2[1])
    print("Mul: ",value_1, " * ", val_in," = ", value_1 * value_2[2])
    print("Div: ",value_1, " / ", val_in," = ", value_1 / value_2[3])
    print("Flo: ",value_1, " // ", val_in," = ", value_1 // value_2[4])
    print("Mod: ",value_1, " % ", val_in," = ", value_1 % value_2[5])
    print("Pow: ",value_1, " ** ", val_in," = ", value_1 ** value_2[6])

    if strValue_3 == "+":
        print("The required operation is Sum: %s" % (value_1), " + ", value_2[value_4], " = ", value_1 + value_2[value_4])
    elif strValue_3 == "-":
        print("The required operation is Substraction: %s" % (value_1), " - ", value_2[value_4], " = ", value_1 - value_2[value_4])
    elif strValue_3 == "*":
        print("The required operation is Multiplication: %s" % (value_1), " * ", value_2[value_4], " = ", value_1 * value_2[value_4])
    elif strValue_3 == "/":
        print("The required operation is Division: %s" % (value_1), " / ", value_2[value_4], " = ", value_1 / value_2[value_4])
    elif strValue_3 == "//":
        print("The required operation is Floor Division: %s" % (value_1), value_1, " // ", value_2[value_4], " = ", value_1 // value_2[value_4])
    elif strValue_3 == "%":
        print("The required operation is Modulus: %s" % (value_1), " % ", value_2[value_4], " = ", value_1 % value_2[value_4])
    elif strValue_3 == "**":
        print("The required operation is Power: %s" % (value_1), " ** ", value_2[value_4], " = ", value_1 ** value_2[value_4])

print_type(["test", "Dog", "cat", "test2"])
do_operations(5, [20, 9, 0, 4, 7, 9, 14], "+", 0)
