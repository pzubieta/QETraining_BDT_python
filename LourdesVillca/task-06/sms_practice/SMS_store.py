from message import Message


class SmsStore:
    def __init__(self):
        self.sms_message_list = []

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        message = Message(from_number, time_arrived, text_of_SMS)
        self.sms_message_list.append(message)

    def message_count(self):
        return len(self.sms_message_list)

    def get_unread_indexes(self):
        unread_messages = [index for index, message in enumerate(self.sms_message_list) if not message.has_been_viewed]
        return unread_messages

    def get_message(self, index):
        if index < len(self.sms_message_list):
            message = self.sms_message_list[index]
            message_detail = "from number: {}\n time arrived: {}\n " \
                             "sms text: {}".format(message.from_number, message.time_arrived, message.text_of_sms)
            message.set_status(True)
            return message_detail
        else:
            return None

    def delete(self, index=None):
        if index <= 0 < len(self.sms_message_list):
            print("Message from {} will be deleted".format(self.sms_message_list[index].from_number))
            self.sms_message_list.pop(index)
            print("Message Deleted")
        elif index is None:
            del self.sms_message_list[:]
        else:
            print("Index does not exist!!")
