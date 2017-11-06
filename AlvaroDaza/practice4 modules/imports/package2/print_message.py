def print_age_message(age):
    """
    this method evaluates the value of age sent and print it in the console.
    :param age:    int    age in years.
    :return:
    """
    if age <= 12:
        print("You are a child")
    elif 13 <= age <= 17:
        print("You are a teenager ")
    elif 18 <= age <= 29:
        print("You are young ")
    else:
        print("You are adult")
