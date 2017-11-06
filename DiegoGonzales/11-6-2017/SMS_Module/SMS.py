class SMS:

    def __init__(self):
        self.inbox = []

    def add_new_arrival(self, number, time, message):
        self.inbox.append(("Status: False", number, time, message))

    def message_count(self):
        return len(self.inbox)

    def get_unread_index(self):
        for i , j in enumerate(self.inbox):
            if j[0] == "Status: False":
                print(self.inbox[i])

    def get_Message(self, index):
        if self.inbox[index] in self.inbox:
            string = self.inbox[index]
            string = ("Status: True",) + string[1:]
            self.inbox[index] = string
            return self.inbox[index][1:]
        else:
            return "None"

    def delete(self, index):
        self.inbox.remove(self.inbox[index])

    def clear(self):
        self.inbox.clear()
        return "Delete all the messages"