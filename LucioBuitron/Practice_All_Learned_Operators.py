#VARIABLES STRING
variable1="Message text"
variable2="Alphanumerial message text 1234567890"

#VARIABLE INT
variable3=3
variable4=40
variable5=500
variable6=6000

#VARIABLE LIST
variable7=[10, 20, 30, 40]


#COMPARISION OPERATORS
#Equal
print("COMPARISION OPERATORS")
print("---------------------")
if variable3==variable4:
    print(variable3," is equal to ",variable4)
    print("Operator used: = =")
    print("\n")
else:
    print(variable3," is not equal to ",variable4)
    print("Operator used: = =")
    print("\n")

#Higher or equal than
if variable5>=variable6:
    print(variable5," is higher than ",variable6)
    print("Operator used: > =")
    print("\n")
else:
    print(variable5," is not higher than ",variable6)
    print("Operator used: > =")
    print("\n")
    print("\n")

#ASSIGNEMENT OPERATORS
#Add and
print("ASSIGNEMENT OPERATORS")
print("---------------------")
result1=variable3+variable4
variable3+=variable4
print("'Result' is equal to ",variable3," + ",variable4)
print("And 'Result' will be: ", result1," if we use '+=' as operator (Same than variable3 = variable3+ variable4)")
print("Operator used: +=")
print("\n")

#Modulus
result2=variable5%variable6
print("'Result' is equal to ",variable5," % ",variable6)
print("The modulus is: ",result2)
print("Operator used: %")
print("\n")
print("\n")

#MEMBERSHIP OPERATORS
print("MEMBERSHIP OPERATORS")
print("---------------------")
#In
if ( variable4 in variable7 ):
   print(variable4," exists in the list: ", variable7)
   print("Operator used: IN")
   print("\n")
else:
   print(variable4," doesn't exists in the list: ", variable7)
   print("Operator used: IN")
   print("\n")

#In Not
if ( variable3 not in variable7):
    print(variable3," doesn't exists in the list: ", variable7)
    print("Operator used: IN NOT")
    print("\n")
else:
    print(variable4," exists in the list: ", variable7)
    print("Operator used: IN NOT")
    print("\n")


#IDENTITY OPERATORS
print("IDENTITY OPERATORS")
print("-------------------")
#Is
if ( variable1 is variable2 ):
   print("'",variable1,"'"," and ", "'",variable2,"'", " has same identity")
   print("Operator used: IS")
   print("\n")
else:
   print("'",variable1,"'"," and ", "'",variable2,"'", " has not same identity")
   print("Operator used: IS")
   print("\n")

#Is Not
if ( variable1 is not variable2 ):
   print("'",variable1,"'"," and ", "'",variable2,"'", " has not same identity")
   print("Operator used: IS NOT")
   print("\n")
else:
   print("'",variable1,"'"," and ", "'",variable2,"'", " has same identity")
   print("Operator used: IS NOT")
   print("\n")
