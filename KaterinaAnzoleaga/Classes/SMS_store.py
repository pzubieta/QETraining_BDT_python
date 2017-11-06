class SMS_store:
    """This class allows to simulate SMS inbox actions"""

    def __init__(self):
        self.inbox = []

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        dic = {'read': False, 'from_number': from_number, 'time_arrived': time_arrived, 'text_of_SMS': text_of_SMS}
        self.inbox.append(dic)

    def message_count(self):
        return (self.inbox.len)

    def get_unread_indexces(self):
        not_read = []
        for i in self.inbox:
            if i['read'] == False: not_read.append(i)
        return not_read

    def get_message(self, i):
        if i in range(len(self.inbox)):
            self.inbox[i]['read'] = True
            return (self.inbox[i])
        else:
            return (None)


my_inbox = SMS_store()
my_inbox.add_new_arrival('457554', '12:30', 'Uno')
my_inbox.add_new_arrival('7857554', '12:30', 'Dos')
my_inbox.add_new_arrival('777554', '12:30', 'Tres')
my_inbox.add_new_arrival('687554', '12:30', 'Cuatro')
my_inbox.add_new_arrival('7014554', '12:30', 'Cinco')
print(my_inbox.get_message(2))
print(my_inbox.get_unread_indexces())
print(my_inbox.get_message(3))
print(my_inbox.get_unread_indexces())