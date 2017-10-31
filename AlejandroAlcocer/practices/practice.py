test_url_string = 'I am in https://google.com this should not care'

def find_url(url_string):

    # string2 = string1[ :string1.find(' ')]
    print(url_string[url_string.find('http'):][:url_string[url_string.find('http'):].find(' ')])
    # print(string2)

    # print(url_string[url_string.find('http'): url_string.find('.com')])

find_url(test_url_string)
