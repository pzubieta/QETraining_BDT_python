a=7
b=4
c= 2
d=2
e=4

#funcion1
def homeW(a,b):
    d=a+b

    if (d==10):
        resp=(d)
    else:
        resp=(d)
    return resp
#funcion2
def exponente(d,e):
    h=0
    exp=d
    while(h<e):
        h+=1
        exp *= d
        print exp
    return exp

#llamada de funcion

respuesta=homeW(a,b)
respuesta*=c
elevado=exponente(d,e)
print "la respuesta al final es:",respuesta
print "y su exponente es:" , elevado