def comparison(num1,num2):
    if(type(num1)==type('a') or type(num2)==type('a') ):

      print('At least one of the value is an string', num1, "",type(num1),"", num2, "",type(num2))
      if (num1==num2):
        print("Are equals, ", num1, "==", num2)
      else:
           print("Are not iqual, " , num1, " != ", num2)
    else:

        if (num1==num2):
             print("Are equals, ", num1, "==", num2)
        elif (num1!=num2):
            a=num1
            b=num2
            print("Are not iqual, " , num1, " != ", num2)
            if (a>b):
                print("Left operand is greater than the value of right operand " , num1, " > ", num2)
            if (a<b):
                print("Left operand is less than the value of right operand " , num1, " < ", num2)

        if (num1>=num2):
            print("Left operand is greater than or equal to the value of right operand, " , num1, " >=", num2 )
        if (num1<=num2):
           print("Left operand is less than or equal to the value of right operand, " , num1, " <=", num2)
#Variables

num1=5
num2= 4

#num1= input("Insert a number:")
#num2= input("Insert a number:")
comparison(num1,num2)
