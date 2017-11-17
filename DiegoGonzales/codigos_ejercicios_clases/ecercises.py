
def area_of_circle(radio):
    pi = 3.1416
    area = pi * (radio * radio)
    if area > 10:
        return area
    else:
        return 0


print(area_of_circle(1))



def sum_to(n):
    for x in n:
        sum = sum + x
        if sum <= 35:
            break
    return sum

print(sum_to(20))



#days_in_mothn(febrary) == 28