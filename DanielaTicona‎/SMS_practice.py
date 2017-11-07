class SMSstore(object):

    def __init__(self):
        self.message_list = []


    def add_new_arrival(self,visto, number, arrived, text_SMS):
        messages_tuples = [visto, number, arrived, text_SMS]
        self.message_list.append(messages_tuples)

    def message_count(self):
        return self.message_list.__len__()

    def get_unread_indexes(self):

        return [index + 1 for index, message in enumerate(self.message_list) if not message[0]]

    def get_message(self, i):
        if i > len(self.message_list):

            print ("THIS message not exist")
        else:
            self.message_list[i - 1][0] = True
        return self.message_list[i - 1][3]

    def delete(self,i):
        self.message_list.pop(i - 1)

    def mostrar_mensajes(self):
        for message in self.message_list:
            print ('De: {}  a las: {} Mensaje: {}'.format(message[1], message[2], message[3]))


inbox = SMSstore()

inbox.add_new_arrival(True, 79152648, "5:00 PM", 'tienes las siguientes llamadas perdidas 65524723(2)')
inbox.add_new_arrival(False, 79370276, "07:23 AM", 'Ola, te estoy esperando')
inbox.add_new_arrival(True, 40404, "12:04 PM", '!Siwon_choi: thanks God')
inbox.add_new_arrival(False, 9101, "04:45 PM", 'Banco Bisa: tu salario ha sido abondo a tu cuenta')
inbox.mostrar_mensajes()
print ('Tienes {} mensajes'.format(inbox.message_count()))
print ('Tine los siguientes {} mensajes no leidos'.format(inbox.get_unread_indexes()))
message_number = int(input('que mensaje quiere leer?'))
print ('El mensaje es: {}'.format(inbox.get_message(message_number)))
print ('Los mensajes no leidos son: {}'.format(inbox.get_unread_indexes()))
message_number = int(input('Borrar mensaje'))
inbox.delete(message_number)
inbox.mostrar_mensajes()
print ('the amount of messages are {}'.format(inbox.message_count()))

