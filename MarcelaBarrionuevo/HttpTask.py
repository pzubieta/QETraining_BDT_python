def retun_string(s):

    val = "https://"
    val2 = ".com"
    val3 = len(val2)
    limit=s.find(val)
    limit2=s.find(val2)
    limit3=limit2+val3
    if limit != -1:
         print(s[limit:limit3])
    else:
        print("There is no URL")
retun_string("I am in https://www.yahoo.com test")