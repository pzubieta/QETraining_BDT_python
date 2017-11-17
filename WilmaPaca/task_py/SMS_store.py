#my_inbox = SMS_store()
#(has_been_viewed, from_number, time_arrived, text_of_SMS)

#my_inbox.add_new_arrival(from_number, time_arrived, text_of_SMS)
# Makes new SMS tuple, inserts it after other messages
# in the store. When creating this message, its # has_been_viewed status is set False.

#	my_inbox.message_count()
 		# Returns the number of sms messages in my_inbox
#	my_inbox.get_unread_indexes()
		# Returns list of indexes of all not-yet-viewed SMS messages
#	my_inbox.get_message(i)
		# Return (from_number, time_arrived, text_of_sms) for message[i]
		# Also change its state to "has been viewed".
	 	# If there is no message at position i, return None
#	my_inbox.delete(i) # Delete the message at index i my_inbox.clear() # Delete all messages from inbox
import time
from Sms import Sms_message
class SMS_store:
    def __init__(self):
#       self.time_s = time.ctime()
#        self.phone_number =phone_user
        self.index = 0
        self.sms_inbox = {}

    def add_new_arrival(self,number, text_of_SMS):
        sms_ph = Sms_message(number,time.ctime(),text_of_SMS)
        self.sms_inbox [self.index]=sms_ph
        self.index += 1

    def countMessage(self):
        for key in self.sms_inbox.keys():
            key += 1
        return key
    def getMessageInbox(self,key):
#        print (key)
        for key, value in self.sms_inbox.items():
            if key in self.sms_inbox.keys():
                print("Message: ",value.getMessage())

    def getUnreadIndexes(self):
        unreadSms = []
        for key, value in self.sms_inbox.items():
            if value.getState() == False:
                unreadSms.append(key+1)
        return unreadSms
    def getInbox(self):
        for key, value in self.sms_inbox.items():
            if value.getState() == False:
                print ("Message datas: ",value.getPhone()+" '"+value.getMessage()+"' "+value.getTimeSms()+" "+"Unread")
            elif value.getState() == True:
                print("Message datas: ",value.getPhone() + " " + value.getMessage() + " " + value.getTimeSms()+" "+ "Read")
    def deleteSms(self, key):
        if key in self.sms_inbox.items():
            del self.sms_inbox[key]
    def clearInbox(self):
        self.sms_inbox.clear()

#phoneUser = input("Enter the phone of user: ")
number_phone = input("Enter the phone that sending message: ")
message_user = input ("Enter the message: ")
inbox = SMS_store()
inbox.add_new_arrival(number_phone,message_user)
inbox.getInbox()
print ("Message Number: ",inbox.countMessage())
inbox.getMessageInbox(1)
print ("--- Message unread ---")
print (inbox.getUnreadIndexes())
