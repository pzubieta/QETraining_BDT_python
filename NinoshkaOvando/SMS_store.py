from SMS_message import *
class SMS_store:

    def __init__(self):
        self.my_inbox = []
        self.count_sms=0

    def print_list_sms(self):
        for val in self.my_inbox:
            print(val.print_SMS())

    def add_message(self,from_number, time_arrived, text_of_SMS):
        has_been_viewerd= False
        message= SMS_message(has_been_viewerd, from_number, time_arrived, text_of_SMS)
        self.my_inbox[self.count_sms] = message
        self.count_sms = self.count_sms + 1

    def add_new_arrival(self,from_number, time_arrived, text_of_SMS):
        has_been_viewerd = False
        message = SMS_message(has_been_viewerd, from_number,time_arrived, text_of_SMS)
        self.my_inbox.append(message)
        self.count_sms = self.count_sms +1

    def message_count(self):
        return self.count_sms

    def get_unreald_indexes(self):
        message_list = []
        if(self.count_sms > 0):
            aux_count=0
            for value in self.my_inbox:
                if(value.get_has_been_viewerd()== False):
                    message_list.append(aux_count)
                aux_count+=1
            return message_list
        else:
            return None

    def get_message(self, i):
        if (self.count_sms > i):
            sms_aux=SMS_message(False, "", "", "")
            sms_aux= self.my_inbox[i]
            if(self.my_inbox[i].get_text_of_SMS() != ""):
                self.my_inbox[i].set_has_been_viewerd(True)
                return 'From Number:  {} ; Time_arrived:  {} ; Text of SMS:  {}'.format(self.my_inbox[i].get_from_number(),self.my_inbox[i].get_time_arrived(), self.my_inbox[i].get_text_of_SMS() )

            else:
                return None
        else:
            return None

    def delete(self, i):
        if (self.count_sms > i):
            del self.my_inbox[i]
            self.count_sms -= 1
            return "SMS of {} position was deleted".format(i)
        else:
            return None

    def delete_all(self):
        if (self.count_sms > 0):
            aux_count = 0
            for value in self.my_inbox:
                self.delete(aux_count)
                aux_count += 1
            self.count_sms = 0
            return "All SMS were deleted"
        else:
            return None




