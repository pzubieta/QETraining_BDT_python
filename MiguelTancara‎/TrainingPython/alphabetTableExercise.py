#Write a program that reads a string and returns a table of the letters of the alphabet in alphabetical order
#which occur in the string together with the number of times each letter occurs.

def alphabetTable(string):
    string = string.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphaDict = {}
    for char in string:
        if char in alphabet:
            if char in alphaDict:
                alphaDict[char] = alphaDict[char] + 1
            else:
                alphaDict[char] = 1
    keys = list(alphaDict.keys())
    keys.sort()
    for char in keys:
        print(char, alphaDict[char])


string = "ThiS is String with Upper and lower case Letters"
text = "When test execution is started, the framework first parses the test data. It then utilizes keywords provided by the test libraries to interact with the system under test. Libraries can communicate with the system either directly or using other test tools as drivers."
alphabetTable(text)


