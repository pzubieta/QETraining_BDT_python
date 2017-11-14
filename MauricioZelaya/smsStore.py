class sms_store:
    def __init__(self):
        self.sms_inbox = []

    def add_message(self, is_read, from_number, time_arrived, text_body):
        new_message = (is_read, from_number, time_arrived, text_body)
        self.sms_inbox.append(new_message)

    def count_messages(self):
        count = 0
        for message in self.sms_inbox:
            count += 1
        return count

    def count_unread(self):
        unread_msgs = []
        # count = 0
        for msg in self.sms_inbox:
            if msg[0] == False:
                unread_msgs.append(msg)
                # count += 1
        return unread_msgs

    def get_message(self, index):
        count = 0
        if index <= len(self.sms_inbox):
            for msg in self.sms_inbox:
                if index == count:
                    return self.sms_inbox[index]
                else:
                    count += 1

    def remove_message(self, index):
        cont = 0
        for msg in self.sms_inbox:
            if index == cont:
                self.sms_inbox.remove(msg)
            else:
                cont += 1

    def remove_all(self):
        del self.sms_inbox[:]


msg1 = sms_store()
unread_counter = 0
msg1.add_message(False, 71720612, '12:30', 'hi my friend')
msg1.add_message(True, 71720612, '12:30', 'bye my friend')
msg1.add_message(False, 71720612, '12:30', 'just a tex')
msg1.add_message(False, 71720612, '12:30', 'new message')
msg1.add_message(False, 71720612, '12:30', 'a message')
msg1.add_message(False, 71720612, '12:30', 'friendly reminder')

print("You have %s messages in your inbox" % msg1.count_messages())
print("current unread messages:")
for msg in msg1.count_unread():
    print(msg)
    unread_counter += 1
print("you currently have", unread_counter, "unread messages")
print(msg1.get_message(1))
msg1.remove_message(1)

print("You have %s messages in your inbox" % msg1.count_messages())
msg1.remove_all()
print("\n\n\nYou have %s messages in your inbox" % msg1.count_messages())
