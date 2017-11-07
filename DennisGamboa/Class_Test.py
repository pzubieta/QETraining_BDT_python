class SMS_store:

    def __init__(self):
        self.store = []

    def add_new_arrival(self, number, time, text):
        self.store.append(("Read: False", number, time, text))

    def message_count(self):
        return len(self.store)

    def get_unread_indexes(self):
        result = []
        #print(self.store)
        for (i, v) in enumerate(self.store):
            print("i", i, "--->", "v", v)
            if v[0] == "Read: False":
                result.append(i)
        return result

    def get_message(self, i):
        msg = self.store[i]
        msg = ("Read: True",) + msg[1:]
        self.store[i] = msg
        return self.store[i][1:]

    def delete(self, i):
        del self.store[i]
        return "delete"

    def clear(self):
        self.store = []
        return "Clear messages"


my_inbox = SMS_store()
my_inbox.add_new_arrival(70809041, "02:00", "Hello")
my_inbox.add_new_arrival(60549125, "03:00", "Where are you?")
my_inbox.add_new_arrival(75992625, "06:00", "Test 2")
my_inbox.add_new_arrival(72225415, "08:00", "We've tasks?")

print(my_inbox.message_count())
print(my_inbox.get_message(2))
print(my_inbox.get_unread_indexes())
print(my_inbox.delete(2))
print(my_inbox.message_count())
print(my_inbox.clear())
print(my_inbox.message_count())
