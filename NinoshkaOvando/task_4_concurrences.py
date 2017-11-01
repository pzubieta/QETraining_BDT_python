def ocurrence_chars(text_example):
    if(type(text_example)):
        result = {'a': 0, 'b': 0,'c': 0, 'd': 0,'e': 0,'f': 0,'g': 0,'h': 0,'i': 0,'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0,
              'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0 ,'w': 0, 'x': 0, 'y': 0, 'z': 0, 'Other chars': 0}
        cont=0
        while(cont < len(str(text_example))):
            if(text_example[cont] == "a"): result['a']+=1
            elif(text_example[cont] == "b"): result['b']+=1
            elif (text_example[cont] == "c"): result['c'] += 1
            elif (text_example[cont] == "d"): result['d'] += 1
            elif (text_example[cont] == "e"): result['e'] += 1
            elif (text_example[cont] == "f"): result['f'] += 1
            elif (text_example[cont] == "g"): result['g'] += 1
            elif (text_example[cont] == "h"): result['h'] += 1
            elif (text_example[cont] == "i"): result['i'] += 1
            elif (text_example[cont] == "j"): result['j'] += 1
            elif (text_example[cont] == "k"): result['k'] += 1
            elif (text_example[cont] == "l"): result['l'] += 1
            elif (text_example[cont] == "m"): result['m'] += 1
            elif (text_example[cont] == "n"): result['n'] += 1
            elif (text_example[cont] == "o"): result['o'] += 1
            elif (text_example[cont] == "p"): result['p'] += 1
            elif (text_example[cont] == "q"): result['q'] += 1
            elif (text_example[cont] == "r"): result['r'] += 1
            elif (text_example[cont] == "s"): result['s'] += 1
            elif (text_example[cont] == "t"): result['t'] += 1
            elif (text_example[cont] == "u"): result['u'] += 1
            elif (text_example[cont] == "v"): result['v'] += 1
            elif (text_example[cont] == "w"): result['w'] += 1
            elif (text_example[cont] == "x"): result['x'] += 1
            elif (text_example[cont] == "y"): result['y'] += 1
            elif (text_example[cont] == "z"): result['z'] += 1
            else: result['Other chars'] += 1
            cont +=1
    else:
        return None
    return result

def test_ocurrence_chars():
    text_example = "January February March May July August October December April June September November"
    results= ocurrence_chars(text_example)
    if(results != None):
        for keys, values in results.items():
            print('Ocurrences that were found of {} is {} '.format(keys,values ))
    else:
        print('there is not any ocurrence in {} '.format(text_example))


def mail():
    print("###Ocurrence Count Program###")
    print("Example: ")
    test_ocurrence_chars()
    input_value= input("Enter a text: ")
    results= ocurrence_chars(input_value)
    if(results != None):
        for keys, values in results.items():
            print('Ocurrences found of {} is {} '.format(keys,values ))
    else:
        print('there is not any ocurrence found in {} '.format(input_value))
mail()