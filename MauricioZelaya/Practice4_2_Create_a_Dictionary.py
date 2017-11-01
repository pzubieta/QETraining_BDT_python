def keyExists(myDictionary, key):
    """return true if key already exists in the dictionary"""
    if key in myDictionary.keys():
        return True


myDictionary = {}
aString = "ThiS is a String with Upper and lower case Letters"
# setting all the string in lower case
aString = aString.lower()
# removing whit spaces
aString = aString.replace(" ", "")
# creating a list from we will create the indexes
indexList = list(aString)
# populating the dictionary
for val in indexList:
    if keyExists(myDictionary, val):
        myDictionary[val] += 1
    else:
        myDictionary[val] = 1
sorted(myDictionary)
print (myDictionary)
