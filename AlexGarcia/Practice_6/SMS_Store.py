from datetime import datetime

class SMS_Store:
    def __init__(self):
        self.store = []

    def add_new_arrival(self, number, time, text):
        self.store.append(("Read: False","From: "+ number, "Recieved: "+ time, "MSg: "+text))

    def message_count(self):
        return (len(self.store))

    def get_unread_indexes(self):
        result = []
        for (i, v) in enumerate(self.store):
            if v[0] == "Read: False":
                result.append(i)
        return (result)

    def get_message(self, i):
        msg = self.store[i]
        msg = ("Read: True",) + msg[1:]
        self.store[i] = (msg)
        return (self.store[i][1:])

    def delete(self, i):
        del self.store[i]

    def clear(self):
        self.store = []


time = datetime.now().strftime('%H:%M:%S')
#creando mi objeto My_inbox
my_inbox = SMS_Store()
primerSMS = my_inbox.add_new_arrival('79386479',time,"Hola Donde estas?")
segundoSMS = my_inbox.add_new_arrival('79386479',time,"Descansa")
terceroSMS = my_inbox.add_new_arrival('79386479',time,"Despierta")
cuartoSMS = my_inbox.add_new_arrival('79386479',time,"Despierta")

#SMS enviados
print(my_inbox.store[0])
print(my_inbox.store[1])
print(my_inbox.store[2])
print(my_inbox.store[3])

#Cantidad de mensajes
print("Cantidad de SMS ",my_inbox.message_count())

#SMS no leidos
print("SMS no leidos ",my_inbox.get_unread_indexes())

#Leer mesajes
print('Mesaje Leido',my_inbox.get_message(0))
print('Mesaje Leido',my_inbox.get_message(3))

#SMS no leidos
print("SMS no leidos ",my_inbox.get_unread_indexes())

#Eliminar un mensaje
print('Eliminar un mensaje')
my_inbox.delete(3)

#Cantidad de mensajes
print("Cantidad de SMS ",my_inbox.message_count())

#Borrar todos los mesajes
print('Borrar todos los mesajes')
my_inbox.clear()

#Cantidad de mensajes
print("Cantidad de SMS ",my_inbox.message_count())




