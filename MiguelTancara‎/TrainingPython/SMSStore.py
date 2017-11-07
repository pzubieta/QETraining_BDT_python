import datetime

class SMSStore:


    smsMessageList = []

    def addNewArrival(self, fromNumber, timeArrived, textOfSMS):
        """Makes new SMS tuple, inserts it after other messages"""
        smsMessageTuple = ('unread', fromNumber, timeArrived, textOfSMS)
        self.smsMessageList.append(smsMessageTuple)


    def message_count(self):
        """Returns the number of sms messages in my_inbox"""
        return(len(self.smsMessageList))


    def getUnreadIndexes(self):
        """Returns list of indexes of all not-yet-viewed SMS messages"""
        smsunreadlist = []
        for i in range(len(self.smsMessageList)):
            mylist = list(self.smsMessageList[i])
            if mylist[0] == 'unread':
                smsunreadlist.append(i +1)
        return smsunreadlist



    def getmessage(self, index):
        """ Return (from_number, time_arrived, text_of_sms) for message[i].
            Also change its state to 'has been viewed'.
            If there is no message at position i, return 'None'"""
        if index - 1 < len(self.smsMessageList):
            self.changeMessageStatus(index)
            return self.smsMessageList[index - 1]
        else:
            return None


    def delete(self, index):
        """Delete the message at index 'index'"""
        i = index - 1
        if i < len(self.smsMessageList):
            del self.smsMessageList[i]
        else:
            print("It is not possible to remove a non-existent item")

    def getCurrentDate(self):
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:$S")

    def changeMessageStatus(self, index):
        """Change the status of the message to readed --> 0"""
        i = index - 1
        mylist = list(self.smsMessageList[i])
        mylist[0] = 'read'
        mytuple = tuple(mylist)
        del self.smsMessageList[i]
        self.smsMessageList.insert(i, mytuple)



myInbox = SMSStore()

#Adding messages to inbox
myInbox.addNewArrival(70303476, myInbox.getCurrentDate(), "It is a text message")
myInbox.addNewArrival(70743365, myInbox.getCurrentDate(), "Please call me now")
myInbox.addNewArrival(71698463, myInbox.getCurrentDate(), "send me the number phone of Marco")
myInbox.addNewArrival(69845678, myInbox.getCurrentDate(), "Tomorrow 9:00 AM at Plaza Colon")
print(myInbox.message_count())

#Getting the messages
print(myInbox.getmessage(1))
print(myInbox.getmessage(5))
print(myInbox.getmessage(4))

#getting unread messages
print(myInbox.getUnreadIndexes())

#Checkibg the list of tuples
print(myInbox.message_count())
print(myInbox.smsMessageList)

#deleting a message
myInbox.delete(4)
myInbox.delete(2)
myInbox.delete(5)

#Checking the list of tuples
print(myInbox.message_count())
print(myInbox.smsMessageList)