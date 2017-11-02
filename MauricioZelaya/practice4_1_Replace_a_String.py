def replaceString(aString, old, new):
    aString = aString.split(old)
    aString = new.join(aString)
    return aString


aString = "I love spom! Spom is my favorite food.Spom, spom, yum!"
print(replaceString(aString, "om", "am"))
print(replaceString(aString, "o", "a"))
print(replaceString("Missisippi", "i", "I"))