#Comparison operators
intNumber00=3
intNumber01=5

strName00="String1"
strName01="String1"

print (intNumber00 == intNumber01)
print (strName00 == strName01)

#Assignments operators
# c+=a is equivalent to c = c + a
#Membership operators (operadores de pertenencia)
#in
#not in

a=1
b=2

list = [1,2,3,4,5]

if(a in list):
    print("a exists list")
else:
    print("a does not exist list")

if(b not in list):
    print("b does not exist list")
else:
    print("b exists list")


#identity operators
#is
#is not

value_1 = 20
value_2 = 20

if(value_1 is value_2):
    print("line 1 - a and b have same identity")
else:
    print("line 1 - a and b do not have have same identity")

if(id(value_1) == id(value_2)):
    print("line 2 - a and b have same identity")
else:
    print("line 2 - a and b do not have have same identity")

print (id(value_1))
print (id(value_2))
