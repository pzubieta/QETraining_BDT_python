def odd_or_even(r):
    for num in range(r):
        # Check if num is odd
        if num % 2 == 0:
            print("Odd numbers: %d " % num)
        else:
        # Check if num is even
            print("Even numbers: %d " % num)
odd_or_even(10)
