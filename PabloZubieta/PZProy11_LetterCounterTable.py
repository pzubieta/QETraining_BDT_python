def lettersTable(strWord):
    letterTable = {}
    for i in range(97,123) :
        letterTable[chr(i)] = count_letters1(strWord, chr(i))

    return(letterTable)

def count_letters1(strWord, charEval):

    letterCount = 0

    # Transforma todo a minusculas
    strWord = str.lower(strWord)


    for char in strWord:
        if charEval == char:
            letterCount += 1

    return letterCount

def count_letters2(word, char):
    """"very efficient way to count letters into a string"""
    return sum(char == c for c in word)

print (count_letters1('AAAAAbanana','a'))

print (count_letters2('aaabanana','a'))

strRes = lettersTable('AAAaabananazzz' )
for chrLetter in strRes:
    print(chrLetter[0], " : ", strRes[chrLetter], "\n")

