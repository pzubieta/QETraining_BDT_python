#Write a function replace(s, old, new) that replaces all occurrences of old with new in a string s


def replaceString(string, old, new):
    string = string.split(old)
    print(string)
    string = new.join(string)
    print (string)



replaceString("Mississippi", "i", "I")

song = "I love spom! Spom is my favorite food.Spom, spom, yum!"

replaceString(song, "o", "a")