def add_char(dict_alpha, key, num):
    if key is not dict_alpha.keys() and key != " ":
        dict_alpha[key] = num
    return dict_alpha

def count_s(string_s,char,len_s):
    count = 0
    i = 0
    while i < len_s:
        if string_s[i] == char:
            count += 1
        i +=1
    return count

def count_alphabet(phrase_s,lengh):
    i = 0
    limit = int(lengh)
    hash_alphabetic = {}
    while i < limit:
 #       print (phrase_s[i])
        num_s = count_s(phrase_s,phrase_s[i],limit)
        char_toadd = phrase_s[i]
#        print(phrase_s[i], "->","Count ",num_s)
        add_char(hash_alphabetic,char_toadd,num_s)
        i +=1
    print (hash_alphabetic)

phrase = input("Enter a phrase: ")
value = len(phrase)
#print(value)
count_alphabet(phrase, value)
