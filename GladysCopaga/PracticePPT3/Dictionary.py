string = "ThiS is String wiTh Upper and lower case Letters"
newstring = string.lower()
print (newstring)
dic = {}
for j in newstring:
    if j in dic:
        dic[j] = dic[j]+1
    else:
        dic[j] = 1
print (dic)
#dic2 = dic.keys()
#dic2.sort()
#for key in sorted(dic2.iterkeys()):
    #print (key + ": " + dic2[key])
#    print ("%s: %s" % (key, dic2[key]))





