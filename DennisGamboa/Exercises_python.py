# -----------------------------------------------------------------------------------------------------------------------
# Suppose any line of text can contain at most one url that starts with “http://” and ends at the next space in the line.
# Write a fragment of code to extract and print the full url if it is present.
# -----------------------------------------------------------------------------------------------------------------------

def find_url(text):
    p = 0
    x = 0
    p = text.find("https")
    x = text.find("com")
    url = ""
    for val in range(p, x + 3):
        url += text[val]
    print(url)


find_url("I am https://www.google.com/dfgodfgd")



# -----------------------------------------------------------------------------------------------------------------------
# Write a function replace(s, old, new) that replaces all occurrences of old with new in a string s:
# -----------------------------------------------------------------------------------------------------------------------

def replace_text(string, old, new):
    ns = string
    while old in ns:
        x = ns.find(old)
        #print("valor x", x)
        ns = ns[:x]+new+ns[x+len(new):]
        #print("valor ns", ns)
    return ns


song = "I love spom! Spom is my favorite food.Spom, spom, yum!"
print(replace_text(song, "om", "am"))
print(replace_text(song, "o", "a"))
print(replace_text("Mississippi", "i", "I"))


def replace_text_second(string, old, new):
    string = string.split(old)
    #print(string)
    string = new.join(string)
    print(string)


song = "I love spom! Spom is my favorite food.Spom, spom, yum!"
replace_text_second(song, "om", "am")
replace_text_second(song, "o", "a")
replace_text_second("Mississippi", "i", "I")


# -----------------------------------------------------------------------------------------------------------------------
# Write a program that reads a string and returns a table of the letters of the alphabet in alphabetical
# order which occur in the string together with the number of times each letter occurs.
# -----------------------------------------------------------------------------------------------------------------------

def letters_alphabet(text):
    text = text.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter_count = {}
    for char in text:
        if char in alphabet:  # ignore any punctuation, numbers, etc
            if char in letter_count:
                letter_count[char] = letter_count[char] + 1
            else:
                letter_count[char] = 1
    keys = list(letter_count.keys())
    #print("keys", keys)
    keys.sort()
    for char in keys:
        print(char, letter_count[char])


string = "ThiS is String with Upper and lower case Letters"
letters_alphabet(string)