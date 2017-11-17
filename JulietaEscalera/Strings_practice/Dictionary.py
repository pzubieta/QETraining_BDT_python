import operator
def count_letters(text):
    t=len(text)
    i=0
    save={}
    while t>0:

        a=text[i]
        t -= 1
        i += 1
        b = text.count(a,0,len(text))
        if (a!=" "):
            save[a] = b


    resultado = sorted(save.items(), key=operator.itemgetter(0))
    print("diccionario", resultado)
count_letters("como se aplica el return y en que casos se puede omitir")
