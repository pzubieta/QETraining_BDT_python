#import Age.CalculeAge as m

def messages(y):
    if y < 12:
        print("you are child")
    elif y > 12 and y < 17:
        print("you are Tenneger")
    elif y > 17 and y < 29:
        print("you are Young")
    elif y > 29:
        print("you are Adult")
    else:
        print("invalid input")