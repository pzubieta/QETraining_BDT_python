value_1 = 20
value_2 = 20



if (value_1 is value_2):
    print ("Line 1 - a and b have same identity")
else:
    print("Line 1 - a and b do not have same identity")

if ( id(value_1) == id(value_2)):
    print("Line 2 - a and b have same identity")
else:
    print("Line 2 - a and b do not have same identity")

print ("Value1>",value_1)
print ("Value2>",value_2)

print ("Value1 ID>",id(value_1))
print ("Value2 ID>",id(value_2))

# el objeto es el mismo porque ambos son integer pero tiene otro nombre.