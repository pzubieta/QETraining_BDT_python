# break

for val in "string":
    if val == "i":
        break
    print(val)
print("Break : The end")


val = 20
while val > 0:
    print("Current value: ", val)
    val -= 1
    if val == 5:
        break
print("Break : Good bye!!")

# Continue

for val in "string":
    if val == "i":
        continue
    print(val)
print("Continue : The end")


val = 20
while val > 0:
    print("Current value: ", val)
    val -= 1
    if val == 5:
        continue
print("Continue : Good bye!!")

# Pass Statement

sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass # --> It indicate that is missing implement something here, this space of code is skipped in the execution.