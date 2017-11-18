def find_url(string_to_evaluate):
    """
    Method to find a url given an string.

    :param string_to_evaluate:  string      Represents the string where to found the url.
    """
    start_url = "http://"
    if start_url in string_to_evaluate:
        start_index = string_to_evaluate.find(start_url)
        string_to_evaluate = string_to_evaluate[start_index: len(string_to_evaluate)]
        end_index = string_to_evaluate.find(" ")
        print("Found Url: ", string_to_evaluate) if end_index == -1 else print("Found Url: ",
                                                                               string_to_evaluate[:end_index])
    else:
        print("Any url was found")


find_url("This is a url http://www.google.com to test")
find_url("This is a string without an url")


def replace_string(string_to_replace, old_string, new_string):
    """
    Method to replaces all occurrences of old with new in a string.

    :param string_to_replace:   string      String where to replace the occurrences.
    :param old_string:          string      Represents the old string to replace.
    :param new_string:          string      Represents the new string to replace.
    """
    print(string_to_replace.replace(old_string, new_string))


replace_string("Mississippi", "i", "I")
replace_string("I love spom! Spom is my favorite food. Spom, spom, yum!", "om", "am")
replace_string("I love spom! Spom is my favorite food. Spom, spom, yum!", "o", "a")


def count_letters(str_to_validate):
    """
    Method to reads a string an count each letter occurs.

    :param str_to_validate:     string      Represents the string to validate.
    """
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    str_to_validate = str_to_validate.lower()
    count_letter = {}
    for letter in alphabet:
        if str_to_validate.count(letter) > 0:
            count_letter[letter] = str_to_validate.count(letter)

    for key, value in count_letter.items():
        print("{} {}".format(key, value))


count_letters("ThiS is String with Upper and lower case Letters")
