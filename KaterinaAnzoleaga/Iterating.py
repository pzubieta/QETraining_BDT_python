genre = ['pop','rock','jazz']
for i in range (len(genre)):
    print("I like ", genre [i])

for val in "string":
        if val == "i":
            break
        print (val)
print ("The end")

val = 20
while val > 0:
    print("Current value: ", val)
    val -= 1
    if val == 5:
        break
print ("Good bye!")


for val in "string":
        if val == "i":
            continue
        print (val)
print ("The end")

val = 20
while val > 0:
    print("Current value: ", val)
    val -= 1
    if val == 5:
        continue
print ("Good bye!")


