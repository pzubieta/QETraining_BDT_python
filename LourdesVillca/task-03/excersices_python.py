def area_of_circle(radio):
    """
    Method that calculate the circle area if the radio is greater than 10.

    :param radio:   int     Represents the circle area.
    """
    print("Circle Area: ", 3.1416 * radio ** 2) if radio > 10 else print("Given Area is less than 10")


# Case when the Radio is less than 10
area_of_circle(5)
# Case when the Radio is greater than 10
area_of_circle(15)


def sum_to(number):
    """
    Method that sum all integers up to and including only until any value lower than 35.

    :param number:     int      represents the  number to will sum
    """
    if number < 35:
        print("Sum of all preceding numbers until {}, is: {}".format(number, sum_numbers(number)))
    else:
        print("Sum of all preceding numbers until 35, is", sum_numbers(35))


def sum_numbers(number):
    """
    Method to sum all preceding numbers until the given number.

    :param number:      int     Number until the sum will be calculated
    :return:            int     Sum of all preceding numbers of number
    """
    sum = 0
    for i in range(number + 1):
        sum += i
    return sum


# Case when the number is greater tha 35
sum_to(40)
# Case when the number is less than 35
sum_to(10)


def days_in_month(month):
    """
    Method that print the days of a given month.

    :param month:   string      represent the name of the month
    :return:        int         the number of the given month
    """
    month_with_31_days = ["January", "March", "May", "July", "August", "October", "December"]
    month_with_30_days = ["April", "June", "September", "November"]
    month_with_28_days = ["February"]

    if month in month_with_31_days:
        return 31
    elif month in month_with_30_days:
        return 30
    elif month in month_with_28_days:
        return 28
    else:
        return None


print(days_in_month("January"))
