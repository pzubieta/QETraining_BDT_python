# Local variables
# Global variables
sz = 2
def h2():
    global sz
    tess.turn(42)
    tess.fordward(sz)
    sz += 1

# String Hadndling

#len(str)
#str[i]
#str[i:j]
#str.find(target)

#Suppose any line of text can contain at most one url that start with "http:// and needs at the next ining[i]

def printURL(string):
    newString = string[string.find("http"):]
    print(newString[:newString.find(" ")])

textWithURL = "I am reviewing information in http://www.google.com URL, it is useful for us"
textWithoutURL = "I am in main page"
printURL(textWithURL)
printURL(textWithoutURL)

# List methods
# append.
# insert(position, value)
# count
# extend
# reverse
# sort
# remove

#split
song = "The rain in Spain..."
words = song.split()
print(words)

words= song.split("ai")
print(words)

#join
glue=";"
phrase = glue.join(song)
print(phrase)


# Practice
# replace (s, old, new)
# replace("Missisipi, "i", "I"") --> "MIssIssIpI"

#Dictionaries
dict = {}
dict['one'] = "this is one"
dict[2] = "this is two"
tinydict = {'name': 'jhon', 'code': 6734, 'dept': 'sales'}
print (dict['one'])
print (dict[2])
print (tinydict)
print (tinydict.keys())
print (tinydict.values())

