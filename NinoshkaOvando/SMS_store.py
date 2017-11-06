from SMS_message import *
class SMS_store:

    def __init__(self):
        my_inbox = {}
        count_sms = 0

    def add_message(self,from_number, time_arrived, text_of_SMS):
        has_been_viewerd= False
        message= SMS_message.SMS_message(has_been_viewerd, from_number, time_arrived, text_of_SMS)
        self.my_inbox[self.count_sms] = message

    def add_new_arrival(self,from_number, time_arrived, text_of_SMS):
        has_been_viewerd = False
        message = SMS_message.SMS_message(has_been_viewerd, from_number)
        self.count_sms+=self.count_sms
        self.my_inbox[self.count_sms] = message

    def message_count(self):
        return self.count_sms

    def get_unreald_indexes(self):
        message_list = []
        if(self.count_sms > 0):
            for k, v in self.my_inbox.items():
                if(v.get_has_been_viewerd()== False):
                    message_list.append(k)
        else:
            return None

    def get_message(self, i):
        if (self.count_sms >= i):
            if(self.my_inbox[i].value().get_text_of_SMS() != ""):
                self.my_inbox[i].value().set_has_been_viewerd(True)
                return "From Number: ", self.my_inbox[i].value().get_from_number(), "; Time_arrived: ", self.my_inbox[i].value().get_time_arrived(),"; Text of SMS: ", self.my_inbox[i].value().get_text_of_SMS()
            else:
                return None
        else:
            return None

    def delete(self, i):
        return None
    def delete_all(self, i):
        self.count_sms =0
        self.my_inbox.clear()


