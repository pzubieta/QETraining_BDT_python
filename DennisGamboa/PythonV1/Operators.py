a = 0
b = 60

if a == b:
    print("a have same value that b")
else:
    print("are different")

if a != 0:
    print("a=", a)
else:
    print("is zero", a)

if a > b:
    print("a > b")
else:
    print("a < b")

if b >= 30:
    print("b is >= to 30")
else:
    print("b is <= to 30")

numbers = [3, 3, 3, 3, 3, 4]
s = 0
for val in numbers:
    s += val
print("sum in array is:", s)



#############################################
# Assignment Operators

def assignment_operators(x, r, y):
    if r == "+":
        res = x + y
        print("case a =:", res)
    if r == "-":
        while x > 0:
            x -= 1
        print("case b X=:", x)
    if r == "*":
        i = 1
        while y > 0:
            i *= y
            y -= 1
        print("factorial of y=", i)
    if r == "/":
        p = x/y
        print("x / y =", p)

assignment_operators(20, "/", 5)


#Task_1-------------------------------

def task(a, b, c):
    res = 0
    if b == "+":
        res = a + c

    if b == "-":
        res = a - c

    if b == "*":
        res = a * c

    if b == "/":
        res = a / c

    return res

print(task(5, "-", 50))

