class Sms_Store:
    def __init__(self):
        self.message = ()
        self.inbox = []

    def add_new_arrival(self, from_number, time_arrived, text_of_sms):
        self.from_number = from_number
        self.time_arrived = time_arrived
        self.text_of_sms = text_of_sms
        self.message = (False, from_number, time_arrived, text_of_sms)
        self.inbox.append(self.message)
        return self.inbox

    def message_count(self):
        number = len(self.inbox)
        return number

    def get_unread_indexes(self):
        listNotReadSmss = []
        size = len(self.inbox)
        for i in range(size):
            message = self.inbox[i]
            if message[0] == False:
                listNotReadSmss.append(message)
        return listNotReadSmss

    def get_messages(self, number):
        self.number = number
        index = number - 1
        try:
            message = self.inbox[index]
            if message:
                new_message = (True, message[1], message[2], message[3])
                self.inbox[index] = new_message
                return new_message
        except:
            print("None")

    def delete(self, number):
        try:
            message = self.get_messages(number)
            self.inbox.remove(message)
        except:
            print("Message not found")

    def clear(self):
        self.inbox = []





my_inbox = Sms_Store()
smss = my_inbox.add_new_arrival(10, 11, "test")
smss = my_inbox.add_new_arrival(20, 12, "test")
smss = my_inbox.add_new_arrival(30, 13, "test")
my_inbox.message_count()
my_inbox.get_messages(2)
my_inbox.delete(1)
print(my_inbox.inbox)
my_inbox.clear()
print(my_inbox.inbox)
