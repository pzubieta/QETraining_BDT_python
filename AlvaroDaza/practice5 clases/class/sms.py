"""
I use a list because a tuple do not support  modifications in the case that we need to change
the status viewed
"""


class SMSStore(object):
    def __init__(self):
        self.message_list = []

    def add_new_arrival_message(self, viewed, number, time, message):
        """
        Add a new message.
        :param viewed:  boolean  true if message was viewed else otherwise.
        :param number:  int      number from message was sent.
        :param time:    string   time that message was sent.
        :param message: string   message.
        :return:
        """
        messages_tuples = [viewed, number, time, message]
        self.message_list.append(messages_tuples)

    def message_count(self):
        """
        show the total of messages sent.
        :return:  number of messages.
        """
        return self.message_list.__len__()  # True, 79370292, "10:03:38", 'this is a text message for you'

    def get_not_read_messages(self):
        """
        shows unread messages.
        :return: the index of the mssages not read.
        """
        return [index + 1 for index, message in enumerate(self.message_list) if not message[0]]

    def get_message(self, index_message):
        """
        get the message of a specific index.
        :param index_message:   int     index of the message.
        :return:                string  the message sent.
        """
        if index_message > len(self.message_list):
            print ("THIS message not exist")
        else:
            self.message_list[index_message - 1][0] = True
            return self.message_list[index_message - 1][3]

    def delete_message(self, index):
        """
        deletes a message from the list.
        :param index:    int  message index.
        :return:
        """
        self.message_list.pop(index - 1)

    def show_messages(self):
        """
        show the number and the time of the messages list.
        :return:
        """
        for message in self.message_list:
            print ('FROM: {}  at: {} '.format(message[1], message[2]))


sms_store = SMSStore()
sms_store.add_new_arrival_message(True, 79370245, "09:03:12", 'this is a text message for you')
sms_store.add_new_arrival_message(False, 79370276, "05:30:34", 'Where are you?')
sms_store.add_new_arrival_message(True, 79370987, "01:15:56", 'hello :)!')
sms_store.add_new_arrival_message(False, 79370123, "08:45:41", 'Im waiting for you ')
sms_store.show_messages()
print ('the amount of messages are {}'.format(sms_store.message_count()))
print ('the messages not read are  {}'.format(sms_store.get_not_read_messages()))
message_number = int(input('what message do you want read?'))
print ('the message is : {}'.format(sms_store.get_message(message_number)))
print ('the messages not read are  {}'.format(sms_store.get_not_read_messages()))
message_number = int(input('delete message'))
sms_store.delete_message(message_number)
sms_store.show_messages()
print ('the amount of messages are {}'.format(sms_store.message_count()))
