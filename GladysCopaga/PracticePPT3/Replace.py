def replace():
    s = "Mississipi si"
    old = "si"
    new = "xx"
    newString = ""
    i = 0
    while (i <= len(s)):
        if s[i:i+ len(old)] == old:
            newString += new
            i = i + len(old)
        else:
            newString += s[i:i+1]
            i = i+1
    print (newString)

replace()
