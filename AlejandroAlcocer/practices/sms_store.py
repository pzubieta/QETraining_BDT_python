
class SMS_store():

    def __init__(self):
        self.messages = []

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS, has_been_viewed = 0):
        message = (from_number, time_arrived, text_of_SMS, has_been_viewed)
        self.messages.append(message)
        return True

    def message_count(self):
        return len(self.messages)

    def get_unread_indexes(self):
        unread_list = []
        for message in self.messages:
            if message[len(message) - 1] == 0:
                unread_list.append(message)
        return unread_list

    def get_message(self, index):
        return self.messages[index]

    def delete(self, index):
        self.messages.pop(index)

    def clear(self):
        self.messages = []

    def get_all_messages(self):
        return self.messages

    def set_message_to_read(self, index):
        message = self.messages[index]
        self.delete(index)
        self.add_new_arrival(message[0], message[1], message[2], 1)



test_sms_store = SMS_store()

test_sms_store.add_new_arrival(55, 45, "testing a text message 1")
test_sms_store.add_new_arrival(55, 45, "testing a text message 2")
test_sms_store.add_new_arrival(55, 45, "testing a text message 3")
test_sms_store.add_new_arrival(55, 45, "testing a text message 4")
test_sms_store.set_message_to_read(0)
test_sms_store.set_message_to_read(1)
print(test_sms_store.get_all_messages())
print(test_sms_store.get_unread_indexes())
print(test_sms_store.get_message(3))
print(test_sms_store.message_count())
test_sms_store.clear()
print(test_sms_store.get_all_messages())

