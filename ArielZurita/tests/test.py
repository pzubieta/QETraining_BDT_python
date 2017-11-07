def listMonths():
    monthEntered = str(input("Enter a month \n"))
    months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "octuber", "november", "december"]
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if monthEntered in months:
        index = months.index(monthEntered)
        days = days[index]
        print("Month %s has %d days" %(monthEntered, days))
    else: print("Invalid value entered")

#listMonths()

def findURL(text):
    startUrl = text.find("http://")
    if startUrl != -1:
        newUrlString = text[startUrl:]
        urlEnd = newUrlString.find(" ")
        if urlEnd != -1:
            urlEndSize = startUrl + urlEnd
            url = text[startUrl:urlEndSize]
            print(url)
        else: print(text[startUrl:])

stringWithURL = "this is a test with url http://www.google.com"
#findURL(stringWithURL)

test = "this is a text"
i = test.count("i")
print(i)