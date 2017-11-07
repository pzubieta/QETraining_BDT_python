import datetime

class SMS_store:
    """This class allows to simulate SMS inbox actions"""

    def __init__(self):
        self.inbox = []

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        if int(from_number) and isinstance(time_arrived, datetime.datetime):
            dic = {'read': False, 'from_number': from_number, 'time_arrived': time_arrived, 'text_of_SMS': text_of_SMS}
            self.inbox.append(dic)
        else:
            print ("Invalid input!")

    def message_count(self):
        return (len(self.inbox))

    def get_unread_indexces(self):
        not_read = []
        for i in range (len(self.inbox)):
            if self.inbox[i]['read'] == False: not_read.append(i)
        return not_read

    def get_message(self, i):
        if i in range(len(self.inbox)):
            self.inbox[i]['read'] = True
            return (self.inbox[i]['from_number'],str(self.inbox[i]['time_arrived'].strftime("%y-%m-%d %H:%M")),self.inbox[i]['text_of_SMS'])
        else:
            return (None)
    def print_raw_index (self):
        for i in my_inbox.inbox:
            print(i)

my_inbox = SMS_store()

my_inbox.add_new_arrival('457554', datetime.datetime.now(), 'Uno')
my_inbox.add_new_arrival('7857554',datetime.datetime.now(), 'Dos')
my_inbox.add_new_arrival('777554', datetime.datetime.now(), 'Tres')
my_inbox.add_new_arrival('687554', datetime.datetime.now(), 'Cuatro')
my_inbox.add_new_arrival('7014554', datetime.datetime.now(), 'Cinco')
my_inbox.print_raw_index()
print ("Messages in the inbox: ", my_inbox.get_unread_indexces() )
print ("Number or messages in the inbox: ", my_inbox.message_count())
print("Getting messges from index [2]", my_inbox.get_message(2))
print("Messages not read: ", my_inbox.get_unread_indexces())
print("Getting messges from index [3]", my_inbox.get_message(3))
print("Messages not read: ", my_inbox.get_unread_indexces())