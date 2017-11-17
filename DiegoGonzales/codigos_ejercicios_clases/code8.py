# ejemplo de if anidado
num = -1

if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")

# ejemplo de while
count = 0
while count < 9:
    print("The count is:", count)
    count = count + 1

print("Good bay!!!")



count = 0
while count < 5:
    print(count, "is less than 5")
    count = count + 1
else:
    print(count, "is not less than 5")


flag = 0
while (flag):
    print("Given flag is really true!")
else:
    print("Chau")

print("Good bay!!!")


# ejemplo de for

numbers = [6, 5, 8, 9, 7, 4, 3, 11, 10, 2, 12]
sum = 0

for val in numbers:
    sum = sum + val

print("The sum is:", sum)


for valx in range(10):
    print(valx)


genre = ['pop', 'rock', 'jazz']

print(genre[1])

for i in range(len(genre)):
    print("I like", genre[i])


# ejemplo break

for val in "String":
    if val == "i":
        break
    print(val)

print("The end")



val = 20

while val > 0:
    print("Current value:", val)
    val -= 1
    if val == 5:
        break

print("Good bay!!")


for val in "String":
    if val == "i":
        continue
    print(val)
print("End")


while val > 0:
    print("Current value:", val)
    val -= 1
    if val == 5:
        continue

print("Good bay!!")


sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass