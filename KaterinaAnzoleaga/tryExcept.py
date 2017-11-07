def get_age ():
    age = int(input ("Plase enter your age: "))
    if age < 0:
        # Create a new instance of an exception
        my_error = ValueError ("{0} is not a valid age".format (age))
        raise my_error
    return age


get_age()






user_input = input ("Enter a floating point number: ")

try:
    #Try to do something that could fail
    input_as_float = float (user_input)
except ValueError:
    # This will be executed if a "ValueError" is raised
    print ("You did not enter a floating point number.", ValueError)
else:
    # This will be executed if not exception got raised in the try statement.
    print ("The square of number is: ", input_as_float**2)
finally:
    # This will be execute whether or not an exception is raised
    print ("Thank you!")


