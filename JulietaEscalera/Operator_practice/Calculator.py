def calculator(op,num1,num2):
    if (op=='+'):
        result=num1+num2
        print("The operation is Addition, " , num1, " + ", num2, " = ", result)
    elif (op=='-'):
        result=num1-num2
        print("The operation is Subtraction, " , num1, " - ", num2, " = ", result)
    elif (op=='*'):
        result=num1*num2
        print("The operation is Multiplication, " , num1, " * ", num2, " = ", result)
    elif op == '/':
        if (num2==0):
           print("It is not possible the division of 0")
        else:
         result= num1/num2
         print("The operation is Division, " , num1, " / ", num2, " = ", result)
    elif (op=='%'):
        result=num1%num2
        print("The operation is Modulus, " , num1, " % ", num2, " = ", result)
    elif (op=='//'):
        result=num1//num2
        print("The operation is Floor Division, " , num1, " // ", num2, " = ", result)
    elif (op=='**'):
        result=num1**num2
        print("The operation is Exponential, " , num1, " ** ", num2, " = ", result)
    else:
        print('The operator is not valid, please try again, operator examples: (+,-,*,/,%,//,**)')

#Variables
op = "**"
num1=4
num2=2

#op = raw_input ('Insert the operator : ')
#num1= input("Insert a number: ")
#num2= input("Insert a number: ")

calculator(op,num1,num2)


