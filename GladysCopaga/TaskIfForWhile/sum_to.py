def sum_to(n):
    sum = 0
    for i in range(n+1):
        if (i > 35):
            break
        sum += i
    print ("The sum is: ", sum)
sum_to(40)
