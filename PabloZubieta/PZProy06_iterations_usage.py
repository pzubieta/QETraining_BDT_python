flag = 1

while flag > 2 : flag = flag - 1

else:
    flag = flag + 1

listArrNums = [3,4,5,2,76,4,2,87,44,11]
sum = 0

for num in listArrNums:
    sum = sum + num

print("The sum is: ", sum)

# Range genera un arreglo de numeros de 0 a la longitud del arreglo listArrNum (innecesario, una vuelta extra solo para mostrar como funciona)
for i in range(len(listArrNums)):
    print("the numbers list is: ", listArrNums[i])
#----------------------------------------------------------------------------

val = 20
while val > 0:
    print("Current value:", val)

        val -= 1
        if val == 5:
            break

print ("Good bye!")