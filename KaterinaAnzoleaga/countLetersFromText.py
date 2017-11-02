def countLetters (text):
    """This function returns the number of times each character different than space appears in text"""
    dic = {}
    for i in text:
        i=i.lower()
        if i != " ":
            if dic.has_key(i):
                new_value = dic[i]+1
                new_elem = {i:new_value}
                dic.update (new_elem)
            else:
                new_elem = {i:1}
                dic.update(new_elem)
    return (dic)
iterations = 0
text = 'test'
while text and iterations <=10:
    text = raw_input ("Ingrese un texto: ")
    print ('El numero de ocurrencias de cada letra es: ', countLetters(text))
    iterations +=1