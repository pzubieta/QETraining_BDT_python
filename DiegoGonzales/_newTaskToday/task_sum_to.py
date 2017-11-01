def sum_to(limit):
    sum = 0
    for i in range(1, limit):
        sum = sum + i
        if sum < 35:
            result = sum
        else:
            break
    return result


print(sum_to(40))