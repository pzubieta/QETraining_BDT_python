def sum_to (n):
    sum = 0
    for i in range (1,n+1):
        sum = sum + i
        print (sum)
        if i > 35:
            break
sum_to(5)