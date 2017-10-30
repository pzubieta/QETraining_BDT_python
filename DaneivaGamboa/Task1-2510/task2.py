def op(numeroMayor,numeroMenor,numeroMedio,numeroExtra):
    print("Testing Arithmetic Operations")
    print("---------------------------------")
    suma = numeroMedio + numeroMayor
    print("La suma es:", suma)
    resta = numeroMayor - numeroMenor
    print("La resta es:", resta)
    multiplicacion = numeroMenor * numeroMedio
    print("La multiplicacion es:", multiplicacion)
    division = numeroMayor / numeroMenor
    print("La division es:", division)
    mod = numeroMenor % numeroMedio
    print("Mod es:", mod)
    exponent = numeroMenor ** numeroMenor
    print("Resultado es:", exponent)
    floatdiv = numeroMedio // numeroExtra
op(10,5,48,555)



def listTest(a,b):
    print("---------------------------------")
    print("Testing a List")
    aList=[1, 2, 3, 4]
    bList=[2, 5, 9]
    if (a in aList):
        print("a exists list")
    else:
        print("a does not exist list")
    if (b not in bList):
        print("b does not exist list")
    else:
        print("b exist list")
list()


def ifElseTest(value_1,value_2):
    print("---------------------------------")
    print("Testing IF-Else")
    if (value_1 == value_2):
        print(id(value_1), "=", id(value_2), ",Line 2-a and b have same identity")
    else:
        print(id(value_1), "=", id(value_2), ",Line 2-a and b do not have same identity")

    if (id(value_1) == id(value_2)):
        print(id(value_1), "=", id(value_2), ",Line 2-a and b have same identity")
    else:
        print(id(value_1), "=", id(value_2), ",Line 2-a and b do not have same identity")
ifElseTest(55,0)



