#VARIABLES OPERATOR
#You can define more operators here
sumOperator="+"
minOperator="-"
multOperator="*"
divOperator="/"

#VARIABLE NUMBER
#You change the value of the numbers
#You cannot define more numbers since the function only uses 2 numbers
num1=12356
num2=78901

#FUNCTION TO HANDLE THE PROVIDED VARIABLES
#Here we receive only the 2 number and 1 operator

def function_3args(operator, number1, number2):
   if operator=="*":
       nameOperation="Multiplication"
       result=num1*num2
       print ("The operation is ",nameOperation," and the result is:",result)

   elif operator=="/":
        nameOperation="Division"
        result=num1/num2
        print ("The operation is ",nameOperation," and the result is:",result)

   elif operator=="+":
        nameOperation="Sum"
        result=num1+num2
        print ("The operation is ",nameOperation," and the result is:",result)

   elif operator=="-":
        nameOperation="Substraction"
        result=num1-num2
        print ("The operation is ",nameOperation," and the result is:",result)

   else:
       #If the operator is not any of existing ones, the operation will be unknown
        nameOperation="Unknown"
        print ("The operation is ",nameOperation," and it is not possible to calculate")

#USIGN THE FUNCTION WITH SPECIFIC VARIABLES
#You can provide and define other variables in order to have different results

function_3args(sumOperator, num1, num2)
