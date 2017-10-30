#inclusion
a=1
b=2
c=3
d=7

list =[1,2,3,4,5]
str1= "vive"
str2 = "ama"
str3= "rie"

list_s = ["vive", "ama","rie"]

if (a in list):
    print("a exists list is ",a)
else:
    print("a does not exists list")



if (b  not in list):
    print("b does not exists list")
else:
    print("b exists list is",b)

if (str1 in list):
    print("str1 does not exists list")
else:
    print("str1 exists list")

#other examples

if (a in list):
    print("a exists list")
    c+=a
    print ("c=c+a:",c)
else:
    print("a does not exists list")
    c-= a
    print("c=c-a:",c)

# Identity

value_1=20
value_2=20

if (value_1 is value_2):
    print("Line 1 -a and b have same identity")
else:
    print("Line 1 -a and b do not have same identity")

if (id(value_1) == id(value_2)):
        print("Line 2 -a and b have same identity")
else:
        print("Line 2 -a and b do not have same identity")

# function

def print_lyrics():
    print("I'm a tester and I'm okay")
    print("I sleep all night and I work all day")
print_lyrics()



def test(a,b):
    sum5=a+b
    return sum5

sumando=test(a,b)
print(sumando)


