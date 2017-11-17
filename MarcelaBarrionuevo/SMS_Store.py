class SMS_store:

    def __init__(self):
        self.inbox = []

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        dic = {"Number": from_number, "Arrive time":time_arrived, "Message":text_of_SMS, "Viewed": False}
        self.inbox.append(dic)

    def message_count(self):
        return len(self.inbox)

    def get_unread_indexes(self):
        listUnread = []
        for ele_dic in self.inbox:

            if ele_dic["Viewed"] == False:
                listUnread.append(ele_dic)
        return listUnread

    def get_message(self, i):

        if i < len(self.inbox):
            self.inbox[i]["Viewed"]= True
            return (self.inbox[i]["Number"], self.inbox[i]["Arrive time"], self.inbox[i]["Message"])
        else:
            return "None"

    def delete(self, i):
        if i < len(self.inbox):
            self.inbox.pop(i)

    def clear(self):
        self.inbox.clear()

my_inbox = SMS_store()
my_inbox.add_new_arrival('123456789', "2017/11/07 20:15", 'Message1')
my_inbox.add_new_arrival('123456788', "2017/11/07 21:15", 'Message2')
print ("Unread Messages: ", my_inbox.get_unread_indexes())
print("Inbox Messages [1]", my_inbox.get_message(1))
print ("Unread Messages: ", my_inbox.get_unread_indexes())
print ("Messages count in the inbox: ", my_inbox.message_count())
print("Delete message in index [0]: ", my_inbox.delete(0))
print ("Messages count in the inbox: ", my_inbox.message_count())
print("Clear Messages: ", my_inbox.clear())

