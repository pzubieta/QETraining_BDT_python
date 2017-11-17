def find_and_print_url(text):
    initUrlPosition = text.find("http://")
    if initUrlPosition != -1:
        allTextFromInitUntilEnd = text[initUrlPosition:]
        endUrlPossition = allTextFromInitUntilEnd.find(" ")
        if endUrlPossition != -1:
            urlLenght = initUrlPosition + endUrlPossition
            print("This is the url found ", text[initUrlPosition:urlLenght])
        else: print("This is the url found ", text[initUrlPosition:])

find_and_print_url("this is a test on http://www.google.com")