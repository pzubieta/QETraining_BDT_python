value_a = float (input ('Introduce el valor de a: '))
value_b = float (input ('Introduce el valor de b: '))

print ("Comparing both values:")
if value_a == value_b: print (value_a, "is equal to", value_b)
if value_a != value_b: print  (value_a,"is different than ", value_b)
if value_a >= value_b: print  (value_a,"is greader of equal than ", value_b , "compared by '>=' operator")
if value_a <= value_b: print  (value_a,"is minor or equal than ", value_b , "compared by '<=' operator")
if value_a < value_b: print  (value_a,"is minor than ", value_b,  "compared by '<' operator")
if value_a > value_b: print  (value_a,"is greader than ", value_b, "compared by '>' operator")

c = value_a
print ("When doing c = a then ", "c = ", c)
c += value_a
print ("When doing c += a then ", "c = ", c)
c-= value_a
print ("When doing c -= a then ", "c = ", c)
c*= value_a
print ("When doing c *= a then ", "c = ", c)
c/= value_a
print ("When doing c /= a then ", "c = ", c)
c%= value_b
print ("When doing c %= b then ", "c = ", c)
if value_a in (0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30):
    print (value_a, "is in (0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30)")
if  value_a not in (0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30):
    print (value_a, "is not in (0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30)")
if value_a in (1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31):
    print (value_a, "is in (1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31):")
if  value_a not in (1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31):
    print (value_a, "is not in ((1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31):")

c = value_a
print ("When doing c = a then ", "'c is value_a' returns ", c is value_a)
c = value_b
print ("When doing c = b then ", "'c is not value_a' returns ", c is not value_a, "and c is not value_b' returns" , c is not value_b)