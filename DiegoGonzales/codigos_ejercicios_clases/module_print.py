def show_ege(ege):
    if ege <= 12:
        print("You are a child: ", ege)
    elif ege >= 13 and ege <= 17:
        print("You are teenager: ", ege)
    elif ege >= 18 and ege <= 29:
        print("You are young: ", ege)
    else:
        print("You are adult: ", ege)
