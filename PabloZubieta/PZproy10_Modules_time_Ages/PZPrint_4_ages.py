# Says if you are young, adult or a child based on ages

def personTypeAgeBased(timeAge):    # write Fibonacci series up to n
    mesage = ""
    if timeAge < 12 : mesage = "You are a child"
    elif timeAge < 17 and timeAge > 12 : mesage = "You are a teenager"
    elif timeAge < 29 and timeAge > 18: mesage = "You are a young"
    else : mesage = "You are an Adult"

    return mesage

print (personTypeAgeBased(11))