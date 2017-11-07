from RosarioFalconi.Practica_5.Inbox import Inbox
from RosarioFalconi.Practica_5.SMS import SMS

my_inbox = Inbox()
nr_opcion=input("Menu\n 1.Ingresar mensaje\n 2.Ver mensaje \n 3. Borrar mensaje \n 4.Total mensajes \n 5.Nro mensajes no leidos\nOpcion:")
while not nr_opcion.isnumeric():
    if nr_opcion.isnumeric():
        break
    print("===========================================")
    nr_opcion = input("Menu\n 1.Ingresar mensaje\n 2.Ver mensaje \n 3. Borrar mensaje \n 4.Total mensajes \n 5.Nro mensajes no leidos\nOpcion:")

opcion=int(nr_opcion)
while opcion > 0 :
    print("===========================================")
    if opcion is 1:
        my_msj = input("Message:")
        my_from = input("From:")
        new_msj = SMS(my_msj,my_from)
        my_inbox.add_sms(new_msj)
        print("===========================================")

    elif opcion is 2:
        index_msj = input("View message:")
        msje= my_inbox.get_message(int(index_msj))
        print("===========================================")

    elif opcion is 3:
        index_msj = input("Borrar mensaje:")
        my_inbox.delete(int(index_msj))
        nro_msges = my_inbox.msg.__len__()
        print("Tienes # mensajes en total", nro_msges)
        print("===========================================")

    elif opcion is 4:
        nro_msges=my_inbox.msg.__len__()
        print("Tienes # mensajes en total", nro_msges)
        print("===========================================")

    elif opcion is 5:
        unreads=my_inbox.get_Unread()
        print("Tienes ",unreads," mensajes sin leer")
        print("===========================================")

    else:
        print("Opcion no valida. Ingrese un numero del 1 al 5.")

    nr_opcion = input("Menu\n 1.Ingresar mensaje\n 2.Ver mensaje \n 3. Borrar mensaje \n 4.Total mensajes \n 5.Nro mensajes no leidos\nOpcion:")
    opcion = int(nr_opcion)
