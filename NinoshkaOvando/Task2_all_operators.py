##########################################################
#Comparison Operators
#==
a=1
if(a==1): print("a is equal than 1")
#!=
a=4
if(a!=1): print("a is different than 1")
#>
a=4
if(a>1): print("a is major than 1")
#<
a=0
if(a<1): print("a is minor than 1")
#>=
a=1
if(a>=1): print("a is major or equal than 1")
#<=
a=1
if(a<=1): print("a is minor or equal than 1")
##########################################################
#Assignement Operator
a = 7
b = 3
c = 0
print("a is ", a)
print("b is ", b)
c = a + b
print("Result- Value of c = a + b is ", c)
c += a
print("Result- Value of c += a is ", c)
c *= a
print("Result- Value of c *= a is ", c)
c /= a
print("Result- Value of c /= a is ", c)
c %= a
print("Result- Value of c %= a is ", c)
c **= a
print("Result- Value of c **= a is ", c)
c //= a
print("Result- Value of c //= a is ", c)
##########################################################
#Identity Operators
a1 = 345
b1 = 345
a2 = 'Ninoshka'
b2 = 'Ninoshka'
a3 = [1,2,3]
b3 = [1,2,3]
print("Example is not")
print(a1 is not b1)
print("Example is ")
print(a2 is b2)
print("Example is ")
print(a3 is a3)
##########################################################
#Membership operators
word = 'Hello world'
print("Example is ")
print('w' in word)
print("Example is not")
print('hello' not in word)

print("in operator")
lst1 = ['Alejandra', 'Adrian','Tony', 'Mary', 'Ana', 'Vera','Alex', 'Christopher']
if 'Alex' in lst1: print('Name Alex exists in lst1')
print("not in operator")
if 'William' not in lst1: print ('Name William does not exists in lst1')