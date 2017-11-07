import RosarioFalconi.Practica_5.SMS as msg

class Inbox:
    def __init__(self):
        self.msg=[]

    def get_sms(self):
        return self.msg

    def add_sms(self, msge):
        self.msg.append(msge)

    def __len__(self):
        return len(self.msg)

    def get_Unread(self):
        aux_msg = self.msg.copy()
        unread = []
        i=1
        for i in range (len(aux_msg)):
            msge = aux_msg.pop()
            if msge.get_state() == 0:
                unread.append(msge)
        return len(unread)

    def get_message (self, index):
        print("index ", index)
        aux_msg = self.get_sms()
        msge = aux_msg.pop(index)
        print("MESSAGE:",msge.get_message())
        print("FROM:", msge.get_number())
        print("TIME:", msge.get_time())

    def set_State(self, index):
        self.msg[index][3]=1

    def delete (self, index):
        self.msg.remove(self.msg[index])

