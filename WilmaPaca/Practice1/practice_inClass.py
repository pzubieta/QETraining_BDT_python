
def are_of_circle(r):
    pi = 3.1416
    if r>10:
        area = (pi*r)**2
        print("This the area for circle: %d" % (area))
    else:
        print("Radious is not greater than 10 -> %d" %(r))

print("------ Calculate area of circle -------- ")
print("")
radious = int(input("Enter the radious: "))
are_of_circle(radious)

print("")
print("------ Perform  addition of n number before 40 -------- ")
print("")
def sum_to(n):
    sum = 0
    val = 1
    while val <= n:
        sum += val
#        print("sum",sum)
        val += 1
#        print("value",val)
        if sum > 35 :
            break

    return sum

number_sum = int(input("Enter the number times to sum: "))
suma_values = sum_to(number_sum)
print("Sum of all number is: %d" %(suma_values))


print("")
print("------ Verify if a number is primo -------- ")
print("")

def is_primo(num):
    if num < 2:
        return False
    elif num == 2:
        return True

    for n in range(2,num):
        if (num % n) == 0:
            return False
    return True

def print_primos(number_sequ):
    count = 0
    for a in range (number_sequ):
        if is_primo(a) == True:
            count +=1
            print ("Number %d"%(a),"is PRIMO")
    print ("There are ",count, "numbers PRIMOS")

number_primo = int(input("Enter the last number to  verify if it is PRIMO: "))
print_primos(number_primo)