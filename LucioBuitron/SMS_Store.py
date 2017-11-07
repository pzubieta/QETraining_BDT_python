class SMS_Store:
    # CREATES A NEW EMPTY LIST FOR THE TUPLES THAT WILL BE ADDED
    # If it is not defined, all values will be appended in one
    def __init__(self):
        self.sms_messages=[]

    #METHOD TO ADD A NEW SMS
    def add_new_arrival(self, h_b_v, f_n, t_a, t_o_s):
        self.has_been_viewed=h_b_v
        self.from_number=f_n
        self.time_arrived=t_a
        self.text_of_SMS=t_o_s

        #Append the tuple to the list
        self.sms_messages.append([self.has_been_viewed, self.from_number, self.time_arrived, self.text_of_SMS])
        print("New SMS added successfully!")

        #*****Test #1: Added items are displayed inside the list*****
        print("This was added: ")
        print(self.sms_messages)
        print("\n")


    #METHOD TO COUNT THE EXISTING SMS
    def message_count(self):
        #Since the SMS are in a list, we only get the length
        count=len(self.sms_messages)
        print("The number of SMS message is: ", count)
        print("\n")
        #return count


    #METHOD TO GET THE INDEXES ONLY FROM UNREAD SMS
    def get_unread_indexes(self):
		# We craete anew list in order to "copy" the indexes from unread SMS after iterate the list
        self.sms_messages_unread=[]

        #Iterate the list and find '0' since it means "no read"
        for i in self.sms_messages:
            if 0 in i:
                self.sms_messages_unread.append(self.sms_messages.index(i))
        print("The list of indexes of unread SMS is:")
        return self.sms_messages_unread
        print("\n")


    #METHOD TO GET THE WHOLE SMS FROM THE LIST PROVIDING AN INDEX
    def get_message(self, i):
        # Return (from_number, time_arrived, text_of_sms) for message[i]
		# Also change its state to "has been viewed".
	 	# If there is no message at position i, return None
        if self.sms_messages[i]:
            self.has_been_viewed=1
            print("The message in position "+str(i)+" is:")
            print(self.sms_messages[i])
            print("\n")
        else:
            print("None - There is not a SMS in that index number.")
            print("\n")


    #METHOD TO DELETE A SMS FROM THE LIST PROVIDIG AN INDEX
    def delete(self, i):
        if i in self.sms_messages:
            print("The message in position "+str(i)+" is: ",self.sms_messages[i])
            print("The message is being deleted!")
            print("\n")
            self.sms_messages[i].remove(i)
            print("Deleted!")

        else:
            print("None - There is not a SMS in that index number.")
            print("No Deleted!")
            print("\n")
#CREATE A NEW OBJECT OF CLASS SMS_STORE:
my_inbox=SMS_Store()

print("**Running FUNCTION to add new SMS: **")
my_inbox.add_new_arrival(0,70700000,"2017-10-10 10:10:10","Content Text 0")
my_inbox.add_new_arrival(0,70711111,"2017-10-11 10:10:10","Content Text 1")
my_inbox.add_new_arrival(0,70722222,"2017-10-11 10:10:10","Content Text 2")
my_inbox.add_new_arrival(0,70733333,"2017-10-11 10:10:10","Content Text 3")

print("**Running FUNCTION to display the count of existing SMS: **")
my_inbox.message_count()

print("**Running FUNCTION to get a SMS providing an index: **")
my_inbox.get_message(0)

print("**Running FUNCTION to display the list of indexes of unread SMS: **")
print(my_inbox.get_unread_indexes())
print("\n")

print("**Running FUNCTION to delete a SMS providing an index: **")
my_inbox.delete(10)
