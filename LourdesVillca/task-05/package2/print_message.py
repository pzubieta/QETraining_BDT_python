def print_age_message(age):
    """
    Method to print message according the range of the age.

    :param age:     int     Represents the age value to validate.
    """
    if age <= 12:
        print("You are a child")
    elif age <= 13 <= 17:
        print("You are a teenager ")
    elif age <= 18 <= 29:
        print("You are young ")
    else:
        print("You are adult")
