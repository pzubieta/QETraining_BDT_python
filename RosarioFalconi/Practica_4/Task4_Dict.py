import RosarioFalconi.Practica_4.Task4 as t4

nro_personas = 0
str_nro = input("Ingresa numero de personas:")
personas = {}
keys={}
if not str_nro.isnumeric():
    print("Ingresa un numero valido")
else:
    nro_personas=int(str_nro)
    i = 0
    for i in range (nro_personas):
        str_persona = input("Ingresa el nombre y la edad separado por comma:")
        persona = str_persona.split(",")
        personas[persona[0]]=persona[1]
        i+=1
    i=0
    keys=personas.keys() # devuelve los keys en un array
    for i in range(len(personas)):
        persona = personas.popitem()
        print ("Nombre: ", persona[i])
        t4.calling_module_functions(persona[i])
        print("====================================")
