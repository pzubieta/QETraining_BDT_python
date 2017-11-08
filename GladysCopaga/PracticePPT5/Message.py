class SMS_Store:
    def __init__(self):
        self.inbox = []
        self.outbox = []

        # Makes new SMS tuple, inserts it after other messages
        # in the store. When creating this message, its # has_been_viewed status is set False.
    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        message = [False, from_number, time_arrived, text_of_SMS]
        self.inbox.append(message)

    # Returns the number of sms messages in my_inbox
    def message_count(self):
        print(len(self.inbox))

    # Returns list of indexes of all not-yet-viewed SMS messages
    def get_unread_indexes(self):
        unread = []
        for index in range(len(self.inbox)):
            if self.inbox[index][0] == False:
                unread.append(index+1)
        print(unread)

        # Return (from_number, time_arrived, text_of_sms) for message[i]
        # Also change its state to "has been viewed".
        # If there is no message at position i, return None
    def get_message(self, index):
        self.inbox[index-1][0] = True
        print(self.inbox[index-1][1], "-", self.inbox[index-1][2], "-",self.inbox[index-1][3])

    # Delete the message at index i
    def delete(self, index):
        del self.inbox[index-1]
        print(self.inbox)

    #my_inbox.clear() # Delete all messages from inbox
    def clear(self):
        self.inbox = []
        print(self.inbox)

message1 = SMS_Store()
message1.add_new_arrival(1,"tuesday 12", "Hola")
message1.add_new_arrival(3,"monday 14", "Hola2")
message1.message_count()
message1.get_unread_indexes()
message1.get_message(0)
message1.get_unread_indexes()
message1.delete(0)
message1.clear()