def prime_or_not(min, max):

    if min == 1:
        print("%d is not prime " % min)
    elif min == 2:
        print("%d is prime " % min)
    else:
        for min in range(max):
            for x in range(2, min):
                if (min % x == 0):
                    print(" %d is prime " % x)
                    break

prime_or_not(4, 12)
