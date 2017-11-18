#if statements

# if expression:
#    statement (s)

var = 100
if var == 100: print("Value of expression is $s", var)
print("That's all!!")


# if expression:
#    statement (s)
# else:
#    statement (s)

some_value = 0
if some_value:
    print("Got a true expression value")
    print(some_value)
else:
    print("Got a false expression value")
    print(some_value)

# if expression1:
#    statement(s)
# elif expression2:
#    statement(s)
# elif expression2:
#    statement(s)
# else:
#    statement(s)

var = 500

if var == 200:
    print("1 - Got a true expression value")
    print(var)
elif var == 150:
    print("2 - Got a true expression value")
    print(var)

elif var == 100:
    print("3 - Got a true expression value")
    print(var)
else:
    print("4 - Got a false expression value")
    print(var)