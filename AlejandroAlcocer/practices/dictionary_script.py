######### FUNCTIONS ###########

def find_url(url_string):
    """
    This method return a URL located in a string.
    :param url_string: String with a URL in it.
    :return: The URL in the string.
    """
    return (url_string[url_string.find('http'):][:url_string[url_string.find('http'):].find(' ')])
    # print(url_string[url_string.find('http'): url_string.find('.com')])


def replace_letter(string_to_change, letter_to_change, new_letter):
    """
    This method replace a letter for another in a given string.
    :param string_to_change: The string where the changes will be made.
    :param letter_to_change: The new letter.
    :param new_letter: The letter that will be replaced.
    :return: The modified string.
    """
    string_to_change.lower()
    letter_to_change.lower()
    new_letter.lower()
    index = 0
    for letter in string_to_change:
        if letter == letter_to_change:
            string_to_change = string_to_change[:index] + new_letter + string_to_change[index + 1:]
        index += 1
    return string_to_change


def counting_letter_in_a_string(string_to_count):
    """
    This method count the amount of letter that are duplicated in a sentence.
    :param string_to_count: The string that will be tested
    :return: A dictionary with the words in sentence with the amount of times a letter is duplicated.
    """
    string_to_count = ''.join(sorted(string_to_count.lower())).strip() #sort the list, cut spaces and lower cases it
    new_dic = {}
    for letter in string_to_count:
        if letter in new_dic:
            times = new_dic[letter] + 1
            new_dic[letter] = times
        else: new_dic[letter] = 1
    return new_dic


######### TESTS ###########

test_string_to_count = 'something In The way'
print(counting_letter_in_a_string(test_string_to_count))

test_string_to_change = 'this is the new word'
test_letter = 's'
test_new_letter = 'n'
print(replace_letter(test_string_to_change, test_letter, test_new_letter))

test_url_string = 'I am in https://google.com this should not care'
print(find_url(test_url_string))
