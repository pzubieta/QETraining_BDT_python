def sum_to(n):
    sum = 0
    val = 1
    while(val <= n):
        sum += val
        val += 1
        if val == 36:
            break
    print("The sum is", sum)
sum_to(35)