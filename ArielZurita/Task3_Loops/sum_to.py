def sum_to():
    number = int(input("Enter a number \n"))
    sum = 0
    for i in range(1, number+1):
        if i < 35:
            sum += i
            print(sum)
        else: break
sum_to()